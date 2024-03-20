import csv  # импортируем модуль для работы с csv файлами


with open('students.csv', encoding='utf8') as file:  # открываем файл для чтения
    reader = list(csv.reader(file, delimiter=','))[1:]  # считываем все его строки с данными в список
    count_class = {}  # словарь кол-ва учеников в каждом классе
    sum_class = {}  # словарь суммы оценок в каждом классе
    for idd, name, titleProject_id, level, score in reader:  # перебираем каждую строку
        if 'Хадаров Владимир' in name:  # если нужный ученик
            print(f"Ты получил: {score}, за проект - {titleProject_id}")  # выводим его результат
        '''в словарь по ключу класса прибавляется ученик и его оценка в 
        соответствующие переменные'''
        count_class[level] = count_class.get(level, 0) + 1
        sum_class[level] = sum_class.get(level, 0) + (int(score) if score != 'None' else 0)

    for el in reader:  # перебираем каждую строку
        if el[-1] == 'None':  # если нет оценки
            el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)  # заменяем на среднее значение по классу

with open("students_new.csv", 'w', encoding="utf8", newline='') as file:  # создаем новый файл для записи
    w = csv.writer(file)  # файловая переменная
    w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])  # записываем заголовок
    w.writerows(reader)  # записываем измененный список
