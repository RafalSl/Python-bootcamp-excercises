# -*- coding: utf-8 -*-
import random 

"""
imnaz = [[1, 'Jan', 'Kowalski'], [2, 'Tomek', 'Kowal'], [3, 'Joanna', 'Myszkowska'], [4, 'Monika', 'Bąk']]
dane = [(1, 1111, 11), (2, 2222, 22), (3, 3333, 33), (4, 4444, 44)]
ind = int(input('Podaj indeks: ')) - 1
print('Imię i Nazwisko:', imnaz[ind][1], imnaz[ind][2], 'data urodzenia:', dane[ind][1], 'PESEL:', dane[ind][2])
"""
"""
napis = input('Wpisz zdanie: ')
napis = napis.strip()
napis = napis.split(' ')
print(napis)
print(len(napis))
for i in range(0, len(napis)):
    print(napis[i], end = ' ')
"""
#p44
"""
konwert = {'jeden' : 1, 'dwa' : 2, 'trzy' : 3, 'czter' : 4, 'pięć' : 5, 'sześć' : 6}
klucz = input('Podaj cyfrę słownie: ')
klucz = klucz.strip()
print(klucz.capitalize(), 'to', konwert[klucz], 'w systemie dziesiętnym', end = ' ')

#p45
konwert_rz = {1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V'}
#klucz = input('Podaj cyfrę: ')
#klucz = klucz.strip()
print('i', konwert_rz[konwert[klucz]], 'w zapisie rzymskim')
"""
"""
#p45
nazwa_tow = {'1' : 'chleb', '2' : 'mleko', '3' : 'piwo'}
cena_n = {'1' : 2, '2' : 2.5, '3' : 1.99}
vat = {'1' : 1.03, '2' : 1.07, '3' : 1.23}
lista_z = []
a = 0
while a != 'q':
    a = input('Podaj kod towaru: ')
    lista_z.append(a)
lista_z.pop()
suma_n = 0
suma_b = 0
print(lista_z)
for i in lista_z:
    suma_n += cena_n[i]
    suma_b += cena_n[i] * vat[i]

print('Lista zakupów:')
print('Nazwa\t\tCena netto\tCena brutto')
for i in lista_z:
    print(nazwa_tow[i]+'\t\t'+str(cena_n[i])+'\t\t'+str(round(cena_n[i] * vat[i], 2)))
print()
print('Suma netto:\t' + str(suma_n))
print('Suma bruto:\t' + str(round(suma_b, 2)))
"""

#zbiory
"""
set1 = ([1,2,3,4,5])
print(len(set1))
print(2 in set1)
"""
"""
lista_los = []
for i in range(1,50):
    lista_los.append(i)
print(lista_los)
los = set()
for j in range(6):
    a = random.randrange(len(lista_los))
    los.add(lista_los[a])
    del lista_los[a]
print(los)
"""
"""
for i in range(5):
    if bool(i) != True:
        print(i, 'ma wartość logiczną False')
    else:
        print(i, 'ma wartość logiczną True')

a = float(input('Podaj liczbę: '))
if a >= 0 and a <= 9:
    print('Liczba z przedziału 0-9')
else:
    print('Liczba spoza przedziału 0-9')
"""
"""
#p57
liczba = float(input('Podaj liczbę: '))
print('Liczba parzysta') if liczba % 2 == 0 else print('Liczba nieparzysta')

"""
#for i in range(5,100,10):
#    print('%2i, %4i, %6i' % (i , i**2, i**3))
"""
sklep_prod = {'monitor1':'monitor 17"', 'myszka':'myszka optyczna', 'klawiatura':'Klawiatura Logitech'}
il_prod = {'monitor1': 1, 'myszka': 20, 'klawiatura': 1}
sklep_cena = {'monitor1': 1000, 'myszka': 50, 'klawiatura':90}
zamowienie = {'monitor1': 1, 'monitor2':2, 'myszka': 3, 'klawiatura': 2}
suma = 0
for prod in zamowienie:
    if prod in sklep_prod.keys() and il_prod[prod] >= zamowienie[prod]:
        print('Produkt %s dostępny' % sklep_prod[prod])
        print('Produkt %s dodany do koszyka' % sklep_prod[prod])
        il_prod[prod] -= zamowienie[prod]
        suma += sklep_cena[prod] * zamowienie[prod]
        print('W sklepie zostało %i produktów: %s' % (il_prod[prod], sklep_prod[prod]))
        print()
    elif prod in sklep_prod.keys() and il_prod[prod] < zamowienie[prod]:
        print('W sklepie dostepnych tylko %i produktów: %s' % (il_prod[prod], sklep_prod[prod]))
        print()
    else:
        print('Produkt %s niedostępny' % prod)
        print()

print('Do zpałaty:', suma)
"""
"""
x = 2
y = 10
wynik = 1
for i in range(y):
    wynik *= x
print(wynik)
"""
a = float(input('Podaj pierwszy wyraz ciągu:'))
q = float(input('Podaj iloraz ciągu:'))
n = int(input('Podaj l. wyrazóW ciągu:'))
suma = 0
for i in range(n):
    suma += a * q**i
print(suma)

    
