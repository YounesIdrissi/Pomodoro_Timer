import tkinter as tk
import threading
import time

#the MAIN THREAD is the default/initial thread of execution in any given program
#OBJECTS & CLASSES - this is the avoidance of global declaration, with no need for mutable containers (lists, dicts, etc.)

class Pomodoro:
    def __init__(self, remain, state):
        self.remain = remain
        self.state = state
    def clock(self):
        while self.remain >= 0:#infinite loop is required here, prevents thread from ending once ss = False
            while self.state == True:
                seconds = self.remain % 60
                minutes = int(self.remain / 60) % 60
                hours = int((self.remain / 60) / 60)
                print(f"{hours:02}:{minutes:02}:{seconds:02}")
                self.remain -= 1
                time.sleep(1)#place time.sleep() at the end to immidiately display initial time before 1 second wait
    def start_stop(self):
        if self.state == True:
            self.state = False
        else:
            self.state = True

pomodoro = Pomodoro(1500, True)

if __name__ == '__main__':
    clock_thread = threading.Thread(target=pomodoro.clock)#this is a CHILD/WORKER THREAD, which can execute its target function 
                                                #simultaneously while we do our other processes
    clock_thread.start()

    root = tk.Tk()
    root.geometry("700x700")
    root.title("Pomodoro")

    btn = tk.Button(root, text="Start/Stop", font=("Ariel", 20))
    btn.config(command=pomodoro.start_stop)
    btn.pack()

    root.mainloop()
