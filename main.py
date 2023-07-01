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

        self.button_params = {'bd': 5, 'fg': '#000', 'bg': '#E2E2E2', 'font': ('sans-serif', 20, 'bold')}
        self.button_params_main = {'bd': 5, 'fg': '#000', 'bg': '#E2E2E2', 'font': ('sans-serif', 20, 'bold')}

        # 1 ряд
        left_par = tkinter.Button(self, self.button_params, text='(',
                                  command=lambda: self.button_click('(')).grid(row=1, column=0, sticky="nsew")

        right_par = tkinter.Button(self, self.button_params, text=')',
                                   command=lambda: self.button_click(')')).grid(row=1, column=1, sticky="nsew")

        pi_num = tkinter.Button(self, self.button_params, text='π',
                                command=lambda: self.button_click(str(math.pi))).grid(row=1, column=2, sticky="nsew")

        eulers_num = tkinter.Button(self, self.button_params, text='e',
                                    command=lambda: self.button_click(str(math.exp(1)))).grid(row=1, column=3,
                                                                                              sticky="nsew")

        # 2 ряд
        asine = tkinter.Button(self, self.button_params, text='asin',
                               command=self.trig_asin).grid(row=2, column=0, sticky="nsew")

        delete_one = tkinter.Button(self, self.button_params, text='DEL',
                                    command=self.button_delete).grid(row=2, column=1, sticky="nsew")

        delete_all = tkinter.Button(self, self.button_params, text='AC',
                                    command=self.button_clear_all).grid(row=2, column=2, sticky="nsew")

        div = tkinter.Button(self, self.button_params_main, text='/',
                             command=lambda: self.button_click('/')).grid(row=2, column=3, sticky="nsew")

        # 3 ряд
        button_7 = tkinter.Button(self, self.button_params_main, text='7',
                                  command=lambda: self.button_click('7')).grid(row=3, column=0, sticky="nsew")

        button_8 = tkinter.Button(self, self.button_params_main, text='8',
                                  command=lambda: self.button_click('8')).grid(row=3, column=1, sticky="nsew")

        button_9 = tkinter.Button(self, self.button_params_main, text='9',
                                  command=lambda: self.button_click('9')).grid(row=3, column=2, sticky="nsew")

        mul = tkinter.Button(self, self.button_params_main, text='*',
                             command=lambda: self.button_click('*')).grid(row=3, column=3, sticky="nsew")

        # 4 ряд
        button_4 = tkinter.Button(self, self.button_params_main, text='4',
                                  command=lambda: self.button_click('4')).grid(row=4, column=0, sticky="nsew")

        button_5 = tkinter.Button(self, self.button_params_main, text='5',
                                  command=lambda: self.button_click('5')).grid(row=4, column=1, sticky="nsew")

        button_6 = tkinter.Button(self, self.button_params_main, text='6',
                                  command=lambda: self.button_click('6')).grid(row=4, column=2, sticky="nsew")

        sub = tkinter.Button(self, self.button_params_main, text='-',
                             command=lambda: self.button_click('-')).grid(row=4, column=3, sticky="nsew")

        # 5 ряд
        button_1 = tkinter.Button(self, self.button_params_main, text='1',
                                  command=lambda: self.button_click('1')).grid(row=5, column=0, sticky="nsew")
        button_2 = tkinter.Button(self, self.button_params_main, text='2',
                                  command=lambda: self.button_click('2')).grid(row=5, column=1, sticky="nsew")
        button_3 = tkinter.Button(self, self.button_params_main, text='3',
                                  command=lambda: self.button_click('3')).grid(row=5, column=2, sticky="nsew")
        add = tkinter.Button(self, self.button_params_main, text='+',
                             command=lambda: self.button_click('+')).grid(row=5, column=3, sticky="nsew")

        # 6 ряд
        button_0 = tkinter.Button(self, self.button_params_main, text='0',
                                  command=lambda: self.button_click('0')).grid(row=6, column=0, sticky="nsew")
        point = tkinter.Button(self, self.button_params_main, text='.',
                               command=lambda: self.button_click('.')).grid(row=6, column=1, sticky="nsew")
        equal = tkinter.Button(self, self.button_params_main, text='=',
                               command=self.button_equal).grid(row=6, columnspan=2, column=2, sticky="nsew")

    def button_click(self, char):
        self.calc_operator += str(char)
        self.text_input.set(self.calc_operator)

    def button_clear_all(self):
        self.calc_operator = ""
        self.text_input.set("")

    def button_delete(self):
        text = self.calc_operator[:-1]
        self.calc_operator = text
        self.text_input.set(text)

    def trig_asin(self):
        if 359.0 > float(self.calc_operator) > -359.0:
            result = str(np.arcsin(math.radians(float(self.calc_operator))))
            self.calc_operator = result
            self.text_input.set(result)
        elif float(self.calc_operator) == 360.0 or float(self.calc_operator) == -360.0:
            result = str(np.arcsin(math.radians(0.0)))
            self.calc_operator = result
            self.text_input.set(result)
        else:
            messagebox.showinfo(title="Количество градусов", message="Введите градусы от -360 до 360")

    def button_equal(self):
        try:
            temp_op = str(eval(self.calc_operator))
            self.text_input.set(temp_op)
        except ZeroDivisionError:
            self.text_input.set("Infinity")
        except NameError:
            self.text_input.set("Error. Try again")
        else:
            self.calc_operator = temp_op


if __name__ == "__main__":
    tk_calc = Calculator()
    tk_calc.mainloop()
