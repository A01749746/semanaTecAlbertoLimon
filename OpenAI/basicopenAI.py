from openai import OpenAI

#llave mia
secret_key = "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"

#llave del profe
#secret_key = "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"
prompt = "Give a summary about history of Turkey"
client = OpenAI(
    api_key=secret_key,
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ],
  max_tokens = 100,
  temperature = 0
)

#print(completion)
print(completion.choices[0].message.content)