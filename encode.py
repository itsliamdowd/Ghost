import sys
import os
from PIL import Image

def encodeImage():
    image = Image.open(image_name)
    data = input("Enter the data to encode: ")
    data = data + "[ENDOFDATA]"
    if len(data) > image.size[0] * image.size[1]:
        print("The data is too large to fit in the image")
        sys.exit()
    data = ''.join(format(ord(i), '08b') for i in data)
    pixels = image.load()
    width = image.size[0]
    height = image.size[1]
    data_length = len(data)
    index = 0
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            if index < data_length:
                red = int(bin(red)[0:7] + data[index], 2)
                index += 1
            if index < data_length:
                green = int(bin(green)[0:7] + data[index], 2)
                index += 1
            if index < data_length:
                blue = int(bin(blue)[0:7] + data[index], 2)
                index += 1
            pixels[x, y] = (red, green, blue)
    image.save("encoded.png")

file_name = input("Enter the name of the file including the extension: ")
file_type = file_name.split('.')[1]
if file_type == "png":
    encodeImage()
else:
    print('Error')
