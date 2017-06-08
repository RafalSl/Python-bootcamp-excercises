# -*- coding: utf-8 -*-
#importowanie pakietu

import os
import fnmatch

#P83 - dopisywanie studentów do listy i zapis w pliku
'''
class Lista:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.otwieranie()
    
    def otwieranie(self):
        if os.path.isfile(self.nazwa) == True:
            self.drukowanie()
            self.L = open(self.nazwa, 'a')
        else:
            self.L = open(self.nazwa, 'w')
        print('Plik %s otwarty do wpisywania' % self.L.name)
        self.wpisywanie()
        
    def wpisywanie(self):
        while True:
            imie = input('Podaj imię: ')
            nazwisko = input('Podaj nazwisko: ')
            grupa = input('Grupa: ')
            self.L.write(imie + '\t' + nazwisko + '\t' + grupa + ';\n')
            dalej = input('Kolejny wpis? (t/n) ') 
            if dalej == 'n' or dalej == 'N':
                break
        self.L.close()
        print('Plik %s zamknięty' % self.L.name)
        
    def drukowanie(self):
        R = open(self.nazwa, 'r')
        print('Plik %s otwarty' % R.name)
        print(R.read())
        R.close()
        print('Plik %s zamknięty' % R.name)

nazwa = input('Podaj nazwę pliku: ')
nazwa.strip()
P1 = Lista(nazwa)
'''
#P83 i P84
class Pliki:    
    def szukanie(self):
        n_k = input('Podaj ścieżkę katalogu: ')
        n_p = input('Czego szukasz: ')        
        lista = [x for x in os.listdir(r'%s' %n_k) if fnmatch.fnmatch(x,('*%s*' % n_p))]
        print('Liczba trafień:', len(lista))
        if len(lista) > 0:
            print(lista)
    
    def najstarszy(self):
        n_k = input('Podaj ścieżkę katalogu: ')
        
    
    def najdluzszy(self):
        n_k = input('Podaj ścieżkę katalogu: ')
        wynik = []
        lista_p = os.listdir(n_k)       
        for plik in lista_p:
            if len(wynik) == 0:
                wynik.append(plik)
            else: 
#Tu jest błąd - nie można dopisywać do listy, tylko trzeba zastępować mniejsze pliki
                for x in wynik:
                    print('for %s in wynik' % x)
                    if os.path.getsize(plik) == os.path.getsize(x):
                        wynik.append(plik)
        print('Lista najdłuższych plików:')
        print(wynik)

P1 = Pliki()
#P1.szukanie()
P1.najdluzszy()