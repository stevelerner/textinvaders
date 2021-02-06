import os, time

def clearscreen(sleeptime):
    time.sleep(sleeptime)
    os.system('tput reset')

class colortable:
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

def printcolor(color):
    if color == 'PURPLE':
        return('\033[1;35;48m')
    elif color == 'CYAN':
        return('\033[1;36;48m')
    elif color == 'BOLD':
        return('\033[1;37;48m')
    elif color == 'BLUE':
        return('\033[1;34;48m')
    elif color == 'GREEN':
        return('\033[1;32;48m')
    elif color == 'YELLOW':
        return('\033[1;33;48m')
    elif color == 'RED':
        return('\033[1;31;48m')
    elif color == 'BLACK':
        return('\033[1;30;48m')
    elif color == 'UNDERLINE':
        return('\033[4;37;48m')
    elif color == 'END':
        return('\033[1;37;0m')
