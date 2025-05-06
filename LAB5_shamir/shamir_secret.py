import random
from decimal import Decimal

p = 1000001
s = random.randint(1, p-1)
print(f'secret:', s)
n = 15  # liczba udziałów
t = 5   # próg

# Podział na udziały
coefficients = []
coefficients.append(s)
for i in range(t-1):
    coefficients.append(random.randint(1, p-1))
print(f't_nums:', coefficients)

def f(x):
    result = 0
    for i, c in enumerate(coefficients):
        term = c * pow(x, i, p)
        result = (result + term) % p
    return result


shares = []
for x in range(1, n+1):
    shares.append((x, f(x)))
print(f'shares:', shares)


# Odtwarzanie sekretu
def lagrange_interpolation(x_0, x_i, x_j, p):
    numerator = (x_0 - x_j) % p
    denominator = (x_i - x_j) % p
    return (numerator * pow(denominator, -1, p)) % p

def reconstruct_secret(shares, p):
    secret = 0
    x_0 = 0  # Rekonstruujemy sekret dla x_0 = 0
    for i, (x_i, y_i) in enumerate(shares):
        # Obliczamy funkcję Lagrange'a dla każdego punktu
        lagrange_sum = 1
        for j, (x_j, _) in enumerate(shares):
            if i != j:
                lagrange_sum *= lagrange_interpolation(x_0, x_i, x_j, p)
                lagrange_sum %= p
        secret += y_i * lagrange_sum
        secret %= p
    return secret

reconstructed = reconstruct_secret(shares[:t+6], p)
print(f'reconstructed:', reconstructed)
