# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

ponto1 = [float(value) for value in input().split(' ')]
ponto2 = [float(value) for value in input().split(' ')]

distancia = (((ponto2[0] - ponto1[0]) ** 2) + ((ponto2[1] - ponto1[1]) ** 2)) ** 0.5

print(f"{distancia:.4f}")