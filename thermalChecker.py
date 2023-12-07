#!/usr/bin/env python3
import time
import logging
import os
import tkinter as tk
from tkinter import messagebox

TEMP_THRESHOLD = 40.0
CHECK_INTERVAL = 10
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cpu_temp_monitor")

class CustomDialog(tk.Toplevel):

    def __init__(self, parent, temp):
        super().__init__(parent)
        self.title("Temperature warning")
        
        msg = f"Processor's temperature is: {temp:.2f} °C"
        tk.Label(self, text=msg).pack(padx=20, pady=20)
        
        tk.Button(self, text="OK", command=self.destroy).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(self, text="Info", command=self.show_info).pack(side=tk.RIGHT, padx=10, pady=10)

    def show_info(self):
        messagebox.showinfo("Information", "This is additional information about the processor's temperature.")
        
        
def read_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp",'r') as file:
        temp = file.read().strip()
        temp = float(temp) / 1000
        logger.info(f"Actual temperature of processor is: {temp:.2f} °C")
        return temp


def check_temperature():
    temp = read_cpu_temperature()
    global TEMP_THRESHOLD
    if (temp > TEMP_THRESHOLD):
            root = tk.Tk()
    root.withdraw()
    CustomDialog(root, temp)
    root.mainloop()

def main():
    while True:
        global CHECK_INTERVAL
        check_temperature()
        time.sleep(CHECK_INTERVAL)
        
        
if __name__ == "__main__":
    main()
