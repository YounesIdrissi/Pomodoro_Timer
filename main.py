#import tkinter as tk
#from functools import partial
import threading
import time

last_time = {'Last': 1500}
ss = False#start/stop is false by default, waiting to be True by start_stop function (False=off/pause True=on/resume)

def clock(s):#inside the while loop we must a have a condition that accepts input data 
    #(input which is processed mid-loop, allowing the instant termination/stop/pause or resume/start of the program)
    while s >= 0 and ss == True:
        seconds = s % 60
        minutes = int(s / 60) % 60
        hours = int((s / 60) / 60)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        last_time.update(Last=s)
        s -= 1
        time.sleep(1)

def start_stop():#should immediately pause/resume the clock function mid-loop
    global ss
    if ss == False:
        ss = True
    else:
        ss = False

start_stop()

if __name__ == '__main__':
    clock_thread = threading.Thread(target=clock, args=(last_time['Last'],))#this is a thread, which can execute its target function 
                                                                            #simultaneously whilst other processes are going
    clock_thread.start()

    ss_thread = threading.Thread(target=start_stop)
    ss_thread.start()











# ticking = False #by default the clock is paused

# last_time = {'Last': 1500}#update last time to this dictionary and call it within start_stop function

# def start_stop(s, t):#arguments are time in seconds and ticking
#     if t == False:#we switch back and forth between on or off (when start_stop is invoked)
#         t = True
#     else:
#         t = False

#     def clock(s):
#         while s >= 0 and t == True:
#             seconds = s % 60
#             minutes = int(s / 60) % 60
#             hours = int((s / 60) / 60)
#             print(f"{hours:02}:{minutes:02}:{seconds:02}")
#             last_time.update(Last=s)
#             s -= 1
#             time.sleep(1)
#     if t == True:
#         return clock(s)
#     else:
#         return #return the last value updated to last_time and display it

# root = tk.Tk()
# root.geometry("700x700")
# root.title("Pomodoro")

# btn = tk.Button(root, text="Start/Stop", font=("Ariel", 20))
# btn.config(command=partial(start_stop, last_time['Last'], ticking))
# btn.pack()

# root.mainloop()



