# -*- coding: utf-8 -*-
'''
liczby = range(0,100)

lista = []
for x in liczby:
    if x % 2 != 0:
        continue
    lista.append(x)

print(lista)
'''
'''
alfa = []
for a in range(97, 123):
    alfa.append(chr(a))
print(alfa)

x = input('Podaj szukaną literę: ')
for i, value in enumerate(alfa):
    if value == x:
        print('Litera %c jest %i literą w alfabecie' % (x, i+1))
        break
    else:
        print('Brak litery %s w alfabecie' % (x))
        break
''' 
#p60
'''
cyfry = {'0' : 'zero', '1' : 'jeden', '2' : 'dwa', '3' : 'trzy', '4' : 'cztery', '5' : 'pięć', '6' : 'sześć', '7' : 'siedem', '8' : 'osiem', '9' : 'dziewięć'}
ciag = input('Wpisz coś: ')
for znak in ciag:
    if (znak not in cyfry.keys()):
        continue
    print(cyfry[znak], end = ' ')
'''
#p61
'''
for a in range(1, 11):
    if a == 2:
        print('-' * 8 * 10)
    for b in range(1, 11):
        if b == 1:
            print('%3i | \t' % (a*b), end = '')
        else:
            print('%3i\t' % (a*b), end = '')
    print()
'''
#p62
'''
print(' C\t F')
for tempC in range(-20, 41):
    print('%.+1f\t%+.1f' % (tempC, 32+9/5*tempC))
 '''

#Średna ocen z wykorzystaniem funkcji
'''
l_ocen = ['1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5']
oceny = []


def sredniaOcen(ocenyF):
    suma = 0
    for i in ocenyF:
        suma += i
    if len(ocenyF) > 0:   
        print()
        temp = str(ocenyF)
        print('Lista ocen: ' + temp[1:len(temp)-1])
        print('Średnia ocen: %.2f' % (suma/len(ocenyF)))
        
while True:
    a = input('Podaj ocenę (sam "Enter" = koniec): ')
    if len(a) == 0:
        break
    if a not in l_ocen:
        print('Pomyłka')
        continue
    oceny.append(float(a))

sredniaOcen(oceny)
'''
'''
#Funkcja n silnia
def silnia(n):
    wynik = 1
    while n > 0:
        wynik *= n
        n -= 1
    return wynik

print(silnia(int(input('Podaj liczbę: '))))
'''
'''
#P70
def fibon(n):
    ciag = [1]
    suma = 1
    i = 1
    while i < n:
        suma += ciag[i-1]
        ciag.append(ciag[i-2] + ciag[i-1])
        i += 1
    return suma, ciag[i-2]

wynik_f = fibon(int(input('Podaj liczbę: ')))
print('Suma: %i\t elemnt n-ty: %i' % (wynik_f[0], wynik_f[1]))
'''
#P71
'''
import random 
def losuj(n = 5):
    alfa = []
    for a in range(97, 123):
        alfa.append(chr(a))
        
    i = 0
    losowe = ''
    while i < n:
        losowe += random.choice(alfa)
        i += 1
    losowe += '!'
    losowe = losowe.capitalize()
    return losowe
n = int(input('Ile ma być liter w wyazie? '))
print(losuj(n))
'''
#P74 - 002
'''
import random 
def wykres(rand, znak  = '*'):
    def rysowanie(znak, wartosci):
        for j in range(0,5):
            print(znak * wartosci[j]) 
        return
    #treść funkcji wykres
    
    wartosci = []
    if rand == 'n':
        for i in range(0,5):
            wartosci.append(int(input('Podaj %i. warotść: ' % (i+1))))
    else:
        for i in range(0,5):
            wartosci.append(random.choice(range(1,11)))
    rysowanie(znak, wartosci)
    return
    
rand = input('Genereować losowo? (t/n) ')
znak = input('Podaj znak: ')
if len(znak) == 0:
    znak = '*'
wykres(rand, znak)
'''
#P74 - 005 generator kodu html
'''
def span_html(napis, color='black', font_size='12px', font_weight='6px'):
    print( #tu napis z html + zmienne w stringach 
           )
span_html('Cześć')
print('Cześć')
'''
#P75
'''
a = 'Biały'
def cz_b():
   global a
   if a == 'Czarny':
      a = 'Biały'
      return a
   else: 
      a = 'Czarny'
      return a

for i in range(5):
   print(cz_b())
'''
#P74 (240)
import random 
def suma(n):
    def gen_tabl(n):
        tabl = []
        for i in range(n):
            tabl.append(random.randint(0,10))
        return tabl
    
    t1 = gen_tabl(n)
    suma = 0
    print(t1)
    for i in t1:
        if i > 5:
            suma += i
    print(suma)

suma(10)

#P74 inny warient 
import random 
def gen_tabl(n):
    global t1
    t1 = []
    for i in range(n):
        t1.append(random.randint(0,10))
   

def suma(n):
    global t1
    gen_tabl(n)
    suma = 0
    print(t1)
    for i in t1:
        if i > 5:
            suma += i
    print(suma)

suma(10)

#zmienne globalne
def potegowanie(x, y):
    global wynik
    wynik = 1
    for i in range(y):
        wynik *= x

def inkrementacja():
    global wynik
    wynik += 1

potegowanie(3,3)
print('Wynik potęgowania:', wynik)
inkrementacja()
print('Po ikrementacji:', wynik)