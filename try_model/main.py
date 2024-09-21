from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from openai import OpenAI
import instructor
import json
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.document_loaders import PyPDFLoader
# from cv_model import CV


loader = PyPDFLoader("Tags, Ranking and Sample CVs/Sample CVs/Fayas .Net Developer.pdf")
pages = loader.load_and_split()
resume_content = "\n".join([page.page_content for page in pages])
# print(resume_content)

class CV(BaseModel):
    full_name: str
    email_address: str
    github_portfolio: Optional[str]
    linkedin_id: Optional[str]
    employment_details: Optional[List[str]]
    technical_skills: List[str]
    soft_skills: Optional[List[str]]

# Define the chat prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an AI resume parser. Your job is to analyze the resume content, and provide its relevant data accordingly. The current/present year is 2024. You'll be provided with a sample input and output to get an idea of what is expected. Provide all outputs as a JSON object."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)


client = instructor.from_openai(OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
),
    mode=instructor.Mode.JSON
)

chain = prompt_template | client

# with open('try_model/few_shots/r1.txt', 'r') as file:
#     r1_txt = file.read()

# with open('try_model/few_shots/r1.json', 'r') as file:
#     r1_json = file.read()

# r1_json = json.dumps(r1_json)

# with open('try_model/resume.txt', 'r') as file:
#     resume = file.read()

# resume.replace('\n', '')

# sample_input = """Alice Johnson
# Email: alice.johnson@company.com
# Phone: 555-123-4567

# Experienced Data Engineer with over 4 years in the industry. Expertise in ETL processes, data warehousing, and cloud platforms like AWS.

# Work Experience:
# - Data Engineer at BigData Inc. 2012-2014
# - ETL Developer at DataWorks. 2015-2020"""


# few_shot_prompts = [ 
#     {
#         "role": "system", 
#         "content": "Analyze the resume content, and provide its relevant data accordingly. The current/present year is 2024. You'll be provided with a sample input and output to get an idea of what is expected."
#     },
#     {"role": "user",
#      "content": r1_txt},
#      {"role": "assistant",
#       "content": r1_json},
#     {
#         "role": "user",
#         "content": resume
#     }
# ]

# response = client.chat.completions.create(
#     model="llama3",
#     max_retries=3,
#     messages=few_shot_prompts,
#     response_model=CV
# )

# print(response.model_dump_json(indent=2))