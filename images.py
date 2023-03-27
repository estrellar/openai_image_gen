import openai
import os
from dotenv import load_dotenv
import cv2
import base64

#load key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create_edit(
  image=open('daisy_stare.png', 'rb'),
  mask=open('daisy_stare_mask.png','rb'),
  prompt="Cat in space",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
