import random


w, h = 8, 8 # width and height
grid = [['-' for _ in range(w)] for _ in range(h)] # all grid will by -
x, y = 4, 4  # player start coordinate

while True:

    move = input("WASD (L to leave): ").lower()
    # i search google of -=, += 
    if move == 'w':
         y -= 1 # opposite
    elif move == 's':
         y += 1 # down because higher it get it goes down in height
    elif move == 'a':
         x -= 1 # opposite
    elif move == 'd':
         x += 1 # if this it goes ->  since it move by adding 1 in width
    elif move == 'l': break
    else:
         ('type correctly')
