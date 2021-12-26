# -
Здесь собраны все практикумы по программированию (1 курс, ФУ при Правительстве РФ)


Практикум 1: Морской бой
9.	(*) Реализовать программу, с которой можно играть в игру «Морской бой». Программа автоматически случайно расставляет на поле размером 10 на 10 клеток: 4 1-палубных корабля, 3 2-палубных корабля, 2 3-палубных корабля и 1 4-х палубный. Между любыми двумя кораблями по горизонтали и вертикали должна быть как минимум 1 незанятая клетка. Программа позволяет игроку ходить, производя выстрелы. Сама программа НЕ ходит т.е. не пытается топить корабли расставленные игроком.
Взаимодействие с программой производится через консоль. Игровое поле изображается в виде 10 текстовых строк и перерисовывается при каждом изменении состояния поля. При запросе данных от пользователя программа сообщает, что ожидает от пользователя (в частности, координаты очередного «выстрела») и проверяет корректность ввода. Программа должна уметь автоматически определять потопление корабля и окончание партии и сообщать об этих событиях.

Практикум 2: Калькулятор
Базовая часть (выполняется всеми самостоятельно!):
Написать калькулятор для строковых выражений вида '<число> <операция> <число>', где <число> - не отрицательное целое число меньшее 100, записанное словами, например "тридцать четыре", <арифмитическая операция> - одна из операций "плюс", "минус", "умножить". Результат выполнения операции вернуть в виде текстового представления числа. Пример calc("двадцать пять плюс тринадцать") -> "тридцать восемь"
Оформить калькулятор в виде функции, которая принимает на вход строку и возвращает строку.

Дополнительные задания:
1)	Реализовать поддержку операции деления и остатка от деления и работу с дробными числами (десятичными дробями). Пример: calc("сорок один и тридцать одна сотая разделить на семнадцать") -> "два и сорок три сотых". Обрабатывать дробную часть до тысячных включительно, если при делении получаются числа с меньшей дробной частью выполнять округление до тысячных.
Сложность 2
2)	Расширение задания 1. Реализовать поддержку десятичной дробной части до миллионных долей включительно. Реализовать корректный вывод информации о периодической десятичной дроби (период дроби вплоть до 4х десятичных знаков). Пример: calc("девятнадцать и восемьдесят две сотых разделить на девяносто девять") -> "ноль и двадцать сотых и ноль два в периоде ".
Сложность 3
3)	Реализовать текстовый калькулятор для выражения из произвольного количества операций с учетом приоритета операций. Пример: calc("пять плюс два умножить на три минус один") -> "десять". (Для реализации рекомендуется использовать алгоритмы основанные на польской инверсной записи см. например, https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D1%8C )
Сложность 3
4)	Расширение задания 3. Добавить поддержку приоритета операций с помощью скобок. Пример: calc("скобка открывается пять плюс два скобка закрывается умножить на три минус один") -> "двадцать". 
Сложность 3
5)	Добавить возможность использования отрицательных чисел. Пример: calc("пять минус минус один") -> "шесть". 
Сложность 1
6)	Добавить возможность оперировать с дробями (правильными и смешанными). Реализовать поддержку сложения, вычитания и умножения, дробей. Результат операций не должен представлять неправильную дробь, такие результаты нужно превращать в смешанные дроби. Пример: calc("один и четыре пятых плюс шесть седьмых ") -> "два и двадцать три тридцать пятых". 
Сложность 3
7)	Расширение задания 6. Добавить автоматическое сокращение дроби в ответе. Пример: calc("одна шестая умножить на две третьих") -> "одна девятая". 
Сложность 1
8)	Расширение задания 1. Добавить операции возведения в степень и тригонометрические операции синус, косинус, тангенс и константу пи. Допускается как минимум одна из этих функций в выражении с обычными операциями. Пример: calc("два в степени четыре") -> "шестнадцать". Пример: calc("синус от пи разделить на четыре") -> "ноли и семьсот семь тысячных".
Сложность 1 или 2
9)	Добавить комбинаторные операции перестановки, размещения и сочетания. Пример: calc("размещений из трех по два") -> "шесть". 
Сложность 1 или 2
10)	Диагностировать ошибки: неправильную запись числа; неправильную последовательность чисел и операций; (задание 1) деление на ноль; (задание 3) неправильную последовательность чисел и операций; (задание 4) некорректный баланс и вложенность скобок; (задание 6) некорректную запись числа 
Сложность 1 или 2

Практикум 3: Реализация собственного пакета модулей по манипулированию табличными данными.
Базовая часть (выполняется всеми самостоятельно!):

На базе модулей: csv, pickle и прямой работы с файлами реализовать следующий базовый функционал:

•	функций load_table, save_table по загрузке/сохранению табличных данных во внутреннее представление модуля/из внутреннего представления модуля:
o	файла формата csv (отдельный модуль с load_table, save_table в рамках общего пакета)

o	файла формата pickle (отдельный модуль с load_table, save_table в рамках общего пакета), модуль использует структуру данных для представления таблицу, удобную автору работы.

