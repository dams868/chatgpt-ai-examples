# Tweet classifier
# Detect sentiment in a tweet
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

system = "You will be provided with a tweet, and your task is to classify its sentiment as positive, neutral, or negative."

user = """
I loved the new Batman movie!
"""

prompt = f"{system}\n\n{user}"

response = get_completion(prompt)
print(response)

# Response:

# Positive