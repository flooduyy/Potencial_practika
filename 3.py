import csv  # импортируем модуль для работы с csv файлами


with open('students_new.csv', encoding="utf8") as file:  # открываем файл для чтения
    reader = csv.DictReader(file, delimiter=',', quotechar='"')  # заносим его строки в список
    data = sorted(reader, key=lambda x: x['titleProject_id'])  # сортируем по id проекта

id_project = input()  # вводим искомый id проекта
while id_project != 'СТОП':  # пока не ввели СТОП
    id_project = int(id_project)  # переводим в число
    for el in data:  # проверяем каждую строку
        if int(el['titleProject_id']) == id_project:  # если нашелся искомый проект
            surname, name, patronumic = el["Name"].split()  # сохраняем ФИО ученика
            print(f'Проект № {id_project} делал: {name[0]}. {surname} он(а) получил(а) оценку - {el["score"]}.')  # выводим его результат
            break
    else:  # иначе
        print('Ничего не найдено')
    id_project = input()  # вводим следующий
