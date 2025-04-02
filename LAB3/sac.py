import hashlib
import string
import random
def hash_sha1(text):
    # Tworzenie skrótu SHA-1 w formie szesnastkowej
    sha1_hash = hashlib.sha1()
    sha1_hash.update(text.encode('utf-8'))
    return sha1_hash.hexdigest()

def generateRandomTxt(size):
    res = []
    for _ in range(0,size):
        res.append(random.choice(string.ascii_letters))
    return ''.join(res)

def binaryToText(text_bin):
    # Dzielimy ciąg binarny na grupy po 8 bitów
    chars = [text_bin[i:i+8] for i in range(0, len(text_bin), 8)]
    
    # Zamieniamy każdą grupę binarnąń na znak
    text = ''.join(chr(int(char, 2)) for char in chars)
    
    return text
def textToBinary(text):
    return ''.join(format(ord(i), '08b') for i in text)

def hexToBinary(hex_string):
    hex_string = hex_string.lstrip("0x")
    
    binary_string = bin(int(hex_string, 16))[2:]
    
    binary_string = binary_string.zfill(len(hex_string) * 4)
    
    return binary_string 

def sac(text,hash_function):
    text_bin = textToBinary(text)
    pos = random.choice(range(len(text_bin)))
    switch_text_bin = list(text_bin)
    if switch_text_bin[pos] == '0':
        switch_text_bin[pos] = '1'
    else:
        switch_text_bin[pos] = '0'
    switch_text = binaryToText(''.join(switch_text_bin))
    original_hash =  hash_function(text)
    switched_hash = hash_function(switch_text)
    bin_original_hash = hexToBinary(original_hash)
    bin_switched_hash = hexToBinary(switched_hash)
    
    sameCount = 0
    size = len(bin_original_hash)
    for i in range(size):
        if bin_original_hash[i] != bin_switched_hash[i]:
            sameCount += 1
    print(f"Liczba różnych bitów: {sameCount}")
    print(f"stosunek różnych do wszystkich{sameCount/size}")
    
     
randText = generateRandomTxt(1000)
sac(randText, hash_sha1)
text = "elo"
text2 = "elo"
print(hash_sha1(text))
print(hash_sha1(text2))