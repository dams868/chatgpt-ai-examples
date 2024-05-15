# Product name generator
# Generate product names from a description and seed words.
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

text = "You will be provided with a product description and seed words, and your task is to generate product names."

user = """
Product description: A home milkshake maker
    Seed words: fast, healthy, compact.
"""

prompt = f"{user}\n\n{text}"

response = get_completion(prompt)
print(response)

# Response:
# 1. QuickBlend Milkshake Maker
# 2. NutriShake Compact Mixer
# 3. SpeedySmooth Milkshake Machine
# 4. HealthFusion Shake Maker
# 5. CompactBlend Milkshake Mixer
# 6. FastFroth Milkshake Maker
# 7. HealthyWhip Milkshake Blender
# 8. QuickMix Milkshake Machine
# 9. CompactChurn Milkshake Maker
# 10. SpeedySip Milkshake Mixer