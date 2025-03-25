import random
import math

p = 8581
q = 6199
N = p * q

def find_relatively_prime(N):
    while True:
        x = random.randint(1, N-1)
        if math.gcd(x, N) == 1:
            return x

def bbs(size):
    x = find_relatively_prime(N)
    print(x)
    rsequence = [0] * size
    for i in range(size):
        x = (x ** 2) % N
        rsequence[i] = x % 2
    return rsequence

def single_bits(rseq):
    count = sum(rseq)
    return 9725 < count < 10275

def series(rseq):
    ser = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    current = rseq[0]
    count = 1
    for bit in rseq[1:]:
        if bit == current:
            count += 1
        else:
            if count > 5:
                ser[6] += 1
            else:
                ser[count] += 1
            count = 1
            current = bit
    if count > 5:
        ser[6] += 1
    else:
        ser[count] += 1
    print(ser)

def long_series(rseq):
    current = rseq[0]
    count = 1
    for bit in rseq[1:]:
        if bit == current:
            count += 1
        else:
            if count > 25:
                return False
            count = 1
            current = bit
    return count <= 25

def fourBittoNum(word):
    return int(''.join(map(str, word)), 2)

def poker_test(rseq):
    n = len(rseq) // 4
    fourBits = {}

    # Count occurrences of each 4-bit sequence
    for i in range(n):
        word = rseq[i * 4:i * 4 + 4]
        number = fourBittoNum(word)
        if number in fourBits:
            fourBits[number] += 1
        else:
            fourBits[number] = 1

    # Print the count of each 4-bit number
    print(fourBits)

    # Calculate the sum of squared counts
    x = 0
    for i in range(16):
        count = fourBits.get(i, 0)
        x += count ** 2
        print(f"Count for {i}: {count}, Count Squared: {count ** 2}")

    # Final calculation of x
    x = (x * 16) / 5000 - 5000
    print(f"Calculated x value: {x}")

    # Return result based on x value
    return 2.16 < x < 46.17

# Generate random sequence and run tests
rsequence = bbs(20000)
print(single_bits(rsequence))
series(rsequence)
print(long_series(rsequence))
print(poker_test(rsequence))
