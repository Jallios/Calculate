import tkinter as tk

def add_digit(digit):
    value = calc.get()
    if value[0] == '0':
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*()':
        value = value[:-1]
    if value[-1] in '**':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def Calculate():
    value = calc.get()
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except:
        calc.insert(0,404)

def Clear():
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0,0)

def make_Digit_Button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 12), command = lambda : add_digit(digit))

def make_Operation_Button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 12), command = lambda : add_operation(operation))

def make_Calc_Button(calc):
    return tk.Button(text=calc, bd=5, font=('Arial', 12), command = Calculate)

def make_Clear_Button(calc):
    return tk.Button(text=calc, bd=5, font=('Arial', 12), command = Clear)


win = tk.Tk()
win.geometry(f"300x350+100+200")
win['bg'] = '#748500'
win.title('Калькулятор')

calc = tk.Entry(win, justify = tk.RIGHT, font=('Arial',18), width=15)
calc.insert(0,'0')
calc.grid(row = 0, column = 0, columnspan = 5, stick = 'we', padx = 5)

make_Digit_Button('1').grid(row = 1 , column = 0, stick='wens', padx = 5, pady = 5)
make_Digit_Button('2').grid(row = 1 , column = 1, stick='wens', padx = 5, pady = 5)
make_Digit_Button('3').grid(row = 1 , column = 2, stick='wens', padx = 5, pady = 5)
make_Digit_Button('4').grid(row = 2 , column = 0, stick='wens', padx = 5, pady = 5)
make_Digit_Button('5').grid(row = 2 , column = 1, stick='wens', padx = 5, pady = 5)
make_Digit_Button('6').grid(row = 2 , column = 2, stick='wens', padx = 5, pady = 5)
make_Digit_Button('7').grid(row = 3 , column = 0, stick='wens', padx = 5, pady = 5)
make_Digit_Button('8').grid(row = 3 , column = 1, stick='wens', padx = 5, pady = 5)
make_Digit_Button('9').grid(row = 3 , column = 2, stick='wens', padx = 5, pady = 5)
make_Digit_Button('0').grid(row = 4 , column = 1, stick='wens', padx = 5, pady = 5)
make_Digit_Button('(').grid(row = 4 , column = 0, stick='wens', padx = 5, pady = 5)
make_Digit_Button(')').grid(row = 4 , column = 2, stick='wens', padx = 5, pady = 5)

make_Operation_Button('+').grid(row = 1 , column = 3, stick='wens', padx = 5, pady = 5)
make_Operation_Button('-').grid(row = 2 , column = 3, stick='wens', padx = 5, pady = 5)
make_Operation_Button('/').grid(row = 3 , column = 3, stick='wens', padx = 5, pady = 5)
make_Operation_Button('*').grid(row = 3 , column = 4, stick='wens', padx = 5, pady = 5)
make_Operation_Button('**').grid(row = 1 , column = 4, stick='wens', padx = 5, pady = 5)
make_Operation_Button('%').grid(row = 2, column = 4, stick='wens', padx = 5, pady = 5)

make_Calc_Button('=').grid(row = 4, column = 3, stick='wens', padx = 5, pady = 5)

make_Clear_Button('C').grid(row = 4, column = 4, stick='wens', padx = 5, pady = 5)

win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)
win.grid_columnconfigure(4,minsize=60)

win.grid_rowconfigure(0,minsize=60)
win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)

win.mainloop()