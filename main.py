from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from cv_model import CV, PersonalInformation
import instructor

class JobProfessions(str, Enum):
    DATA_SCIENTIST = "data_scientist"
    SOFTWARE_DEVELOPER = "software_developer"
    DATA_ENGINEER = "data_engineer"
    ETL_DEVELOPER = "etl_developer"

class JobExperience(BaseModel):
    PROFESSION: JobProfessions
    COMPANY: str | None
    EXPERIENCE: float
    
    # def __post_init__(self):
    #     if self.EXPERIENCE < 0.0:
    #         raise ValueError("Experience Value must be greater than 0.0 years")


class Resume(BaseModel):
    NAME: str
    EMAIL_ID: str
    PHONE_NUMBER: List[str]
    JOB_EXPERIENCE: List[JobExperience]
    SKILLS: List[str]


client = instructor.from_openai(OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
),
    mode=instructor.Mode.JSON
)

sample_input = """Alice Johnson
Email: alice.johnson@company.com
Phone: 555-123-4567

Experienced Data Engineer with over 4 years in the industry. Expertise in ETL processes, data warehousing, and cloud platforms like AWS.

Work Experience:
- Data Engineer at BigData Inc. 2012-2014
- ETL Developer at DataWorks. 2015-2020"""


few_shot_prompts = [ 
    {
        "role": "system", 
        "content": "Analyze the resume content, and provide its relevant data accordingly. The current/present year is 2024."
    },
    {
        "role": "user",
        "content": "John Doe\nEmail: john.doe@outlook.com\nPhone: 123-456-7890\n\nSKILLS Python, JavaScript, and SQL.\n\nExperience:\n- Software Engineer at TechCorp - 2012-17\n- Senior Developer at WebWorks 2017-Present"
    },
    {
        "role": "assistant",
        "content": '{"NAME": "John Doe", "EMAIL_ID": "john.doe@outlook.com", "PHONE_NUMBER": "123-456-7890", "JOB_EXPERIENCE": [{"PROFESSION": "software_developer", "COMPANY": "TechCorp", "EXPERIENCE": 5.0}, {"PROFESSION": "senior_developer", "COMPANY": "WebWorks", "EXPERIENCE": 7.0}], "SKILLS": ["Python", "JavaScript", "SQL"]}'
    },
    {
        "role": "user",
        "content": "Jane Smith\nContact: jane.smith@gmail.com | 987-654-3210\nHave experience in Cloud Computing AWS Azure\n- Data Scientist at DataInsights 06/2010-12/2011\n Software Engineer @ Microsoft 08/2012-08/2023"
    },
    {
        "role": "assistant",
        "content": '{"NAME": "Jane Smith", "EMAIL_ID": "jane.smith@gmail.com", "PHONE_NUMBER": "987-654-3210", "JOB_EXPERIENCE": [{"PROFESSION": "software_engineer", "COMPANY": "DataInsights", "experience": 1.5}, {"PROFESSION": "software_developer": "experience": 3.0}], "SKILLS": ["Cloud", "Computing", "AWS", "Azure"]'
    },
    {
        "role": "user",
        "content": sample_input
    }
]

response = client.chat.completions.create(
    model="llama3",
    max_retries=3,
    messages=few_shot_prompts,
    response_model=Resume
)

# print(response)
print(response.model_dump_json(indent=2))