o	текстового файла (только функция save_table сохраняющая в текстовом файле представление таблицы, аналогичное выводу на печать с помощью функции print_table()).

Примечание: внутреннее представление может базироваться на словаре, где по разным ключам хранятся ключевые «атрибуты» таблицы, а значения таблицы хранятся в виде вложенных списков. Студент может выбрать другое внутреннее представление таблицы (согласовав его с преподавателем), в том числе, студенты знакомые с ООП на Python, могут реализовать собственный класс для таблицы.

При определении api модулей максимально полно использовать возможности сигнатур функций на Python (значения по умолчанию, запаковка/распаковка, в т.ч. именованных параметров, возвращение множественных значений), интенсивно выполнять проверки и возбуждать исключительные ситуации.

•	модуля с базовыми операциями над таблицами:

o	get_rows_by_number(start, [stop], copy_table=False) – получение таблицы из одной строки или из строк из интервала по номеру строки. Функция либо копирует исходные данные, либо создает новое представление таблицы, работающее с исходным набором данных (copy_table=False), таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.

o	get_rows_by_index(val1, … , copy_table=False) – получение новой таблицы из одной строки или из строк со значениями в первом столбце, совпадающими с переданными аргументами val1, … , valN. Функция либо копирует исходные данные, либо создает новое представление таблицы, работающее с исходным набором данных (copy_table=False), таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.

o	get_column_types(by_number=True) – получение словаря вида столбец:тип_значений. Тип значения: int, float, bool, str (по умолчанию для всех столбцов). Параметр by_number определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.

o	set_column_types(types_dict, by_number=True) – задание словаря вида столбец:тип_значений. Тип значения: int, float, bool, str (по умолчанию для всех столбцов). Параметр by_number определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.

o	get_values(column=0) – получение списка значений (типизированных согласно типу столбца) таблицы из столбца либо по номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца)

o	get_value(column=0) – аналог get_values(column=0) для представления таблицы с одной строкой, возвращает не список, а одно значение (типизированное согласно типу столбца).
o	set_values(values, column=0) – задание списка значений values для столбца таблицы (типизированных согласно типу столбца) либо по номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца).

o	set_value(column=0) – аналог set_values(value, column=0) для представления таблицы с одной строкой, устанавливает не список значений, а одно значение (типизированное согласно типу столбца).

o	print_table() – вывод таблицы на печать.

•	Для каждой функции должно быть реализована генерация не менее одного вида исключительных ситуаций. 
Дополнительные задания:

1)	В load_table реализовать load_table(file1, …) – поддержку загрузки таблицы, разбитой на несколько файлов (произвольное количество фйалов) (для форматов csv и pickle). В случае несоответствия структуры столбцов файлов вызывать исключительную ситуацию.
Сложность 1

2)	Расширение задания 1.
В save_table реализовать поддержку сохранения таблицы в разбитой на несколько файлов (произвольное количество фйалов) по параметру max_rows, определяющему максимальное количество строк в файле. Файлы csv и pickle, полученные с помощью save_table должны быть совместимы с load_table из задания 1.
Сложность 1

3)	Реализовать функцию concat(table1, table2) и split(row_number) склеивающую две таблицы или разбивающую одну таблицу на 2 по номеру строки.
Сложность 1

4)	Реализовать автоматическое определение типа столбцов по хранящимся в таблице значениям. Оформить как отдельную функцию и встроить этот функционал как опцию работы функции load_table. 
Сложность 1 или 2

5)	Реализовать поддержку дополнительного типа значений «дата и время» на основе модуля datetime.
Сложность 1 или 2

6)	Добавить набор функций add, sub, mul, div, которые обеспечат выполнение арифмитических операций для столбцов типа int, float, bool. Продумать сигнатуру функций и изменения в другие функции, которые позволят удобно выполнять арифметические операции со столбцами и присваивать результаты выч. Реализовать реагирование на некорректные значения с помощью генерации исключительных ситуаций.
Сложность 2

7)	По аналогии с п. 6 реализовать функции eq (==), gr (>), ls (<), ge (>=), le (<=), ne (==), которые возвращают список булевских значений длинной в количество строк сравниваемых столбцов. Реализовать функцию filter_rows (bool_list, copy_table=False) – получение новой таблицы из строк для которых в bool_list (длинной в количество строк в таблице) находится значение True.
Сложность 3

8)	Реализовать функцию merge_tables(table1, table2, by_number=True): в результате слияния создается таблица с набором столбцов, соответствующих объединенному набору столбцов исходных таблиц. Соответствие строк ищется либо по их номеру (by_number=True) либо по значению индекса (1й столбец). При выполнении слияния возможно множество конфликтных ситуаций. Автор должен их описать и определить допустимый способ реакции на них (в т.ч. через дополнительные параметры функции и инициацию исключительных ситуаций).
Сложность 2

9)	Реализовать полноценную поддержку значения None в незаполненных ячейках таблицы. Должно работать при загрузке ячеек с пропусками значений, при операциях приводящих к появлению пустых ячеек, при работе с get и set операциями.
Сложность 1 или 2
(Сделаны все задания)
