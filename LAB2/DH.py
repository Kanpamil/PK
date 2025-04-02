import random

n = 919 #liczba pierwsza
g = 7 #pierwisatek pierwotny

x = random.randint(450,100000)#klucz prywatny a

X = pow(g,x,n)
y = random.randint(450,100000)#klucz prywatny b
Y = pow(g,y,n)

#przesłanie Y do a oraz X do b
ak = pow(Y,x,n)
bk = pow(X,y,n)


print(f" klucz prywatny A: {x}, klucz publiczny B: {X}, klucz wspolny A: {ak}")
print(f" klucz prywatny B: {y}, klucz publiczny A: {Y}, klucz wspolny B: {bk}")


