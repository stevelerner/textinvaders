from classes import printcolor, colortable, getinp
from classes import clearscreen

inp = 0
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
    for m in range(9,-1,-1):
        grid[m][3]=('^')
        gridcolor[m][3]='RED'
        printgrid()
        if m > 0:
            clearscreen(.150)
        grid[m][3]=' '
        gridcolor[m][3]='END'
        inp = getinp()
        if inp == 'q':
            exit()
        else:
            pass

# Main Loop

while True:
    mainroutine()
