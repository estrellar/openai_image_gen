import openai
import os
from dotenv import load_dotenv

#load key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create_edit(
  image=open('daisy_smile.png', 'rb'),
  mask=open('daisy_smile_mask.png','rb'),
  prompt="Cat in space",
  n=4,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
