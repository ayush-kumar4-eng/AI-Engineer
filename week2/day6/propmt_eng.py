import os                                              ## Saari library access kiye 
from pathlib import Path 
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()                                          ## jo bhi .evn me hai usko access kiye 

my_api = os.getenv("GROQ_API_KEY")                     ## API key access kiye 

if not my_api:                                         ## Agar API key Available nhi hai toh error throw kiye 
    raise ValueError("API nhi mila")

client = Groq(api_key = my_api)                        ## Groq me as a client register kiye 

model = "llama-3.3-70b-versatile"

User_Complaint = input("Enter Your Complaint : ")

print("Processing..............")
time.sleep(0.5)

prompt = f"""
#ROLE:
You are a support assistant at a mobile/laptop company
#TASK: 
You have to classify the issue in a category
#CONSTRAINT:
You have to classify the issue in one of three categories namely billing, technical, return.
#OUTPUT FORMAT:
Your answer should contain two things first The one word shoud be one of the categories given in constraints and the second thing why in that category in one small line 
#Example:
For instance if a user compalin says he wants a refund then the category is Return
#FALLBACK:
If the issue is unrelated to any of the categories mentioned in constraints, then the answer should be OTHER
This is a user complaint:
{User_Complaint}
"""

def LLM_response(prompt):

    message = {
        "role" : "user",
        "content" : prompt
    }

    messages = [message]

    response = client.chat.completions.create(model=model, messages=messages)

    answer = response.choices[0].message.content

    return answer

print(LLM_response(prompt))



