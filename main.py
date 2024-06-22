from dotenv import load_dotenv
load_dotenv()

from utils.pdf_extractor import extract_text_from_pdf
from models.embeddings import create_and_store_embeddings
from chatbot.bot import chatbot
from utils.database import create_tables
import traceback

def main():
    try:
        # Create necessary tables
        create_tables()

        pdf_path = "data/Bitumag-BM-AL-tape-TDS.pdf"
        pdf_text = extract_text_from_pdf(pdf_path)
        create_and_store_embeddings(pdf_text)
        chatbot()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Traceback:")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()