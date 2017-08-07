"""
TODO:

nie usuwa liczb dwucyfrowych z entry
problem z literami (raz działa raz nie)


"""

from tkinter import *
import calculator
import helpmenu as hm

mainWindow = Tk()
mainWindow.title("RPN Calculator")

mainWindow.geometry("{}x{}".format(220, 280))
mainWindow.resizable(width=False, height=False)
mainWindow.grid_rowconfigure(0, weight=1)
mainWindow.grid_rowconfigure(12, weight=1)
mainWindow.grid_columnconfigure(0, weight=1)
mainWindow.grid_columnconfigure(5, weight=1)
menu = Menu(mainWindow)
mainWindow.config(menu=menu)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="How to use it...", command=hm.how_to)
helpMenu.add_command(label="About", command=hm.about_window)


# declaration and positioning labels (in which current stack values will be displayed), entry field and
# - lets call it - registers flags


def on_validate(s):

    if calculator.is_int(s) or calculator.is_float(s) or s == ".":
        return True
    else:
        mainWindow.bell()
        return False


validate_cmd = (mainWindow.register(on_validate), '%S')

a_reg_label = Label(mainWindow, text="0")
a_reg_label.grid(column=3, row=3, columnspan=4, sticky=E)
b_reg_label = Label(mainWindow, text="0")
b_reg_label.grid(column=3, row=2, columnspan=4, sticky=E)
c_reg_label = Label(mainWindow, text="0")
c_reg_label.grid(column=3, row=1, columnspan=4, sticky=E)
input_field = Entry(mainWindow, width=30, justify=RIGHT, validate="key", validatecommand=validate_cmd)
input_field.grid(row=4, column=1, columnspan=4, pady=5)
input_field.focus()
abcd_flags = [0, 0, 0]


def on_clear(char):
    if char == "c":
        input_field.delete(0, END)
    elif char == "ac":
        a_reg_label.config(text="0")
        b_reg_label.config(text="0")
        c_reg_label.config(text="0")
        for i in range(0, 3):
            abcd_flags[i] = 0
        input_field.delete(0, END)
        calculator.on_ac()


def on_enter():
    if input_field.get() != "":
        try:
            num = int(input_field.get())
        except ValueError:
            num = float(input_field.get())
        if abcd_flags[0] == 0:
            a_reg_label.config(text=calculator.proc_number(num))
            abcd_flags[0] = 1
            input_field.delete(0, 'end')
        elif abcd_flags[0] == 1 and abcd_flags[1] == 0:
            b_reg_label.config(text=a_reg_label.cget("text"))
            a_reg_label.config(text=calculator.proc_number(num))
            abcd_flags[1] = 1
            input_field.delete(0, 'end')
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 0:
            c_reg_label.config(text=b_reg_label.cget("text"))
            b_reg_label.config(text=a_reg_label.cget("text"))
            a_reg_label.config(text=calculator.proc_number(num))
            abcd_flags[2] = 1
            input_field.delete(0, 'end')
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 1:
            c_reg_label.config(text=b_reg_label.cget("text"))
            b_reg_label.config(text=a_reg_label.cget("text"))
            a_reg_label.config(text=calculator.proc_number(num))
            input_field.delete(0, 'end')


def enter_number(n):
    input_field.insert(len(input_field.get()), n)


