import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_community.utilities.sql_database import SQLDatabase 
from langchain_experimental.sql import SQLDatabaseChain

load_dotenv()
client = OpenAI(api_key= os.environ["OPENAI_API_KEY"],)

hostname = os.getenv("DB_HOST")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
port = os.getenv("PORT") 
database = os.getenv("DB_NAME")

dburi = f"mysql+mysqlconnector://{username}:{password}@{hostname}:{port}/{database}"
db = SQLDatabase.from_uri(dburi)
llm = OpenAI(temperature=0)

def chat_with_db():
    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
    user_input = input("What do you want to know about: ")
    response = db_chain.invoke(user_input)
    print("[Chatbot]: ", response)