# For In-Context Learning (ICL) task
# This script is used to perform in-context learning (ICL) on GSM8K dataset using deepseek-R1 model.

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
import json
import random

# Load environment variables from .env file
# especially for the API key
_ = load_dotenv(find_dotenv())

# Load GSM8K Questions
sampled_examples_path = os.path.join(os.getenv("WORKING_DIR"), "sampled_examples.json")
with open(sampled_examples_path, 'r') as f:
    examples = json.load(f) 
    # list of 3 dictionaries
    # each dictionary like:
    # {
    #     "question": "What is 2 + 2?",
    #     "answer": "4"
    # }
    
# Create OpenAI client
api_key = os.getenv("DEEPSEEK_API_KEY")
if api_key is None:
    raise ValueError("API key not found. Please set the DEEPSEEK_API_KEY environment variable.")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    
# Prepare the messages for the chat completion
system_message = """You are a helpful assistant. Please solve the following three reasoning-based questions from the GSM-8K dataset. Provide a detailed step-by-step solution for each question to clearly show your logical process, and then state the final answer. Ensure the output is in a structured format, such as JSON, and includes the following fields:
    • Question ID
    • Reasoning Process (a list)
    • Final Answer
    • Difficulty Classification",
"""

system_message_2 = "You are a helpful assistant specialized in solving mathematical reasoning problems from the GSM-8K dataset. For each question, provide a detailed step-by-step reasoning process as a list of logical steps, the final numerical answer, and assign a difficulty classification (Easy/Medium/Hard). Ensure the output strictly follows the specified JSON format with all required fields."

# Extract questions and answers from examples
user_message = f"""
    Here are three reasoning-based questions from the GSM-8K dataset:
    1. Question: {examples[0]["question"]}
    2. Question: {examples[1]["question"]}
    3. Question: {examples[2]["question"]}
    Please solve these questions step by step and provide the final answers.
    """
    
user_message_2 = f"""Here are demonstration examples of solving GSM-8K problems, followed by the questions you need to answer. Study the structure and reasoning style carefully:\n\n### Demonstration Example 1\n**Question ID**: DEMO1\n**Question**: A bookstore sells 35 novels in the morning and twice as many in the afternoon. If they had 150 novels in stock at the start, how many remain unsold?\n**Reasoning Process**: [\n  \"Calculate afternoon sales: 35 novels * 2 = 70 novels\",\n  \"Sum total sales: 35 novels + 70 novels = 105 novels\",\n  \"Subtract total sales from stock: 150 novels - 105 novels = 45 novels\"\n]\n**Final Answer**: 45\n**Difficulty Classification**: Medium\n\n### Demonstration Example 2\n**Question ID**: DEMO2\n**Question**: A baker uses 2 cups of flour for each loaf of bread. If she has a 50-cup bag of flour and bakes 12 loaves, how many cups of flour remain?\n**Reasoning Process**: [\n  \"Calculate flour used: 12 loaves * 2 cups/loaf = 24 cups\",\n  \"Subtract used flour from total: 50 cups - 24 cups = 26 cups\"\n]\n**Final Answer**: 26\n**Difficulty Classification**: Easy\n\n### Now Solve These Questions\n1. **Question ID**: Q1\n   **Question**: {examples[0]["question"]}\n2. **Question ID**: Q2\n   **Question**: {examples[1]["question"]}\n3. **Question ID**: Q3\n   **Question**: {examples[2]["question"]}\n
"""

messages = [
    {"role": "system", "content": system_message_2},
    {"role": "user", "content": user_message_2}
]

# Call the chat completion API
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages,
    stream=False
)

# Print the response
print("Response:")
response_str = response.choices[0].message.content
print(response.choices[0].message.content)

# Save the response to a file
response_path = os.path.join(os.getenv("WORKING_DIR"), "response.json")
with open(response_path, 'w') as f:
    # 去掉里面的```json ```
    cleaned_response = response_str.replace("```json", "").replace("```", "")
    f.write(cleaned_response)
    





# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)