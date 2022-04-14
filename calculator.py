from cmath import exp
import tkinter as tk
from tkinter import ttk
from math import sqrt

root = tk.Tk()
root.title("calculator")

result = ttk.Label(text="", style="BW.TLabel")
result.pack()

first_num = ttk.Entry(root, text="input calculator")
first_num.pack()
second_num = ttk.Entry(root, text="input calculator1")
second_num.pack()

def calc_sum(first_num, second_num):

    try:
        return float(first_num) + float(second_num)
    except ValueError as err:
        return "unexpected value"

def calc_sub(first_num, second_num):

    try:
        return float(first_num) - float(second_num)
    except ValueError as err:
        return "unexpected value"
    
def calc_multi(first_num, second_num):
    try:
       return float(first_num) * float(second_num)
    except ValueError as err:
        return "unexpected value"

def calc_div(first_num, second_num):

    try:
        return float(first_num) / float(second_num)
    except ZeroDivisionError as err:
        result.config(text=err)
    except ValueError as err:
        result.config(text="ValueError")

def calc_exp(first_num, second_num):

    try:
        return float(first_num) ** float(second_num)
    except ValueError as err:
        result.config(text="ValueError")

def calc_mod(first_num, second_num):
    
    try:
        return float(first_num) % float(second_num)
    except ValueError as err:
        result.config(text="ValueError")

sum_bt = ttk.Button(root, text="+", command=lambda: result.config(text=calc_sum(first_num.get(), second_num.get())))
sum_bt.pack()

sub_bt = ttk.Button(root, text="-", command=lambda: result.config(text=calc_sub(first_num.get(), second_num.get())))
sub_bt.pack()

multi_bt = ttk.Button(root, text="*", command=lambda: result.config(text=calc_multi(first_num.get(), second_num.get())))
multi_bt.pack()

div_bt = ttk.Button(root, text="/", command=lambda: result.config(text=calc_div(first_num.get(), second_num.get())))
div_bt.pack()

exp_bt = ttk.Button(root, text="**", command=lambda: result.config(text=calc_exp(first_num.get(), second_num.get())))
exp_bt.pack()

mod_bt = ttk.Button(root, text="%", command=lambda: result.config(text=calc_mod(first_num.get(), second_num.get())))
mod_bt.pack()


root.mainloop()
