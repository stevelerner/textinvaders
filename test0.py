import os, time
grid=[]
grid=[[' '] * 10 for x in range(0,10)]
#grid=[[x] * 10 for x in range(0,10)]

alienflip=0
alienY=0
alienX=3
missileX=3

def printgrid():
    for y in range(0,9):
        for x in range(0,9):
            print(grid[y][x],end='')
#       print('\r')

def alienflipper():
        if alienflip==0:
            grid[alienY][alienX]='A'
            alienflip=1
        else:
            grid[alienY][alienX]='V'
            alienflip=0

def clearscreen(sleeptime):
    time.sleep(sleeptime)
    os.system('tput reset')

def printgrid():
    for y in range(10):
        for x in range(10):
            print(grid[y][x],end='')
        print('\r')

def mainroutine():
    for m in range(9,-1,-1):
        grid[m][3]='^'
        printgrid()
#       print('\r',m)
#       input(" Press Enter to continue...")
        if m > 0:
                clearscreen(.250)
        grid[m][3]=' '
#       print('\r')

clearscreen(0)
mainroutine()
