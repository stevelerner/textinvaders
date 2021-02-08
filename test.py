import os, sys

grid=[]
#grid=[[' '] * 10 for x in range(0,10)]
grid=[[x] * 10 for x in range(0,10)]

def printgrid():
    print('------------')
    for y in range(10):
        print('|', end='')
        for x in range(10):
            print(grid[y][x], end='')
        print('|', end='')
        print('\r')
    print('------------')
os.system('tput reset')
printgrid()
