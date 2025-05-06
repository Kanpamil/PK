from PIL import Image

text = "siemano czesc asdasdasdsadsadas"


text += "EnD"
bits_message = ''.join(format(byte, '08b') for byte in bytearray(text, 'utf-8'))
message_length = len(bits_message)
print(f"Message: {bits_message}")

img = Image.open('LAB6/image.png').convert('RGB')

width, height = img.size



msg_idx = 0
for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        if msg_idx >= message_length:
            break
        pixel = [r, g, b]
        for i in range(3):
            if msg_idx < message_length:
                bit = int(bits_message[msg_idx])
                pixel[i] = (pixel[i] & ~1) | bit
                msg_idx += 1
        img.putpixel((x, y), tuple(pixel))
    if msg_idx >= message_length:
        break
    
img.save('LAB6/hidden_image.png')