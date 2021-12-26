import pandas as pd
import pickle as pkl
import csv
import os
import datetime

"""Можно импортировать Tabulate для красивого вывода"""

def load_table_csv(*file_csv):
    output_file = input('Введите название csv файла, в который хотите сохранить данные: ')
    csv_file = pd.concat(map(pd.read_csv, file_csv))
    csv_file.to_csv(output_file)
#загрузка во внутреннее представление модуля

def save_table_csv(*f):
    max_rows = int(input('Введите максимальное количество столбцов: '))
    output_csv = pd.concat(map(pd.read_csv, f), ignore_index=True)
    print(output_csv[:max_rows])
#сохранение из внутреннего представления модуля

def load_table_pickle(*file_csv):
    #Преобразовываем данные в словарь
    csv_file = pd.concat(map(pd.read_csv, file_csv))
    csv_file.to_csv('new_table.csv')
    with open('new_table.csv', "r", encoding='utf-8') as input_file:
        reader = csv.DictReader(input_file)
        dict = list(reader)
    os.remove('new_table.csv')
    #Здесь мы уже записываем наши данные в pkl файл
    pickle_file = input("Введите название pkl файла: ")
    with open(pickle_file, 'wb') as output:
        pkl.dump(dict, output)
#Функция сохраняет содержимое csv файла(-ов) в двоичном виде в указанном пользователем файле (.pkl)

