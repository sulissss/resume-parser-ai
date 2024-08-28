from openai import OpenAI
from pydantic import BaseModel
from typing import List
from pydantic import BaseModel, Field
from enum import Enum
import instructor

class JobProfessions(str, Enum):
    DATA_SCIENTIST = "data_scientist"
    SOFTWARE_DEVELOPER = "software_developer"
    DATA_ENGINEER = "data_engineer"

class Skills(Enum):
    PROFESSION: JobProfessions

    @property
    def experience(self) -> int:
        return self._experience
    
    @experience.setter
    def experience(self, value: float) -> None:
        if value > 0.0:
            self._experience = value
        else:
            raise ValueError("Experience Value must be greater than 0.0 years")


class Resume(BaseModel):
    NAME: str
    EMAIL_ID: str
    PHONE_NUMBER: str
    SKILLS: List[Skills]
    PAST_JOBS: List[str] | None


client = instructor.from_openai(OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
),
    mode=instructor.Mode.JSON
)

few_shot_prompts = [
    {
        "role": "user",
        "content": "John Doe\nEmail: john.doe@example.com\nPhone: 123-456-7890\n\nJohn is a seasoned Software Developer with 5 years of experience. Skilled in Python, JavaScript, and SQL.\n\nExperience:\n- Software Engineer at TechCorp\n- Junior Developer at WebWorks"
    },
    {
        "role": "assistant",
        "content": '{"NAME": "John Doe", "EMAIL_ID": "john.doe@example.com", "PHONE_NUMBER": "123-456-7890", "SKILLS": [{"PROFESSION": "software_developer", "experience": 5}], "PAST_JOBS": ["Software Engineer at TechCorp", "Junior Developer at WebWorks"]}'
    },
    {
        "role": "user",
        "content": "Jane Smith\nContact: jane.smith@gmail.com | 987-654-3210\nSkilled in Python, C++, Java\n- Data Scientist at DataInsights\n Software Engineer at Microsoft 2010-2013 - Intern at AnalyticsPro."
    },
    {
        "role": "assistant",
        "content": '{"NAME": "Jane Smith", "EMAIL_ID": "jane.smith@gmail.com", "PHONE_NUMBER": "987-654-3210", "SKILLS": [{"PROFESSION": "data_scientist", "experience": 5.0}, {"PROFESSION": "software_developer": "experience": 3.0}], "PAST_JOBS": ["Data Scientist at DataInsights", "Intern at AnalyticsPro"]}'
    },
    {
        "role": "user",
        "content": """Alice Johnson
Email: alice.johnson@company.com
Phone: 555-123-4567

Experienced Data Engineer with over 4 years in the industry. Expertise in ETL processes, data warehousing, and cloud platforms like AWS.

Work Experience:
- Data Engineer at BigData Inc.
- ETL Developer at DataWorks"""
    }
]

response = client.chat.completions.create(
    model="llama3",
    max_retries=3,
    messages=few_shot_prompts,
    response_model=Resume
)

print(response.model_dump_json(indent=2))