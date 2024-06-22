from openai import OpenAI
from models.embeddings import get_relevant_chunks
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(query, relevant_chunks):
    prompt = f"""You are a helpful assistant answering questions about a specific PDF document. 
    Use the following relevant excerpts from the document to answer the user's question. 
    If you can't answer the question based on these excerpts, say so.

    Relevant excerpts:
    {' '.join(relevant_chunks)}

    User question: {query}

    Assistant:"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content

def answer_query(query):
    relevant_chunks = get_relevant_chunks(query)
    return generate_response(query, relevant_chunks)

def chatbot():
    print("Welcome to the PDF Chatbot! Ask me anything about the PDF content.")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        response = answer_query(user_input)
        print("Bot:", response)