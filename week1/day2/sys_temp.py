import os                                              ## Saari library access kiye 
from pathlib import Path 
from groq import Groq
from dotenv import load_dotenv

load_dotenv()                                          ## jo bhi .evn me hai usko access kiye 

my_api = os.getenv("GROQ_API_KEY")                     ## API key access kiye 

if not my_api:                                         ## Agar API key Available nhi hai toh error throw kiye 
    raise ValueError("API nhi mila")

client = Groq(api_key = my_api)                        ## Groq me as a client register kiye 

model = "llama-3.3-70b-versatile"                      ## model btae 

role = "user"                                          ## Role btae 

prompt = "I love you"                                  ## Msg diye 

message_system = {                                     ## system message btae hai isko kii tum kya hoo mtlb iko hm btae kii tum kon hoo mere relationship
    "role" : "system",
    "content" : "You are my spouse" 
}

message = {                                            ## Msg ka dictionary bnae 
    "role" : role,
    "content" : prompt
}

messages = [message_system, message]                   ## Groq list of dictionary me mgs accecp krta hai 
                                                       ## phele isko btaenge kii tm kon hoo then msg pucghenge 

response = client.chat.completions.create(model=model, messages=messages, temperature=2)     ## response generate kiye 3 chiz liye tempratre for randomness, msg and model 

print(response.choices[0].message.content)             ## print krwae