import os, time

class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

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

def clearscreen(sleeptime):
    time.sleep(sleeptime)
    os.system('tput reset')

def printgrid():
    for y in range(10):
        for x in range(10):
            print(color.RED,grid[y][x],color.END,end='')
        print('\r')

def mainroutine():
    for m in range(9,-1,-1):
        grid[m][3]=('^')
        printgrid()
#       input(" Press Enter to continue...")
        if m > 0:
                clearscreen(.250)
        grid[m][3]=' '
#       print('\r')

clearscreen(0)
mainroutine()
