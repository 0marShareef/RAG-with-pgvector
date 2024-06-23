
# PDF-based RAG Chatbot

This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers queries about a PDF document. It uses PostgreSQL with pgvector as the vector database, GPT-4 as the language model via OpenAI's API, and OpenAI's text embeddings for semantic search.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Database Setup](#database-setup)
4. [Project Structure](#project-structure)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [How It Works](#how-it-works)
8. [Troubleshooting](#troubleshooting)

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- OpenAI API key
- Git
- C compiler (gcc or equivalent)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/0marShareef/RAG-with-pgvector.git

cd RAG-with-pgvector
```

2. Create a virtual environment and activate it:

```bash 
python -m venv venv
source venv/bin/activate  
# On Windows, use venv\Scripts\activate
```

3. Install the required packages:

```bash 
pip install -r requirements.txt
```

## Database Setup

1. Install PostgreSQL if you haven't already:

```bash 
sudo apt update
sudo apt install postgresql postgresql-contrib
```

2. Install the necessary development libraries:

```bash 
sudo apt install postgresql-server-dev-all
```

3. Install pgvector:

```bash 
cd /tmp
git clone --branch v0.7.2 https://github.com/pgvector/pgvector.git
cd pgvector
make
make install # may need sudo
```

4. Start the PostgreSQL service:

```bash 
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

5. Log in as the postgres user:

```bash 
sudo -i -u postgres
```

6. Create a new database and user:

```sql 
createdb rag_chatbot_db
createuser rag_chatbot_user
```

7. Enter the PostgreSQL shell:

```sql 
psql
```

8. Set a password for the new user and grant privileges:

```sql
ALTER USER rag_chatbot_user WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE rag_chatbot_db TO rag_chatbot_user;
```

9. Connect to the new database:

```sql 
\c rag_chatbot_db
```

10. Install the pgvector extension:

```sql 
CREATE EXTENSION vector;
```

11. Exit the PostgreSQL shell:

``` 
\q
```

12. Exit the postgres user shell:
```
exit
```


## Project Structure

```
pdf-rag-chatbot/
│
├── .env
├── requirements.txt
├── main.py
├── config.py
│
├── utils/
│   ├── __init__.py
│   ├── pdf_extractor.py
│   └── database.py
│
├── models/
│   ├── __init__.py
│   └── embeddings.py
│
└── chatbot/
    ├── __init__.py
    └── bot.py
```


## Configuration

1. Create a ```.env``` file in the project root directory with the following content:

```
OPENAI_API_KEY=your_openai_api_key_here
DB_NAME=rag_chatbot_db
DB_USER=rag_chatbot_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
```

Replace ```your_openai_api_key_here``` with your actual OpenAI API key and ```your_secure_password``` with the password you set for the database user.


2. Update the ```pdf_path``` variable in ```main.py``` to point to your PDF file:

```python
pdf_path = "path/to/your/pdf/file.pdf"
```


## Usage

1. Run the main script:

```python
python main.py
```

2. The script will extract text from the PDF, create embeddings, store them in the database, and then start the chatbot interface.

3. You can now ask questions about the content of the PDF. Type 'quit' to exit the chatbot.


## How it works

1. The PDF text is extracted and split into chunks.
2. Each chunk is embedded using OpenAI's text embedding model.
3. The embeddings are stored in the PostgreSQL database using pgvector.
4. When a query is received, it's embedded and semantically similar chunks are retrieved from the database.
5. The relevant chunks and the query are sent to GPT-4 to generate a response.


## Troubleshooting

- If you encounter database connection issues, make sure your PostgreSQL service is running and the credentials in the .env file are correct.
- If you get an error about the vector extension, ensure you've installed the pgvector extension in your database as described in the Database Setup section.
- For any OpenAI API errors, check that your API key is correct and you have sufficient credits.
- If you encounter issues with pgvector installation, make sure you have the necessary build tools installed (```sudo apt install build-essential```).

If you encounter any other issues, please open an issue in the GitHub repository with a detailed description of the problem and the full error traceback.