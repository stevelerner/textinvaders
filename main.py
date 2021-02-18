from classes import getinp, alienClass, missileClass, shipClass
import os, sys, random, time

grid=[]
grid=[[' '] * 10 for x in range(0,10)]

def printgrid():
    os.system('tput reset')
    grid[9][ship.x]='T'
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
    print('alien.approach = ', alien.approach, '\r')

#initialize game
inp = 0
alienlife = 3
score = 0
alien=alienClass(random.randint(0,7), random.randint(0,9), alienlife, 7)
missile=missileClass(0,8,0)
ship=shipClass(9,4)

os.system('tput reset')
grid[alien.y][alien.x] = 'A'
printgrid()

#main routine
while True:
    #check if alien life has expired 
    if time.time() > alien.endtime:
        grid[alien.y][alien.x] = ' '
        currentapproach = alien.approach+1
        alien=alienClass(random.randint(0,currentapproach),
                         random.randint(0,9), alienlife, currentapproach)
        if alien.approach==9:
            print('Aliens Win!\n')
            exit()
        grid[alien.y][alien.x] = 'A'
        printgrid()
    grid[alien.y][alien.x] = 'A'
    #check for keyboard input
    inp = getinp()
    if inp == 'q':
        exit()
    elif inp == 'a':
        ship.x = ship.x - 1
        if ship.x <= 0:
            ship.x = 0
    elif inp == 'd':
        ship.x = ship.x + 1
        if ship.x >= 9:
            ship.x = 9
    elif inp == 's':
        missile = missileClass(8, ship.x, 1)
    #redraw screen if ship is moved
    if inp == 'a' or inp == 'd':
        printgrid()
    #missile is fired 
    if missile.fire == 1:
        #missile has not yet hit top of range
        if missile.y > -1:
            grid[missile.y][missile.x] = '^'
            printgrid()
            grid[missile.y][missile.x] = ' '
            missile.y = missile.y - 1
            # missile intercepts alien
            if (missile.y == alien.y) and (missile.x == alien.x):
                grid[alien.y][alien.x] = ' '
                grid[missile.y][missile.x] = ' '
                alien=alienClass(random.randint(0,7), random.randint(0,9),
                                 alienlife, 7)
                grid[alien.y][alien.x] = 'A'
                score=score+1
                missile.y = 8
                missile.fire = 0
                printgrid()
        #missile missed
        else:
            missile.y = 8
            missile.fire = 0
            printgrid()
    grid[9][ship.x]=' '
