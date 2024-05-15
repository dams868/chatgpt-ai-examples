# Emoji Translation
# adapted from https://platform.openai.com/examples
# Translate regular text into emoji text.

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

text = f"""
You will be provided with text, and your task is to translate it into emojis. Do not use any regular text. Do your best with emojis only.
"""
prompt = f"""
Artificial intelligence is a technology with great promise.
```{text}```
"""
response = get_completion(prompt)
print(response)

# Response at:
# 🤖🧠🌟