import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

TEMP_THRESHOLD = 60.0
CHECK_INTERVAL = 10

def read_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp",'r') as file:
        temp = file.read().strip()
        return float(temp) / 1000


def check_temperature():
    temp = read_cpu_temperature()
    global TEMP_THRESHOLD
    if (temp > TEMP_THRESHOLD):
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning("Temperature warning", f"teplota procesoru je: {temp:.2f} °C")
        root.destroy()

def main():
    while True:
        global CHECK_INTERVAL
        check_temperature()
        time.sleep(CHECK_INTERVAL)
        
        
if __name__ == "__main__":
    main()
