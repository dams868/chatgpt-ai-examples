# Turn by turn directions
# Convert natural language to turn-by-turn directions.
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

system = "You will be provided with a text, and your task is to create a numbered list of turn-by-turn directions from it."

user = """
    Go south on 95 until you hit Sunrise boulevard then take it east to us 1 and head south. Tom Jenkins bbq will be on the left after several miles.
"""

prompt = f"{user}\n\n{system}"

response = get_completion(prompt)
print(response)

# Response:
# 1. Head south on 95.
# 2. Continue on 95 until you reach Sunrise Boulevard.
# 3. Take Sunrise Boulevard east.
# 4. Continue on Sunrise Boulevard until you reach US 1.
# 5. Turn south onto US 1.
# 6. After several miles, Tom Jenkins BBQ will be on the left.