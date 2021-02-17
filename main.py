from classes import getinp, colortable, alien, missile
import os, sys, random, time

grid=[]
grid=[[' '] * 10 for x in range(0,10)]
#grid=[[x] * 10 for x in range(0,10)]

#initialize variables
shipX = 4
inp = 0
alienlife = 3
score = 0

alien1=alien(random.randint(0,7), random.randint(0,9), alienlife)
missile1=missile(0,8,0)

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
#   print('time = ', abs(int(alien1.endtime-time.time())), '\r')

#initialize game

os.system('tput reset')
grid[alien1.y][alien1.x] = 'A'
grid[9][shipX]='T'
printgrid()
grid[9][shipX]=' '

#main routine
while True:
    #check if alien life has expired 
    if time.time() > alien1.endtime:
        grid[alien1.y][alien1.x] = ' '
        alien1=alien(random.randint(0,7), random.randint(0,9), alienlife)
        grid[alien1.y][alien1.x] = 'A'
        grid[9][shipX]='T'
        printgrid()
    else:
        grid[alien1.y][alien1.x] = 'A'

    #check for keyboard input
    inp = getinp()
    if inp == 'q':
        exit()
    elif inp == 'a':
        shipX = shipX - 1
        if shipX <= 0:
            shipX = 0
    elif inp == 'd':
        shipX = shipX + 1
        if shipX >= 9:
            shipX = 9
    elif inp == 's':
        missile1 = missile(8, shipX, 1)

# redraw screen if ship is moved
    if inp == 'a' or inp == 'd':
        grid[9][shipX]='T'
        printgrid()

# missile is fired 
    if missile1.fire == 1:
        if missile1.y >= 0:
            grid[missile1.y][missile1.x] = '^'
            grid[9][shipX]='T'
            printgrid()
            grid[missile1.y][missile1.x] = ' '
            missile1.y = missile1.y - 1
            time.sleep(.100)

# missile intercepts alien
            if (missile1.y == alien1.y) and (missile1.x == alien1.x):
                missile1.y = 8
                missile1.fire = 0
                grid[alien1.y][alien1.x] = ' '
                grid[missile1.y][missile1.x] = ' '
                alien1=alien(random.randint(0,7), random.randint(0,9), alienlife)
                grid[alien1.y][alien1.x] = 'A'
                score=score+1
                grid[9][shipX]='T'
                printgrid()
        else:
            missile1.y = 8
            missile1.fire = 0
            printgrid()
    grid[9][shipX]=' '
