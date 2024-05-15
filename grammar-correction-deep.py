# Grammar correction
# adapted from https://platform.openai.com/examples
# Convert ungrammatical statements into standard English.

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
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    return response.choices[0].message["content"]

text = f"""
You will be provided with statements, and your task is to convert them to standard English.
"""
prompt = f"""
She no went to the market.
```{text}```
"""
response = get_completion(prompt)
print(response)

# Response at:

# She did not go to the market.
