# BM25 OpenAI RAG Chatbot

## Overview
This project implements an advanced chatbot that combines OpenAI's GPT-4 for generating responses with a hybrid retrieval system using vector search and BM25. It's designed to provide accurate and contextually relevant answers to a wide range of queries by integrating generative AI with retrieval-augmented generation (RAG) techniques.

## Features
- Hybrid retrieval system combining vector search and BM25
- Integration with OpenAI's GPT-4 for natural language understanding and generation
- Flask-based backend with rate limiting and CORS support
- Modern and responsive frontend interface
- Persistent storage using ChromaDB
- Sentence transformer-based reranking for improved relevance
- Customizable and expandable document base

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Backend Setup
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/bm25-openai-rag-chatbot.git
   cd bm25-openai-rag-chatbot/Backend
   ```

2. Run the `start_project.bat` file (for Windows users):
   ```
   start_project.bat
   ```
   This script will:
   - Create and activate a virtual environment
   - Install required packages
   - Set up environment variables
   - Start the Flask server
   - Open the frontend in your default web browser

   For manual setup or non-Windows users, follow these steps:
   ```
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   export FLASK_APP=main.py
   export OPENAI_API_KEY=your_api_key_here
   flask run
   ```

3. Place any documents you want the chatbot to use in the `./documents` directory. Supported formats include .txt, .pdf, and .docx.

### Frontend Setup
The frontend is automatically opened by the `start_project.bat` script. If you need to open it manually:

1. Ensure the backend server is running.
2. Open `Frontend/index.html` in a web browser.

## Usage
1. After running `start_project.bat`, the chatbot interface should open in your default web browser.
2. Enter your query in the input field and click "Send" or press Enter.
3. The chatbot will process your query and display the response.
4. Use the "Clear Chat" button to start a new conversation.

## Configuration
- Adjust rate limiting in `main.py` if needed.
- Modify the `chroma_db` path in `main.py` to change the location of the vector store.
- You can customize the number of retrieved documents by adjusting the `similarity_top_k` parameter in the `HybridRetriever` class.
- To change the reranking model, modify the `model` parameter in the `SentenceTransformerRerank` initialization.

## Troubleshooting

### Common Issues
1. **OpenAI API Key Error**: 
   - Ensure you've entered a valid API key when prompted by the `start_project.bat` script.
   - For manual setup, make sure the `OPENAI_API_KEY` environment variable is set correctly.

2. **Port Already in Use**: 
   - If port 5000 is occupied, change the port in `main.py` or stop the conflicting process.
   - You can modify the `flask run` command in `start_project.bat` to use a different port, e.g., `flask run --port=5001`.

3. **CORS Issues**: 
   - Verify that the frontend URL is correctly set in the CORS configuration in `main.py`.
   - If you're running the frontend from a different location, update the CORS settings accordingly.

4. **Python Version Mismatch**:
   - Ensure you're using Python 3.8 or higher. You can check your version with `python --version`.

### FAQs
Q: How do I add new documents for the chatbot to use?
A: Place new files (txt, pdf, docx) in the `./documents` directory and restart the backend server.

Q: Can I use a different language model?
A: Yes, modify the `llm` variable in `main.py` to use a different model from OpenAI or other providers supported by LangChain.

Q: How can I improve the retrieval quality?
A: You can experiment with different values for `similarity_top_k` in the `HybridRetriever` class or try different reranking models.

Q: How can I customize the chatbot's appearance?
A: Edit the `Frontend/style.css` file to change the chatbot's visual design.

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and test thoroughly.
4. Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements
- OpenAI for providing the GPT-4 model and embeddings
- The Langchain community for their excellent tools and documentation
- ChromaDB for vector storage capabilities
- Contributors and users of this project for their valuable input and feedback

## Support
If you encounter any issues or have questions, please open an issue on the GitHub repository or contact the maintainers directly.

Remember to keep your OpenAI API key confidential and never share it publicly or commit it to version control systems.
