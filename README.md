# BM25 OpenAI RAG Chatbot

## Description
This project implements an advanced chatbot that combines OpenAI's GPT-4 for generating responses and embeddings with BM25 for information retrieval. It utilizes a hybrid retrieval approach to provide accurate and contextually relevant answers. The chatbot is designed to handle a wide range of queries by integrating generative AI with retrieval-augmented generation (RAG) techniques.

## Features
- Hybrid retrieval system combining vector search and BM25
- Integration with OpenAI's GPT-4 for natural language understanding and generation
- Flask-based backend with rate limiting and CORS support
- Simple and intuitive frontend interface

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js and npm (for potential frontend package management)
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

   For manual setup or non-Windows users, follow these steps:
   ```
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   export FLASK_APP=main.py
   export OPENAI_API_KEY=your_api_key_here
   flask run
   ```

3. Place any documents you want the chatbot to use in the `./documents` directory.

### Frontend Setup
1. Navigate to the Frontend directory:
   ```
   cd ../Frontend
   ```

2. Open `index.html` in a web browser.

## Usage
1. Ensure the backend server is running.
2. Open the frontend (`index.html`) in a web browser.
3. Enter your query in the input field and click "Send" or press Enter.
4. The chatbot will process your query and display the response.

## Configuration
- Adjust rate limiting in `main.py` if needed.
- Modify the `chroma_db` path in `main.py` to change the location of the vector store.

## Troubleshooting

### Common Issues
1. **OpenAI API Key Error**: Ensure you've set the `OPENAI_API_KEY` environment variable correctly.
2. **Port Already in Use**: If port 5000 is occupied, change the port in `main.py` or stop the conflicting process.
3. **CORS Issues**: Verify that the frontend URL is correctly set in the CORS configuration in `main.py`.

### FAQs
Q: How do I add new documents for the chatbot to use?
A: Place new text files in the `./documents` directory and restart the backend server.

Q: Can I use a different language model?
A: Yes, modify the `llm` variable in `main.py` to use a different model from OpenAI or other providers.

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
- Contributors and users of this project for their valuable input and feedback
