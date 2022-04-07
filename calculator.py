import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("calculator")

ttk.result = ttk.Label(text="", style="BW.TLabel")
ttk.result.grid(column=0, row=0)

ttk.first_num = ttk.Entry(root, text="input calculator")
ttk.first_num.grid(column=0, row=1)

ttk.second_num = ttk.Entry(root, text="input calculator1")
ttk.second_num.grid(column=0, row=2)

ttk.restart = ttk.Button(root, text="C")
ttk.restart.grid(column=0, row=3)

ttk.addition = ttk.Button(root, text="+" )
ttk.addition.grid(column=0, row=4)

ttk.subtraction = ttk.Button(root, text="-")
ttk.subtraction.grid(column=0, row=5)

ttk.multiplication = ttk.Button(root, text="*")
ttk.multiplication.grid(column=0, row=6)

ttk.division = ttk.Button(root, text="/")
ttk.division.grid(column=0, row=7)

ttk.exponentiation = ttk.Button(root, text="**")
ttk.exponentiation.grid(column=0, row=8)

ttk.modulo = ttk.Button(root, text="&")
ttk.modulo.grid(column=0, row=9)

num_1 = tk.IntVar()
num_2 = tk.IntVar()

def count():

    ttk.result["text"] = sum(num_1, num_2)    

window_width = 150
window_height = 300

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# max min window size
root.minsize(150, 290)
root.maxsize(150, 290)
# Changing the default icon
#root.iconbitmap('./assets/pythontutorial.ico')


# keep the window displaying
root.mainloop()



