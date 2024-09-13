from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List, Dict
from enum import Enum
import instructor
from cv_model import CV, PersonalInformation
import json


client = instructor.from_openai(
    OpenAI(
        base_url='http://localhost:11434/v1',
        api_key='ollama',
    ), 
    mode=instructor.Mode.JSON
)

with open('examples/resume1.txt', 'r') as file:
    sample_input = file.read()

with open('sample_outputs.txt', 'r') as file:
    sample_outputs = file.read()

with open('examples/resume2.txt', 'r') as file:
    resume2 = file.read()


few_shot_prompts = [
    {
        "role": "system",
        "content": "You are a Job Resume Parser. You are to analyze the contents of the following resume and provide its relevant data accordingly as a JSON object. The current/present year is 2024. You will be provided with a sample input and output." 
    },
    # {"role": "user", "content": sample_input},
    # {"role": "assistant", "content": sample_outputs},
    {"role": "user", "content": resume2},
]

response = client.chat.completions.create(
    model="llama3",
    max_retries=3,
    messages=few_shot_prompts,
    response_model=CV
)

# # # Parse the response and calculate the resume score
# # parsed_resume = response
# # resume_score = calculate_resume_score(parsed_resume, job_description)

# # print(f"Resume Score: {resume_score}%")

print(response.model_dump_json(indent=2))