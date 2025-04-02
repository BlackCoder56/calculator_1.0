from tkinter import *
from tkinter import ttk

root = Tk()
root.title("CALCULATOR 1.0")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 400
window_height = 300

# Calculate the position to center the window
position_top = (screen_height // 2) - (window_height // 2)
position_right = (screen_width // 2) - (window_width // 2)

# Set the window size and position
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Disable resizing
root.resizable(False, False)

# Create a style for the ttk.Frame
style = ttk.Style()
style.configure("TFrame", background="lightblue")

# Frame to hold ttk components
frame = ttk.Frame(root, style="TFrame", width=window_width, height=window_height)
frame.pack_propagate(False)
# frame.pack()
frame.grid(column=0, row=0)

# Run the Tkinter event loop
root.mainloop()