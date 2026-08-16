import os                                              ## Saari library access kiye 
from pathlib import Path 
from groq import Groq
from dotenv import load_dotenv
import time

load_dotenv()

my_api = os.getenv("GROQ_API_KEY")

if not my_api:
    raise ValueError("API nhi mila")

client = Groq(api_key = my_api)

model = "llama-3.3-70b-versatile"

prompt = input("Enter your prompt: ")

message = {
    "role" : "user",
    "content" : prompt
}

messages = [message]

response = client.chat.completions.create(model = model, messages = messages, stream = True)

# answer = response.choices[0].message.content

for chunk in response:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
