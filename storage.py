
def printgrid():
    for y in range(10):
        for x in range(10):
            print(gridcolor[y][x],grid[y][x],color.END,end='')
        print('\r')

def mainroutine():
    for m in range(9,-1,-1):
        grid[m][3]=('^')
        gridcolor[m][3]='RED'
        printgrid()
#       input(" Press Enter to continue...")
#       if m > 0:
#               clearscreen(.250)
        grid[m][3]=' '
        gridcolor[m][3]='END'
#       print('\r')

clearscreen(0)
mainroutine()
