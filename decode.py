import sys
import os
from PIL import Image

def decode():
    image_name = input("Enter the name of the image: ")
    image = Image.open(image_name)
    pixels = image.load()
    width = image.size[0]
    height = image.size[1]
    data = ""
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            data += bin(red)[7]
            data += bin(green)[7]
            data += bin(blue)[7]
    data = [data[i:i+8] for i in range(0, len(data), 8)]
    decoded_data = ""
    test_data = ""
    for byte in data:
        if byte != "00000000" and byte != "0000000" and byte != "000000" and byte != "00000" and byte != "0000" and byte != "000" and byte != "00" and byte != "0":
            test_data += chr(int(byte, 2))
            if test_data[-11:] == "[ENDOFDATA]":
                test_data = test_data[:-11]
                break
            else:
                charlist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}|:"<>?`~-=[]\;\',./ '
                if str(chr(int(byte, 2))) in charlist:
                    decoded_data += str(chr(int(byte, 2)))
                else:
                    pass
        else:
            break
    decoded_data = decoded_data[:-10]
    print(decoded_data)

decode()