def on_sign(sign):

    if sign == "+":
        if abcd_flags[0] == 1 and abcd_flags[1] == 0 and abcd_flags[2] == 0:
            pass
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 0:
            a_reg_label.config(text=str(calculator.on_plus()))
            b_reg_label.config(text=str(calculator.get_second()))
            abcd_flags[1] = 0
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 1:
            a_reg_label.config(text=str(calculator.on_plus()))
            b_reg_label.config(text=str(calculator.get_second()))
            c_reg_label.config(text=str(calculator.get_third()))
            if calculator.get_third() == 0:
                abcd_flags[2] = 0
    elif sign == "-":
        if abcd_flags[0] == 1 and abcd_flags[1] == 0 and abcd_flags[2] == 0:
            pass
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 0:
            a_reg_label.config(text=str(calculator.on_minus()))
            b_reg_label.config(text=str(calculator.get_second()))
            abcd_flags[1] = 0
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 1:
            a_reg_label.config(text=str(calculator.on_minus()))
            b_reg_label.config(text=str(calculator.get_second()))
            c_reg_label.config(text=str(calculator.get_third()))

            if calculator.get_third() == 0:
                abcd_flags[2] = 0
    elif sign == "*":
        if abcd_flags[0] == 1 and abcd_flags[1] == 0 and abcd_flags[2] == 0:
            pass
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 0:
            a_reg_label.config(text=str(calculator.on_multiply()))
            b_reg_label.config(text=str(calculator.get_second()))
            abcd_flags[1] = 0
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 1:
            a_reg_label.config(text=str(calculator.on_multiply()))
            b_reg_label.config(text=str(calculator.get_second()))
            c_reg_label.config(text=str(calculator.get_third()))

            if calculator.get_third() == 0:
                abcd_flags[2] = 0
    elif sign == "/":
        if abcd_flags[0] == 1 and abcd_flags[1] == 0 and abcd_flags[2] == 0:
            pass
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 0:
            a_reg_label.config(text=str(calculator.on_divide()))
            b_reg_label.config(text=str(calculator.get_second()))
            abcd_flags[1] = 0
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 1:
            a_reg_label.config(text=str(calculator.on_divide()))
            b_reg_label.config(text=str(calculator.get_second()))
            c_reg_label.config(text=str(calculator.get_third()))

            if calculator.get_third() == 0:
                abcd_flags[2] = 0
    elif sign == "^":
        if abcd_flags[0] == 1 and abcd_flags[1] == 0 and abcd_flags[2] == 0:
            pass
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 0:
            a_reg_label.config(text=str(calculator.on_pow()))
            b_reg_label.config(text=str(calculator.get_second()))
            abcd_flags[1] = 0
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 1:
            a_reg_label.config(text=str(calculator.on_pow()))
            b_reg_label.config(text=str(calculator.get_second()))
            c_reg_label.config(text=str(calculator.get_third()))

            if calculator.get_third() == 0:
                abcd_flags[2] = 0
    elif sign == "sqrt":
        if abcd_flags[0] == 1 and abcd_flags[1] == 0 and abcd_flags[2] == 0:
            a_reg_label.config(text=str(calculator.on_sqrt()))
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 0:
            a_reg_label.config(text=str(calculator.on_sqrt()))
            b_reg_label.config(text=str(calculator.get_second()))
            abcd_flags[1] = 0
        elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 1:
            a_reg_label.config(text=str(calculator.on_sqrt()))
            b_reg_label.config(text=str(calculator.get_second()))
            c_reg_label.config(text=str(calculator.get_third()))

            if calculator.get_third() == 0:
                abcd_flags[2] = 0


def add_sign(sign):
    if sign == ".":
        input_field.insert(INSERT, ".")


def on_pop():
    if abcd_flags[0] == 1 and abcd_flags[1] == 0 and abcd_flags[2] == 0:
        a_reg_label.config(text="0")
        abcd_flags[0] = 0
        calculator.on_pop()
    elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 0:
        calculator.on_pop()
        a_reg_label.config(text=str(calculator.get_first()))
        b_reg_label.config(text=str(calculator.get_second()))
        abcd_flags[1] = 0
    elif abcd_flags[0] == 1 and abcd_flags[1] == 1 and abcd_flags[2] == 1:
        calculator.on_pop()
        a_reg_label.config(text=str(calculator.get_first()))
        b_reg_label.config(text=str(calculator.get_second()))
        c_reg_label.config(text=str(calculator.get_third()))
        if calculator.get_third() == 0:
            abcd_flags[2] = 0


def plus_minus():
    if abcd_flags[0] == 0:
        return
    else:
        a_reg_label.config(text=str(calculator.change_sign()))

# declaring events binded to keystrokes

