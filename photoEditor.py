from PIL import Image, ImageEnhance, ImageFilter
import os;

path = "./imgs"
pathOut = "/editedImgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN()).convert('L') # To do the image a little bit sharpened and using convert it will return us the black n white image

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit) 
    edit = enhancer.enhance(factor) # We use factor to adjust the contrast of the image copy

    clean_name = os.path.splitext(filename)[0] # With this we get rid of the extension for example if we have "Mario1.png" then we will get "Mario1"

    edit.save(f".{pathOut}/{clean_name}_edited.jpg") # And then we save it
