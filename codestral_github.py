from dotenv import load_dotenv
load_dotenv()
from rich import print

user_question = "What model are you?"

import os
from openai import OpenAI


client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
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
    model= "Codestral-2501",
    temperature= 0.8,
    max_tokens= 2048,
    top_p= 0.1
)


answer = response.choices[0].message.content

print("--"*40)
print(f"** Question: {user_question} **")
print()
print(f"** Answer: {answer} **")
print("--"*40)
