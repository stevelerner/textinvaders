import os, time
grid=[]
#grid=[[x] * 10 for x in range(0,10)]
grid=[[' '] * 10 for x in range(0,10)]
#print(grid)

#for y in range(10):
#   grid[y][10]="\n"

def printgrid():
    for y in range(10):
        for x in range(10):
            print(grid[y][x],end='')
        print('\r')


os.system('tput reset')
time.sleep(.500)
#for y in range(0,10):
for y in range(9,0,-1):
        tmp=(grid[y][3])
        grid[y][3]='^'
        printgrid()
        grid[y][3]=tmp
#       print(y)
        time.sleep(.250)
        os.system('tput reset')
