import hashlib
import string
import random
def hash_md5(text):
    # Tworzenie skrótu MD5 w formie szesnastkowej
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()

def hash_sha1(text):
    # Tworzenie skrótu SHA-1 w formie szesnastkowej
    sha1_hash = hashlib.sha1()
    sha1_hash.update(text.encode('utf-8'))
    return sha1_hash.hexdigest()

def hash_sha256(text):
    # Tworzenie skrótu SHA-256 w formie szesnastkowej
    sha256_hash = hashlib.sha256()
    sha256_hash.update(text.encode('utf-8'))
    return sha256_hash.hexdigest()

def generateRandomTxt(size):
    res = []
    for _ in range(0,size):
        res.append(random.choice(string.ascii_letters))
    return ''.join(res)

def binaryToText(text_bin):
    # Dzielimy ciąg binarny na grupy po 8 bitów
    chars = [text_bin[i:i+8] for i in range(0, len(text_bin), 8)]
    
    # Zamieniamy każdą grupę binarną na znak
    text = ''.join(chr(int(char, 2)) for char in chars)
    
    return text
def textToBinary(text):
    return ''.join(format(ord(i), '08b') for i in text)

def hexToBinary(hex_string):
    hex_string = hex_string.lstrip("0x")
    
    binary_string = bin(int(hex_string, 16))[2:]
    
    binary_string = binary_string.zfill(len(hex_string) * 4)
    
    return binary_string 

def bit_checker(hash_function, text_size, comparisions):
    text_one = generateRandomTxt(text_size)
    text_one_hash = hash_function(text_one)
    text_one_bin = hexToBinary(text_one_hash) 
    bits = [6,8,12,15,17, 20, 32, 50, 64, 100, 128, 256]
    bit_dict = {bit: 0 for bit in bits}  

    for _ in range(comparisions):
        text_two = generateRandomTxt(text_size)
        text_two_hash = hash_function(text_two)
        text_two_bin = hexToBinary(text_two_hash)

        for bit_length in bits:
            if text_one_bin[:bit_length] == text_two_bin[:bit_length]:
                bit_dict[bit_length] += 1
            else:
                break

    return bit_dict

print(bit_checker(hash_sha256, 256, 1000))