# -*- coding: utf-8 -*-

#Funkcja n silnia
def silnia(n):
    wynik = 1
    while n > 0:
        wynik *= n
        n -= 1
    return wynik

#print(silnia(int(input('Podaj liczbę: '))))

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


