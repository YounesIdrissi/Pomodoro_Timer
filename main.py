import tkinter as tk
from functools import partial
import time

ticking = False #by default the clock is paused

last_time = {'Last': 1500}#update last time to this dictionary and call it within start_stop function

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
            last_time.update(Last=s)
            s -= 1
            time.sleep(1)
    if t == True:
        return clock(s)
    else:
        return #return the last value updated to last_time and display it

root = tk.Tk()
root.geometry("700x700")
root.title("Pomodoro")

btn = tk.Button(root, text="Start/Stop", font=("Ariel", 20))
btn.config(command=partial(start_stop, last_time['Last'], ticking))
btn.pack()

root.mainloop()



