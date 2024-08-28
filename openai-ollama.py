from openai import OpenAI
from openai.types.chat.completion_create_params import ResponseFormat


client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)


response = client.chat.completions.create(
  model="llama3",
  messages=[
    {"role": "user", "content": "Hi how are you?"}
  ]
)
print(response.choices[0].message.content)
# print(response)