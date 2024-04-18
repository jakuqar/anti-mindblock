#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
import subprocess
import os
from PIL import Image
import time
from pynput.keyboard import Controller, Key
import json

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
            def monitor_inversion_command():
                os.system("xrandr --output " + monitor + " --rotate inverted")
            monitor_inversion_command()  
    else:
        print("No monitors detected.")

def revert_monitor():
    monitors = detect_monitor_output()
    if monitors:
        for monitor in monitors:
            def monitor_reversion_command():
                os.system("xrandr --output " + monitor + " --rotate normal")
            monitor_reversion_command()  
    else:
        print("No monitors detected.")


root = tk.Tk()
root.title('Anti Mindblock')
root.configure(background='black')
root.minsize(500,500)

UI_flip_button = tk.Button(
    text="Flip monitor!",
    width=25,
    height=5,
    bg="#444444",
    fg="white",
    command=invert_monitor
)
UI_flip_button.pack()

UI_unflip_button = tk.Button(
    text="Unflip monitor!",
    width=25,
    height=5,
    bg="#444444",
    fg="white",
    command=revert_monitor
)
UI_unflip_button.pack()

def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_var.set(folder_path)
        print("Skin selected:", folder_path)

folder_var = tk.StringVar()

folder_entry = tk.Entry(root, textvariable=folder_var, state="readonly", width=30)
folder_entry.pack()

select_button = tk.Button(root, text="Select Skin", command=select_folder)
select_button.pack()

def skin_processing():
    # hitcircle rotation
    hitcircle = Image.open(folder_path + "/hitcircle.png")
    rotated_hitcircle = hitcircle.rotate(180)
    rotated_hitcircle.save(folder_path + "/hitcircle.png")
    # number0 rotation
    number0 = Image.open(folder_path + "/default-0.png")
    rotated_number0 = number0.rotate(180)
    rotated_number0.save(folder_path + "/default-0.png")
    # number1 rotation
    number1 = Image.open(folder_path + "/default-1.png")
    rotated_number1 = number1.rotate(180)
    rotated_number1.save(folder_path + "/default-1.png")
    # number2 rotation
    number2 = Image.open(folder_path + "/default-2.png")
    rotated_number2 = number2.rotate(180)
    rotated_number2.save(folder_path + "/default-2.png")
    # number3 rotation
    number3 = Image.open(folder_path + "/default-3.png")
    rotated_number3 = number3.rotate(180)
    rotated_number3.save(folder_path + "/default-3.png")
    # number4 rotation
    number4 = Image.open(folder_path + "/default-4.png")
    rotated_number4 = number4.rotate(180)
    rotated_number4.save(folder_path + "/default-4.png")
    # number5 rotation
    number5 = Image.open(folder_path + "/default-5.png")
    rotated_number5 = number5.rotate(180)
    rotated_number5.save(folder_path + "/default-5.png")
    # number6 rotation
    number6 = Image.open(folder_path + "/default-6.png")
    rotated_number6 = number6.rotate(180)
    rotated_number6.save(folder_path + "/default-6.png")
    # number7 rotation
    number7 = Image.open(folder_path + "/default-7.png")
    rotated_number7 = number7.rotate(180)
    rotated_number7.save(folder_path + "/default-7.png")
    # number8 rotation
    number8 = Image.open(folder_path + "/default-8.png")
    rotated_number8 = number8.rotate(180)
    rotated_number8.save(folder_path + "/default-8.png")
    # number9 rotation
    number9 = Image.open(folder_path + "/default-9.png")
    rotated_number9 = number9.rotate(180)
    rotated_number9.save(folder_path + "/default-9.png")
    # hitcircleoverlay rotation
    hitcircleoverlay = Image.open(folder_path + "/hitcircleoverlay.png")
    rotated_hitcircleoverlay = hitcircleoverlay.rotate(180)
    rotated_hitcircleoverlay.save(folder_path + "/hitcircleoverlay.png")

UI_skin_rotation_button = tk.Button(
    text="Flip skin!",
    width=25,
    height=5,
    bg="#444444",
    fg="white",
    command=skin_processing
)
UI_skin_rotation_button.pack()


keyboard = Controller()


def focus_window_by_class(window_class):
    command = "wmctrl -l -x"
    output = os.popen(command).read()
    window_id_lines = output.strip().splitlines()
    for line in window_id_lines:
        parts = line.split()
        if window_class in parts[2]:
            os.system(f"wmctrl -i -a {parts[0]}")
            return True
    return False

def focus_window():
    global window_class
    window_class = "osu!.exe"
    focused = focus_window_by_class(window_class)
    if focused:
        time.sleep(0.5)
        keyboard.press(Key.ctrl)
        keyboard.press(Key.alt)
        keyboard.press(Key.shift)
        keyboard.press('s')
        time.sleep(0.2)
        keyboard.release('s')
        keyboard.release(Key.shift)
        keyboard.release(Key.alt)
        keyboard.release(Key.ctrl)
        time.sleep(0.2)
    else:
        status_label.config(text="Window not found or could not be focused.")

username_bytes = subprocess.check_output(["whoami"])
username_str = username_bytes.decode("utf-8")
first_line_username = username_str.split('\n')[0]
otd_config_location = "/home/" + first_line_username + "/.config/OpenTabletDriver/settings.json"

def tablet_inversion():
    with open(otd_config_location, "r") as file:
        config = json.load(file)

    config["Profiles"][0]["AbsoluteModeSettings"]["Tablet"]["Rotation"] = 180.0
    with open(otd_config_location, "w") as file:
        json.dump(config, file, indent=2)
        time.sleep(0.3)
        os.system("systemctl restart --user opentabletdriver.service")

def tablet_reversion():
    with open(otd_config_location, "r") as file:
        config = json.load(file)

    config["Profiles"][0]["AbsoluteModeSettings"]["Tablet"]["Rotation"] = 0.0
    with open(otd_config_location, "w") as file:
        json.dump(config, file, indent=2)
        time.sleep(0.3)
        os.system("systemctl restart --user opentabletdriver.service")


def full_rotation():
    detect_monitor_output()
    invert_monitor()
    time.sleep(2)
    skin_processing()
    time.sleep(0.3)
    focus_window()
    time.sleep(0.2)
    tablet_inversion()

def full_reversion():
    detect_monitor_output()
    revert_monitor()
    time.sleep(2)
    skin_processing()
    time.sleep(0.3)
    focus_window()
    time.sleep(0.2)
    tablet_reversion()

UI_full_rotation_button = tk.Button(
    text="Flip everything!",
    width=25,
    height=5,
    bg="grey",
    fg="white",
    command=full_rotation
)
UI_full_rotation_button.pack()

UI_full_reversion_button = tk.Button(
    text="Unflip everything!",
    width=25,
    height=5,
    bg="grey",
    fg="white",
    command=full_reversion
)
UI_full_reversion_button.pack()

root.mainloop()