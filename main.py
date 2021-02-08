from classes import getinp
import os, sys

grid=[]
grid=[[' '] * 10 for x in range(0,10)]
#grid=[[x] * 10 for x in range(0,10)]

alienflip=0
alienY=0
alienX=3
missileX=3

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

# main routine

os.system('tput reset')
printgrid()

shipx = 4
inp = 0
while True:
#   for m in range(9,-1,-1):
#       inp = getinp(timeout=0.5)
        inp = getinp()
        if inp:
            if inp == 'q':
                exit()
            elif inp == 'a':
                shipx = shipx - 1
                if shipx <= 0:
                    shipx = 0
            elif inp == 'd':
                shipx = shipx + 1
                if shipx >= 9:
                    shipx = 9
            else:
                pass
            grid[9][shipx]='T'
            printgrid()
            grid[9][shipx]=' '
#           grid[m][3]=('^')
#       grid[m][3]=' '
