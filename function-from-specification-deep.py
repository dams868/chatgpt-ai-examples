# Function from specification
# Create a Python function from a description
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
Write a Python function that takes as input a file path to an image, loads the image into memory as a numpy array, then crops the rows and columns around the perimeter if they are darker than a threshold value. Use the mean value of rows and columns to decide if they should be marked for deletion.
"""

#prompt = f"{user}\n\n{system}"
prompt = f"{user}"

response = get_completion(prompt)
print(response)

# Response:
# Here is a Python function that accomplishes the task described:

# ```python
# import cv2
# import numpy as np

# def crop_dark_perimeter(image_path, threshold=100):
#     # Load the image
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
#     # Calculate the mean value of rows and columns
#     row_means = np.mean(image, axis=1)
#     col_means = np.mean(image, axis=0)
    
#     # Find rows and columns to crop
#     rows_to_crop = np.where(row_means < threshold)[0]
#     cols_to_crop = np.where(col_means < threshold)[0]
    
#     # Crop the image
#     cropped_image = image[rows_to_crop[-1]+1:rows_to_crop[0], cols_to_crop[-1]+1:cols_to_crop[0]]
    
#     return cropped_image

# # Example usage
# image_path = 'example.jpg'
# cropped_image = crop_dark_perimeter(image_path, threshold=100)
# ```

# This function first loads the image using OpenCV, then calculates the mean values of rows and columns. It identifies rows and columns that have mean values below the specified threshold and crops the image accordingly. Finally, it returns the cropped image as a numpy array.