from openai import OpenAI
from pydantic import BaseModel
from typing import List
from pydantic import BaseModel, Field
from enum import Enum
import instructor

class FieldExpertise(str, Enum):
    DATA_SCIENTIST = "data_scientist"
    SOFTWARE_DEVELOPER = "software_developer"
    DATA_ENGINEER = "data_engineer"

class ExperienceLevel(BaseModel):
    JOB: FieldExpertise
    EXPERIENCE: float = Field(description = "How much experience does the person have in the field")

client = instructor.from_openai(OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
),
    mode=instructor.Mode.JSON,
)

response = client.chat.completions.create(
    model="llama3",
    response_model=ExperienceLevel,
    messages=[
        {"role": "system", "content": "Analyze the following resume, and provide its relevant data accordingly."},
        {"role": "user", "content": "Rufus Stewart Data Engineer More than 10 years experience in the field."},
        {"role": "assistant", "content": "{'JOB': 'data_engineer', 'EXPERIENCE': 10.0}"},
        {"role": "user", "content": "John Mark Worked in data science-related projects from 2018 to 2023."},
        {"role": "assistant", "content": "{'JOB': 'data_scientist', 'EXPERIENCE': 5.0}"},
        {"role": "user", "content": "Name: Stuart Broadmore. Age: 36. Skills: Python, SQL, C++ Previous Jobs: Data Engineer 2020 - 2022."},
        {"role": "assistant", "content": "{'JOB': 'data_engineer', 'EXPERIENCE': 2.0}"},
        {"role": "user", "content": "Michael Bird. Hi, I worked for Microsoft's AI research team. I worked as a data scientist there from 2015-2023."}
    ]
)

print(response.model_dump_json(indent=2))