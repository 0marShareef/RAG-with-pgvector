from openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.database import get_db_connection
from config import OPENAI_API_KEY
import numpy as np

client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text):
    response = client.embeddings.create(input=text, model="text-embedding-ada-002")
    return response.data[0].embedding

def create_and_store_embeddings(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)

    conn = get_db_connection()
    with conn.cursor() as cur:
        for chunk in chunks:
            embedding = get_embedding(chunk)
            cur.execute(
                "INSERT INTO pdf_embeddings (content, embedding) VALUES (%s, %s)",
                (chunk, embedding)
            )
        conn.commit()
    conn.close()

def get_relevant_chunks(query, top_k=3):
    query_embedding = get_embedding(query)
    
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
        SELECT content, embedding <-> %s::vector AS distance
        FROM pdf_embeddings
        ORDER BY distance
        LIMIT %s
        """, (query_embedding, top_k))
        
        results = cur.fetchall()
    conn.close()
    
    return [result[0] for result in results]