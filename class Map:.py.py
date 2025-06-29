import random

def map(): # put define function
    w, h = 8, 8  # width and height to put 8x8 grid on 2d way
    grid = [['-' for _ in range(w)] for _ in range(h)]  # initialize grid
    x, y = 0, 0  # realise they use zero based indexing no wonder i was confused
    grid[y][x] = '0'  # mark player

    def showgrid():
        for row in grid:
            print(' '.join(row)) #remove the bracket
        print()
        pass
  
    def findsomething():
        find = random.choice(['nothing', 'enemy', 'heal'])
        if find == 'enemy':
            print('enemy')
            pass
        elif find == 'heal':
            print('heal')
        elif find == 'nothing':
            print ( 'nothin')
        

    showgrid() # print it

    while True:
        move = input("Move (WASD) or L to leave: ").lower()

        if move == 'l':
            print("Leaving the map...")
            break # use for save implatation

        # remove the used player pos old position when it loop again
        grid[y][x] = '-'

        if move == 'w' and y > 0: # if y greater/higher than 0 it would go up vertical in a 2d dimention when connecting with it
            y -= 1 # it minus the grid section so it will be going up since
        elif move == 's' and y < h - 1: # due to zero based index need -1  so h need to be 7 
            y += 1                      # mean y < 7
        elif move == 'a' and x > 0: #opposite of  y > 0
            x -= 1
        elif move == 'd' and x < w - 1: # x < 7
            x += 1
        else:
            print("Invalid move or edge of map!")
        
        # update new position
        grid[y][x] = '0'
        showgrid()
        findsomething()

map()
