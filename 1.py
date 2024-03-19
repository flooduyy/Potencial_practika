import csv  # импортируем модуль для работы с cvs файлами

with open('students.csv', encoding='utf8') as file:  # открываем файл
    reader = csv.reader(file, delimiter=',')  # считываем все его строки
    answer = list(reader)[1:]  # массив с данными учеников
    count_class = {}  # словарь
    sum_class = {}  # словарь
    for id, name, titleProject_id, level, score in answer:  # перебираем каждую строку
        if 'Хадаров Владимир' in name:  # если нужный ученик
            print(f"Ты получил: {score}, за проект - {titleProject_id}")  # выводим его результат
        count_class[level] = count_class.get(level, 0) + 1
        sum_class[level] = sum_class.get(level, 0) + (int(score) if score != 'None' else 0)

    for el in answer:  # заменяем каждый None на среднее значение по классу
        if el[-1] == 'None':
            el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)

with open("students_new.csv", 'w', encoding="utf8", newline='') as file:
    w = csv.writer(file)
    w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    w.writerows(answer)
