import os                                             
from pathlib import Path 
from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()                                           

my_api = os.getenv("GROQ_API_KEY")                     

if not my_api:                                         
    raise ValueError("API nhi mila")

client = Groq(api_key = my_api)                        

model = "llama-3.3-70b-versatile"                       

role = "user"                                           

class Ticket(BaseModel):
    Name : str
    Problem : str
    E_mail : str 
    Phone_number : int

schema = Ticket.model_json_schema()

response_type = {
    "type" : "json_object",
}

system_prompt = f"""I STRICTLY want every response in the JSON format like {schema}"""

message_system = {        
    "role" : "system",                             
    "content" : system_prompt 
}

Consumer_Mail = input("Enter your Conplaint : ")               

prompt = f"""{Consumer_Mail}"""

message = {                                            
    "role" : role,
    "content" : prompt
}

messages = [message_system, message]                 

response = client.chat.completions.create(model=model, messages=messages, response_format=response_type)

print(response.choices[0].message.content)            