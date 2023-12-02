# -*- coding: utf-8 -*-

# Открываем файл с данными для чтения
with open('blockList.txt', 'r') as file:
    lines = file.readlines()  # Считываем строки из файла

# Создаем множество для хранения уникальных строк
unique_lines = set()

# Добавляем уникальные строки в множество, удаляем начальные || и символы ^
for line in lines:
    line_without_pipe = line.replace('||', '', 1).rstrip('\n').rstrip('^')  # Удаляем первые два символа || и символ ^ справа
    unique_lines.add(line_without_pipe.strip())  # Удаляем лишние пробелы и символы переноса строки

# Открываем новый файл для записи уникальных строк
with open('flbl.txt', 'w') as new_file:
    # Записываем уникальные строки в новый файл
    for unique_line in unique_lines:
        new_file.write(unique_line + '\n')  # Добавляем символ переноса строки между строками
