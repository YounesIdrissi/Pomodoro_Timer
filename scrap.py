import time

last_time = {'Last': 1500}

def clock(s):
    tic = input("Enter y to begin/continue: ")#this loop prompts for input every time, we don't want this, we only want it to check for input, not prompt it every time
    #in otherwords, continue unless there is input (input which tells function to pause/resume)
    while s >= 0 and tic == 'y':
        seconds = s % 60
        minutes = int(s / 60) % 60
        hours = int((s / 60) / 60)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        last_time.update(Last=s)
        s -= 1
        time.sleep(1)
        tic = input("Enter y to continue: ")

clock(last_time['Last'])




