import time

ticking = False #by default the clock is paused

last_time = [1500]#append time to this list and call the last index (last time)

def start_stop(s, t):#arguments are time in seconds and ticking
    if t == False:#we switch back and forth between on or off (when start_stop is invoked)
        t = True
    else:
        t = False

    def clock(s):
        while s >= 0:
            seconds = s % 60
            minutes = int(s / 60) % 60
            hours = int((s / 60) / 60)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            last_time.append(s)
            s -= 1
            time.sleep(1)
    if t == True:
        return clock(s)
    else:
        return 
        #return the last value appended to last_time and display it

start_stop(last_time[-1], ticking)#argument is number of seconds, we want to return the argument inside of the loop when this function is invoked