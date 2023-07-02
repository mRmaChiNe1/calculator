import tkinter
from tkinter import *
from tkinter import messagebox
import math


class Calculator(tkinter.Tk):

    def __init__(self):
        """
        Метод инициализации объекта
        """
        super().__init__()
        self.title('Calculator')

        self.calc_operator = ''
        self.configure(bg="#E2E2E2", bd=20)
        self.text_input = StringVar()
        self.e = round(math.e, 6)
        self.pi = round(math.pi, 6)
        self.E = '*10**'

        self.text_display = tkinter.Entry(self, font=('sans-serif', 20, 'bold'), textvariable=self.text_input,
                                          bd=5, insertwidth=5, bg='#fff', justify='right').grid(columnspan=5, pady=20)

        self.button_params = {'bd': 5, 'fg': '#000', 'bg': '#E2E2E2', 'font': ('sans-serif', 20, 'bold')}

        self.buttons = [
            {'name': '(', 'function': lambda: self.button_click('('), 'row': 1, 'column': 0, 'columnspan': 1},
            {'name': ')', 'function': lambda: self.button_click(')'), 'row': 1, 'column': 1, 'columnspan': 1},
            {'name': 'π', 'function': lambda: self.button_click(str(self.pi)), 'row': 1, 'column': 2, 'columnspan': 1},
            {'name': 'e', 'function': lambda: self.button_click(self.e), 'row': 1, 'column': 3, 'columnspan': 1},

            {'name': 'asin', 'function': lambda: self.trig_asin(), 'row': 2, 'column': 0, 'columnspan': 1},
            {'name': 'DEL', 'function': lambda: self.button_delete(), 'row': 2, 'column': 1, 'columnspan': 1},
            {'name': 'AC', 'function': lambda: self.button_clear_all(), 'row': 2, 'column': 2, 'columnspan': 1},
            {'name': '/', 'function': lambda: self.button_click('/'), 'row': 2, 'column': 3, 'columnspan': 1},

            {'name': '7', 'function': lambda: self.button_click('7'), 'row': 3, 'column': 0, 'columnspan': 1},
            {'name': '8', 'function': lambda: self.button_click('8'), 'row': 3, 'column': 1, 'columnspan': 1},
            {'name': '9', 'function': lambda: self.button_click('9'), 'row': 3, 'column': 2, 'columnspan': 1},
            {'name': '*', 'function': lambda: self.button_click('*'), 'row': 3, 'column': 3, 'columnspan': 1},

            {'name': '4', 'function': lambda: self.button_click('4'), 'row': 4, 'column': 0, 'columnspan': 1},
            {'name': '5', 'function': lambda: self.button_click('5'), 'row': 4, 'column': 1, 'columnspan': 1},
            {'name': '6', 'function': lambda: self.button_click('6'), 'row': 4, 'column': 2, 'columnspan': 1},
            {'name': '-', 'function': lambda: self.button_click('-'), 'row': 4, 'column': 3, 'columnspan': 1},

            {'name': '1', 'function': lambda: self.button_click('1'), 'row': 5, 'column': 0, 'columnspan': 1},
            {'name': '2', 'function': lambda: self.button_click('2'), 'row': 5, 'column': 1, 'columnspan': 1},
            {'name': '3', 'function': lambda: self.button_click('3'), 'row': 5, 'column': 2, 'columnspan': 1},
            {'name': '+', 'function': lambda: self.button_click('+'), 'row': 5, 'column': 3, 'columnspan': 1},

            {'name': '0', 'function': lambda: self.button_click('0'), 'row': 6, 'column': 0, 'columnspan': 1},
            {'name': '.', 'function': lambda: self.button_click('.'), 'row': 6, 'column': 1, 'columnspan': 1},
            {'name': '=', 'function': lambda: self.button_equal(), 'row': 6, 'column': 2, 'columnspan': 2},
        ]

        for button in self.buttons:
            tkinter.Button(self, self.button_params, text=button['name'], command=button['function'])\
                .grid(row=button['row'], column=button['column'], columnspan = button['columnspan'], sticky="nsew")


    def button_click(self, char):
        """
        Метод обработки нажатия кнопки на форме
        :param char: символ нажатой кнопки
        """
        self.calc_operator += str(char)
        self.text_input.set(self.calc_operator)

    def button_clear_all(self):
        """
        Метод полной очистки текстового поля
        """
        self.calc_operator = ""
        self.text_input.set("")

    def button_delete(self):
        """
        Метод удаления символа из текстового поля
        """
        text = self.calc_operator[:-1]
        self.calc_operator = text
        self.text_input.set(text)

    def trig_asin(self):
        """
        Метод для расчета арксинуса
        """
        if 1 >= float(self.calc_operator) >= -1:
            result = str(math.asin(float(self.calc_operator)))
            self.calc_operator = result
            self.text_input.set(result)
        else:
            messagebox.showinfo(title="Значение арксинуса", message="Введите значение от -1 до 1")

    def button_equal(self):
        """
        Метод для расчета значений, указанных в текстовом поле
        """
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
