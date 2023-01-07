import os
from PIL import Image
import natsort
import time
import asyncio
import os
from tqdm import tqdm
try:
    os.mkdir("ascii_2")
except:
    pass
ascii_characters_by_surface = " ^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@■"
#ascii_characters_by_surface = ".^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@&"
async def convert_to_ascii_art(image, name):
    ascii_art = []
    (width, height) = image.size
    for y in range(0, height - 1):
        line = ''
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            line += convert_pixel_to_character(px)
        ascii_art.append(line)
    with open(os.path.join("ascii_2", name+'.txt'), 'w') as f:
        for line in ascii_art:
            f.write(line+'\n')
def convert_pixel_to_character(pixel):
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    max_brightness = 255 * 3
    brightness_weight = len(ascii_characters_by_surface) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    if index<0:
        index=0
    return ascii_characters_by_surface[index]
#1920.................1080
#100..................x
def generate_ascii_txt():
    images=[]
    if os.path.exists("frames_2")==False:
        files=os.listdir("frames")
        files=natsort.natsorted(files)
        os.mkdir("frames_2")
        print ("Generating updated frames...")
        for file in tqdm(files):
            file_name=os.path.splitext(file)[0]
            path=os.path.join("frames", file)
            image=Image.open(path)
            image=image.resize((378, 86))
            image = image.convert('RGB')
            image.save(os.path.join("frames_2", file))
        print ("Updating Images done... Please run again to generate ascii art")
    else:
        print ("Generating ascii art...")
        files=os.listdir("frames_2")
        files=natsort.natsorted(files)
        i=0
        for file in tqdm(files):
            i+=1
            file_name=os.path.splitext(file)[0]
            path=os.path.join("frames_2", file)
            image=Image.open(path)
            asyncio.run(convert_to_ascii_art(image, file_name))
if __name__=="__main__":
    generate_ascii_txt()
