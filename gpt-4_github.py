from dotenv import load_dotenv
load_dotenv()
from rich import print

user_question = "How can you help me with?"

import os
from openai import OpenAI


client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

system_message = """
Please answer the user's questions in a clear and structured way. 
For example, you should break down the answer into sections if applicable, 
and be concise and precise. Start with a direct answer to the question, followed by any relevant details or context.
"""

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_message,
        },
        {
            "role": "user",
            "content": user_question,
        }
    ],
    model="gpt-4o",
    temperature=1,
    max_tokens=4096,
    top_p=1
)


answer = response.choices[0].message.content

print("--"*40)
print(f"** Question: {user_question} **")
print()
print(f"** Answer: {answer} **")
print("--"*40)
