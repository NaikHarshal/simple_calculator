import tkinter as tk
from tkinter import ttk

# Function to update the expression on the display
def button_click(char):
    global expression
    expression = expression + str(char)
    input_text.set(expression)

# Function to clear the display
def button_clear():
    global expression
    expression = ""
    input_text.set(expression)

# Function to evaluate the expression
def button_equal():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")

# Function to add an opening bracket
def button_open_bracket():
    global expression
    expression = expression + "("
    input_text.set(expression)

# Function to add a closing bracket
def button_close_bracket():
    global expression
    expression = expression + ")"
    input_text.set(expression)

# Function to add a percentage
def button_percentage():
    global expression
    expression = expression + "/100"
    input_text.set(expression)

# Main window
window = tk.Tk()
window.title("Simple Calculator")

# Expression variable
expression = ""

# Input field
input_text = tk.StringVar()
input_field = tk.Entry(window, textvariable=input_text, font=('arial', 16, 'bold'), justify='right')
input_field.grid(columnspan=4, ipadx=70)

# Style for buttons
style = ttk.Style()
style.configure('Calc.TButton', font=('Arial', 12))

# Buttons
button_open_bracket = ttk.Button(window, text='(', style='Calc.TButton', command=button_open_bracket)
button_open_bracket.grid(row=1, column=0)
button_close_bracket = ttk.Button(window, text=')', style='Calc.TButton', command=button_close_bracket)
button_close_bracket.grid(row=1, column=1)
button_percentage = ttk.Button(window, text='%', style='Calc.TButton', command=button_percentage)
button_percentage.grid(row=1, column=2)
button_clear = ttk.Button(window, text='AC', style='Calc.TButton', command=button_clear)
button_clear.grid(row=1, column=3)

button_7 = ttk.Button(window, text='7', style='Calc.TButton', command=lambda: button_click(7))
button_7.grid(row=2, column=0)
button_8 = ttk.Button(window, text='8', style='Calc.TButton', command=lambda: button_click(8))
button_8.grid(row=2, column=1)
button_9 = ttk.Button(window, text='9', style='Calc.TButton', command=lambda: button_click(9))
button_9.grid(row=2, column=2)
button_div = ttk.Button(window, text='/', style='Calc.TButton', command=lambda: button_click('/'))
button_div.grid(row=2, column=3)

button_4 = ttk.Button(window, text='4', style='Calc.TButton', command=lambda: button_click(4))
button_4.grid(row=3, column=0)
button_5 = ttk.Button(window, text='5', style='Calc.TButton', command=lambda: button_click(5))
button_5.grid(row=3, column=1)
button_6 = ttk.Button(window, text='6', style='Calc.TButton', command=lambda: button_click(6))
button_6.grid(row=3, column=2)
button_mul = ttk.Button(window, text='*', style='Calc.TButton', command=lambda: button_click('*'))
button_mul.grid(row=3, column=3)

button_1 = ttk.Button(window, text='1', style='Calc.TButton', command=lambda: button_click(1))
button_1.grid(row=4, column=0)
button_2 = ttk.Button(window, text='2', style='Calc.TButton', command=lambda: button_click(2))
button_2.grid(row=4, column=1)
button_3 = ttk.Button(window, text='3', style='Calc.TButton', command=lambda: button_click(3))
button_3.grid(row=4, column=2)
button_sub = ttk.Button(window, text='-', style='Calc.TButton', command=lambda: button_click('-'))
button_sub.grid(row=4, column=3)

button_0 = ttk.Button(window, text='0', style='Calc.TButton', command=lambda: button_click(0))
button_0.grid(row=5, column=0)
button_dot = ttk.Button(window, text='.', style='Calc.TButton', command=lambda: button_click('.'))
button_dot.grid(row=5, column=1)
button_equal = ttk.Button(window, text='=', style='Calc.TButton', command=button_equal)
button_equal.grid(row=5, column=2)
button_add = ttk.Button(window, text='+', style='Calc.TButton', command=lambda: button_click('+'))
button_add.grid(row=5, column=3)

window.mainloop()
