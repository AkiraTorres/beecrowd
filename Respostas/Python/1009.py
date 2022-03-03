# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

nome = input()
salario_fixo = float(input())
total_de_vendas = float(input())

salario_final = (total_de_vendas * 0.15) + salario_fixo

print(f"TOTAL = R$ {salario_final:.2f}")