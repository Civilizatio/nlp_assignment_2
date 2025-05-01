from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
import json

_ = load_dotenv(find_dotenv())

# api_key = os.getenv("DEEPSEEK_API_KEY")
# if api_key is None:
#     raise ValueError("API key not found. Please set the DEEPSEEK_API_KEY environment variable.")
# client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)

response_path = os.path.join(os.getenv("WORKING_DIR"), "response.json")
with open(response_path, 'r') as f:
    response = f.read()
    
print("Response:")
print(response)

json_response = json.loads(response)
print("Parsed JSON Response:")
print(json_response)

{
    "system_message": "You are a helpful assistant specialized in solving mathematical reasoning problems from the GSM-8K dataset. For each question, provide a detailed step-by-step reasoning process as a list of logical steps, the final numerical answer, and assign a difficulty classification (Easy/Medium/Hard). Ensure the output strictly follows the specified JSON format with all required fields.",
    
    "user_message": "Here are demonstration examples of solving GSM-8K problems, followed by the questions you need to answer. Study the structure and reasoning style carefully:\n\n### Demonstration Example 1\n**Question ID**: DEMO1\n**Question**: A bookstore sells 35 novels in the morning and twice as many in the afternoon. If they had 150 novels in stock at the start, how many remain unsold?\n**Reasoning Process**: [\n  \"Calculate afternoon sales: 35 novels * 2 = 70 novels\",\n  \"Sum total sales: 35 novels + 70 novels = 105 novels\",\n  \"Subtract total sales from stock: 150 novels - 105 novels = 45 novels\"\n]\n**Final Answer**: 45\n**Difficulty Classification**: Medium\n\n### Demonstration Example 2\n**Question ID**: DEMO2\n**Question**: A baker uses 2 cups of flour for each loaf of bread. If she has a 50-cup bag of flour and bakes 12 loaves, how many cups of flour remain?\n**Reasoning Process**: [\n  \"Calculate flour used: 12 loaves * 2 cups/loaf = 24 cups\",\n  \"Subtract used flour from total: 50 cups - 24 cups = 26 cups\"\n]\n**Final Answer**: 26\n**Difficulty Classification**: Easy\n\n### Now Solve These Questions\n1. **Question ID**: Q1\n   **Question**: Nancy is crafting clay pots to sell. She creates 12 clay pots on Monday, twice as many on Tuesday, a few more on Wednesday, then ends the week with 50 clay pots. How many did she create on Wednesday?\n2. **Question ID**: Q2\n   **Question**: For the first hour of work, Manolo can make face-masks at the rate of one every four minutes. Thereafter, he can make face-masks at the rate of one every six minutes. How many face-masks does Manolo make in a four-hour shift?\n3. **Question ID**: Q3\n   **Question**: The Tigers played 56 home games this year. They had 12 losses and half as many ties. How many games did they win?"
}