input_field.bind("<Return>", lambda x: on_enter())
input_field.bind("<Key-plus>", lambda x: on_sign("+"))
input_field.bind("<Key-minus>", lambda x: on_sign("-"))
input_field.bind("<Key-asterisk>", lambda x: on_sign("*"))
input_field.bind("<Key-slash>", lambda x: on_sign("/"))
# declaring and positioning buttons

# ROW 1
c_button = Button(mainWindow, text="C", command=lambda: on_clear("c"),
                  height=1, width=6, anchor=CENTER).grid(column=1, row=5)
ac_button = Button(mainWindow, text="AC", command=lambda: on_clear("ac"),
                   height=1, width=6, anchor=CENTER).grid(column=2, row=5)
pop_button = Button(mainWindow, text="POP", command=on_pop,
                    height=1, width=6, anchor=CENTER).grid(column=3, row=5)

# ROW 2
sqrt_button = Button(mainWindow, text="SQRT", command=lambda: on_sign("sqrt"),
                     height=1, width=6, anchor=CENTER).grid(column=1, row=6)
power_button = Button(mainWindow, text="POW", command=lambda: on_sign("^"),
                      height=1, width=6, anchor=CENTER).grid(column=2, row=6)
plus_minus_button = Button(mainWindow, text="+/-", command=plus_minus,
                           height=1, width=6, anchor=CENTER).grid(column=3, row=6)
divide_button = Button(mainWindow, text="/", command=lambda: on_sign("/"),
                       height=1, width=6, anchor=CENTER).grid(column=4, row=6)

# ROW 3
seven_button = Button(mainWindow, text="7", command=lambda: enter_number("7"),
                      height=1, width=6, anchor=CENTER).grid(column=1, row=7)
eight_button = Button(mainWindow, text="8", command=lambda: enter_number("8"),
                      height=1, width=6, anchor=CENTER).grid(column=2, row=7)
nine_button = Button(mainWindow, text="9", command=lambda: enter_number("9"),
                     height=1, width=6, anchor=CENTER).grid(column=3, row=7)
multiply_button = Button(mainWindow, text="*", command=lambda: on_sign("*"),
                         height=1, width=6, anchor=CENTER).grid(column=4, row=7)

# ROW 4
four_button = Button(mainWindow, text="4", command=lambda: enter_number("4"),
                     height=1, width=6, anchor=CENTER).grid(column=1, row=8)
five_button = Button(mainWindow, text="5", command=lambda: enter_number("5"),
                     height=1, width=6, anchor=CENTER).grid(column=2, row=8)
six_button = Button(mainWindow, text="6", command=lambda: enter_number("6"),
                    height=1, width=6, anchor=CENTER).grid(column=3, row=8)
plus_button = Button(mainWindow, text="+", command=lambda: on_sign("+"),
                     height=1, width=6, anchor=CENTER).grid(column=4, row=8)

# ROW 5
three_button = Button(mainWindow, text="3", command=lambda: enter_number("3"),
                      height=1, width=6, anchor=CENTER).grid(column=1, row=9)
two_button = Button(mainWindow, text="2", command=lambda: enter_number("2"),
                    height=1, width=6, anchor=CENTER).grid(column=2, row=9)
one_button = Button(mainWindow, text="1", command=lambda: enter_number("1"),
                    height=1, width=6, anchor=CENTER).grid(column=3, row=9)
minus_button = Button(mainWindow, text="-", command=lambda: on_sign("-"),
                      height=1, width=6, anchor=CENTER).grid(column=4, row=9)

# ROW 6
zero_button = Button(mainWindow, text="0", command=lambda: enter_number("0"),
                     height=1, width=6, anchor=CENTER).grid(column=1, row=10)
coma_button = Button(mainWindow, text=",", command=lambda: add_sign("."),
                     height=1, width=6, anchor=CENTER).grid(column=2, row=10)
enter_button = Button(mainWindow, text="ENTER", command=on_enter,
                      height=1, width=13, anchor=CENTER)
enter_button.grid(column=3, row=10, columnspan=2)


mainWindow.mainloop()
