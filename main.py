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
    print("Invader's score = ", alienscore, '\r')
    print('Your score = ', score, '\r')
    grid[9][ship.x]=' '

#initialize game
inp = 0
score = 0
alienscore = 0
alienlife = 1
alien=alienClass(random.randint(0,5), random.randint(0,9), alienlife)
grid[alien.y][alien.x] = 'A'
missile=missileClass(0,8,0)
ship=shipClass(9,4)
printgrid()

while True: #main routine
    if time.time() > alien.endtime: #check if alien life has expired and if so, move alien down +1
        grid[alien.y][alien.x] = ' '
        alien=alienClass(alien.y+1, random.randint(0,9), alienlife)
        grid[alien.y][alien.x] = 'A'
        printgrid()
        if alien.y==9 and alienscore < 3:
            print('Invader Scores!\n')
            alienscore=alienscore+1
            grid[alien.y][alien.x] = ' '
            alien=alienClass(random.randint(0,5), random.randint(0,9), alienlife)
            printgrid()
        elif alien.y==9 and alienscore == 3:
            print('Invaders Win!\n')
            exit()
    grid[alien.y][alien.x] = 'A'
    inp = getinp() # check for keyboard input
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
    if inp == 'a' or inp == 'd': # redraw screen if ship is moved
        printgrid()
    if missile.fire == 1: # missile is fired 
        if missile.y > -1: # missile has not yet hit top of range
            grid[missile.y][missile.x] = '^'
            printgrid()
            grid[missile.y][missile.x] = ' '
            missile.y = missile.y - 1
            if (missile.y == alien.y) and (missile.x == alien.x): # missile intercepts alien
                grid[alien.y][alien.x] = '*'
                printgrid()
                time.sleep(.5)
                grid[alien.y][alien.x] = ' '
                alien=alienClass(random.randint(0,5), random.randint(0,9), alienlife)
                grid[alien.y][alien.x] = 'A'
                alienlife = alienlife - .25
                score=score+1
                missile.y = 8
                missile.fire = 0
                printgrid()
        else: #missile missed
            missile.y = 8
            missile.fire = 0
            printgrid()
    grid[9][ship.x]=' '
