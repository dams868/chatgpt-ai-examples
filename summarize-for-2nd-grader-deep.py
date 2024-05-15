# Summarize for a 2nd grader
# adapted from https://platform.openai.com/examples
# Simplify text to a level appropriate for a second-grade student.

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

text = f"""
Summarize content you are provided with for a second-grade student.
"""
prompt = f"""
Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.
```{text}```
"""
response = get_completion(prompt)
print(response)

# Response at:

# Jupiter is a big planet that is very far away from the Sun. It is made of gas and is much bigger than all the other planets combined. It is very bright in the sky at night and has been known to people for a long time. Jupiter is named after a Roman god. It is one of the