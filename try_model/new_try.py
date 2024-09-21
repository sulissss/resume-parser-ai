from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from cv_model import CV
from typing import Dict
import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
        base_url="http://localhost:11434/v1",
        api_key='ollama',
        model="llama3",
        max_tokens=1024,
    )

system_message = """Your task is to extract structured information from a resume and map it to predefined categories based on the provided schema. The resume data should be parsed into a JSON format, ensuring the accuracy and relevance of the extracted details. Each section of the resume should correspond to its respective model field, and all entries must be well-formatted, complete, and consistent with the following structure:

	1.	Personal Information: Includes full name, contact details, address, and optional profile links.
	2.	Objective or Summary: A career objective or summary statement that reflects the individual's professional goals.
	3.	Professional Experience: Details of past or current job roles, including company, title, dates, responsibilities, and achievements.
	4.	Education: Includes degrees, institutions, dates, and academic performance.
	5.	Skills: A list of technical and soft skills, including languages known by the individual.
	6.	Certifications and Courses: Any relevant certifications and courses, along with issuing organizations and completion dates.
	7.	Projects: Descriptions of personal or professional projects, including roles and technologies used.
	8.	Awards and Achievements: Information about any awards or recognitions the individual has received.
	9.	Publications and Research: Academic publications and research projects, including dates and details.
	10.	Volunteering or Community Service: Descriptions of volunteer work or community involvement.
	11.	Hobbies and Interests: (Optional) Information about personal hobbies and interests.
	12.	References: (Optional) List of professional references with contact information.
	13.	Additional Information: (Optional) Any other relevant information that does not fit into the above categories.

Each section of the extracted content should be carefully assigned to its corresponding field in the JSON. Ensure that dates are in the format YYYY-MM-DD and lists are properly populated for fields that accept multiple entries (e.g., job responsibilities, skills, certifications). If any optional information is missing, leave the fields as None or omit them.
The expected JSON structure is as follows: {json_structure}"""

with open('sample_outputs.txt', 'r') as file:
    json_structure = file.read()

with open('try_model/resume.txt', 'r') as file:
    texts = file.read()

structured_llm = llm.with_structured_output(CV, method="json_mode")
system_prompt = system_message.format(json_structure=json_structure)
prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("human", "{input}")]
)
few_shot_structured_llm = prompt | structured_llm
input_prompt = f"raw_texts: {texts}"
data = few_shot_structured_llm.invoke({"input": input_prompt})
print(data)