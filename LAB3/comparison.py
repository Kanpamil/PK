import hashlib
import time
import string
import random
import matplotlib.pyplot as plt
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

def generateRandomTxt(sizeMB):
    res = []
    size = sizeMB * pow(2,20)
    for _ in range(0,size):
        res.append(random.choice(string.ascii_letters))
    return ''.join(res)
def measureFunctionTime(text, hash_function):
    start_time = time.perf_counter()
    hash_function(text)
    end_time = time.perf_counter()
    hash_time = end_time - start_time
    hash_time_ms = round(hash_time * 1000, 5)
    return hash_time_ms
    
def measureFunctionTimes(size, hash_function):
    start_time = time.perf_counter()
    text = generateRandomTxt(size)
    end_time = time.perf_counter()
    gen_time = end_time - start_time
    print(f"File generator time: {gen_time}")
    start_time = time.perf_counter()
    hash_md5(text)
    end_time = time.perf_counter()
    hash_time = end_time - start_time
    hash_time_ms_md5 = round(hash_time * 1000, 5)
    print(f"MD5 time with {size}MB: {hash_time_ms_md5}ms")
    start_time = time.perf_counter()
    hash_sha1(text)
    end_time = time.perf_counter()
    hash_time = end_time - start_time
    hash_time_ms_ = round(hash_time * 1000, 5)
    print(f"SHA-1 time with {size}MB: {hash_time_ms}ms")
    start_time = time.perf_counter()
    hash_md5(text)
    end_time = time.perf_counter()
    hash_time = end_time - start_time
    hash_time_ms = round(hash_time * 1000, 5)
    print(f"SHA-256 time with {size}MB: {hash_time_ms}ms")

    
sizes = [1,5,10]
text1 = generateRandomTxt(1)
text5 = generateRandomTxt(5)
text10 = generateRandomTxt(10)
texts = [text1, text5, text10]

md5_times = []
sha1_times = []
sha256_times = []
for text in texts:
    md5_times.append(measureFunctionTime(text,hash_md5))
    sha1_times.append(measureFunctionTime(text,hash_sha1))
    sha256_times.append(measureFunctionTime(text, hash_sha256))

plt.plot(sizes, md5_times, label='MD5', marker = 'o')
plt.plot(sizes, sha1_times, label='SHA-1', marker = 'o')
plt.plot(sizes, sha256_times, label='SHA-256', marker = 'o')

# Add labels and title
plt.xlabel('Wielkość pliku wejściowego (MB)')
plt.ylabel('Czas generowania pliku(ms)')
plt.title('Porównanie czasów generowania funkcji skrótu')

# Show legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
print(md5_times)
print(sha1_times)
print(sha256_times)
    

# Przykład użycia
text = "Hello, World!"
