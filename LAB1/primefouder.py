def sieve_of_eratosthenes(limit):
    prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Updating all multiples of p to false
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    
    # Collecting all prime numbers
    primes = []
    for p in range(2, limit + 1):
        if prime[p] and p % 3 == 1:
            primes.append(p)
    
    return primes

# Call the function and get all primes between 0 and 10000
primes = sieve_of_eratosthenes(10000)

# Output the result
print(primes)