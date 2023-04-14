import tkinter

# Функции

def math_operators(operator):
    current_data = window.get()
    window.delete(0, tkinter.END)
    if current_data == "" or current_data == "На ноль делить нельзя!":
        if operator in ["+", "-"]:
            window.insert(0, str(operator))
        else:
            pass
    elif current_data[-1] in ["+", "-", "/", "*", "%"]:
        window.insert(0, str(current_data))
    else:
        window.insert(0, str(current_data) + operator)

def button_clicked(number):
    current_data = window.get()
    window.delete(0, tkinter.END)
    if "." in current_data and number == ".":
        window.insert(0, str(current_data))
    elif current_data != str(0) and current_data != "На ноль делить нельзя!":
        window.insert(0, str(current_data) + str(number))
    else:
        window.insert(0, str(number))

def button_clear():
    window.delete(0, tkinter.END)

def button_equation():
    current_data = window.get()
    window.delete(0, tkinter.END)
    try:
        if "%" in current_data:
            if current_data.split("%")[0][-3:].isdigit():
                window.insert(0, str(0))
            elif current_data.split("%")[0][-2:].isdigit():
                percent = eval(current_data.split("%")[0][-2:])
                value = eval(current_data.split("%")[0][:-3])
                result = value - (percent / 100 * value)
                window.insert(0, str(result))
        else:
            current_data = eval(current_data)
            window.insert(0, str(current_data))
    except ZeroDivisionError:
        window.insert(0, "На ноль делить нельзя!")


# Главное окно
calculator = tkinter.Tk()
calculator.title("Калькулятор")

# Характеристики кнопок
button_font = ("Times new Roman", 30)
button_padx = 30
button_pady = 30


# Создаем элементы
window = tkinter.Entry(calculator, width=40, borderwidth=5)
button_C = tkinter.Button(calculator, text='C', font=button_font, padx=button_padx, pady=button_pady, command=button_clear)
button_opening_parentheses = tkinter.Button(calculator, text='(', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked('('))
button_closing_parentheses = tkinter.Button(calculator, text=')', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(')'))
button_division = tkinter.Button(calculator, text=':', font=button_font, padx=button_padx, pady=button_pady, command=lambda: math_operators("/"))
button_7 = tkinter.Button(calculator, text='7', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(7))
button_8 = tkinter.Button(calculator, text='8', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(8))
button_9 = tkinter.Button(calculator, text='9', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(9))
button_multiplication = tkinter.Button(calculator, text='X', font=button_font, padx=button_padx, pady=button_pady, command=lambda: math_operators("*"))
button_4 = tkinter.Button(calculator, text='4', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(4))
button_5 = tkinter.Button(calculator, text='5', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(5))
button_6 = tkinter.Button(calculator, text='6', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(6))
button_subtraction = tkinter.Button(calculator, text='-', font=button_font, padx=button_padx, pady=button_pady, command=lambda: math_operators("-"))
button_1 = tkinter.Button(calculator, text='1', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(1))
button_2 = tkinter.Button(calculator, text='2', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(2))
button_3 = tkinter.Button(calculator, text='3', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(3))
button_sum = tkinter.Button(calculator, text='+', font=button_font, padx=button_padx, pady=button_pady, command=lambda: math_operators("+"))
button_percent = tkinter.Button(calculator, text='%', font=button_font, padx=button_padx, pady=button_pady, command=lambda: math_operators("%"))
button_0 = tkinter.Button(calculator, text='0', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked(0))
button_decimal_point = tkinter.Button(calculator, text='.', font=button_font, padx=button_padx, pady=button_pady, command=lambda: button_clicked('.'))
button_equation = tkinter.Button(calculator, text='=', font=button_font, padx=button_padx, pady=button_pady, command=button_equation)


# Размещаем элементы
window.grid(row=0, column=0, columnspan=20, padx=10, pady=10)
button_C.grid(row=1, column=0)
button_opening_parentheses.grid(row=1, column=1)
button_closing_parentheses.grid(row=1, column=2)
button_division.grid(row=1, column=3)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiplication.grid(row=2, column=3)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subtraction.grid(row=3, column=3)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_sum.grid(row=4, column=3)
button_percent.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_decimal_point.grid(row=5, column=2)
button_equation.grid(row=5, column=3)


    
calculator.mainloop()