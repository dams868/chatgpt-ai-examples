# Spreadsheet creator
# Create spreadsheets of various kinds of data.
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

user = """
Create a three-column CSV of top science fiction movies along with the year of release and protagonist.
"""

prompt = f"{user}"

response = get_completion(prompt)
print(response)

# Response:

# Movie,Year,Protagonist
# Blade Runner,1982,Rick Deckard
# The Matrix,1999,Neo
# Star Wars: A New Hope,1977,Luke Skywalker
# Inception,2010,Dominic Cobb
# E.T. the Extra-Terrestrial,1982,Elliott
# Interstellar,2014,Cooper
# Alien,1979,Ellen Ripley
# The Terminator,1984,Sarah Connor
# Avatar,2009,Jake Sully
# Back to the Future,1985,Marty McFly