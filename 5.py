import csv  # модуль для работы с csv


def generate_hash(s: str):  # генерация хеша
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    d = {l: i for i, l in enumerate(alphabet, 1)}  # словарь, ключ-буква, номер соответствует буквам
    p = 67
    m = 10**9 + 9
    hash_value = 0
    p_pow = 1  # p**0
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


students_with_hash = []
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for row in reader:
        row['id'] = generate_hash(row['Name'])
        students_with_hash.append(row)

with open('students_with_hash.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    w.writeheader()
    w.writerows(students_with_hash)
