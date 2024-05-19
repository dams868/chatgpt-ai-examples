# Parse unstructured data
# adapted from https://platform.openai.com/examples
# Create tables from unstructured text.

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
You will be provided with unstructured data, and your task is to parse it into CSV format.
"""
prompt = f"""
There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy. There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. Pounits are a bright green color and are more savory than sweet. There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them.
```{text}```
"""
response = get_completion(prompt)
print(response)

# Response at:
# Fruit Name, Color, Flavor
# neoskizzles, purple, candy
# loheckles, grayish blue, tart
# pounits, bright green, savory
# loopnovas, neon pink, cotton candy
# glowls, pale orange, sour/bitter