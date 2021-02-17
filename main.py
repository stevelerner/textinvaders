from classes import getinp, colortable, alien
import os, sys, random, time

grid=[]
grid=[[' '] * 10 for x in range(0,10)]
#grid=[[x] * 10 for x in range(0,10)]

alienlife = 3

alien1=alien(random.randint(0,7), random.randint(0,9), alienlife)

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
    print('time = ', abs(int(alien1.endtime-time.time())), '\r')

# main routine

os.system('tput reset')

#initialize variables
shipX = 4
inp = 0
missileX = 0
missileY = 8
missile = 0

grid[alien1.y][alien1.x] = 'A'
grid[9][shipX]='T'
printgrid()
grid[9][shipX]=' '

#main routine
while True:
    if (alien1.y == 9) or (time.time() > alien1.endtime):
        grid[alien1.y][alien1.x] = ' '
        grid[9][shipX]='T'
        printgrid()
        alien1.y= random.randint(0,7)
        alien1.x= random.randint(0,9)
        alien1.endtime = time.time() + alienlife
    else:
        grid[alien1.y][alien1.x] = 'A'
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
            if (missileY == alien1.y) and (missileX == alien1.x):
                missileY = 8
                missile = 0
                grid[alien1.y][alien1.x] = ' '
                grid[missileY][missileX] = ' '
                alien1.y= random.randint(0,7)
                alien1.x= random.randint(0,9)
                grid[alien1.y][alien1.x] = 'A'
                score=score+1
                grid[9][shipX]='T'
                printgrid()
        else:
            missileY = 8
            missile = 0
            printgrid()
    grid[9][shipX]=' '
