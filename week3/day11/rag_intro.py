import os
from pathlib import Path 
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

my_api = os.getenv("GROQ_API_KEY")

if not my_api:
    raise ValueError("API nhi mila")

client = Groq(api_key = my_api) 

model="openai/gpt-oss-120b" 

knowlegde_base = {
    "age" : "ayush is 19 year old",
    "name" : "Ayush Kumar"
}

def RAG(question):
    question = question.lower()
    if "age" in question:
        return knowlegde_base["age"]
    elif "name" in question:
        return knowlegde_base["name"]
    else:
        return "I don't have information about that."

def ask_LLM(question):

    context = RAG(question)

    sys_prompt = f"""Do not exceed the response limit of 1 line. and do not hallucinate and if you dont know the answer search the context. Context : {context}. And also do not give your suggestions"""

    system_messgae = {
        "role": "system",
        "content" : "sys_prompt" 
    }

    user_message = {
        "role" : "user",
        "content" : question
    }

    messages = [system_messgae, user_message]
    response = client.chat.completions.create(messages= messages, model= model)
    return response.choices[0].message.content

print(ask_LLM("who is ayush"))


