import os                                             
from pathlib import Path 
from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel
import json 

load_dotenv()                                           

my_api = os.getenv("GROQ_API_KEY")                     

if not my_api:                                         
    raise ValueError("API nhi mila")

client = Groq(api_key = my_api)                        

model = "llama-3.3-70b-versatile"                       

role = "user"

# PART 1

class Job_D(BaseModel):
    Role : str
    Required_Qualification : list[str] 
    Preffered_skills : list[str] 
    Minimum_experience : float | None
    Educational_qualifications : list[str]
    Responsibilities : list[str]

schema_JOB_D = Job_D.model_json_schema()

response_format = {
    "type" : "json_object"
}

system_prompt = f"""

You are an expert HR assistant.
Your job is to analyze job descriptions and extract structured information from them.

Return ONLY valid JSON matching this schema: {schema_JOB_D}

IMPORTANT:
Do NOT return the schema itself.
Do NOT return fields like "properties", "title" or "type".
Fill the schema with actual information extracted from the job description

If minimum experience is not mentioned, return null.If information for a list is missing, return an empty list.
Do not invent information. 

"""

Job_disc = input("Enter Job Discription : ")

User_prompt = f"""

Analyse the given job discription {Job_disc}

"""

message_system = {
    "role" : "system",
    "content" : system_prompt
}

message = {                                            
    "role" : role,
    "content" : User_prompt
}

messages = [message_system, message]                 

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)

answer = response.choices[0].message.content

raw_jobD = answer 

job_data = json.loads(raw_jobD)

Job = Job_D(**job_data)

# # PART 2

class Experience(BaseModel):
    company : str | None 
    role : str | None 
    duration : float | None 
    discription : str | None 
    skills : list[str] | None 

class Resume(BaseModel):
    Name : str | None 
    E_mail : str | None 
    Phone_number : int | None 
    Total_experience_in_Years : int | None 
    Experiences : list[Experience] | None 
    Skills : list[str] | None 
    Projects : list[str] | None
    Certifications : list[str] | None 

Resume_schema = Resume.model_json_schema()

# PART 3

from pypdf import PdfReader
from docx import Document
import docx2txt

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def read_docx(file_path):
    return docx2txt.process(file_path)

def read_resume(file_path):
    if file_path.suffix.lower() == ".pdf":
        return read_pdf(file_path)
    elif file_path.suffix.lower() == ".docx":
        return read_docx(file_path)
    else:
        return None

# PART 4

file_path = Path("resumes\\ZURAIDE ELORRIAGA.docx")

# if file_path.suffix.lower() != ".pdf" or file_path.suffix.lower() != ".docx":
#     print("Not a proper formate of resume")

print("Proessing........" + file_path.name)

resume_text = read_resume(file_path)


def parsed_resume(resume_text, Resume_schema):

    system_prompt = f"""

    You are an expert resume parser.

    Extract information from the resume based on its meaning, not only based on exact section headings.

    Different resumes may use different headings.

    For example:
    - Experience
    - Professional Experience
    - Work History
    - Employment
    - Internships

    These may all contain relevant experience.

    Skills may also appear in the skills section, work experience, internships or projects.

    Return ONLY valid JSON matching this schema:

    {Resume_schema}

    Important rules:

    1. Do not invent information.
    2. If a value is not available, return null.
    3. If a list has no information, return an empty list.
    4. Include internships inside experiences.
    5. Extract skills mentioned across the entire resume.

    """

    User_prompt = f"""
    Parse the given Resume text. {resume_text}
    """

    message_system ={
    "role" : "system",
    "content" : system_prompt
    }

    message = {
        "role" : "user",
        "content" : User_prompt
    }

    response_format = {
        "type" : "json_object"
    }

    messages = [message_system, message]                 

    response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)

    answer = response.choices[0].message.content

    raw_resume = answer 

    resume_data = json.loads(raw_resume)

    resume  = Resume(**resume_data)

    return resume

Resume_txt = parsed_resume(resume_text, Resume_schema)

class Match_score(BaseModel):
    score : float
    details : dict

Score_schema = Match_score.model_json_schema()

def Final_score(Job, Resume_txt, Score_schema):

    prompt = f"""
    
    You are an HR recruiter.

    Compare the candidate's resume with the job description.

    JOB DESCRIPTION:
    {Job.model_dump_json(indent=2)}

    CANDIDATE RESUME:
    {Resume_txt.model_dump_json(indent=2)}
    Return JSON matching this schema:

    {Score_schema}

    Give me:

    1. Candidate name
    2. Matching skills
    3. Missing important skills
    4. Whether experience requirement is met
    5. Overall match percentage from 0 to 100
    6. And a Final Verdict for this score

    """

    response_Format = {
        "type" : "json_object"
    }

    message = {
        "role" : "user",
        "content" : prompt
    }

    messages = [message]                 

    response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)

    answer = response.choices[0].message.content

    raw_score = answer 

    score = json.loads(raw_score)

    score  = Match_score(**score)

    return score

score = Final_score(Job, Resume_txt, Score_schema)
print(score)
print(score.score)
# print(resume_text)
# print(score.details.Final_Verdict)