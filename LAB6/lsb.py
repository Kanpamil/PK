from PIL import Image

img = Image.open('wykres_czasow.png').convert('RGB')
pixels = img.load()

message = "tajna wiadomość" + "###"
binary_message = ''.join(format(ord(char), '08b') for char in message)


width, height = img.size
idx = 0

for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]

        if idx < len(binary_message):
            r = (r & ~1) | int(binary_message[idx])  # LSB r
            idx += 1
        if idx < len(binary_message):
            g = (g & ~1) | int(binary_message[idx])  # LSB g
            idx += 1
        if idx < len(binary_message):
            b = (b & ~1) | int(binary_message[idx])  # LSB b
            idx += 1

        pixels[x, y] = (r, g, b)

        if idx >= len(binary_message):
            break
    if idx >= len(binary_message):
        break

img.save('output.png')


binary_bits = []  # używamy listy zamiast stringa

for y in range(height):
    print("Odczytuję linię:", y)
    for x in range(width):
        r, g, b = pixels[x, y]
        binary_bits.append(str(r & 1))
        binary_bits.append(str(g & 1))
        binary_bits.append(str(b & 1))

binary_data = ''.join(binary_bits)  # łączenie na końcu


chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
message = ''.join(chars)

# Zatrzymaj się na znaczniku końca
message = message.split("###")[0]
print("Odczytana wiadomość:", message)
