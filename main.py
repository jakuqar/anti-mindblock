import tkinter as tk
import subprocess
import os
from PIL import Image

# Monitor inverting

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
            def monitor_inversion_command():
                os.system("xrandr --output " + monitor + " --rotate inverted")
            monitor_inversion_command()  
    else:
        print("No monitors detected.")

def revert_monitor():
    monitors = detect_monitor_output()
    if monitors:
        for monitor in monitors:
            print(monitor)
            def monitor_reversion_command():
                os.system("xrandr --output " + monitor + " --rotate normal")
            monitor_reversion_command()  
    else:
        print("No monitors detected.")

# Skin inverting /todo/

# UI

root = tk.Tk()
root.title('Anti Mindblock')
root.configure(background='black')
root.minsize(500,500)

UI_flip_button = tk.Button(
    text="Flip monitor!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=invert_monitor
)
UI_flip_button.pack()

UI_unflip_button = tk.Button(
    text="Unflip monitor!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=revert_monitor
)
UI_unflip_button.pack()



root.mainloop()