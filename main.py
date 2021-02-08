from classes import getinp
import os, sys, time

grid=[]
grid=[[' '] * 10 for x in range(0,10)]
#grid=[[x] * 10 for x in range(0,10)]

alienflip=0
alienY=0
alienX=3

def alienflipper():
    if alienflip==0:
        grid[alienY][alienX]='A'
        alienflip=1
    else:
        grid[alienY][alienX]='V'
        alienflip=0

def printgrid():
    os.system('tput reset')
    print('------------')
    for y in range(10):
        print('|', end='')
        for x in range(10):
            print(grid[y][x], end='')
        print('|', end='')
        print('\r')
    print('------------')
    print('a/d=move s=fire q=quit\r')

# main routine

os.system('tput reset')

shipX = 4
inp = 0
missileX = 0
missileY = 8
missile = 0

grid[9][shipX]='T'
printgrid()
grid[9][shipX]=' '

while True:
#   for m in range(9,-1,-1):
#       inp = getinp(timeout=0.5)
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
    else:
        pass
    if missile == 1:
        if missileY >= 0:
            grid[missileY][missileX] = '^'
            grid[9][shipX]='T'
            printgrid()
            grid[missileY][missileX] = ' '
            missileY = missileY - 1
            time.sleep(.150)
        else:
            missileY = 8
            missile = 0
            printgrid()
    grid[9][shipX]=' '
