from PIL import Image

img = Image.open('LAB6/hidden_image.png').convert('RGB')
end_mark ="EnD"
width, height = img.size
message = ""
bits = []
for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        pixel = [r, g, b]
        for i in range(3):
            if len(bits) == 8:
                char = chr(int(''.join(bits), 2))
                bits.clear()
                message += char
                if message.endswith(end_mark):
                    break
            bits.append(str(pixel[i] & 1))
        if message.endswith(end_mark):
            break
    if message.endswith(end_mark):
        break

print("Odczytana wiadomosc:", message[:-len(end_mark)])  # Usuwamy znacznik końca