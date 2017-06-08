# -*- coding: utf-8 -*-
#Klasa z konstruktorem domyślnym
'''
class Pierwsza:
    a = 1
    b = 2
    def dodaj(self, a, b):
        self.a = a
        self.b = b
        return self.a + self.b
    
    def odejmij(self, c = 0, d = 0, e = 0):
        self.c = c
        self.d = d
        self.e = e
        print('Wynik:', c - d - e)
    def minus(self):
        return self.a - self.b


o1 = Pierwsza()
print(o1.a)
print(o1.b)
o1.a = 'tekst'
print(o1.a)

o2 = Pierwsza()
#print(o2.dodaj(5, 4))
o2.odejmij(10, 1, 2)
o2.odejmij(10,2)
print('Wynik "minus":', o2.minus())
'''
#Klasa z konstruktorem
'''
class Druga:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __add__(self, other):
        return self.dodaj() + other.dodaj()
#lub to:    def __add__(self, other):
#        return self.a + other.a, self.b + other.b, self.c + other.c
    def __sub__(self, other):
        return self.a - other.a, self.b - other.b, self.c - other.c
    
    def __eq__(self, other):
        return self.a == other.a
    
    def __str__(self):
        return 'Wynik wynosi:'
        
    def dodaj(self):
        return self.a + self.b + self.c

d1 = Druga(5,3,1)
print(d1.a, d1.b, d1.c)
print(d1.dodaj())
d2 = Druga(1,2,3)
print('Dodawanie d1 + d2:', d1 + d2)
print('d1 - d2', d1 - d2)
print('d1 == d2', d1 == d2)
print(d1, d1.dodaj())
'''
'''
class Zawodnik:
    def __init__(self, wzrost, waga, imie, nazwisko):
        self.wzrost = wzrost
        self.waga = waga
        self.imie = imie
        self.nazwisko = nazwisko
    
    def bmi(self):
        return round(self.waga/(self.wzrost/100)**2, 1)
    
    def __str__(self):
        return 'Zawodnik ' + self.imie + ' ' + self.nazwisko + ' BMI: ' + str(round(self.bmi(),1))

z1 = Zawodnik(188, 75, 'aaa', 'bbb')
print('BMI:', z1.bmi())
print(z1)
'''
#P76 średnia ocen
'''
class SrOcen:
    l_ocen =  ['1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5']
    
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []
        
        self.srednia()
    
    def __add__(self, other):
        return (self.srednia() + other.srednia())/2
    
    def __str__(self):
        if len(self.oceny) > 0:
            temp = str(self.oceny)
            return '\n\n' + self.imie + ' ' + self.nazwisko + '\n' + 'Lista ocen: ' + temp[1:len(temp)-1] + '\n' + 'Średnia ocen: ' + str(self.srednia())
        else:
            return '\n\n' + self.imie + ' ' + self.nazwisko + '\n' + 'Lista ocen: brak\nŚrednia ocen: brak ocen'
    
    def wpisywanie(self):
        while True:
            ocena = input('Podaj ocenę (sam "Enter" = koniec): ')
            if len(ocena) == 0:
                break
            elif ocena not in self.l_ocen:
                print('Pomyłka')
                continue
            else:
                self.oceny.append(float(ocena))
        return self.oceny
    
    def srednia(self):
        self.wpisywanie()
        suma = 0
        for i in self.oceny:
            suma += i
        if len(self.oceny) > 0:
            sr_ocen = round(suma/len(self.oceny),2)
            return sr_ocen
class Studenci:
    def __init__(self):
        pass
    
     
s1 = SrOcen('Adam', 'Kowalski') 
print(s1) 

s2 = SrOcen('Adam', 'Kowalski2') 
print(s2) 

s3 = SrOcen('Adam', 'Kowalski3') 
print(s3) 

print(s1 + s2)
'''
#Totolotek obiektowo
'''
import random 
class Lotto:
    def __init__(self):
        self.wylosowane = random.sample(range(1,50), 6)
        self.sortowanie()
    
    def __str__(self):
        return str(self.wylosowane) + '\n' + str(self.posortowane)
    
    def sortowanie(self):
        self.posortowane = sorted(self.wylosowane)

l1 = Lotto()
print(l1)
'''
#Dziedziczenie w klasach
'''
class Bazowa:
    a = 1
    def wypisz(self):
        print('Zawartość metody >wypisz< klasy bazowej')

class Potomna(Bazowa):
    b = 2
    def info(self):
        print('Zawartość metody >info< klasy potomnej')
        

class Dziecko(Potomna):
    c = 3
    def metoda(self):
        print('Zawartość metody >metoda< klasy >dziecko<')

b1 = Bazowa()
b1.wypisz()

p1 = Potomna()
p1.info()
p1.wypisz()

d1 = Dziecko()
d1.metoda()
d1.info()
d1.wypisz()
print(d1.a)

#Tak nie można: b1.info()
'''
#Super - ze szkoleniami jest ok w P80
'''
class Bazowa:
    def __init__(a,b):
        self.a = a
        self.b = b
      
    def dodaj(self):
        return self.a + self.b
    
class Potomna(Bazowa):
    def __init__(self, c):
        super(Bazowa, self)
        self.c = c
 
    def dodaj(self, c):
        self.c = c
        return super(Bazowa, self).dodaj()

p1 = Potomna()
print(p1.dodaj(1,2,3))
'''
#P80
'''
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
        print('k1')
    
    def info(self):
        print('%s kosztuje %i zł' % (self.nazwa, self.cena))


class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa,cena)       
        self.jezyk = jezyk
        self.system = system
        print('k2')
        
    def info(self):
        print('%s kosztuje %i zł. Język: %s, sytem: %s' % (self.nazwa, self.cena, self.jezyk, self.system))
              

class Szkolenia(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, szkolenie, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.szkolenie = szkolenie
        self.termin = termin
        print('k3')
        
    def info(self):
        print('%s kosztuje %i zł. Język: %s, sytem: %s\nTermin szkolenia %s: %s' % (self.nazwa, self.cena, self.jezyk, self.system, self.szkolenie, self.termin))    

p1 = Produkt('Woda', 2)
p1.info()

p2 = Oprogramowanie('PC', 2000, 'polski', 'Widnows 10')
p2.info()

p3 = Szkolenia('Aplikacja XXX', 6000, 'polski', 'Widnows 10', '"Obługa"', '21-05-2017')
p3.info()
'''
#P80 - (444)
'''
class Kolor:
    r = 0
    g = 0
    b = 0
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __str__(self):
        return ('Wartość koloru w RGB: ' + str(self.r) + str(self.g) + str(self.b))
    
    def __add__(self, other):
        return self.r + other.r, self.g + other.g, self.b + other.b

k1 = Kolor(255, 10, 11)
k2 = Kolor(0, 0, 200)
print(k1)
print(k1 + k2)
'''
#P80
'''
class Model:
    def __init__(self, nazwa, cena_n, vat):
        self.nazwa = nazwa
        self.cena_n = cena_n
        self.vat = vat
    
    def brutto(self):
        self.cena_b = self.cena_n * (1 + self.vat)
        return self.cena_b
    
class Dodatki(Model):
    def __init__(self, nazwa, cena_n, vat, dodatki, vat_d):
        super().__init__(nazwa, cena_n, vat)
        self.dodatki = dodatki
        self.vat_d = vat_d
    
    def brutto(self):
        super().brutto()
        return self.cena_b + (self.dodatki * (1 + self.vat_d))

a1n = input('Podaj model: ')
a1c = float(input('Podaj cenę: '))
a1v = float(input('Podaj stawkę VAT: '))

a1 = Model(a1n, a1c, a1v)
print(a1.brutto())
a2 = Dodatki('Audi', 200000, 0.23, 10000, 0.1)
print(a2.brutto())
'''
#P80
class Pracownik:
    def __init__(self, imie, nazwisko, kontrakt = 'staż'):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kontrakt = kontrakt
        print(self.imie, self.nazwisko, self.kontrakt)
    
    def zmiana_etatu(self):
        if self.kontrakt == 'staż':
            self.kontrakt = 'etat'
        else:
            self.kontrakt = 'staż'
        print('Zmieniłem kontrakt')

class Pensja(Pracownik):
    def __init__(self, imie, nazwisko, kontrakt, nadgodz = 0):
        super().__init__(imie, nazwisko, kontrakt)
        self.nadgodz = nadgodz
        
    
    def __str__(self):
        return 'Pensja: ' + str(self.wyplata)
    
    def pensja(self):
        if self.kontrakt == 'staż':
            self.wyplata = 1000
        else:
            self.wyplata = 5000 + (self.nadgodz * 1.5)
        return self.wyplata

p1 = Pensja('Adam', 'Kowalski', 'staż', 0)
print(p1.pensja())
p1.zmiana_etatu()
print(p1.pensja())
#p2 = Pensja('a', 'b')

#p2.zmiana_etatu()
