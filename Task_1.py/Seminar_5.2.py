#Вводится десятичное число. Реализовать алгоритм его перевода 
#в двоичную систему счисления через рекурсию. Нельзя использовать функцию bin()

def bin(T):
    if T == 0 or T == 1:
        return f'{T}'
    return bin(T // 2) + f'{T % 2}'

T = int(input("Введите десятичное число: "))
print(bin(T))