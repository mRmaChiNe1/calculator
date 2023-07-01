import tkinter
from tkinter import *
from tkinter import messagebox
import math
import numpy as np


class Calculator(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title('Calculator')

        self.calc_operator = ''
        self.configure(bg="#E2E2E2", bd=20)
        self.text_input = StringVar()
        self.e = math.exp
        self.p = math.pi
        self.E = '*10**'

        self.text_display = tkinter.Entry(self, font=('sans-serif', 20, 'bold'), textvariable=self.text_input,
                                          bd=5, insertwidth=5, bg='#fff', justify='right').grid(columnspan=5, pady=20)


if __name__ == "__main__":
    tk_calc = Calculator()
    tk_calc.mainloop()
