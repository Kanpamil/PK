from PIL import Image
import numpy as np
import random

def bialo_czarne(image, threshold=128):
    return image.convert("L").point(lambda p: 255 if p > threshold else 0, mode='1')

def generate_shares(image_path):
    image = Image.open(image_path)
    image = bialo_czarne(image)
    width, height = image.size

    udzial1 = Image.new('1', (width * 2, height * 2))
    udzial2 = Image.new('1', (width * 2, height * 2))

    pixels = image.load()
    s1 = udzial1.load()
    s2 = udzial2.load()

    patterns = [
        ([1, 1, 0, 0], [1, 1, 0, 0]),
        ([0, 0, 1, 1], [0, 0, 1, 1]),
        ([1, 0, 1, 0], [1, 0, 1, 0]),
        ([0, 1, 0, 1], [0, 1, 0, 1]), 
        ([1, 0, 0, 1], [1, 0, 0, 1]),  
        ([0, 1, 1, 0], [0, 1, 1, 0]),  
    ]

    for y in range(height):
        for x in range(width):
            pixel = 0 if pixels[x, y] == 0 else 1
            pattern = random.choice(patterns)
            p1 = pattern[0]
            p2 = pattern[1] if pixel == 1 else [1 - i for i in pattern[0]]

            for dy in range(2):
                for dx in range(2):
                    idx = dy * 2 + dx
                    if p1[idx] == 1:
                        s1[x * 2 + dx, y * 2 + dy] = 255
                    else:
                        s1[x * 2 + dx, y * 2 + dy] = 0
                        
                    if p2[idx] == 1:
                        s2[x * 2 + dx, y * 2 + dy] = 255
                    else:
                        s2[x * 2 + dx, y * 2 + dy] = 0

    return udzial1, udzial2

def combine_shares(udzial1, udzial2):
    width, height = udzial1.size
    result = Image.new('1', (width, height))
    p1 = udzial1.load()
    p2 = udzial2.load()
    r = result.load()

    for y in range(height):
        for x in range(width):
            if p1[x,y] == 0 or p2[x,y] == 0:
                r[x,y] = 0
            else:
                r[x,y] = 1
    return result


if __name__ == "__main__":
    udzial1, udzial2 = generate_shares("LAB5/tajemnica.png")
    udzial1.save("udzial1.png")
    udzial2.save("udzial2.png")

    recovered = combine_shares(udzial1, udzial2)
    recovered.save("zlozone.png")
