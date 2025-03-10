from dotenv import load_dotenv
load_dotenv()
from rich import print


import os
from openai import OpenAI

from google import genai

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="How many openai models are created?"
)


print(response.text)