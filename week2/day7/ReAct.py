import os                                              ## Saari library access kiye 
from pathlib import Path 
import time
from groq import Groq
from dotenv import load_dotenv
import re

load_dotenv()                                          ## jo bhi .evn me hai usko access kiye 

my_api = os.getenv("GROQ_API_KEY")                     ## API key access kiye 

if not my_api:                                         ## Agar API key Available nhi hai toh error throw kiye 
    raise ValueError("API nhi mila")

client = Groq(api_key = my_api)                        ## Groq me as a client register kiye 

model = "llama-3.3-70b-versatile"

#tools

def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Error"

def getProductPrice(product):
    if product == "iPhone 17":
        return 100000
    elif product == "Bottel":
        return 2000
    elif product == "Diary" :
        return 1000
    else:
        return 200


tools = {
    "getProductPrice" : getProductPrice,
    "calculate" : calculate
}

system_prompt = """

You are a shopping assistant.

You have these tools:
getProductPrice(product)
calculate(expression)

IMPORTANT:
Call tools exactly like these examples:

Action: getProductPrice("iPhone 17")
Action: calculate("5000 - 1000")

Never write:getProductPrice(product="iPhone 17")
Never write:calculate(expression="5000 - 1000")

Follow these rules:

Decide what you need to do next.
Call ONLY ONE tool at a time.
After writing an Action, STOP immediately.
Never guess or invent a tool result.
Wait until you receive an Observation.
Then decide your next action.
When the task is complete, 
give the Final Answer.

Format:
Thought: what you need to do
Action: tool_name(argument)

When finished:
Final Answer: your answer

"""


def LLM_response(prompt):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    for step in range(8000):

        print("\n------------------")
        print("STEP", step + 1)
        print("------------------")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0
        )

        answer = response.choices[0].message.content

        print(answer)

        # Agent has finished
        if "Final Answer:" in answer:
            break


        # Find the Action
        match = re.search(
            r"Action:\s*(\w+)\((.*?)\)",
            answer
        )

        if match:

            tool_name = match.group(1)

            tool_input = match.group(2)

            tool_input = tool_input.strip()

            tool_input = tool_input.strip('"')


            # Run the tool
            if tool_name in tools:

                tool = tools[tool_name]

                observation = tool(tool_input)

            else:

                observation = "Tool not found"


            print("Observation:",observation)

            # Add LLM response to memory
            messages.append({
                "role": "assistant",
                "content": answer
            })


            # Give tool result back to LLM
            messages.append({
                "role": "user",
                "content":
                    "Observation: "
                    + str(observation)
            })
            




prompt = """
I have 5000 rupees. What is the price of an iphone 17?
and how much money will I have left?
"""

LLM_response(prompt)