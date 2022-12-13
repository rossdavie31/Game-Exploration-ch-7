#Ross Davie
#COSC1315
#12/12/2022
#Game Exploration

#Random module for randomly accepting the values
# ‘X’ indicates the ships hit
# ‘-‘ indicates the hits missed
from random import randint

Hidden_Pattern=[[' ']*8 for x in range(8)]
Guess_Pattern=[[' ']*8 for x in range(8)]

let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

def print_board(board):
    print(' A B C D E F G H')
    print(' ***************')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def get_ship_location():
    #Enter the row number between 1 to 8
    row=input('Please enter a ship row 1-8 ').upper()
    while row not in '12345678':
        print("Please enter a valid row ")
        row=input('Please enter a ship row 1-8 ')
    #Enter the Ship column from A TO H
    column=input('Please enter a ship column A-H ').upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column ")
        column=input('Please enter a ship column A-H ')
    return int(row)-1,let_to_num[column]

#Function that creates the ships
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='O':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'O'



def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='O':
                count+=1
    return count

create_ships(Hidden_Pattern)
#print_board(Hidden_Pattern)
turns = 20
while turns > 0:
    print('Welcome to Battleship')
    print_board(Guess_Pattern)
    row,column =get_ship_location()
    if Guess_Pattern[row][column] == '-':
        print(' You already guessed that ')
    elif Hidden_Pattern[row][column] =='O':
        print(' You Hit a Battleship! ')
        Guess_Pattern[row][column] = 'O'
        turns -= 1
    else:
        print('Better Luck Next Time')
        Guess_Pattern[row][column] = '-'
        turns -= 1
    if  count_hit_ships(Guess_Pattern) == 5:
        print("Congratulations You Win! ")
        break
    print(' You have ' +str(turns) + ' turns remaining ')
    if turns == 0:
        print('Thanks for Playing! ')
        