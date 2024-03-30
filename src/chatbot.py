import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key= os.environ["OPENAI_API_KEY"],)

def chat_with_gpt():
    prompt = input("Chat Prompt: ")
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user","content": prompt}]
    )
    print("[Chatbot]: ", response.choices[0].message.content)