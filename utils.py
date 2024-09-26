from openai import OpenAI
from langchain.embeddings import OpenAIEmbeddings
import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()


# open ai 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()
def open_ai_llm(prompt):
    completion = client.chat.completions.create(
    messages = [
        {"role": "system", "content": "You are a professional job profile reviewer."},
        {"role": "user", "content": prompt},
    ],
    model = "gpt-4o",
    temperature=1,
    max_tokens=4096
    )
    return completion

# mysql connection

# MySQL database connection
def my_sql_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="job_profiles"
    )

    cursor = db.cursor()
    return cursor,db

def embeddings_openai():
    embeddings = OpenAIEmbeddings()
    return embeddings