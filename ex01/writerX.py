
import csv
import os

a1 = (input('введите имя:'))
a2 = (input('введите телефон:'))
a3 = (input('введите заметку:'))

info1=["Олег", 4242, "студент"]
info2=[a1, a2, a3]

path = os.path.join('PythonHW07', 'ex01', 'output.csv')

with open(path, 'a') as file:
    writer=csv.writer(file)
    # название столбцов это надо добавить в отдельный файл, чтобы исполнялось однажды, а не после каждого ввода дописывалось
    # writer.writerow(("имя","телефон","заметки"))
    writer.writerow(info2)
    