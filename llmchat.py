from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # load from .env file

a4f_api_key = os.getenv("a4f_api_key_llm")
a4f_base_url = "https://api.a4f.co/v1"

client = OpenAI(
    api_key=a4f_api_key,
    base_url=a4f_base_url,
)

completion = client.chat.completions.create(
  model="provider-2/gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Why?"}
  ]
)
print(completion.choices[0].message.content)