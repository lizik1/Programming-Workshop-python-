import random
row = [[0 for g in range(12)] for l in range(12)]
for i in range(12):
    row[0][i] = 'X'
    row[i][0] = 'X'
    row[11][i] = 'X'
    row[i][11] = 'X'

s = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

for i in range(len(s)):
    if s[i] == 4:
        napr = random.randint(0, 1) #Если 0 - корабль горизонталный, 1 - вертикальный
        x_start = random.randint(1, 10)
        y_start = random.randint(1, 10)
        if napr == 0:
            while x_start > 7:
                x_start = random.randint(1, 10)
            for i in range(4):
                row[y_start][x_start + i] = 4
            for j in range(6):
                row[y_start - 1][x_start + j - 1] = '-'
                row[y_start + 1][x_start + j - 1] = '-'
            row[y_start][x_start-1] = '-'
            row[y_start][x_start+4] = '-'
        else:
            while y_start > 7:
                y_start = random.randint(1, 10)
            for i in range(4):
                row[y_start + i][x_start] = 4
            for j in range(6):
                row[y_start + j - 1][x_start + 1] = '-'
                row[y_start + j - 1][x_start - 1] = '-'
            row[y_start-1][x_start] = '-'
            row[y_start+4][x_start] = '-'

#так как это наш первый корабль -> все клетки свободны и не нужно проверять, являются ли клетки нулями

    if s[i] == 3:
        napr = random.randint(0, 1)
        x_start = random.randint(1, 10)
        y_start = random.randint(1, 10)
        if napr == 0:
            while x_start > 8 or row[y_start][x_start] != 0 or row[y_start][x_start + 1] != 0 or row[y_start][x_start + 2] != 0:
                x_start = random.randint(1, 10)
            for i in range(3):
                row[y_start][x_start + i] = 3
            for j in range(5):
                row[y_start - 1][x_start + j - 1] = '-'
                row[y_start + 1][x_start + j - 1] = '-'
            row[y_start][x_start-1] = '-'
            row[y_start][x_start+3] = '-'
        else:
            while y_start > 8 or row[y_start][x_start] != 0 or row[y_start + 1][x_start] != 0 or row[y_start + 2][x_start] != 0:
                y_start = random.randint(1, 10)
            for i in range(3):
                row[y_start + i][x_start] = 3
            for j in range(5):
                row[y_start + j - 1][x_start + 1] = '-'
                row[y_start + j - 1][x_start - 1] = '-'
            row[y_start-1][x_start] = '-'
            row[y_start+3][x_start] = '-'

    if s[i] == 2:
        napr = random.randint(0, 1)
        x_start = random.randint(1, 11)
        y_start = random.randint(1, 11)
        if napr == 0:
            while x_start > 9 or row[y_start][x_start] != 0 or row[y_start][x_start + 1] != 0:
                x_start = random.randint(1, 10)
            for i in range(2):
                row[y_start][x_start + i] = 2
            for j in range(4):
                row[y_start - 1][x_start + j - 1] = '-'
                row[y_start + 1][x_start + j - 1] = '-'
            row[y_start][x_start-1] = '-'
            row[y_start][x_start+2] = '-'
        else:
            while y_start > 9 or row[y_start][x_start] != 0 or row[y_start + 1][x_start] != 0:
                y_start = random.randint(1, 11)
            for i in range(2):
                row[y_start + i][x_start] = 2
            for j in range(4):
                row[y_start + j - 1][x_start + 1] = '-'
                row[y_start + j - 1][x_start - 1] = '-'
            row[y_start-1][x_start] = '-'
            row[y_start+2][x_start] = '-'

    if s[i] == 1:
        x_start = random.randint(1, 10)
        y_start = random.randint(1, 10)
        while row[y_start][x_start] != 0:
            x_start = random.randint(1, 10)
            y_start = random.randint(1, 10)
        row[y_start][x_start] = 1
        for j in range(3):
            row[y_start + j - 1][x_start + 1] = '-'
            row[y_start + j - 1][x_start - 1] = '-'
        row[y_start-1][x_start] = '-'
        row[y_start+1][x_start] = '-'

for i in range(12):
    row[0][i] = '-'
    row[11][i] = '-'
for i in range(12):
    row[i][0] = '|'
    row[i][11] = '|'

print("      " + "Морской бой")

for i in range(12):
    print(*row[i])

field = [[0 for g in range(12)] for l in range(12)]
for i in range(12):
    field[0][i] = '-'
    field[11][i] = '-'

for i in range(12):
    field[i][0] = '|'
    field[i][11] = '|'

for i in range(12):
    print(*field[i])

count = 0
play = True
while play == True:

    hod_x = int(input("Введите координату x"))
    while hod_x > 10 or hod_x < 1:
        hod_x = int(input("Некорректный ввод. Введите координату x"))
    hod_y = int(input("Введите координату y"))
    while hod_y > 10 or hod_y < 1:
        hod_y = int(input("Некорректный ввод. Введите координату y"))

    ship_dead = False
    if row[hod_y][hod_x] != 0 and row[hod_y][hod_x] != '-' and field[hod_y][hod_x] == 0:
        field[hod_y][hod_x] = 'X'
        count += 1
        if (row[hod_y+1][hod_x] != 0 and row[hod_y+1][hod_x] != '-' and field[hod_y+1][hod_x] == 0) or (row[hod_y+1][hod_x] != 0 and row[hod_y+1][hod_x] != '-' and field[hod_y][hod_x+1] == 0) or (row[hod_y+1][hod_x] != 0 and row[hod_y+1][hod_x] != '-' and field[hod_y-1][hod_x] == 0) or (row[hod_y+1][hod_x] != 0 and row[hod_y+1][hod_x] != '-' and field[hod_y][hod_x-1] == 0):
            ship_dead = False
        else:
            ship_dead = True

        if count == 20:
            play = False

    elif field[hod_y][hod_x] != 'X':
        field[hod_y][hod_x] = '-'

    for i in range(12):
        print(*field[i])
    if ship_dead == True:
        print("Убит!")

if play == False:
    print("Игра закончена!")
