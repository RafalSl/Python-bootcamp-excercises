# -*- coding: utf-8 -*-
"""
a = 1
b = 2.4
c = 'w1'
print(a, b, c)
a = 2.1
b = 'abc'
c = 0
print(a, b, c)
b = c
a = 13
print(a, b, c)
del(a)
del(c)
#c+=31.3

imie = 'Adam'
nazwisko = 'Kowalski'
rok_ur = 1910
stan = 'emeryt'
placa = 800
placa_n = 0.81 * placa
print(imie, nazwisko, rok_ur, stan, placa, placa_n)

r = 5
pi = 3.14
pk = pi * r**2
print(pk)

print(3.0//2)
print(round(1.2), round(1.5), round(1.8))
print(round(-1.2), round(-1.5), round(-1.8))
print(type(imie), type(rok_ur), type(stan), type(placa), type(placa_n))
imie = 10.2
print(type(imie))

v3 = 0.03
v7 = 0.07
v23 = 0.23
cena_b = 1000
print('Cena brutto:', cena_b, 'cena netto VAT 3%:', round(cena_b/(1+v3), 2), 'cena netto VAT 7%', round(cena_b/(1+v7), 2), 'cena netto VAT 23%', round(cena_b/(1+v23), 2))

cChleb = 1.99
cMleko = 2.5
cCukierki = 12.99
zChleb = 2
zMleko = 0.5
zCukierki = 0.3
suma = cChleb * zChleb + cCukierki * zCukierki + cMleko * zMleko
print('Zaplac', round(suma, 2), 'za swoje zamowienie')
print('Zaplac', round(suma, 2), 'za swoje zamowienie')

print((2+5j) + (4+6j))
print(4 + (4+6j))

a = 12
b = 1+(-1j)
print(a*b)

p = True
q = False
zdanie = p and q
print(zdanie)
print(bool(12), bool(""), bool(''))

print("Cytat: \"Byc albo nie byc\" \n\"Luke I'm your father\"")
print("Cytat: \"Być albo nie być\" \n\"Luke I'm your father\"")

print("Napis" + " jest " + ("złączony x3 " * 3))
print('Twoja cena to: ' + str(round(suma, 2)) + 'zł')

print(bool(7))
a = 'cześć'
print((a + ' ')*3)

print(pk)
r = 'Rafał'
m = 'Marcin'
d = 'Daniel'
print(d + ', ' + m + ' i ' + r)

a = 2
t1 = 3
t2 = 4
t3 = 6
r = 3
pk = round(pi * r**2, 2)
print('Pole kwadratu o boku', str(a) + ':', a**2)
print('Obwód trójkąta o bokach', str(t1) + ', ' + str(t2) + ', ' + str(t3) + ':', (t1+t2+t3))
print('Pole koła o promieniu', str(r) + ':', round(pi * r**2, 2))

p = True
q = True
print(not(p and q) == (not p or not q))
p = True
q = False
print(not(p and q) == (not p or not q))
p = False
q = False
print(not(p and q) == (not p or not q))
p = False
q = True
print(not(p and q) == (not p or not q))

a = False
b = False
c = True
f1 = not a and not b and not c
f2 = not a and not b and c
f3 = not a and b and not c
f4 = a and not b and not c
f = f1 or f2 or f3 or f4
print('Funkcja f:', f)

#pierwiastek 2 st. z -17 = pierw2 -1 * pierw2 17
#pierw2 -1 = j
multiplex = 17**0.5
im = 1j
result = round(multiplex, 2) * im
print(result)

Z = 17 % 7
Z *= Z+3
print(Z)

Z = 17 % 7
print(Z**2 + 3*Z)

print((str(1.2e+3+34.5) + ' ') * 10)

n1 = 'Dom'
n2 = 'Domy'
print(n1<n2)


# Pole kwadratu
print()
print('Obliczę pole kwadratu')
a = float(input('Podaj długość boku: '))
print('Pole kwadratu:', a**2)
"""
"""
print()
imie = input('Podaj imię: ')
print('Witaj ' + str(imie) + '!')
"""
"""
print()
napis = input('Wpisz coś (nizebyt długiego): ')
print('Ile razy to wyświetlić?')
i = int(input())
print((napis + '\n') * i)
"""

"""
print()
spk = int(input('Podaj stan konta: '))
p = float(input('Podaj oprocentowanie: '))
n = float(input('Podaj liczbę lat: '))
k = float(input('Podaj okres kapitalizacji: '))
skk = spk * (1 + p/k)**(n*k)
print(skk)


print()
spk = int(input('Podaj stan konta: '))
p = float(input('Podaj oprocentowanie: '))
n = float(input('Podaj liczbę lat: '))
k = float(input('Podaj okres kapitalizacji: '))
for i in range(0, int(n*k)):
    spk += 500
    skk = spk * (1 + p/k)**(n*k)
print(round(skk, 2))
"""

# Metody napisowe
k = 'WIELKI NAPIS'
print(k.capitalize())
print(k.center(len(k) + 10))
print(k.replace('NAPIS', 'napis'))
print(k.split('\n'))

# Listy
l1 = []
l1.append('a')
l1.append(33)
print(l1)

l2 = [ [1, 2, 3], ['a', 'b', 'c']]
print(l2[0][2])

l3 = [1,2,3,4,5]
print(l3[2:5])
print(l3[::2])

l1 = [[],[]]
l1[0].append('Adam')
l1[0].append('Ewa')
l1[1].append(1)
l1[1].append(2)
l1[1].append(3)
print(l1)
"""
l1[0].append(input('Podaj imię: '))
l1[0].append(input('Podaj imię: '))
for i in range(0, len(l1[0])):
    print(l1[0][i])
"""
prod = [['piwo', 'wino', 'chipsy', 'czekolada', 'ser'], [1.99, 20, 5.20, 4, 8.99]]
print(prod[0][0], prod[1][0]) 
print(prod[0][len(prod[0])-1], prod[1][(len(prod[1])-1)])
print(type(prod))