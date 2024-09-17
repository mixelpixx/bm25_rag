# BM25 OpenAI RAG Chatbot

## Description
This project is a chatbot that leverages OpenAI's GPT-4 for generating responses and embeddings in combination with BM25 for information retrieval. It uses a hybrid retrieval approach to provide accurate and contextually relevant answers. The chatbot is designed to handle a range of queries by integrating generative AI with retrieval-augmented generation (RAG) techniques.

## Installation
The project is divided into two main parts: the backend and the frontend. 

### Backend
The backend is written in Python and uses Flask as a web server. It also utilizes libraries such as OpenAI, ChromaDB, and others. Ensure you have Python and pip installed on your machine. Follow these steps to set up the backend:

#### Setting up the Python environment
1. **Install Python and pip**: Download Python from the official website. Pip is included in the Python installation.
2. **Create a virtual environment**: Run `python -m venv env` in the /Backend directory.
3. **Activate the virtual environment**: On Windows, run `.\env\Scripts\activate`. On macOS/Linux, use `source env/bin/activate`.
4. **Install dependencies**: Run `pip install -r requirements.txt`.

#### Running the Flask server
1. **Set the FLASK_APP environment variable**: On Windows, run `set FLASK_APP=main.py`. On macOS/Linux, use `export FLASK_APP=main.py`.
2. **Run the Flask server**: Execute `flask run` to start the server.

#### Placing files for ingestion
Place any files or documents you want the backend to ingest in the `./documents` directory.

### Frontend
The frontend is a simple HTML, CSS, and JavaScript application.

#### Opening the frontend
Navigate to the /Frontend directory and open the `index.html` file in a web browser.

## Usage
To interact with the chatbot:
1. Open the frontend in your browser.
2. Enter your query in the input field and press "Send".
3. The chatbot will process your query and display the response.

## Troubleshooting and FAQs
### Common Issues

### FAQs

## Contribution Guidelines
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License and Credits
This project is licensed under the MIT License. Special thanks to OpenAI and contributors for their support and resources.

## Additional setup instructions for Windows 10
If you are using Windows 10, you may need to add Python and pip to your PATH. You can do this by following the instructions on the Python website.
