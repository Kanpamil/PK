import random

# Parametry publiczne
n = 919  # Moduł (np. liczba pierwsza)
g = 7    # Podstawa (generator)

# Użytkownicy
users = ['A', 'B', 'C']
x_values = {}
X_values = {}

# 1. Każdy użytkownik wybiera swój klucz tajny (x) i oblicza wartość (X = g^x % n)
for user in users:
    x_values[user] = random.randint(450, 1000)  # Losowy klucz tajny
    X_values[user] = pow(g, x_values[user], n)  # Obliczamy X = g^x % n
    print(f'{user} - x: {x_values[user]}, X: {X_values[user]}')

# 2. Wymiana wartości: każdy użytkownik wysyła swoje X do pozostałych użytkowników

# 3. Każdy użytkownik oblicza pośredni klucz (np. A oblicza K_A = X_B^x_A % n)
shared_keys = {}

for user in users:
    # A oblicza klucz z X_B (przekazane przez B), B z X_C, C z X_A
    shared_key = 1
    for other_user in users:
        if other_user != user:
            shared_key = shared_key * pow(X_values[other_user], x_values[user], n) % n
    shared_keys[user] = shared_key

# 4. Wszyscy powinni mieć ten sam klucz
print("\nPo obliczeniu wspólnych kluczy przez każdego użytkownika:")
for user in users:
    print(f'{user} - wspólny klucz: {shared_keys[user]}')

# Sprawdzenie, czy wszystkie klucze są takie same
if len(set(shared_keys.values())) == 1:
    print("\nWszyscy użytkownicy uzyskali ten sam klucz!")
else:
    print("\nWystąpił problem z obliczeniem wspólnego klucza.")
