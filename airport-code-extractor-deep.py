# Airport code extractor
# Extract airport codes from text
# adapted from https://platform.openai.com/examples

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

system = "You will be provided with a text, and your task is to extract the airport codes from it."

user = """
I want to fly from Orlando to Boston
"""

prompt = f"{system}\n\n{user}"

response = get_completion(prompt)
print(response)

# Response:
# MCO (Orlando) and BOS (Boston)