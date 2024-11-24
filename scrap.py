import time

#start = True whether start or stop is true (start/stop button)
start = str(input("print t for true: "))
if start == "t":
    start = True
else:
    start = False
work = True

def clock(s):#clock/ticking timer function
    while s >= 0:
        if not start:#if start is false, immediately stop clock, but don't exit clock
            time.sleep(1)
            #sleep until start
        seconds = int(s % 60)
        minutes = int(s / 60) % 60
        hours = int((s / 60) / 60) 
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        s -= 1
        time.sleep(1)

def start_stop():
    pass#lets define a start_stop function which when button start/stop is pressed, retrieves the current time from clock function
    #and saves it until button is clicked again to resume, that is when the saved time (s) can be passed to a new call of the function clock
    #

def reset():
    pass

def work_rest(w):
    while start:
        if w: #pomodoro work timer
            min = 25
            sec = min * 60
            clock(sec)
            start_stop()
            w = False
        else: #pomodoro rest timer
            min = 5
            sec = min * 60
            clock(sec)
            w = True

work_rest(work)