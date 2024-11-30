import tkinter as tk
import threading
from functools import partial
import time

#the MAIN THREAD is the default/initial thread of execution in any given program
#OBJECTS & CLASSES - this is the avoidance of global declaration, with no need for mutable containers (lists, dicts, etc.)

saved = {}#dictionary pairs: ("text_entry": "elapsed_time"), we can use enumerate to extract index

class Pomodoro:
    def __init__(self, work, rest, state, wr_state, total):#work/rest state, work=true, rest=false
        self.work = work
        self.rest = rest
        self.state = state
        self.wr_state = wr_state#brute forced this, created a new object which determines work/rest state
        self.total = total#total elasped time, includes work and rest times; total session time
        self.remain = work #remaining time cycles between work/rest times, starts with work time as default

    def clock(self):
        seconds = self.remain % 60
        minutes = int(self.remain / 60) % 60
        hours = int((self.remain / 60) / 60)
        text = tk.Label(timer, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Ariel", 60))
        text.grid(row=0, column=0)
        while True:#infinite loop is required here, prevents thread from ending once inner loop is False
            while self.state and self.remain >= 1:#self.remain >= 1 and not 0, because it decrements an extra 1
                self.total += 1#increment total session time
                self.remain -= 1
                seconds = self.remain % 60
                minutes = int(self.remain / 60) % 60
                hours = int((self.remain / 60) / 60)
                text = tk.Label(timer, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Ariel", 60))
                text.grid(row=0, column=0)
                time.sleep(1)#place time.sleep() at the end to immidiately display initial time before 1 second wait
                pomodoro.switch()

    def start_stop(self):
        if self.state:
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
        text = tk.Label(timer, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Ariel", 60))
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

    def save(self):#initial save button; pauses timer and opens save prompt
        if self.state:
            self.state = False
        pomodoro.save_prompt()

    def save_prompt(self):
        text = tk.Label(save_menu, text="Session Name:", font=("Ariel", 15))
        text.grid(row=0, column=0)
        entry = tk.Entry(save_menu, text="", font=("Ariel", 15))
        entry.grid(row=0, column=1)
        save = tk.Button(save_menu, text="Save", font=("Ariel", 10))
        save.config(command=partial(pomodoro.appender, entry))
        save.grid(row=0, column=2)
        #pomodoro.save_iter()

    def appender(self, entry):
        seconds = self.total % 60
        minutes = int(self.total / 60) % 60
        hours = int((self.total / 60) / 60)
        saved[entry.get()] = f"{hours:02}:{minutes:02}:{seconds:02}"#can't have identical entry names
        for widget in save_menu.winfo_children():
            widget.destroy()
        self.total = 0#resets total elapsed time when a new save entry is made
        pomodoro.save_iter()

    def save_iter(self):
        for index, (key, value) in enumerate(saved.items()):
            sesh = tk.Label(session, text=f"{key} -- Elapsed time: {value}", font=("Ariel", 15))
            sesh.grid(row=index, column=0)
            dlt = tk.Button(session, text="Delete", font=("Ariel", 10))
            dlt.config(command=partial(pomodoro.delete, key))
            dlt.grid(row=index, column=1)
    
    def delete(self, key):
        saved.pop(key)
        for widget in session.winfo_children():
            widget.destroy()
        pomodoro.save_iter()



#work time, rest time, start/stop state, work/rest state (work is true by default), total elapsed time (0 by default)
pomodoro = Pomodoro(10, 5, False, True, 0)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Pomodoro")

    timer = tk.Frame(root)
    timer.columnconfigure(0, weight=1)

    session = tk.Frame(root)
    session.columnconfigure(0, weight=1)#general info
    session.columnconfigure(1, weight=1)#delete session

    save_menu = tk.Frame(root)
    save_menu.columnconfigure(0, weight=1)
    save_menu.columnconfigure(1, weight=1)
    save_menu.columnconfigure(2, weight=1)

    
    clock_thread = threading.Thread(target=pomodoro.clock)#this is a CHILD/WORKER THREAD, which can execute its target function 
                                                #simultaneously while we do our other processes
    clock_thread.start()

    ssbtn = tk.Button(timer, text="Start/Stop", font=("Ariel", 20))
    ssbtn.config(command=pomodoro.start_stop)
    ssbtn.grid(row=1, column=0)

    rbtn = tk.Button(timer, text="Reset", font=("Ariel", 20))
    rbtn.config(command=pomodoro.reset)
    rbtn.grid(row=2, column=0)

    sbtn = tk.Button(timer, text="Save", font=("Ariel", 20))
    sbtn.config(command=pomodoro.save)
    sbtn.grid(row=3, column=0)

    save_menu.pack()

    session.pack()

    timer.pack()

    root.mainloop()