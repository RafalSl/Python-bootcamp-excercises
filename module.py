# -*- coding: utf-8 -*-
#importowanie pakietu

from mypackage.module1 import *
from os import *
import random
'''
o1 = Info()
funkcja()
print(a)

print(dir(random))
'''
'''
F = open('pliczek.txt', 'w')
CSV = open('csv.csv', 'w')
print(F.name, F.mode, F.closed)
print(CSV.name, CSV.mode, CSV.closed)

F.write('Tekst do pliku')
print('Zapisuję do pliku %s' % F.name)
F.close
print('Plik %s zamknięty' % F.name)
'''
'''
F = open('oceny.txt', 'w')
print('Plik %s otwarty' % F.name)
F.writelines(['3','\t4','\t5','\t6\n'])
print('Zapisuję do pliku %s' % F.name)
F.close
print('Plik %s zamknięty' % F.name)
'''
'''
F = open('pliczek.txt', 'rb+')
print(F.tell())
print(F.read())
F.seek(4)
print(F.tell())
print(F.read(4))
F.seek(-8, 2)
print(F.tell())
F.seek(0)
F.truncate(10)
print(F.read())
F.close
print('Plik %s zamknięty' % F.name)
'''
'''
print(getcwd())
print(listdir('.'))
chdir('mypackage')
print(getcwd(), listdir('.'))
'''
#P83
class Lista:
    def wpisywanie(self):
        