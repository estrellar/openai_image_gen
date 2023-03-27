# Setup

Images need the following requirements:
- < 4MB
- .png type
- format: RGBA (so needs opacity level
- 2 images: the original image and a mask of the image. The images in this dir are a bad example of the images, as the images should be a small mask (see the openai docs)
- The two aforementioned images need to be the same dimensions.

```
pip install -r requirements.txt

cp .env .env.example
#add your own openai api key to .env
```

run with `python gen_image.py`

