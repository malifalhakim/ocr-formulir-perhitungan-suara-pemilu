from PIL import Image
import random
import glob
from pathlib import Path

from straug.noise import GaussianNoise
from straug.camera import Brightness,Pixelate,Contrast, JpegCompression
from straug.blur import DefocusBlur,GlassBlur
from straug.weather import Frost

# Load Image in path augmentation
image_path = "augmentation//"
image_path = list(glob.glob(image_path + "*.jpg"))
image_path = sorted(image_path)
image_path = list(map(str, image_path))
images = image_path


for image in images:
    img = Image.open(image)

    # Brightness augmentation
    img_bright = Brightness()(img,mag=3)
    filename = "augmentation_result//" + Path(image).stem + "_bright.jpg"
    img_bright.save(filename)

    # Contrass augmentation
    img_contrass = Contrast()(img,mag=3)
    filename = "augmentation_result//" + Path(image).stem + "_contrass.jpg"
    img_contrass.save(filename)

    # Defocus blur augmentation
    img_blur = DefocusBlur()(img,mag=3)
    filename = "augmentation_result//" + Path(image).stem + "_blur.jpg"
    img_blur.save(filename)

    # Glass blur augmentation
    img_glass = GlassBlur()(img)
    filename = "augmentation_result//" + Path(image).stem + "_glass.jpg"
    img_glass.save(filename)


    # Randomly choose an augmentation
    rand = random.randint(1,4)
    
    if rand == 1:
        img = GaussianNoise()(img,mag=3)
    elif rand == 2:
        img = JpegCompression()(img,mag=3)
    elif rand == 3:
        img = Frost()(img,mag=3)
    else:
        img = Pixelate()(img,mag=3)
    
    # Save the image with a new name in a different directory
    filename = "augmentation_result//" + Path(image).stem + "_random.jpg"
    print(filename)
    img.save(filename)


