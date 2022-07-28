#1
'''
def candy_game(n, m, players):
    count = 0
    if n%10 == 1 and 9 > n > 10: letter = 'а'
    elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
    else: letter = ''
    while n > 0:
        print(f'{players[count%2]}')
        move = int(input())
        if move > n or move > m:
            print(f'Не горчись амиго! Можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Не тупи! У тебя еще {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'Доигрался? Все game over!')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

player1 = input('МС слева представься \n')
player2 = input('МС справа представься \n')
players = [player1, player2]

n = int(input('Сколько конфет будем разыгрывать?\n '))
m = int(input('Сколько максимально будем брать конфет за один ход?\n '))

winer = candy_game(n, m, players)
if not winer:
    print('Победила дружба!')
else: print(f'Респект и уважуха {winer}! Красавчег, иди кушай конфеты!')


# Крестики - нолики
d= [1,2,3,4,5,6,7,8,9]

kol = 0

q = "X"

for i in range(0,3):print(f' {d[i*3]} {d[i*3+1]} {d[i*3+2]}')
while kol<9:
    t ="Крестик " if q=="X" else "Нолик "
    while True:
        n=int(input(t))
        if n>10 or n<1 or not (n in d):
            print('Введите другое число')
            continue
        break
    d[n-1]=q
    for i in range(0,3):print(f' {d[i*3]} {d[i*3+1]} {d[i*3+2]}')
    kol+=1
    q="X" if q!="X" else"O"
    r=""
    for i in range(0,2):
        if d[3*i]==d[3*i+1] and d[3*i+1]==d[3*i+2]:
            r=d[3*i]
        if d[i]==d[3+i] and d[3+i]==d[6+i]:r=d[i]
    if d[0]==d[4] and d[4]==d[8]:r=d[0]

    if d[2]==d[4] and d[4]==d[6]:r=d[2]
    if r=="" and kol>8:
        print("Ничья")
        break
    if r!="" :
        print(f'{"Крестики" if r=="X" else "Нолики"} выиграли')
        break
'''
#3 RLE
string = input()
count = 1
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[i]
            print(count, string[i])
            count = 1
print(count, string[i])