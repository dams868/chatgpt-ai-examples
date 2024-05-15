# Python bug fixer
# Find and fix bugs in source code
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

text = "You will be provided with a piece of Python code, and your task is to find and fix bugs in it."

user = """
import Random
    a = random.randint(1,12)
    b = random.randint(1,12)
    for i in range(10):
        question = "What is "+a+" x "+b+"? "
        answer = input(question)
        if answer = a*b
            print (Well done!)
        else:
            print("No.")
"""

prompt = f"{user}\n\n{text}"

response = get_completion(prompt)
print(response)

# Response:

# Here is the corrected code:
# 
# ```python
# import random
# a = random.randint(1,12)
# b = random.randint(1,12)
# for i in range(10):
#     question = "What is "+str(a)+" x "+str(b)+"? "
#     answer = int(input(question))
#     if answer == a*b:
#         print("Well done!")
#     else:
#         print("No.")
# ```

# Changes made:
# 1. Imported `random` module correctly.
# 2. Converted `a` and `b` to strings when creating the question string.
# 3. Converted the user input to an integer.
# 4. Fixed the comparison operator in the `if` statement.