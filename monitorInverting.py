import tkinter as tk
import subprocess
import os

def detect_monitor_output():
    try:
        # Run the xrandr command and capture its output
        output = subprocess.check_output(['xrandr']).decode('utf-8')
        
        # Split the output into lines
        lines = output.split('\n')
        
        # Iterate through the lines to find the connected monitor(s)
        connected_monitors = []
        for line in lines:
            if ' connected' in line:
                # Extract the monitor name from the line
                monitor_name = line.split()[0]
                connected_monitors.append(monitor_name)
        
        return connected_monitors
    except subprocess.CalledProcessError:
        print("Error: Unable to run xrandr command.")
        return None

def invert_monitor():
    monitors = detect_monitor_output()
    if monitors:
        for monitor in monitors:
            print(monitor)
            def monitor_choice():
                os.system("xrandr --output " + monitor + " --rotate inverted")
            monitor_choice()  
    else:
        print("No monitors detected.")

root = tk.Tk()
button = tk.Button(
    text="Flip monitor!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=invert_monitor
)
button.pack()

root.mainloop()