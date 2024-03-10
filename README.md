# BM25 OpenAI RAG Chatbot

## Description
This project is a chatbot that uses OpenAI for embeddings and partial response creation. It also incorporates generative AI. It's kind of a monster RAG bot.

## Installation
The project is divided into two main parts: the backend and the frontend. 

### Backend
The backend is written in Python and uses Flask as a web server. It also uses several libraries such as openai, llama_index, and chromadb. To install these dependencies, you will need Python and pip installed on your machine. Once you have Python and pip, you can install the dependencies by running the following command in the /Backend directory:

#### Setting up the Python environment
1. Install Python and pip. You can download Python from the official website and pip is included in the Python installation.
2. Create a virtual environment. You can do this by running the command `python -m venv env` in the /Backend directory.
3. Activate the virtual environment. On Windows, you can do this by running the command `.\env\Scripts\activate`.
4. Install the necessary dependencies. You can do this by running the command `pip install -r requirements.txt`.

#### Running the Flask server
1. Set the FLASK_APP environment variable to main.py. On Windows, you can do this by running the command `set FLASK_APP=main.py`.
2. Run the Flask server. You can do this by running the command `flask run`.

#### Placing files for ingestion
Place any files or documents you want the backend to ingest in the ./documents directory.

### Frontend
The frontend is a simple HTML, CSS, and JavaScript application.

#### Opening the frontend
Navigate to the /Frontend directory and open the index.html file in a web browser.

## Additional setup instructions for Windows 10
If you are using Windows 10, you may need to add Python and pip to your PATH. You can do this by following the instructions on the Python website.
