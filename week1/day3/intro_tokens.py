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

prompt1 = "I love you"                                 ## Msg diye 
prompt2 = "What is ML"
prompt3 = "What I am doing?"

prompts = [prompt1,prompt2,prompt3]                    ## list of prompt bnae 

for prompt in prompts:                                 ## chalane ke liye Loop lga diye 
    message = {                                        ## Msg ka dictionary bnae 
    "role" : role,
    "content" : prompt
    }
    messages = [message]                                   
    response = client.chat.completions.create(model=model, messages=messages)
    # print(response.choices[0].message.content)         ## print krwae
    print(f"Prompt - {response.usage.prompt_tokens} , Response - {response.usage.completion_tokens}")