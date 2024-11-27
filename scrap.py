#Tkinter clock display
import tkinter as tk
import threading
import time

#the MAIN THREAD is the default/initial thread of execution in any given program
#OBJECTS & CLASSES - this is the avoidance of global declaration, with no need for mutable containers (lists, dicts, etc.)

class Pomodoro:
    def __init__(self, work, rest, state, wr_state):#work/rest state, work=true, rest=false
        self.work = work
        self.rest = rest
        self.state = state
        self.wr_state = wr_state#brute forced this, created a new object which determines work/rest state
        self.remain = work #remaining time cycles between work/rest times, starts with work time as default

    def clock(self):
        seconds = self.remain % 60
        minutes = int(self.remain / 60) % 60
        hours = int((self.remain / 60) / 60)
        text = tk.Label(timer, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Ariel", 40))
        text.grid(row=0, column=0)
        while True:#infinite loop is required here, prevents thread from ending once inner loop is False
            while self.state == True and self.remain >= 1:#self.remain >= 1 and not 0, because it decrements an extra 1
                self.remain -= 1
                seconds = self.remain % 60
                minutes = int(self.remain / 60) % 60
                hours = int((self.remain / 60) / 60)
                text = tk.Label(timer, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Ariel", 40))
                text.grid(row=0, column=0)
                time.sleep(1)#place time.sleep() at the end to immidiately display initial time before 1 second wait
                pomodoro.switch()

    def start_stop(self):
        if self.state == True:
            self.state = False
        else:
            self.state = True

    def reset(self):#should simply reset clock to original set starting time
        if self.wr_state:
            self.remain = self.work
        else:
            self.remain = self.rest
        #The below block of code is necessary to display restarted timer when clock is paused
        seconds = self.remain % 60
        minutes = int(self.remain / 60) % 60
        hours = int((self.remain / 60) / 60)
        text = tk.Label(timer, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Ariel", 40))
        text.grid(row=0, column=0)

    def switch(self):#switches from work timer to rest timer
        if self.remain >= 1:
            return
        if self.wr_state:
            self.remain = self.rest#display 'REST' text on the top
            self.wr_state = False
        else:
            self.remain = self.work#display 'WORK' text on the top
            self.wr_state = True

    def save(self):
        pass

pomodoro = Pomodoro(10, 5, False, True)#work time, rest time, start/stop state, work/rest state (work is true by default)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Pomodoro")

    timer = tk.Frame(root)
    timer.columnconfigure(0, weight=1)
    
    clock_thread = threading.Thread(target=pomodoro.clock)#this is a CHILD/WORKER THREAD, which can execute its target function 
                                                #simultaneously while we do our other processes
    clock_thread.start()

    ssbtn = tk.Button(timer, text="Start/Stop", font=("Ariel", 20))
    ssbtn.config(command=pomodoro.start_stop)
    ssbtn.grid(row=1, column=0)

    rbtn = tk.Button(timer, text="Reset", font=("Ariel", 20))
    rbtn.config(command=pomodoro.reset)
    rbtn.grid(row=2, column=0)

    timer.pack()

    root.mainloop()