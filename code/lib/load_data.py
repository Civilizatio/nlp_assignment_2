# Load GSM8K dataset
from dotenv import load_dotenv, find_dotenv
import os
import json
import random

_ = load_dotenv(find_dotenv())

gsm8k_path = os.getenv("GSM8K_PATH") # jsonl file, we only use train file
if gsm8k_path is None:
    raise ValueError("GSM8K_PATH not found. Please set the GSM8K_PATH environment variable.")

# Randomly sample 3 examples from the GSM8K dataset
with open(gsm8k_path, 'r') as f:
    lines = f.readlines()
    examples = [json.loads(line) for line in lines]
    
# Sample 3 examples
examples = random.sample(examples, 3)

# Save the sampled examples to a file
sampled_examples_path = os.path.join(os.getenv("WORKING_DIR"), "sampled_examples.json")
with open("sampled_examples.json", 'w') as f:
    json.dump(examples, f, indent=4)
    

print("Examples:")
for example in examples:
    print(f"Question: {example['question']}")
    print(f"Answer: {example['answer']}")
    print()
    
print(f"Sampled examples saved to {sampled_examples_path}")
