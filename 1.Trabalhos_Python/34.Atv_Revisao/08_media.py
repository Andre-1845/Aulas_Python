# 8. Crie um programa em que o usuário informe uma quantidade desejada de números decimais de, no mínimo 0 e no máximo 10, e o programa calcula a média desses números.

import os
lista_numeros = []
i = 1
print ('Digite os numeros. ')
while True:
    os.system('cls')
    numero_input = input(f'Digite o {i}º numero (Deixe em branco para encerrar)')
    
    i = i+1
    if numero_input != "":
        numero = float(numero_input)
        lista_numeros.append(numero)
        continue
    else:
        
        qtde = len(lista_numeros)
        soma = sum(lista_numeros)
        media = soma/qtde
        print(f'\nA média das {qtde} numeros é {media:,.2f}')
        
    continuar = input('Deseja calcular outra média? (s/n) ')
    if continuar != "n":
        i=1
        lista_numeros = []
        continue
    else:
        break