text = "Hello"
bits = ''.join(format(byte, '08b') for byte in bytearray(text, 'utf-8'))
print(bits)
bytes_list = [int(bits[i:i+8], 2) for i in range(0, len(bits), 8)]

# Convert byte values to a bytes object, then decode
decoded_text = bytes(bytes_list).decode('utf-8')
print(decoded_text)  # Output: Hello