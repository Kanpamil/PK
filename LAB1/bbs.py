import random
import math

def find_relatively_prime(N):
    while True:
        x = random.randint(1, N-1)
        if math.gcd(x, N) == 1:
            return x
        
def bbs(size, p, q):
    N = p * q
    x= find_relatively_prime(N)
    print(x)
    rsequence = [0]*size
    for i in range(0, size):
        x = (x**2) % N
        rsequence[i] = x % 2
    return rsequence

def single_bits(rseq):
    count = 0
    for bit in rseq:
        if bit == 1:
            count +=1
    if count > 9725 and count < 10275:
        return True
    return False
def series(rseq):
    ser = {1:0,2:0,3:0,4:0,5:0,6:0}
    current = rseq[0]
    count = 0
    for bit in rseq:
        if bit == current:
            count += 1
        else:
            if count > 5:
                ser[6] +=1
            else:
                ser[count] += 1
            count = 1
            current = bit
    if count > 5:
                ser[6] +=1
    else:
        ser[count] += 1
    print(ser)

def long_series(rseq):
    current = rseq[0]
    count = 0
    for bit in rseq:
        if bit == current:
            count += 1            
        else:
            if count > 25:
                return False
            count = 1
            current = bit
    return True

def fourBittoNum(word):
    return int(''.join(map(str, word)), 2)
def poker_test(rseq):
    n = len(rseq) // 4
    fourBits = {}
    for i in range(0, n):
        word = rseq[i*4:i*4+4]
        number = fourBittoNum(word)
        if number in fourBits:
            fourBits[number] += 1
        else:
            fourBits[number] = 1
            
    x = 0
    for i in range (0,16):
        x = x + fourBits[i]**2
    x = (x * (16 / n)) - n

    if x > 2.16 and x < 46.17:
        return True
    return False

p = 8581
q = 6199
N = p * q
rsequence = bbs(20000, p, q)

print(single_bits(rsequence))
series(rsequence)
print(long_series(rsequence))
print(poker_test(rsequence))