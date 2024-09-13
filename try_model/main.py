from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from openai import OpenAI
import instructor
import json

class CV(BaseModel):
    full_name: str
    email_address: str
    github_portfolio: Optional[str]
    linkedin_id: Optional[str]
    employment_details: Optional[List[str]]
    technical_skills: List[str]
    soft_skills: Optional[List[str]]


client = instructor.from_openai(OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
),
    mode=instructor.Mode.JSON
)

with open('try_model/few_shots/r1.txt', 'r') as file:
    r1_txt = file.read()

with open('try_model/few_shots/r1.json', 'r') as file:
    r1_json = file.read()

r1_json = json.dumps(r1_json)

with open('try_model/resume.txt', 'r') as file:
    resume = file.read()


# sample_input = """Alice Johnson
# Email: alice.johnson@company.com
# Phone: 555-123-4567

# Experienced Data Engineer with over 4 years in the industry. Expertise in ETL processes, data warehousing, and cloud platforms like AWS.

# Work Experience:
# - Data Engineer at BigData Inc. 2012-2014
# - ETL Developer at DataWorks. 2015-2020"""


few_shot_prompts = [ 
    {
        "role": "system", 
        "content": "Analyze the resume content, and provide its relevant data accordingly. The current/present year is 2024. You'll be provided with a sample input and output to get an idea of what is expected."
    },
    {"role": "user",
     "content": r1_txt},
     {"role": "assistant",
      "content": r1_json},
    {
        "role": "user",
        "content": resume
    }
]

response = client.chat.completions.create(
    model="gemma2",
    max_retries=3,
    messages=few_shot_prompts,
    response_model=CV
)

print(response.model_dump_json(indent=2))