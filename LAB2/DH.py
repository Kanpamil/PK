import random

n = 919
g = 7

x = random.randint(450,1000)
print(x)
X = g**x % n
y = random.randint(450,1000)
Y = g**y % n

ak = pow(Y,x,n)
bk = pow(X,y,n)


print(ak)
print(bk)


print(f" liczba a: {x}, klucz A: {ak}")
print(f" liczba b: {y}, klucz B: {bk}")


