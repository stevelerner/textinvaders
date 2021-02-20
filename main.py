from classes import getinp, alienClass, missileClass, shipClass
import os, sys, random, time

grid=[]
grid=[[' '] * 10 for x in range(0,10)]

def printgrid(): #routine to print grid as if its a motion frame- grid will be updated with ship, missile, and alien locations
    os.system('tput reset')
    print('Trace Invaders\r')
    print('|----------|')
    for y in range(10):
        print('|', end='')
        for x in range(10):
            print(grid[y][x], end='')
        print('|', end='')
        print('\r')
    print('|----------|')
    print('a/d=move s=fire q=quit\r')
    print("Invader's score = ", alienscore, '\r')
    print('Your score = ', score)

inp = 0 #initialize game
score = 0
alienscore = 0
alienwin = 5
alienlife = 1
alien=alienClass(random.randint(0,5), random.randint(0,9), alienlife) #reset alien
grid[alien.y][alien.x] = 'A'
missile=missileClass(0,8,0)
ship=shipClass(4)
grid[9][ship.x] = 'T'
printgrid()

while True: #main routine
    grid[9][ship.x]='T'
    if time.time() > alien.endtime: #check if alien life has expired and if so, move alien down +1
        grid[alien.y][alien.x] = ' '
        alien=alienClass(alien.y+1, random.randint(0,9), alienlife) #reset alien
        grid[alien.y][alien.x] = 'A'
        printgrid()
        if alien.y==9 and alienscore < alienwin: #if alien reaches ship, increase its score and get faster before resetting alien
            alienscore+=1
            alienlife-=.05 #get a little faster
            grid[9][ship.x] = '*'
            printgrid()
            if alien.y == 9 and alienscore == alienwin: #alien wins
                print('Invaders Win!\n')
                exit()
            time.sleep(.5)
            grid[alien.y][alien.x] = ' '
            alien=alienClass(random.randint(0,5), random.randint(0,9), alienlife) #reset alien
            printgrid()
    grid[alien.y][alien.x] = 'A'
    inp = getinp() #check for keyboard input, if there is input change ship location and reprint grid or fire missile
    if inp == 'q':
        exit()
    elif inp == 'a':
        grid[9][ship.x]=' '
        ship.x-=1
        if ship.x <= 0:
            ship.x = 0
        grid[9][ship.x]='T'
        printgrid()
    elif inp == 'd':
        grid[9][ship.x]=' '
        ship.x+=1
        if ship.x >= 9:
            ship.x = 9
        grid[9][ship.x]='T'
        printgrid()
    elif inp == 's':
        missile = missileClass(8, ship.x, 1)
    if missile.fire == 1: #missile is fired 
        if missile.y > -1: #missile has not yet hit top of range
            grid[missile.y][missile.x] = '^'
            printgrid()
            grid[missile.y][missile.x] = ' '
            missile.y-=1
            if (missile.y == alien.y) and (missile.x == alien.x): #missile intercepts alien
                grid[alien.y][alien.x] = '*'
                printgrid()
                time.sleep(.5)
                grid[alien.y][alien.x] = ' '
                alien=alienClass(random.randint(0,5), random.randint(0,9), alienlife) #reset alien
                grid[alien.y][alien.x] = 'A'
                alienlife-=.15 #get a little faster
                score+=1
                missile = missileClass(8, ship.x, 0) #reset missile status
                printgrid()
        else: #missile missed
            missile = missileClass(8, ship.x, 0) #reset missile status
            printgrid()
