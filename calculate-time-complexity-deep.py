# Calculate time complexity
# adapted from https://platform.openai.com/examples
# Find the time complexity of a function.

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
You will be provided with Python code, and your task is to calculate its time complexity.
"""
prompt = f"""
def foo(n, k):
        accum = 0
        for i in range(n):
            for l in range(k):
                accum += i
        return accum
```{text}```
"""
response = get_completion(prompt)
print(response)

# Response at:
# The time complexity of the given code is O(n*k) because there are two nested loops, one running n times and the other running k times. This results in a total of n*k iterations, making the time complexity O(n*k).