# -*- coding: utf-8 -*-
#P76 średnia ocen - wersja z błędem - podwójny Enter na zakończenie wpisywania
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
            return '\n\n' + self.imie + ' ' + self.nazwisko + '\n' + 'Lista ocen: brak\n Średnia ocen: brak ocen'
    
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

s1 = SrOcen('Adam', 'Kowalski') 
print(s1) 


#Wersja OK
class SrOcen:
    l_ocen =  ['1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5']
    
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []
        self.wpisywanie()
        self.srednia()
    
    def __add__(self, other):
        return (self.srednia() + other.srednia())/2
    
    def __str__(self):
        if len(self.oceny) > 0:
            temp = str(self.oceny)
            return '\n\n' + self.imie + ' ' + self.nazwisko + '\n' + 'Lista ocen: ' + temp[1:len(temp)-1] + '\n' + 'Średnia ocen: ' + str(self.srednia())
        else:
            return '\n\n' + self.imie + ' ' + self.nazwisko + '\n' + 'Lista ocen: brak\n Średnia ocen: brak ocen'
    
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
        
        suma = 0
        for i in self.oceny:
            suma += i
        if len(self.oceny) > 0:
            sr_ocen = round(suma/len(self.oceny),2)
            return sr_ocen

s1 = SrOcen('Adam', 'Kowalski') 
print(s1) 