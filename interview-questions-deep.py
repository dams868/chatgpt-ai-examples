# Interview questions
# Create interview questions.
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

# system = ""

user = """
Create a list of 8 questions for an interview with a science fiction author.
"""

#prompt = f"{user}\n\n{system}"
prompt = f"{user}"

response = get_completion(prompt)
print(response)

# Response:
# 1. What inspired you to start writing science fiction?
# 2. How do you approach world-building in your stories?
# 3. Can you discuss the role of technology in your work and how it impacts your storytelling?
# 4. How do you incorporate scientific concepts and theories into your writing?
# 5. What do you think sets your science fiction writing apart from others in the genre?
# 6. How do you envision the future of humanity and technology in your stories?
# 7. Can you discuss any challenges you face when writing science fiction and how you overcome them?
# 8. How do you balance the speculative elements of science fiction with the emotional and human aspects of your characters?