# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

a, b, c = [int(value) for value in input().split(' ')]

maior_ab = (a + b + abs(a - b)) / 2
maior_abc = int((maior_ab + c + abs(maior_ab - c)) / 2)

print(f"{maior_abc} eh o maior")