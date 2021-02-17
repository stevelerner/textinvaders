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

import GetInput
import signal

getch = GetInput._getChUnix()

def alarmhandler(signum, frame):
    raise TypeError

def getinp(timeout=0.05):
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        ch = getch()
        signal.alarm(0)
        return ch
    except TypeError:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

class alien:
    def __init__(self, y, x, life):
        self.y = y
        self.x = x
        self.life = life
        alien.endtime = time.time() + self.life
