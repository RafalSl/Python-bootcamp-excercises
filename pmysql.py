# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect('localhost', 'rafal', 'rafal', 'testowa')
print('połączono')
c = conn.cursor()

#Wyświetlanie wyników z bazy danych

sql = 'select * from uzytkownicy'

try:
    c.execute(sql)
    result = c.fetchall()
    print('%3s%15s%15s%11s' %  ('ID', 'Imię', 'Nazwisko', 'PESEL'))
    for kol in result:
        lp = kol[0]
        imie = kol[1]
        nazwisko = kol[2]
        pesel = kol[3]
        print('%3s%15s%15s%11s' % (lp, imie, nazwisko, pesel))
except:
    print('Błąd. Nie wykonano polecenia')
conn.close()

#Wprowadzanie danych do bazy
'''
insert = ("insert into uzytkownicy (id, imie, nazwisko, pesel) values ('3', 'c', 'd', '1555')")
try:
    c.execute(insert)
    conn.commit()
except:
    print('Błąd. Nie wykonano polecenia')
    
sql = 'select * from uzytkownicy'

try:
    c.execute(sql)
    result = c.fetchall()
    print('%3s%15s%15s%11s' %  ('ID', 'Imię', 'Nazwisko', 'PESEL'))
    for kol in result:
        lp = kol[0]
        imie = kol[1]
        nazwisko = kol[2]
        pesel = kol[3]
        print('%3s%15s%15s%11s' % (lp, imie, nazwisko, pesel))
except:
    print('Błąd. Nie wykonano polecenia')
    
conn.close()
'''

#Próby przenisione do innego pliku - nie ruszaj
"""
class Db:
    def polacz(self):
        try:
            self.conn = pymysql.connect('localhost', 'rafal', 'rafal', 'testowa')       
            self.c = self.conn.cursor()
        except:
            print('Błąd połączenia')
        #Tutaj dodać pętlę - czy próbować jeszcze raz
    def menu(self):
        while True:
            print('--== Menu ==--')
            wybor = input('"r" - operacje na rekordach\n"q" - wyjście z programu')
            if wybor == 'r' or wybor == 'R':
                rekord = Rekord()
                rekord.menu()
            elif wybor == 'q' or wybor =='Q':
                break
            else:
                print('Błędny wybór. Spróbuj jeszcze raz')
                continue
        

class Rekord(Db):
    def __init__(self):
        self.c = self.conn.cursor()
    #polacz() jest w klasie DB
    '''
    def polacz(self):
        try:
            self.conn = pymysql.connect('localhost', 'rafal', 'rafal', 'testowa')       
            self.c = self.conn.cursor()
        except:
            print('Błąd połączenia')  
    '''
    def menu(self):
        print('--== Menu ==--')
        print('"d" - dodaj wpis\n("m" - modyfikuj wspis)\n"o" - odczyt bazy danych\n"q" - wyjście poziom wyżej')
        while True:
            pass
    
    def odczyt(self):
        self.polacz()
        try:
            sql = 'select * from uzytkownicy'
            self.c.execute(sql)
            result = self.c.fetchall()
            print('%3s%15s%15s%11s' %  ('ID', 'Imię', 'Nazwisko', 'PESEL'))
            for kol in result:
                lp = kol[0]
                imie = kol[1]
                nazwisko = kol[2]
                pesel = kol[3]
                print('%3s%15s%15s%11s' % (lp, imie, nazwisko, pesel))                
        except:
            print('Błąd. Nie można odczytać') 
        self.conn.close()
    
    def wpis(self):
        self.polacz()
        insert = ("insert into uzytkownicy (imie, nazwisko, pesel) values ('c', 'd', '155560')")
        try:
            self.c.execute(insert)
            self.conn.commit()
        except:
            print('Błąd. Nie można dodać rekordu')
        self.conn.close()

db = Rekord()
db.wpis()
db.odczyt()
"""