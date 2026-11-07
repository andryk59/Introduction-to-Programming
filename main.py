print ("Hello, world!") # Вывести любой текст в терминал
print ("Heloo", "World", "!")
print ("Heloo", "World", "!", sep=", ") # Параметр sep разделяет слова в функции принт, по дефолту пробел 
print("A great man doesn't seek to lead.", end=' ', sep='') # Параметр end функции print по дефолту переносит следующий print на следующую строку, чтобы этого избежать следует оставить параметр end пустым
print("He's called", "\n" "to it. And he answers.") # Символ \n обозначает перевод строки
#password = input("Enter your password: ")
#print(password)

name = "Angelina"
print(type(name))

age = 23
print(type(age)) # Класс переменной int - целое число, str - строка, float - числа с плавающей запитой 

# Из int в float x = float(y)
# x = int(y) из float сделать int - убирает все знаки после запятой
# округление x = round(y)

# В python есть x, y = y, x которая меняет знаения переменных местами без дополнительной переменной
# Стандарт названия переменных snake_case - имена переменных, функциии, методов модулей
# CamelCase - имена классов
# yet-another-package - название пакетов
# CONSTANT - константы

""" Операции с числами:
+ - сложение
- - вычитание
* - умножение
/ - деление
** - возведение в степень
// - целочисленное деление
% - остаток от деления

"""

flat_number = int(input("Введите номер квартиры: "))
print(type(flat_number))

entrance_number = (flat_number - 1) // 20 + 1
print(entrance_number)

floor_number =  (flat_number - 1) % 20 // 4 + 1
print(floor_number)