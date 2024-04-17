import tkinter as tk

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