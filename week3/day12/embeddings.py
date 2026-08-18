import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer

load_dotenv()

model = SentenceTransformer('all-MiniLM-L6-v2')

def cosine_similarity(v1,v2):
    return np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))

text1 = input("Enter the first text to be embedded: ")
text2 = input("Enter the second text to embedded: ")

vec1 = model.encode(text1)
print()
vec2 = model.encode(text2)

print(cosine_similarity(vec1,vec2))