import string
import random
import base64
import matplotlib.pyplot as plt
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import time
import gc

def generateRandomTxt(sizeMB):
    res = []
    size = sizeMB * pow(2,20)
    for _ in range(0,size):
        res.append(random.choice(string.ascii_letters))
    return ''.join(res)


def encrypt_decrypt(cipher_mode, data):
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    
    if cipher_mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    elif cipher_mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif cipher_mode == 'CTR':
        nonce = get_random_bytes(12)
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    else:
        raise ValueError("Unsupported mode")
    data = pad(data, AES.block_size)
    # Szyfrowanie
    gc.disable()
    start_enc = time.perf_counter()
    ciphertext = cipher.encrypt(data)
    end_enc = time.perf_counter()
    gc.enable()

    # Deszyfrowanie
    if cipher_mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    elif cipher_mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif cipher_mode == 'CTR':
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)# trzeba użyć tego samego numerka

    #print("encrypted (binary):", ' '.join(format(byte, '08b') for byte in ciphertext))
    ciphertext_base64 = base64.b64encode(ciphertext)

    # print("Ciphertext (Base64):", ciphertext_base64.decode('utf-8'))
    #print(ciphertext)
    gc.disable()
    start_dec = time.perf_counter()
    decrypted = cipher.decrypt(ciphertext)
    end_dec = time.perf_counter()
    gc.enable()
    decrypted = unpad(decrypted, AES.block_size)
    

    return end_enc - start_enc, end_dec - start_dec
def average_encrypt_decrypt(mode, data, runs=10):
    enc_total = 0
    dec_total = 0
    for _ in range(runs):
        enc, dec = encrypt_decrypt(mode, data)
        enc_total += enc
        dec_total += dec
    return (enc_total / runs), (dec_total / runs)

# Testy dla plików 1MB, 5MB, 10MB
sizes = [1, 5, 10]
modes = ['ECB', 'CBC', 'CTR']
ecb_times_e = []
cbc_times_e = []
ctr_times_e = []
ecb_times_d = []
cbc_times_d = []
ctr_times_d = []
for size in sizes:
    filename = f'test_{size}MB.bin'
    data = generateRandomTxt(size).encode('utf-8')
    print(f"\n--- {size}MB ---")
    
    for mode in modes:
        enc_time, dec_time = average_encrypt_decrypt(mode, data,15)
        if mode == "ECB":
            ecb_times_e.append(round(enc_time*1000,4))
            ecb_times_d.append(round(dec_time*1000,4))
        if mode == "CBC":
            cbc_times_e.append(round(enc_time*1000,4))
            cbc_times_d.append(round(dec_time*1000,4))
        if mode == "CTR":
            ctr_times_e.append(round(enc_time*1000,4))
            ctr_times_d.append(round(dec_time*1000,4))

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.plot(sizes, ecb_times_e, label="ECB", marker='o')
plt.plot(sizes, cbc_times_e, label="CBC", marker='o')
plt.plot(sizes, ctr_times_e, label="CTR", marker='o')
plt.xlabel("Size (MB)")
plt.ylabel("Encryption Time (ms)")
plt.title("Encryption Time")
plt.legend()
print("1MB----------------5MB--------------10MB")
print("ECB decryption and encryption")
print(ecb_times_d)
print(ecb_times_e)
print("CBC decryption and encryption")
print(cbc_times_d)
print(cbc_times_e)
print("CTR decryption and encryption")
print(ctr_times_d)
print(ctr_times_e)

plt.subplot(1, 2, 2)
plt.plot(sizes, ecb_times_d, label="ECB", marker='o')
plt.plot(sizes, cbc_times_d, label="CBC", marker='o')
plt.plot(sizes, ctr_times_d, label="CTR", marker='o')
plt.xlabel("Size (MB)")
plt.ylabel("Decryption Time (ms)")
plt.title("Decryption Time")
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()

