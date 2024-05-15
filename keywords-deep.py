# Keywords
# Extract keywords from a block of text
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

text = "You will be provided with a block of text, and your task is to extract a list of keywords from it."

user = """
Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors.
"""

prompt = f"{user}\n\n{text}"

response = get_completion(prompt)
print(response)

# Response at:
# 1. Black-on-black ware
# 2. Puebloan
# 3. Native American
# 4. Pottery
# 5. Northern New Mexico
# 6. Reduction-fired
# 7. Burnishing
# 8. Refractory slip
# 9. Carving
# 10. Incising
# 11. Polishing
# 12. Kha'po Owingeh
# 13. P'ohwhóge Owingeh
# 14. Matriarch potters
# 15. Contemporary artists
# 16. Ancestors