from classes import getinp, colortable
import os, sys, random, time

grid=[]
grid=[[' '] * 10 for x in range(0,10)]
#grid=[[x] * 10 for x in range(0,10)]

alienY= random.randint(0,7)
alienX= random.randint(0,9)
alienlife=3
alienendtime = time.time() + alienlife

score = 0

def printgrid():
    os.system('tput reset')
    print('Trace Invaders\r')
    print('------------')
    for y in range(10):
        print('|', end='')
        for x in range(10):
            print(grid[y][x], end='')
        print('|', end='')
        print('\r')
    print('------------')
    print('a/d=move s=fire q=quit\r')
    print('score = ', score, '\r')
    print('time = ', abs(int(alienendtime-time.time())), '\r')

# main routine

os.system('tput reset')

#initialize variables
shipX = 4
inp = 0
missileX = 0
missileY = 8
missile = 0

grid[alienY][alienX] = 'A'
grid[9][shipX]='T'
printgrid()
grid[9][shipX]=' '

#main routine
while True:
    if (alienY == 9) or (time.time() > alienendtime):
        grid[alienY][alienX] = ' '
        grid[9][shipX]='T'
        printgrid()
        alienY= random.randint(0,7)
        alienX= random.randint(0,9)
        alienendtime = time.time() + alienlife
    else:
        grid[alienY][alienX] = 'A'
    inp = getinp()
    if inp == 'q':
        exit()
    elif inp == 'a':
        shipX = shipX - 1
        if shipX <= 0:
            shipX = 0
        grid[9][shipX]='T'
        printgrid()
    elif inp == 'd':
        shipX = shipX + 1
        if shipX >= 9:
            shipX = 9
        grid[9][shipX]='T'
        printgrid()
    elif inp == 's':
        missileY = 8
        missile = 1
        missileX = shipX
    if missile == 1:
        if missileY >= 0:
            grid[missileY][missileX] = '^'
            grid[9][shipX]='T'
            printgrid()
            grid[missileY][missileX] = ' '
            missileY = missileY - 1
            time.sleep(.100)
            if (missileY == alienY) and (missileX == alienX):
                missileY = 8
                missile = 0
                grid[alienY][alienX] = ' '
                grid[missileY][missileX] = ' '
                alienY= random.randint(0,7)
                alienX= random.randint(0,9)
                grid[alienY][alienX] = 'A'
                score=score+1
                grid[9][shipX]='T'
                printgrid()
        else:
            missileY = 8
            missile = 0
            printgrid()
    grid[9][shipX]=' '
