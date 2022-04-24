import tkinter as tk
from tkinter import ttk
from calculator import Calculator


root = tk.Tk()
root.title("calculator")

result = ttk.Label(text="", style="BW.TLabel")
result.pack()

first_num = ttk.Entry(root, text="input calculator")
first_num.pack()
second_num = ttk.Entry(root, text="input calculator1")
second_num.pack()

sum_bt = ttk.Button(root, text="+", command=lambda: result.config(text=Calculator.calc_sum(first_num.get(), second_num.get())))
sum_bt.pack()

sub_bt = ttk.Button(root, text="-", command=lambda: result.config(text=Calculator.calc_sub(first_num.get(), second_num.get())))
sub_bt.pack()

multi_bt = ttk.Button(root, text="*", command=lambda: result.config(text=Calculator.calc_multi(first_num.get(), second_num.get())))
multi_bt.pack()

div_bt = ttk.Button(root, text="/", command=lambda: result.config(text=Calculator.calc_div(first_num.get(), second_num.get())))
div_bt.pack()

exp_bt = ttk.Button(root, text="**", command=lambda: result.config(text=Calculator.calc_exp(first_num.get(), second_num.get())))
exp_bt.pack()

mod_bt = ttk.Button(root, text="%", command=lambda: result.config(text=Calculator.calc_mod(first_num.get(), second_num.get())))
mod_bt.pack()


root.mainloop()
