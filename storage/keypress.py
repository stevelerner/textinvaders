import GetInput
import signal

getch = GetInput._getChUnix()

def alarmhandler(signum, frame):
    raise TypeError

def getinp(timeout=0.5):
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

while True:
    inp = getinp()
    if inp == 'a':
       print('a \r')
    elif inp == 'd':
       print('d \r')
    elif inp == 'q':
       exit()
