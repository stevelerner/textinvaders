from classes import printcolor, colortable, getinp
from classes import clearscreen
import os, sys

grid=[]
grid=[[' '] * 10 for x in range(0,10)]
#grid=[[x] * 10 for x in range(0,10)]

gridcolor=[]
gridcolor=[['END'] * 10 for x in range(0,10)]

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
#   print('----------')
    for y in range(10):
        for x in range(10):
            print(printcolor(gridcolor[y][x]), grid[y][x], colortable.END, end='')
        print('\r')

def mainroutine():
    shipx = 4
    if shipx==4:
        shipxlocal = shipx
    shipx = 0
    for m in range(9,-1,-1):
#       grid[m][3]=('^')
#       gridcolor[m][3]='RED'
#       grid[m][3]=' '
#       gridcolor[m][3]='END'
        inp = getinp()
        if inp:
            if inp == 'q':
                exit()
            elif inp == 'a':
                shipxlocal = shipxlocal - 1
                if shipxlocal <= 0:
                    shipxlocal = 0
            elif inp == 'd':
                shipxlocal = shipxlocal + 1
                if shipxlocal >= 9:
                    shipxlocal = 9
            else:
                pass
            grid[9][shipxlocal]='T'
            printgrid()
            if m > 0:
                os.system('tput reset') 
            grid[9][shipxlocal]=' '

inp = 0

# Main Loop

while True:
    mainroutine()
