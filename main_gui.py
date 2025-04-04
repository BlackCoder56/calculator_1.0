from tkinter import *
from tkinter import ttk

root = Tk()
root.title("CALCULATOR 1.0")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 400
window_height = 600

# Calculate the position to center the window
position_top = (screen_height // 2) - (window_height // 2)
position_right = (screen_width // 2) - (window_width // 2)

# Set the window size and position
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Disable resizing
root.resizable(False, False)

# Create a style for the ttk.Frame
style = ttk.Style()
style.configure("TFrame", background="#0000")

# Frame to hold ttk components
frame = ttk.Frame(root, style="TFrame", width=window_width, height=window_height)
frame.pack_propagate(False)
# frame.pack()
frame.grid(column=0, row=0)

# Gui
listvalue = ('example1', 'example2', 'example3')
lname = StringVar(value=listvalue)
historyList = Listbox(frame, listvariable=lname, height=3, width=50)
historyList.grid(column=0, row=0, columnspan=4, sticky=(N,S,E,W))




# Colorize alternating lines of the listbox
for i in range(0, len(listvalue),2):
    historyList.itemconfigure(i, background='#f0f0ff')
# Run the Tkinter event loop
root.mainloop()