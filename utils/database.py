import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

def get_db_connection():
    try:
        return psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

def create_tables():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            # Ensure the vector extension is created
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            
            cur.execute("""
            CREATE TABLE IF NOT EXISTS pdf_embeddings (
                id SERIAL PRIMARY KEY,
                content TEXT,
                embedding vector(1536)
            )
            """)
        conn.commit()
        print("Table 'pdf_embeddings' created successfully.")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()