
def printgrid(celltype):
    for y in range(10):
        for x in range(10):
            if celltype=='missile':
                print(color.RED,grid[y][x],color.END,end='')
            elif celltype!='missile':
                print(color.END,grid[y][x],color.END,end='')
        print('\r')

def mainroutine():
    for m in range(9,-1,-1):
        grid[m][3]=('^')
        printgrid('missile')
#       input(" Press Enter to continue...")
        if m > 0:
                clearscreen(.250)
        grid[m][3]=' '
#       print('\r')

clearscreen(0)
mainroutine()
