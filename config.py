import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(var_name, default_value):
    value = os.getenv(var_name)
    if value is None:
        print(f"Warning: Environment variable {var_name} not set. Using default value.")
        return default_value
    return value

OPENAI_API_KEY = get_env_variable("OPENAI_API_KEY", "")
DB_NAME = get_env_variable("DB_NAME", "rag_chatbot_db")
DB_USER = get_env_variable("DB_USER", "rag_chatbot_user")
DB_PASSWORD = get_env_variable("DB_PASSWORD", "password")
DB_HOST = get_env_variable("DB_HOST", "localhost")