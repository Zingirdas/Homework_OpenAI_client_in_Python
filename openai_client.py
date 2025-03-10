from openai import OpenAI
import os
from dotenv import load_dotenv
from rich import print

load_dotenv
 
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this i a test",
        }
    ],
    model="gpt-4o"
)

print(chat_completion)