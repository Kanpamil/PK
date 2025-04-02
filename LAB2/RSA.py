import random
import math
import string
def find_relatively_prime(N):
    while True:
        x = random.randint(1, N-1)
        if math.gcd(x, N) == 1:
            return x
        
def sito(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    
    return primes

def find_coprime_prime(phi):
    if phi < 2:
        raise ValueError("Argument musi być większy lub równy 2")
    
    primes = sito(phi)
    
    for prime in primes:
        if math.gcd(phi, prime) == 1:
            return prime
    
    raise RuntimeError("Nie znaleziono odpowiedniej liczby pierwszej")
def randString(size):
    res = ''
    for _ in range(size):
        res += random.choice(string.ascii_lowercase)
    return res

def encrypt(m,e,n):
    return m**e % n

def decrypt(c, d, n):
    return c**d % n
def encryptMsg(msg,e,n):
    res = []
    for i in range(0, len(msg)):
        num = ord(msg[i])
        res.append(encrypt(num,e,n))
    return res

def decryptMsg(emsg, d, n):
    res =''
    for i in range(0, len(emsg)):
        char = decrypt(emsg[i],d,n)
        res += chr(char)
    return res
        
p = 577
q = 307
n = p * q
phi = (p - 1)* (q - 1)
eKey = find_coprime_prime(phi)
dKey = pow(eKey,-1,phi)

message = 13
print(message)
c = encrypt(message,eKey,n)
print(c)
m = decrypt(c,dKey,n)
print(m)

message = randString(50)
print(message)
emsg = encryptMsg(message,eKey,n)
dmsg = decryptMsg(emsg,dKey,n)
print(dmsg)

if message == dmsg:
    print("Sa takie same!")
else:
    print("Coś jest nie tak")

