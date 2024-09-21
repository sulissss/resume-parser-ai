import json
from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional

# Initialize the LLM
llm = Ollama(model="llama3")

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

class CV(BaseModel):
    full_name: str
    email_address: str
    github_portfolio: Optional[str]
    linkedin_id: Optional[str]
    employment_details: Optional[List[str]]
    technical_skills: List[str]
    soft_skills: Optional[List[str]]

parser = JsonOutputParser(pydantic_object=CV)

# Define the chain using the prompt template and LLM
chain = prompt_template | llm | parser


def save_chat_history(filename="chat_history.json"):
    # Convert the chat history to a list of dictionaries
    history_data = [
        {"role": "human", "content": msg.content} if isinstance(msg, HumanMessage) else {"role": "AI", "content": msg.content}
        for msg in chat_history
    ]
    
    # Write the chat history to a file
    with open(filename, "w") as f:
        json.dump(history_data, f, indent=4)

def load_chat_history(filename="chat_history.json"):
    # Load chat history from a file
    global chat_history
    try:
        with open(filename, "r") as f:
            history_data = json.load(f)
            chat_history = [
                HumanMessage(content=msg["content"]) if msg["role"] == "human" else AIMessage(content=msg["content"])
                for msg in history_data
            ]
    except FileNotFoundError:
        # If file doesn't exist, start with an empty history
        chat_history = []

def start_app():
    load_chat_history()  # Load the previous chat history if it exists

    # Read the resume from the file
    with open('try_model/resume.txt', 'r') as file:
        resume = file.read()

    resume = resume.replace('\n', '')

    # Ensure resume content is properly formatted
    resume = resume.strip()

    # Define the question as the resume content
    question = "Return the following resume content as a JSON object strictly as per the format defined in the previous conversation: " + resume
    # question = "Give the response of the previous conversation"
    # question = resume
    if question == "done":
        save_chat_history()  # Save chat history when exiting
        return

    # Generate a response from the chain
    response = chain.invoke({"input": question, "chat_history": chat_history})
    
    # Ensure response is JSON
    # try:
    #     # Try to parse the response as JSON
    #     parsed_response = json.loads(response)
    # except json.JSONDecodeError:
    #     # Handle the case where response is not valid JSON
    #     parsed_response = {"error": "Response is not valid JSON."}

    # Append the new chat messages to history
    chat_history.append(HumanMessage(content=question))
    chat_history.append(AIMessage(content=response))
    
    # Print and return the AI response
    print("AI: ", response)
    print("\n\n\n\n\nParser: ", parser.parse(response))
    return response

if __name__ == "__main__":
    start_app()