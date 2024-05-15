# Explain code
# Explain a complicated piece of code.
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

text = "You will be provided with a piece of code, and your task is to explain it in a concise way."

code = """
class Log:
    def __init__(self, path):
        dirname = os.path.dirname(path)
        os.makedirs(dirname, exist_ok=True)
        f = open(path, "a+")
    
        # Verifica que el archivo termine con una nueva línea
        size = os.path.getsize(path)
        if size > 0:
            f.seek(size - 1)
            end = f.read(1)
            if end != "\\n":
                f.write("\\n")
        self.f = f
        self.path = path

    def log(self, event):
        event["_event_id"] = str(uuid.uuid4())
        json.dump(event, self.f)
        self.f.write("\\n")

    def state(self):
        state = {"complete": set(), "last": None}
        for line in open(self.path):
            event = json.loads(line)
            if event["type"] == "submit" and event["success"]:
                state["complete"].add(event["id"])
                state["last"] = event
        return state
"""

prompt = f"{code}\n\n{text}"

response = get_completion(prompt)
print(response)

# Response at:
# This code defines a Log class that creates a log file, writes events to it in JSON format, and provides a method to retrieve the state of completed events. The log file is created if it doesn't exist, and each event is assigned a unique ID before being written to the file. The state method returns a dictionary with a set of completed event IDs and the details of the last completed event.