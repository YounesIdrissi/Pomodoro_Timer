#Tkinter clock display
import tkinter as tk
import threading
import time

#the MAIN THREAD is the default/initial thread of execution in any given program
#OBJECTS & CLASSES - this is the avoidance of global declaration, with no need for mutable containers (lists, dicts, etc.)

class Pomodoro:
    def __init__(self, start, state):
        self.start = start
        self.remain = start
        self.state = state
    def clock(self):
        seconds = self.remain % 60
        minutes = int(self.remain / 60) % 60
        hours = int((self.remain / 60) / 60)
        text = tk.Label(timer, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Ariel", 40))
        text.grid(row=0, column=0)
        while True:#infinite loop is required here, prevents thread from ending once ss = False
            while self.state == True and self.remain >= 1:#self.remain >= 1 and not 0, because it decrements an extra 1
                self.remain -= 1
                seconds = self.remain % 60
                minutes = int(self.remain / 60) % 60
                hours = int((self.remain / 60) / 60)
                text = tk.Label(timer, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Ariel", 40))
                text.grid(row=0, column=0)
                time.sleep(1)#place time.sleep() at the end to immidiately display initial time before 1 second wait
    def start_stop(self):
        if self.state == True:
            self.state = False
        else:
            self.state = True
    def reset(self):#should simply reset clock to original set starting time
        self.remain = self.start
        seconds = self.remain % 60
        minutes = int(self.remain / 60) % 60
        hours = int((self.remain / 60) / 60)
        text = tk.Label(timer, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Ariel", 40))
        text.grid(row=0, column=0)

pomodoro = Pomodoro(1500, False)#starting time, start/stop

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