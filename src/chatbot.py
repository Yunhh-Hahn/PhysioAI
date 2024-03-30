import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_community.utilities.sql_database import SQLDatabase 
from langchain_experimental.sql import SQLDatabaseChain

load_dotenv()
client = OpenAI(api_key= os.environ["OPENAI_API_KEY"],)

hostname = os.getenv("DB_HOST")
username =  os.getenv("DB_PASSWORD")
password =  os.getenv("DB_PASSWORD")
port = os.getenv("PORT") 
database = os.getenv("DB_NAME")

dburi = f"mysql+mysqlconnector://{username}:{password}@{hostname}:{port}/{database}"
db = SQLDatabase.from_uri(dburi)
llm = OpenAI(temperature=0)

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True) #verbose is to let the llm know it should do the explanation a bit more
user_input = input("What do you want to know about: ")
db_chain.invoke(user_input)