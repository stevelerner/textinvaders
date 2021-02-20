import os, time
import getinput
import signal

def clearscreen(sleeptime):
    time.sleep(sleeptime)
    os.system('tput reset')

def alarmhandler(signum, frame):
    raise TypeError

getch = getinput._getChUnix()

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

class alienClass:
    def __init__(self, y, x, speed):
        self.y = y
        self.x = x
        self.speed = speed
        alienClass.endtime = time.time() + self.speed

class missileClass:
    def __init__(self, y, x, fire):
        self.y = y
        self.x = x
        self.fire = fire

class shipClass:
    def __init__(self, x):
        self.x = x
