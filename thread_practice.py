import threading
import time

#must learn map, pool, parallelism and multithreading to handle communication between threads 
#(handle communication between different functions/loops)
#to allow user input to immediately update a loop, mid-loop, without waiting for the loop to end

#lets start with elementary examples and build our way up (lets try some map functions)

# stuff = ['123', '234', '345', '456', '567']

# result = list(map(lambda s: s[0], stuff))#lambda is basically a single line function
# print(result)

last_time = {'Last': 1500}

def clock(s):
    while s >= 0:
        seconds = s % 60
        minutes = int(s / 60) % 60
        hours = int((s / 60) / 60)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        last_time.update(Last=s)
        s -= 1
        time.sleep(1)

thread = threading.Thread(target=clock, args=(last_time['Last'],))#this is a thread, which can execute its target function simultaneously whilst other processes are going

thread.start()