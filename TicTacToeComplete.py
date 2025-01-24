##MADE BY CODERBOY.

c11 = '?'
c12 = '?'
c13 = '?'
c21 = '?'
c22 = '?'
c23 = '?'
c31 = '?'
c32 = '?'
c33 = '?'
p1name = ''
p2name = ''
print('Welcome to Tic-Tac-Toe!')
print()
print("Player 1, choose your name.")
p1name = input()
print("Nice! PLayer 2, choose your name.")
p2name = input()
print('Noice!')
print()
loop = True
while loop:
    loop1 = True
    while loop1:
        print('1  2  3')
        print(c11,'',c12,'',c13, '1')
        print(c21,'',c22,'',c23, '2')
        print(c31,'',c32,'',c33, '3')
        print()
        print("It is", p1name, "'s turn. Input the coordinates as the format xy.")
        coords = input()
        if coords == '11' and c11 == '?':
            c11 = 'O'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '12' and c12 == '?':
            c12 = 'O'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '13' and c13 == '?':
            c13 = 'O'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '21' and c21 == '?':
            c21 = 'O'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '22' and c22 == '?':
            c22 = 'O'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '23' and c23 == '?':
            c23 = 'O'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '31' and c31 == '?':
            c31 = 'O'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '32' and c32 == '?':
            c32 = 'O'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '33' and c33 == '?':
            c33 = 'O'
            print('Good job!')
            print()
            loop1 = False
        else:
            print('That is not a valid coordinate.')
            
    if c11 == 'O' and c12 == 'O' and c13 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c21 == 'O' and c22 == 'O' and c23 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c31 == 'O' and c32 == 'O' and c33 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c12 == 'O' and c21 == 'O' and c31 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c12 == 'O' and c22 == 'O' and c32 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c13 == 'O' and c23 == 'O' and c33 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c11 == 'O' and c22 == 'O' and c33 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c13 == 'O' and c22 == 'O' and c31 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False

    if c11 == 'X' and c12 == 'X' and c13 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c21 == 'X' and c22 == 'X' and c23 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c31 == 'X' and c32 == 'X' and c33 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c12 == 'X' and c21 == 'X' and c31 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c12 == 'X' and c22 == 'X' and c32 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c13 == 'X' and c23 == 'X' and c33 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c11 == 'X' and c22 == 'X' and c33 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c13 == 'X' and c22 == 'X' and c31 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    loop1 = True
    while loop1:
        print('1  2  3')
        print(c11,'',c12,'',c13, '1')
        print(c21,'',c22,'',c23, '2')
        print(c31,'',c32,'',c33, '3')
        print()
        print("It is", p2name, "'s turn. Input the coordinates as the format xy.")
        coords = input()
        if coords == '11' and c11 == '?':
            c11 = 'X'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '12' and c12 == '?':
            c12 = 'X'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '13' and c13 == '?':
            c13 = 'X'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '21' and c21 == '?':
            c21 = 'X'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '22' and c22 == '?':
            c22 = 'X'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '23' and c23 == '?':
            c23 = 'X'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '31' and c31 == '?':
            c31 = 'X'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '32' and c32 == '?':
            c32 = 'X'
            print('Good job!')
            print()
            loop1 = False
        elif coords == '33' and c33 == '?':
            c33 = 'X'
            print('Good job!')
            print()
            loop1 = False
        else:
            print('That is not a valid coordinate.')
    if c11 == 'O' and c12 == 'O' and c13 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c21 == 'O' and c22 == 'O' and c23 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c31 == 'O' and c32 == 'O' and c33 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c12 == 'O' and c21 == 'O' and c31 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c12 == 'O' and c22 == 'O' and c32 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c13 == 'O' and c23 == 'O' and c33 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c11 == 'O' and c22 == 'O' and c33 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False
    if c13 == 'O' and c22 == 'O' and c31 == 'O':
        print("Congratulations!", p1name, "won the game!")
        loop = False

    if c11 == 'X' and c12 == 'X' and c13 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c21 == 'X' and c22 == 'X' and c23 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c31 == 'X' and c32 == 'X' and c33 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c12 == 'X' and c21 == 'X' and c31 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c12 == 'X' and c22 == 'X' and c32 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c13 == 'X' and c23 == 'X' and c33 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c11 == 'X' and c22 == 'X' and c33 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
    if c13 == 'X' and c22 == 'X' and c31 == 'X':
        print("Congratulations!", p2name, "won the game!")
        loop = False
