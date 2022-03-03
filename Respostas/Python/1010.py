# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

codigo1, quantidade1, valor1 = [float(value) for value in input().split(' ')]
codigo2, quantidade2, valor2 = [float(value) for value in input().split(' ')]

valor_total = (quantidade1 * valor1) + (quantidade2 * valor2)

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")