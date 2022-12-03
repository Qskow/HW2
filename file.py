#1

print("Введите первое число:")
a = float(input())
print("Введите второе число:")
b = float(input())

print(f"Сумма a и b: {a + b}")
print(f"Разность a и b: {a - b}")
print(f"Произведение a и b: {a*b}")
print(f"Частное a и b: {a/b}")
print(f"Число a в степени b: {a**b}")
print(f"Деление числа a по модулю b: {a%b}")
print(f"Целочисленное деление a на b: {a//b}")
print("")

#2

print("Как вас зовут?")
name = input(str())
print(f"Зравствуйте, {name}!")
print("")

#3

my_string = input("Введите строку: ")
print(my_string[-1] + my_string[-2])
print("")
#4

from math import pi
print("Введите радиус круга для вычисления его площади: ")
r = float(input())
print(f"Площадь круга равна: {pi * r}")
print("")