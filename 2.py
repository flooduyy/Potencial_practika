import csv  # импортируем модуль для работы с csv файлами

with open('students.csv', encoding='utf8') as file:  # открываем файл для чтения
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))  # заносим его строки в список
    for i in range(len(reader)):  # сортировка списка
        j = i - 1
        key = reader[i]  # ключевое значение
        while float(reader[j]['score'] if reader[j]['score'] != 'None' else 0) < float(key['score'] if key['score'] != 'None' else 0) and j >= 0:
            reader[j + 1] = reader[j]
            j -= 1
        reader[j+1] = key

print('10 класс')  # выводим класс
count = 1  # место ученика
for el in reader:  # перебираем каждый элемент
    if '10' in el["class"]:  # если ученик из 10 класса
        surname, name, patronumic = el["Name"].split()  # сохраняем ФИО ученика
        print(f"{count} место: {name[0]}. {surname}")  # выводим место ученика и его именем и фамилией
        count += 1
    if count == 4:  # ломаем цикл на 4 месте
        break
