import tkinter as tk
from functools import partial
import threading
import time

#the MAIN THREAD is the default/initial thread of execution in any given program

time_state = {'Remain': 1500, 'State': True}
'''
above time_state refers to dict container, with two object references, 'Remain' and 'State'; update remaining time to this dictionary
start/stop state is false by default, waiting to be updated to True by start_stop function (False=off/pause True=on/resume)
'''

def clock(ts):
    '''target function of CHILD/WORKER THREAD - inside the nested while loop we constantly listen for bool ss being true or false
    input (ss boolean) is processed mid-loop, allowing the instant stop/pause or resume/start of the program'''
    while ts['Remain'] >= 0:#infinite loop is required here, prevents thread from ending once ss = False
        while ts['State'] == True:
            seconds = ts['Remain'] % 60
            minutes = int(ts['Remain'] / 60) % 60
            hours = int((ts['Remain'] / 60) / 60)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            ts['Remain'] -= 1
            time.sleep(1)#place time.sleep() at the end to immidiately display initial time before 1 second wait

def start_stop(ts):#must use partial when referencing this function; it must return
    if ts['State'] == True:
        ts['State'] = False
    else:
        ts['State'] = True

if __name__ == '__main__':
    clock_thread = threading.Thread(target=clock, args=(time_state,))#this is a CHILD/WORKER THREAD, which can execute its target function 
                                                #simultaneously while we do our other processes
    clock_thread.start()

    root = tk.Tk()
    root.geometry("700x700")
    root.title("Pomodoro")

    btn = tk.Button(root, text="Start/Stop", font=("Ariel", 20))
    btn.config(command=partial(start_stop, time_state))
    btn.pack()

    root.mainloop()

