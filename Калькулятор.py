print("""
Калькулятор может складывать, умножать, делить, отнимать и находить остаток. Операции выполняются с учетом приоритета. 
Возможна смена приоритета с помощью скобок. Поддерживается работа как с целыми, так и с вещественными числами (до тысячных, ответ тоже до тысячных)
Длина выражения не ограничена. 
Реализован отлов ошибок. В случае неправильного ввода предлагается ввести снова.
Выполненные задания:
0, 1, 3, 4, 10
""")

chisla = {"ноль":0,"один":1,"два":2,"три":3,"четыре":4,"пять":5,"шесть":6,"семь":7,"восемь":8,"девять":9,"десять":10,
    "одиннадцать":11,"двенадцать":12,"тринадцать":13,"четырнадцать":14,"пятнадцать":15,'шестнадцать':16,'семнадцать':17, 'восемнадцать':18,
    "девятнадцать":19,"двадцать":20,"тридцать":30,"сорок":40, "пятьдесят":50,"шестьдесят":60,"семьдесят":70,"восемьдесят":80,
    "девяносто":90, "сто":100, "двести":200, "триста": 300, "четыреста":400, "пятьсот":500, "шестьсот":600,
    "семьсот":700, "восемьсот":800, "девятьсот":900,"десятых":0.1, "сотых": 0.01, "тысячных": 0.001, "плюс": "+", "минус": "-", "умножить": "*", "делить":"/","остаток":"%", "и":"@",
    "скобка1":"(", "скобка2":")"}
#Словарь необходим нам для перевода строковых чисел в обычные

def skleivanie(a):
    i = 0
    while '@' in a:
        if a[i] == '@':
            a[i: i + 3] = [round(a[i+1] * a[i+2], 4)]
        i += 1
    for j in range(len(a) - 1):
        for i in range(len(a) - 1):
            try:
                new = float(a[i]) + float(a[i + 1])
                a[i:i + 2] = [new]
            except BaseException:
                continue
    return a
#Функция делает из 20 5 -> 25, соединяет части вещественного числа и т.д.

def preobr(chisla, a):
    s = skleivanie([chisla[i] for i in a])
    print(s)
#Получаем на вход строку, преобразуем строковые числа в обычные
    while '(' in s:
        rez = calc(s[len(s) - 1 - s[::-1].index('(') + 1: s.index(')')])
        s[len(s) - 1 - s[::-1].index('(') : s.index(')') + 1] = rez
    return calc(s)
#Здесь мы сначала отправляем в наш калькулятор выражения в скобках и подставляем результат на место скобок и их содержимого.
# А когда скобок не остается, мы отправляем получившееся выражение в калькулятор целиком
# Далее отправляем его в место вызова. То есть на вывод

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
#Функция возвращает ключ по значнию. Нужно для обратного перевода

def dec(chisla, a):
    a = a[2:]
    if len(a) == 3:
        try:
            a = int(a)
            return get_key(chisla, (a//100) * 100) + " " + get_key(chisla, a -  (a//100) * 100) + " тысячных"
        except BaseException:
            a = int(a)
            return get_key(chisla, (a//100) * 100) + " " + get_key(chisla, (a -  a % 10 - (a//100)*100)) + " " + get_key(chisla, (a -  (a//100) * 100)%10) + " тысячных"
    elif len(a) == 2:
        try:
            a = int(a)
            return get_key(chisla, a) + " сотых"
        except BaseException:
            a = int(a)
            return get_key(chisla, a//10) + " " + get_key(chisla, a % 10) + " сотых"
    elif len(a) == 1:
        return get_key(chisla, int(a)) + " десятых"
#Функция для перевода остатка в строковые числа. Похоже по сути на перевод целой части, но в конце добавляем сотых, десятых и т.д.

def obr_zam(chisla, a):
    a = float(a)
    if len(str(int((a)))) == 3:
        try:
            if a % 1 == 0.0:
                a = int(a)
                return get_key(chisla, (a//100) * 100) + " " + get_key(chisla, a -  (a//100) * 100) + " целых"
            else:
                return get_key(chisla, (int(a)//100) * 100) + " " + get_key(chisla, int(a) -  (int(a)//100) * 100) + " целых и "  + dec(chisla, str(round(a % 1, 3)))
        except BaseException:
            if a % 1 == 0.0:
               a = int(a)
               return get_key(chisla, (a//100) * 100) + " " + get_key(chisla, (a - a % 10 - (a//100)*100)) + " " + get_key(chisla, (a -  (a//100) * 100)%10) + " целых"
            else:
               return get_key(chisla, (int(a)//100) * 100) + " " + get_key(chisla, int(a) -  int(a) % 10 - (int(a)//100) * 100) + " " + get_key(chisla, (int(a) -  (int(a)//100) * 100)%10) + " целых и " + dec(chisla, str(round(a % 1, 3)))
    elif len(str(int((a)))) == 2:
        try:
            if a % 1 == 0.0:
                a = int(a)
                return get_key(chisla, a) + " целых"
            else:
                return get_key(chisla, int(a)) + " целых и "  + dec(chisla, str(round(a % 1, 3)))
        except BaseException:
            if a % 1 == 0.0:
               a = int(a)
               return get_key(chisla, (a//10)*10) + " " + get_key(chisla, (a % 10)) + "целых"
            else:
               return get_key(chisla, (int(a)//10)*10) + " " + get_key(chisla, (int(a) % 10)) + " целых и " + dec(chisla, str(round(a % 1, 3)))
    elif len(str(int((a)))) == 1:
        if a % 1 == 0.0:
            return get_key(chisla, int(a)) + " целых"
        else:
            return get_key(chisla, int(a)) + " целых и " + dec(chisla, str(round(a % 1, 3)))
#Функция перевода числа в строковое.
#Суть в том, что мы проверяем число на наличие остатка и длину. А отлов ошибок помогает нам не забытьь про такие числа как 11, 12 и т.д.
#Мы сначала пытаемся найти число (десятки плюс единицы) в словаре, если результат None, то потом позникает ошибка сложения строковых данных, и мы делаем переход в блок except.
#Там мы уже ищем в словаре отдельно десятки, отдельно единицы.
#В случае, если у нас вещественное число, то дробную часть мы переводим в функции dec()

def calc(s):
    i = 1
    while "*" in s:
        if s[i] == '*':
            s[i - 1: i + 2] =  [float(s[i-1]) * float(s[i+1])]
        else:
            i += 1
    i = 1
    while "/" in s:
        if s[i] == '/':
            s[i - 1: i + 2] = [float(s[i-1]) / float(s[i+1])]
        else:
            i += 1
    i = 1
    while "%" in s:
        if s[i] == '%':
            s[i - 1: i + 2] = [float(s[i-1]) % float(s[i+1])]
        else:
            i += 1
    i = 1
    while "-" in s:
        if s[i] == '-':
            s[i - 1: i + 2] = [float(s[i-1]) - float(s[i+1])]
        else:
            i += 1
    i = 1
    while "+" in s:
        if s[i] == '+':
            s[i - 1: i + 2] = [float(s[i-1]) + float(s[i+1])]
        else:
            i += 1
    s = s[0]
    return obr_zam(chisla, float(s))
#Сам калькулятор. Совершает операции над числамм по приоритету

flag = False
while flag == False:
    try:
        print((preobr(chisla, input("Введите выражение: ").split())))
        flag = True
    except BaseException as b:
        print(f'Неверный ввод: {b}')
#Проверка ввода
