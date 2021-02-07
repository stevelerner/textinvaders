from classes import printcolor, colortable
from classes import clearscreen

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
            clearscreen(.100)
        grid[m][3]=' '
        gridcolor[m][3]='END'

clearscreen(0)
mainroutine()
