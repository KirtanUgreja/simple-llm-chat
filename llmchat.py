from openai import OpenAI

a4f_base_url = "a4f_api_key"

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
