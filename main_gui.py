from tkinter import *
from tkinter import font
from tkinter import ttk

root = Tk()
root.title("CALCULATOR 1.0")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 410
window_height = 380

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
frame.grid(column=0, row=0, padx=2, pady=10, sticky=(N,E,S,W))

# Listbox to display history calculations
listvalue = ('example1', 'example2', 'example3')
lname = StringVar(value=listvalue)
historyList = Listbox(frame, listvariable=lname, bd=2, relief="solid", highlightbackground="red", height=5, width=50)
historyList.grid(column=0, row=0, columnspan=4, sticky=(N,S,E,W))

# Entry for Calculations
textsize = font.Font(size=22, weight='bold')
calculation_entry = ttk.Entry(frame, font=textsize,justify=RIGHT)
calculation_entry.grid(column=0, row=1, columnspan=4, sticky=(N,S,E,W), pady=5, padx=3)

# Buttons on row=2
btn_ac = ttk.Button(frame, text="AC").grid(column=0, row=2, pady=3)
btn_c = ttk.Button(frame, text="C").grid(column=1, row=2, pady=5)
btn_percent = ttk.Button(frame, text="%").grid(column=2, row=2, pady=5)
btn_division = ttk.Button(frame, text="/").grid(column=3, row=2, pady=5)

# Buttons on row=3
btn_7 = ttk.Button(frame, text="7").grid(column=0, row=3, pady=5)
btn_8 = ttk.Button(frame, text="8").grid(column=1, row=3, pady=5)
btn_9 = ttk.Button(frame, text="9").grid(column=2, row=3, pady=5)
btn_multiply = ttk.Button(frame, text="x").grid(column=3, row=3, pady=5)

# Buttons on row=4
btn_4 = ttk.Button(frame, text="4").grid(column=0, row=4, pady=5)
btn_5 = ttk.Button(frame, text="5").grid(column=1, row=4, pady=5)
btn_6 = ttk.Button(frame, text="6").grid(column=2, row=4, pady=5)
btn_subtraction = ttk.Button(frame, text="-").grid(column=3, row=4, pady=5)

# Button on row=5
btn_1 = ttk.Button(frame, text="1").grid(column=0, row=5, pady=5)
btn_2 = ttk.Button(frame, text="2").grid(column=1, row=5, pady=5)
btn_3 = ttk.Button(frame, text="3").grid(column=2, row=5, pady=5)
btn_add = ttk.Button(frame, text="+").grid(column=3, row=5, pady=5)

# Button on row=6
btn_point = ttk.Button(frame, text=".").grid(column=0, row=6, pady=5)
btn_zero = ttk.Button(frame, text="0").grid(column=1, row=6, pady=5)
btn_del = ttk.Button(frame, text="<=").grid(column=2, row=6, pady=5)
btn_equals = ttk.Button(frame, text="=").grid(column=3, row=6, pady=5)

# Colorize alternating lines of the listbox
for i in range(0, len(listvalue),2):
    historyList.itemconfigure(i, background='#f0f0ff')
# Run the Tkinter event loop
root.mainloop()