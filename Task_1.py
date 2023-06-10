# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

base_1 = 5 # основание
power_1 = 5 #назначаем степень

def Exponentiation(base, power):
    if power == 1:
        return base
    return  base * Exponentiation(base, power -1)

print(Exponentiation(3,4))