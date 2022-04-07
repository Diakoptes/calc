import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("calculator")

result = ttk.Label(text="", style="BW.TLabel")
result.pack()

first_num = ttk.Entry(root, text="input calculator")
first_num.pack()
second_num = ttk.Entry(root, text="input calculator1")
second_num.pack()


def calc_sum():
    num1 = float(first_num.get())
    num2 = float(second_num.get())

    result.config(text=str(num1 + num2))


def calc_sub():
    num1 = float(first_num.get())
    num2 = float(second_num.get())

    result.config(text=str(num1 - num2))

def calc_multi():
    num1 = float(first_num.get())
    num2 = float(second_num.get())

    result.config(text=str(num1 * num2))

def calc_div():
    num1 = float(first_num.get())
    num2 = float(second_num.get())

    result.config(text=str(num1 / num2))

def calc_exp():
    num1 = float(first_num.get())
    num2 = float(second_num.get())

    result.config(text=str(num1 ** num2))

def calc_mod():
    num1 = float(first_num.get())
    num2 = float(second_num.get())

    result.config(text=str(num1 % num2))


sum_bt = ttk.Button(root, text="+", command=calc_sum)
sum_bt.pack()
sub_bt = ttk.Button(root, text="-", command=calc_sub)
sub_bt.pack()
multi_bt = ttk.Button(root, text="*", command=calc_multi)
multi_bt.pack()
div_bt = ttk.Button(root, text="/", command=calc_div)
div_bt.pack()
sum_exp = ttk.Button(root, text="**", command=calc_exp)
sum_exp.pack()
sum_mod = ttk.Button(root, text="%", command=calc_mod)
sum_mod.pack()
root.mainloop()
