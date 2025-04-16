from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import random
import string

# Helper function to generate random text
def generateRandomTxt(sizeMB):
    res = []
    size = sizeMB * pow(2, 20)
    for _ in range(size):
        res.append(random.choice(string.ascii_letters))
    return ''.join(res)

# Function to flip a random bit in a bytearray
def flip_random_bit(byte_array):
    byte_index = random.randint(0, len(byte_array) - 1)
    bit_index = random.randint(0, 7)
    byte_array[byte_index] ^= (1 << bit_index)
    return byte_array

def flip_bit_in_block(byte_array, block_index, block_size=16):
    start = block_index * block_size
    if start >= len(byte_array):
        print(f"[!] Block {block_index} is out of range for input size {len(byte_array)} bytes.")
        return byte_array
    byte_index = random.randint(start, min(start + block_size - 1, len(byte_array) - 1))
    bit_index = random.randint(0, 7)
    byte_array[byte_index] ^= (1 << bit_index)
    return byte_array


def error_propagation(mode, data):
    key = get_random_bytes(16) 
    iv = get_random_bytes(16)
      
    
    data_flipped = flip_random_bit(bytearray(data))
    
    
    encrypt_errors = 0
    decrypt_errors = 0

    padded_data = pad(data, AES.block_size)
    padded_data_flipped = pad(data_flipped, AES.block_size)
    
    # Encryption
    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
        cipher_origin = cipher.encrypt(padded_data)
        cipher_flipped = cipher.encrypt(padded_data_flipped)
    elif mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
        cipher_origin = cipher.encrypt(padded_data)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        cipher_flipped = cipher.encrypt(padded_data_flipped)
    elif mode == 'CTR':
        nonce = get_random_bytes(12)
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        cipher_origin = cipher.encrypt(padded_data)
        
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        cipher_flipped = cipher.encrypt(padded_data_flipped)
        
    
    
    # Count encryption bit-level errors
    for i in range(len(cipher_origin)):
        byte1 = cipher_origin[i]
        byte2 = cipher_flipped[i]
        # Compare byte1 and byte2 bit by bit
        for bit_index in range(8):  # 8 bits in a byte
            if (byte1 >> bit_index & 1) != (byte2 >> bit_index & 1):
                encrypt_errors += 1
    
    # Decryption
    
    cipher_origin_flipped = flip_random_bit(bytearray(cipher_origin))
    #cipher_origin_flipped = flip_bit_in_block(bytearray(cipher_origin), 1)
    
    
    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted_origin = cipher.decrypt(cipher_origin)
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted_flipped = cipher.decrypt(cipher_origin_flipped)
    elif mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_origin = cipher.decrypt(cipher_origin)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_flipped = cipher.decrypt(cipher_origin_flipped)
    elif mode == 'CTR':
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        decrypted_origin = cipher.decrypt(cipher_origin)
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        decrypted_flipped = cipher.decrypt(cipher_origin_flipped)
    
    
    # print(decrypted_origin.decode('utf-8', errors='replace'))
    # print(decrypted_flipped.decode('utf-8', errors='replace'))

    
    # Count decryption bit-level errors
    for i in range(len(decrypted_origin)):
        byte1 = decrypted_origin[i]
        byte2 = decrypted_flipped[i]
        # Compare byte1 and byte2 bit by bit
        for bit_index in range(8):  # 8 bits in a byte
            if (byte1 >> bit_index & 1) != (byte2 >> bit_index & 1):
                decrypt_errors += 1
    
    return encrypt_errors, decrypt_errors

# Generate random text (1MB in size) and convert to bytearray
size = 1
text = generateRandomTxt(size)
#text = "Hello world lets decipher it aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
byte_text = bytearray(text, 'utf-8')  # Convert to bytearray

# Test error propagation for all AES modes (ECB, CBC, CTR)
for mode in ['ECB', 'CBC', 'CTR']:
    encrypt_err, decrypt_err = error_propagation(mode, byte_text)
    print(f"Mode: {mode}, Encryption Bit Errors: {encrypt_err}, Decryption Bit Errors: {decrypt_err}")
