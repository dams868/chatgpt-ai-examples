# VR fitness idea generator
# Generate ideas for fitness promoting virtual reality games.
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
Brainstorm some ideas combining VR and fitness.
"""

prompt = f"{user}"

response = get_completion(prompt)
print(response)

# Response:
# 1. VR fitness classes: Create virtual reality fitness classes where users can participate in a variety of workouts such as yoga, HIIT, dance, and more from the comfort of their own home.

# 2. VR personal training sessions: Offer virtual reality personal training sessions where users can work one-on-one with a trainer to receive personalized workouts and feedback.

# 3. VR fitness challenges: Create virtual reality fitness challenges where users can compete against each other in various fitness activities such as running, cycling, or weightlifting.

# 4. VR fitness games: Develop virtual reality fitness games that require physical movement to play, such as boxing, dancing, or obstacle courses.

# 5. VR outdoor adventures: Create virtual reality experiences that simulate outdoor activities such as hiking, mountain biking, or rock climbing to provide a fun and immersive way to stay active indoors.

# 6. VR meditation and relaxation: Offer virtual reality meditation and relaxation experiences to help users de-stress and improve their mental well-being while also incorporating physical movement and mindfulness practices.

# 7. VR fitness tracking and analytics: Develop virtual reality fitness apps that track users' movements and provide real-time feedback on their form, progress, and performance to help them reach their fitness goals.