import tkinter as tk
#from functools import partial
import threading
import time

#the MAIN THREAD is the default/initial thread of execution in any given program

last_time = {'Remain': 1500}#update remaining time to this dictionary
ss = True#start/stop is false by default, waiting to be True by start_stop function (False=off/pause True=on/resume)

def clock(s):#target function of CHILD/WORKER THREAD - inside the nested while loop we constantly listen for bool ss being true or false
    #input (ss boolean) is processed mid-loop, allowing the instant stop/pause or resume/start of the program
    while s >= 0:#keeps testing the while loop for its conditions, does not allow this thread to end once ss = False
        while ss:
            seconds = s % 60
            minutes = int(s / 60) % 60
            hours = int((s / 60) / 60)
            time.sleep(1)#placing timesleep before input gives enough downtime to display input text below first
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            last_time.update(Remain=s)
            s -= 1

def start_stop():
    global ss
    while True:#button must always be available in the main thread for terminal pausing/resuming
        if ss:
            input("Enter to pause\n")
            ss = False
        else:
            input("Enter to resume\n")
            ss = True

if __name__ == '__main__':
    clock_thread = threading.Thread(target=clock, args=(last_time['Remain'],))#this is a CHILD/WORKER THREAD, which can execute its target function 
                                                                              #simultaneously while we do our other processes
    clock_thread.start()

    start_stop()

# root = tk.Tk()
# root.geometry("700x700")
# root.title("Pomodoro")

# btn = tk.Button(root, text="Start/Stop", font=("Ariel", 20))
# btn.config(command=start_stop)
# btn.pack()

# root.mainloop()



