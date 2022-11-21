
import time
from tkinter.messagebox import showinfo, showwarning

# Time for watchdog how long time working program
start = time.time()


if __name__ == '__main__':
    # table = 'items'
    # name = '6ES'
    # ozm = 707801
    # new_val = []

# Time of watchdog resolve work time
    work_time = time.time() - start
    print(f'Work time of program = {work_time}')
