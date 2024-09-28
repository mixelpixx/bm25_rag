import os
import openai
import logging
import sys
import chromadb
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_cors import CORS
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

app = Flask(__name__)
CORS(app)

# Retrieve the OpenAI API key from an environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().handlers = []
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Document loading and processing
loader = DirectoryLoader('./documents', glob="**/*.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Embedding and vector store setup
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(texts, embeddings)

# Retrieval setup
retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 5})

# LLM setup
llm = OpenAI(temperature=0)

# Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

embed_model = OpenAIEmbedding(
    model="text-embedding-3-large",
    dimensions=3072,
)

# load documents
documents = SimpleDirectoryReader("./documents").load_data()


# initialize LLM + node parser
llm = OpenAI(model="gpt-4")
splitter = SentenceSplitter(chunk_size=512)
nodes = splitter.get_nodes_from_documents(documents)


# initialize storage context 
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("quickstart")
vector_store = chromadb.ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
  documents, storage_context=storage_context, embed_model=embed_model
)


# retireve the top 10 most similar nodes using embeddings
vector_retriever = index.as_retriever(similarity_top_k=10)


# retireve the top 10 most similar nodes using bm25
bm25_retriever = BM25Retriever.from_defaults(nodes=nodes, similarity_top_k=10)

class HybridRetriever(BaseRetriever):
    def __init__(self, vector_retriever, bm25_retriever):
        self.vector_retriever = vector_retriever
        self.bm25_retriever = bm25_retriever
        super().__init__()

    def _retrieve(self, query, **kwargs):
        bm25_nodes = self.bm25_retriever.retrieve(query, **kwargs)
        vector_nodes = self.vector_retriever.retrieve(query, **kwargs)

        # combine the two lists of nodes
        all_nodes = []
        node_ids = set()
        for n in bm25_nodes + vector_nodes:
            if n.node.node_id not in node_ids:
                all_nodes.append(n)
                node_ids.add(n.node.node_id)
        return all_nodes

hybrid_retriever = HybridRetriever(vector_retriever, bm25_retriever)

reranker = SentenceTransformerRerank(top_n=4, model="BAAI/bge-reranker-base")

query_engine = RetrieverQueryEngine.from_args(
    retriever=hybrid_retriever,
    node_postprocessors=[reranker],
    llm=llm,
)


# Initialize rate limiter
limiter = Limiter(
    app,
    key_func=lambda: request.remote_addr,
    default_limits=["5 per minute", "100 per day"]
)

# Users Query
@app.route('/query', methods=['POST'])
@limiter.limit("5 per minute")
def query():
    try:
        data = request.get_json()
        user_query = data['query']
        result = qa_chain({"query": user_query})
        response = {
            "answer": result['result'],
            "sources": [doc.metadata['source'] for doc in result['source_documents']]
        }
        return jsonify(response)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    app.run(debug=True)
