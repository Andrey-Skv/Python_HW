# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

doska = list(range(1, 10))


def draw_board(board):
    for i in range(3):
        print('|', doska[0+i*3], '|', doska[1+i*3], '|', doska[2+i*3], '|')


def stavim_hod(hod):
    valid = False
    while not valid:
        otvet = input(
            'Введите номер клетки куда поставить значение ' + hod + '?')
        otv = int(otvet)
        if otv >= 1 and otv <= 9:
            if (str(doska[otv-1]) not in 'XO'):
                doska[otv-1] = hod
                valid = True
            else:
                print('Эта клетка занята')


def kto_viigral(doska):
    pobeda = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
              (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in pobeda:
        if doska[i[0]] == doska[i[1]] == doska[i[2]]:
            return doska[i[0]]
    return False


def igra(doska):
    count = 0
    win=False
    while not win:
        draw_board(doska)
        if count%2==0:
            stavim_hod('X')
        else:
            stavim_hod('0')
        count+=1
        if count>4:
            m=kto_viigral(doska)
            if m:
                print(m, 'Победил')
                win=True
                break
        if count==9:
            print('победила дружба!')
            break
    draw_board(doska)

igra(doska)