def save_table_pickle(*f):
    file_csv = pd.concat(map(pd.read_csv, f))
    file_csv.to_csv('new.csv', index=False)
    max_rows = int(input('Введите максимальное количество столбцов: '))
    with open('new.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dict = list(reader)[:max_rows]
    os.remove('new.csv')
    print(pkl.dumps(dict))
#Функция выводит выбранное представление объекта как объекта байтов вместо записи его в файл

def load_table_txt(file_csv):
    txt_file = input("Введите название txt файла: ")
    with open(txt_file, "w", encoding='utf-8') as output_file:
        with open(file_csv, "r", encoding='utf-8') as input_file:
            [output_file.write(" ".join(row)+'\n') for row in csv.reader(input_file)]
#Функция сохраняет содержимое csv файла в текстовом виде в указанном пользователем тектовом файле (.txt)

def save_table_txt(file_csv):
    with open(file_csv, "r", encoding='utf-8') as input_file:
        f = [(" ".join(row)).split(',') for row in csv.reader(input_file)]
        for row in f:
            print(*row)
#Функция выводит на экран содерживое csv файла в текстовом виде (.txt)

"""Операции с таблицей"""

def get_rows_by_number(start, stop, file_csv, copy_table = True):
    csv_file = pd.read_csv(file_csv)
    if copy_table:
        print(csv_file[start:stop + 1])
#Мы выводим на экран срез из строк таблицы. Нумерация строк начинается с 0. Заголовок выводится в любом случае
    else:
        output_file_csv = input('Введите название csv файла, в который хотите сохранить данные: ')
        csv_file[start:stop + 1].to_csv(output_file_csv, index=False)
#Здесь мы записываем наши изменения в новый файл

def get_rows_by_index(file_csv, val, copy_table = True):
    csv_file = pd.read_csv(file_csv)
    value_first_column = csv_file.columns.to_list()[0]
    if copy_table:
        if len(csv_file[csv_file[value_first_column].isin(val)]) >= 0: #исключение
            print(csv_file[csv_file[value_first_column].isin(val)])
        else:
            print('Такого значения в этой таблице нет. Пожалуйста, введите существующее значение')
#Мы выводим на экран срез из строк таблицы, что совпадают по переданному значению имени (Мы ищем по первому столбцу)
    else:
        if len(csv_file[csv_file[value_first_column].isin(val)]) >= 0:  # исключение
             output_file_csv = input('Введите название csv файла, в который хотите сохранить данные: ')
             csv_file[csv_file[value_first_column].isin(val)].to_csv(output_file_csv, index=False)
        else:
            print('Такого значения в этой таблице нет. Пожалуйста, введите существующее значение') #здесь мне (гумиста) надо перепроверить tryexcept с copytable=false
#Здесь мы записываем наши изменения в новый файл

def get_column_types(file_csv):
    try: #исключение (если например, ввели название столбца с пробелом или вообще ввели название, которого не существует
        csv_file = pd.read_csv(file_csv)
        print(csv_file.dtypes)
    except KeyError:
        print('Пожалуйста введите правильное название столбца')
#Узнаем, какого типа наши данные (по столбцам)

def set_column_types(file_csv, copy_table = True):
    try: #исключение (если например, хотят поменять str на float
        column = input('Введите название столбца: ')
        type = input('Введите тип, в который хотите преобразовать столбец: ')
        csv_file = pd.read_csv(file_csv)
        csv_file[column] = csv_file[column].astype(type)
        if copy_table:
            print(csv_file)
        else:
            output_file_csv = input('Введите название csv файла, в который хотите сохранить данные: ')
            csv_file.to_csv(output_file_csv, index=False)
    except ValueError:
        print('Смена типа выбранного вами столбца невозможна')

def get_values(file_csv,column, copy_table = True):
    try: #исключение ( если в файле 10 столбоц, а ввели номер 20
        csv_file = pd.read_csv(file_csv)
        if copy_table:
            print(csv_file[csv_file.columns.to_list()[column]].values)
        else:
            output_file_csv = input('Введите название csv файла, в который хотите сохранить данные: ')
            data = csv_file[csv_file.columns.to_list()[column]].values
            with open(output_file_csv, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                for item in data:
                    csv_writer.writerow([item])
    except IndexError:
        print("Такого номера столбца не существует")

def get_value(file_csv, column, number):
    try: #исключение (если у нас например 10 строк, а ввели 20 номер)
        csv_file = pd.read_csv(file_csv)
        print(csv_file[csv_file.columns.to_list()[column]].values[number])
    except IndexError:
        print("Такого номера строки не существует")
#Здесь мы выводим одно значение по заданным номеру столбца и номеру строки

def set_values(file_csv, new_value, column, copy_table=True):
    csv_file = pd.read_csv(file_csv)
    csv_file.loc[[i for i in range(len(csv_file.index))], csv_file.columns.to_list()[column]] = new_value
    if copy_table:
        print(csv_file)
    else:
        output_file_csv = input('Введите название csv файла, в который хотите сохранить данные: ')
        csv_file.to_csv(output_file_csv, index=False)
#Функция выводит значения столбца

def set_value(file_csv, new_value, column,number, copy_table=True):
    csv_file = pd.read_csv(file_csv)
    csv_file.loc[number, csv_file.columns.to_list()[column]] = new_value
    if copy_table:
        print(csv_file)
    else:
        output_file_csv = input('Введите название csv файла, в который хотите сохранить данные: ')
        csv_file.to_csv(output_file_csv, index=False)
#Функция выводит значение(1!) столбца

def print_table(file_csv):
    csv_file = pd.read_csv(file_csv)
    print(csv_file)
#Печать таблицы

def concat(table1, table2, copy_table=True):
    two_tables = pd.concat(map(pd.read_csv, [table1, table2]))
    if copy_table:
        print(two_tables)
    else:
        output_file_csv = input('Введите название csv файла, в который хотите сохранить данные: ')
        two_tables.to_csv(output_file_csv, index=False)
#Функция склеивает две таблицы

def split(file_csv, row_number):
    csv_file = pd.read_csv(file_csv)
    output_file1, output_file2 = (input() for i in range(2))
    csv_file[:row_number + 1].to_csv(output_file1, index=False)
    csv_file[row_number + 1:].to_csv(output_file2, index=False)
#Функция разделяет таблицы на две по переданному значению и загружает в файлы, указанные пользователем

def equal(file_csv, **columns):
    csv_file = pd.read_csv(file_csv)
    column = list(columns.values())
    if type(column[0]) == str:
        csv_file['eq'] = (csv_file[column[0]] == csv_file[column[1]])
        print(csv_file['eq'])
    elif type(column[0]) == int:
        column_index_1, column_index_2 = csv_file.columns[column[0]], csv_file.columns[column[1]]
        csv_file['eq'] = csv_file[column_index_1] == csv_file[column_index_2]
        print(csv_file['eq'])
#Функция сравнивает значения указанных колонок (==)

def more(file_csv, **columns):
    csv_file = pd.read_csv(file_csv)
    column = list(columns.values())
    if type(column[0]) == str:
        csv_file['more'] = (csv_file[column[0]] > csv_file[column[1]])
        print(csv_file['more'])
    elif type(column[0]) == int:
        column_index_1, column_index_2 = csv_file.columns[column[0]], csv_file.columns[column[1]]
        csv_file['more'] = csv_file[column_index_1] > csv_file[column_index_2]
        print(csv_file['more'])
#Функция сравнивает значения столбцов (>)

def less(file_csv, **columns):
    csv_file = pd.read_csv(file_csv)
    column = list(columns.values())
    if type(column[0]) == str:
        csv_file['less'] = (csv_file[column[0]] < csv_file[column[1]])
        print(csv_file['less'])
    elif type(column[0]) == int:
        column_index_1, column_index_2 = csv_file.columns[column[0]], csv_file.columns[column[1]]
        csv_file['less'] = csv_file[column_index_1] < csv_file[column_index_2]
        print(csv_file['less'])
#Функция сравнивает значения столбцов (<)

def more_equal(file_csv, **columns):
    csv_file = pd.read_csv(file_csv)
    column = list(columns.values())
    if type(column[0]) == str:
        csv_file['more_equal'] = (csv_file[column[0]] >= csv_file[column[1]])
        print(csv_file['more_equal'])
    elif type(column[0]) == int:
        column_index_1, column_index_2 = csv_file.columns[column[0]], csv_file.columns[column[1]]
        csv_file['more_equal'] = csv_file[column_index_1] >= csv_file[column_index_2]
        print(csv_file['more_equal'])
#Функция сравнивает значения столбцов (>=)

def less_equal(file_csv, **columns):
    csv_file = pd.read_csv(file_csv)
    column = list(columns.values())
    if type(column[0]) == str:
        csv_file['less_equal'] = (csv_file[column[0]] <= csv_file[column[1]])
        print(csv_file['less_equal'])
    elif type(column[0]) == int:
        column_index_1, column_index_2 = csv_file.columns[column[0]], csv_file.columns[column[1]]
        csv_file['less_equal'] = csv_file[column_index_1] <= csv_file[column_index_2]
        print(csv_file['less_equal'])
#Функция сравнивает значения столбцов (<=)

def not_equal(file_csv, **columns):
    csv_file = pd.read_csv(file_csv)
    column = list(columns.values())
    if type(column[0]) == str:
        csv_file['not_equal'] = (csv_file[column[0]] != csv_file[column[1]])
        print(csv_file['not_equal'])
    elif type(column[0]) == int:
        column_index_1, column_index_2 = csv_file.columns[column[0]], csv_file.columns[column[1]]
        csv_file['not_equal'] = csv_file[column_index_1] != csv_file[column_index_2]
        print(csv_file['not_equal'])
#Функция сравнивает значения столбцов (!=)

def filter_rows(file_csv, bool_list, copy_table=True):
        csv_file = pd.read_csv(file_csv)
        df_bool_list = pd.DataFrame(bool_list, columns =['value'])
        rslt_df = csv_file.loc[df_bool_list['value'] == True]
        if copy_table:
            print(rslt_df)
        else:
            output_file_csv = input('Введите название csv файла, в который хотите сохранить данные: ')
            csv_file.to_csv(output_file_csv, index=False)
#Функция выводит строчки, в которых значение bool_list == True


# filter_rows('1.csv', [False, True, True, True, False])


def add(file_csv):
    file_csv = pd.read_csv(file_csv)
    try:
        from_user = int(input("Введите число, которое хотите добавить к столбцу: "))
        x = input('Введите название столбца: ')
        column = file_csv[x].add(from_user)
        print(column)
    except TypeError:
        print('Ошибка')


def sub(file_csv):
    file_csv = pd.read_csv(file_csv)
    try:
        from_user = int(input("Введите число, которое хотите вычесть из столбца: "))
        x = input('Введите название столбца: ')
        column = file_csv[x].sub(from_user)
        print(column)
    except TypeError:
        print('Ошибка')


def div(file_csv):
    file_csv = pd.read_csv(file_csv)
    try:
        from_user = int(input("Введите число, на которое хотите разделить столбец: "))
        x = input('Введите название столбца: ')
        column = file_csv[x].div(from_user)
        print(column)
    except TypeError:
        print('Ошибка')


def mul(file_csv):
    file_csv = pd.read_csv(file_csv)
    from_user = int(input("Введите число, на которое хотите умножить столбец: "))
    x = input('Введите название столбца: ')
    column_type = str(file_csv.dtypes[x])
    try:
        if column_type == 'int64' or column_type == 'float64':
            column = file_csv[x].mul(from_user)
            print(column)
        else:
            print('Нельзя умножать столбец данного типа')
    except TypeError:
        print('Ошибка')

def merge_tables(f1, f2):
    try:
        file_csv1 = pd.read_csv(f1)
        file_csv2 = pd.read_csv(f2)
        res = file_csv1.merge(file_csv2)
        print(res)
    except pd.errors.MergeError as e:
        if 'No common columns to perform merge on' in str(e):
            print('Нет общих столбцов')
        else:
            print('Ошибка')


def date_time(file_csv):
    file_csv = pd.read_csv(file_csv)
    x = input('введите название столбца, которое хотите изменить в формат datetime: ')
    file_csv[x] = pd.to_datetime(file_csv[x])
    print(file_csv)
    print(file_csv.dtypes)


def date_time2(file_csv):
    file_csv = pd.read_csv(file_csv)
    file_csv['meeting date'] = pd.Timestamp('2021-12-20')
    print(file_csv)
    print(file_csv.dtypes)




# load_table_csv('1.csv', '2.csv')
#file_csv = input('Введите название файла, из которого необходимо взять информацию: ')
# split('1.csv', 2)
# equal('ludiki.csv', column1 = 'Год рождения',column2 = 'Дом')
# filter_rows('1.csv')
# load_table_pickle('1.csv','2.csv')
# get_value(file_csv, column, 2)
# val = ['Саша', 'Маша']
# set_column_types(file_csv, copy_table=False)
# get_rows_by_index(file_csv, val, copy_table=True)

# add(file_csv)
# sub(file_csv)
# div(file_csv)
# mul(file_csv)
#date_time(file_csv)
#date_time2(file_csv)

# get_rows_by_index('ludiki.csv', ['П','К'])
"""Мы вводим название csv файла, с которым хотим работать. 
После выполнения всех операций можем записать результат в любом из возможных расширений: csv, txt, pickle. 
Мы можем записать результат в файл или выывести на экран
Также Натали проверила, можно ли вводить путь. И да, можно 
C:/Users/User/Desktop/Учеба/Прога/Питон/2.txt"""

"""
Описание функций операций:

get_rows_by_number(start, [stop], copy_table=False) – получение таблицы 
из одной строки или из строк из интервала по номеру строки.
Функция либо копирует исходные данные, либо создает новое представление таблицы, 
работающее с исходным набором данных (copy_table=False),
таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.

get_rows_by_index(val1, … , copy_table=False) – получение новой таблицы из одной строки или 
из строк со значениями в первом столбце(!!!), совпадающими с переданными аргументами val1, … , valN. 
Функция либо копирует исходные данные, либо создает новое представление таблицы, работающее с 
исходным набором данных (copy_table=False), таким образом изменения, внесенные через это представления 
будут наблюдаться и в исходной таблице.

Нам нужно передать в функцию список значений, по которым мы хотим искать совпадения. 
В каждой таблице автоматически подставляется значение первого столбца (Например, имя)
Например:
val = ['Саша', 'Петя']
get_rows_by_index(file_csv, val)
>>
    Имя Успеваемость  Год рождения
0  Саша     отличник          2000
2  Петя     троечник          2000

get_column_types(by_number=True) – получение словаря вида столбец:тип_значений. 
Тип значения: int, float, bool, str (по умолчанию для всех столбцов).
Параметр by_number определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.
(Пишу столбец, который хочу выбрать и эта функция мне показывает тип этого столбца. 
Например, пишу что хочу узнать тип столбца (Имя) – он выводит мне str

set_column_types(types_dict, by_number=True) – задание словаря вида столбец:тип_значений. 
Тип значения: int, float, bool, str (по умолчанию для всех столбцов).
Параметр by_number определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.
(меняем значения столбцов, например: я хочу поменять столбец (Год рождения) с int на float)

get_values(column=0) – получение списка значений (типизированных согласно типу столбца) таблицы из столбца либо по 
номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца)
(выводим список значений из одного столбца, например: столбец(имя)): [даша, маша,наташа])

get_value(column=0) – аналог get_values(column=0) для представления таблицы с одной строкой, 
возвращает не список, а одно значение (типизированное согласно типу столбца).
(используем get_values для этой функции. Здесь надо вывести имя под номер 5, значит только одно имя)

set_values(values, column=0) – задание списка значений values для столбца таблицы (типизированных 
согласно типу столбца) либо по номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца).
(меняем значения столбца на одно и тоже значение. 
Например, были разные имена и после этой функции все строки будут только с именем катя)

set_value(column=0) – аналог set_values(value, column=0) для представления таблицы с одной строкой, 
устанавливает не список значений, а одно значение (типизированное согласно типу столбца).
(прошлая функция, но только для одной строки)

print_table() – вывод таблицы на печать


"""
a = datetime.datetime(year=2001, month=7, day=4)
"""Дополнительные операции:

В load_table реализовать load_table(file1, …) – поддержку загрузки таблицы, разбитой на несколько файлов 
(произвольное количество фйалов) (для форматов csv и pickle). В случае несоответствия структуры столбцов 
файлов вызывать исключительную ситуацию.
Сложность 1

Реализовать функцию concat(table1, table2) и split(row_number) склеивающую две таблицы (или разбивающую одну 
таблицу на 2 по номеру строки.)
Сложность 1

По аналогии с п. 6 реализовать функции eq (==), gr (>), ls (<), ge (>=), le (<=), ne (==), которые возвращают 
список булевских значений длинной в количество строк сравниваемых столбцов. Реализовать функцию 
filter_rows (bool_list, copy_table=False) – получение новой таблицы из строк для которых в bool_list 
(длинной в количество строк в таблице) находится значение True.
Сложность 3
Пример использования filter_rows (bool_list, copy_table=False)
filter_rows('1.csv', [False, True, True, True, False])
>>>
    Имя Успеваемость  Год рождения  Возраст   Дети
1  Маша   хорошистка          1999       10   True
2  Петя     троечник          2000       17  False
3  Саша     троечник          2001       26  False


"""


"""

Полезные ссылки:
https://habr.com/ru/company/ruvds/blog/494720/

https://dfedorov.spb.ru/pandas/Обзор%20типов%20данных%20pandas.html

Эксель портит данные. Если мы хоти открыть файл csv в экселе, то нужно выполнить некоторые манипуляции
https://habr.com/ru/company/hflabs/blog/432906/


"""
