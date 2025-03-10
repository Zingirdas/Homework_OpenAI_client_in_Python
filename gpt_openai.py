from dotenv import load_dotenv
load_dotenv()
from rich import print

user_question = "What capital is Finland?"

import os
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": user_question,
        }
    ],
    model= "gpt-4o",
)


answer = response.choices[0].message.content

print("--"*40)
print(f"** Question: {user_question} **")
print()
print(f"** Answer: {answer} **")
print("--"*40)
