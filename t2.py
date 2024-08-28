from openai import OpenAI
from pydantic import BaseModel
from typing import List
import instructor


class UserDetail(BaseModel):
    name: str
    age: int | None
    skills: str | None

# Enables `response_model` in create call
client = instructor.from_openai(
    OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    ),
    mode=instructor.Mode.JSON,
)

# Few-shot examples
few_shots = [
    {
        "role": "user",
        "content": "John works as a software developer.",
    },
    {
        "role": "assistant",
        "content": '{"name": "John", "age": 28, "skills": "Software Development"}',
    },
    {
        "role": "user",
        "content": "Jane is a data scientist.",
    },
    {
        "role": "assistant",
        "content": '{"name": "Jane", "age": 28, "skills": "Data Science"}',
    },
    {
        "role": "user",
        "content": "Bob does the same job as John.",
    }
]

# Main input you want to process
messages = few_shots

# Combine few-shot examples with the main input
# messages = few_shots + [main_input]

# Call the API with the few-shot examples
user = client.chat.completions.create(
    model="llama3",
    messages=messages,
    response_model=UserDetail,
)

print(user)
# print(user.model_dump_json(indent=2))
#> name='Jason' age=30