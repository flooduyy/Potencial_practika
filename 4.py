import csv  # для работы с csv
import string  # для взятия инициалов
import random  # для генерации пароля


def create_initials(s):  # генерация логина
    names = s.split()  # список из Ф И О
    return f'{names[0]}_{names[1][0]}{names[2][0]}'


def create_password():  # генерация пароля
    characters = string.ascii_letters + string.digits  # всевозможные буквы и цифры
    password = ''.join(random.choice(characters) for i in range(8))  # пароль из рандомных символов строки characters длиной 8
    return password


students_with_password = []  # новый список с данными от личного кабинета
with open('students.csv', encoding='utf-8') as file:  # открываем файл
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))  # список из csv файла
    for row in reader:  # берем каждую строку из файла
        row['login'] = create_initials(row['Name'])  # создаем новую ячейку и вписываем туда сгенерированный логин
        row['password'] = create_password()  # ещё одна новая ячейка со сгенерированным паролем
        students_with_password.append(row)  # добавляем новую строку в результирующий список

with open('students_password.csv', 'w', newline='', encoding='utf-8') as file:  # создаём новый файл из результирующего списка
    w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])  # создает файл с указанными индексами
    w.writeheader()  # записываем заголовок в файл
    w.writerows(students_with_password)  # записываем список новых строк с логином и паролем
