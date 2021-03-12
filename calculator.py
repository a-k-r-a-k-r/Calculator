'''
    Program: Calculator
    Author : akr
    GitHub : https://github.com/a-k-r-a-k-r
    Blog   : https://a-k-r-a-k-r.blogspot.com
'''

#Simple Calculator
import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL


#Defining colors and fonts
root_bg = "black"
button_bg = "black"
button_fg = "green"
display_bg = "green"
display_fg= "black"
button_font = ('Arial', 18)
display_font = ('Arial', 30)


#Defining window
root = tkinter.Tk()
root.title('Calculator')
root.iconbitmap('resources/icons/calculator.ico')
root.geometry('300x375')
root.resizable(0,0)
root.config(bg=root_bg)


#Define functions
def submit_number(number):
    display.insert(END, number)
    if "." in display.get():
        decimal_button.config(state=DISABLED)


def operate(operator):
    global first_number
    global operation
    operation = operator
    first_number = display.get()
    display.delete(0, END)
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)
    decimal_button.config(state=NORMAL)


def equal():
    if operation == 'add':
        value = float(first_number) + float(display.get())
    elif operation == 'subtract':
        value = float(first_number) - float(display.get())
    elif operation == 'multiply':
        value = float(first_number) * float(display.get())
    elif operation == 'divide':
        if display.get() == "0":
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())
    elif operation == 'exponent':
        value = float(first_number) ** float(display.get())

    display.delete(0, END)
    display.insert(0, value)
    enable_buttons()


def enable_buttons():
    decimal_button.config(state=NORMAL)
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state=NORMAL)


def clear():
    display.delete(0, END)
    enable_buttons()


def inverse():
    if display.get() == '0':
        value = 'ERROR'
    else:
        value = 1/float(display.get())

    display.delete(0, END)
    display.insert(0, value)


def square():
    value = float(display.get())**2
    display.delete(0, END)
    display.insert(0, value)


def find_negative():
    value = -1*float(display.get())
    display.delete(0, END)
    display.insert(0, value)


#Define frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg="black")
display_frame.pack(padx=0, pady=0)
button_frame.pack(padx=2, pady=5)


#Layout for the display frame
display = tkinter.Entry(display_frame, width=50, font=display_font, bg=display_bg,fg=display_fg,borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)


#Layout for the button frame
clear_button = tkinter.Button(button_frame, text="Clear", font=button_font,bg=button_bg,fg=button_fg, command=clear)
quit_button = tkinter.Button(button_frame, text="Quit", font=button_font,bg=button_bg,fg=button_fg, command=root.destroy)
inverse_button = tkinter.Button(button_frame, text='1/x', font=button_font,bg=button_bg,fg=button_fg, command=inverse)
square_button = tkinter.Button(button_frame, text='x^2', font=button_font,bg=button_bg,fg=button_fg, command=square)
exponent_button = tkinter.Button(button_frame, text='x^n', font=button_font,bg=button_bg,fg=button_fg, command=lambda:operate('exponent'))
divide_button = tkinter.Button(button_frame, text=' / ', font=button_font,bg=button_bg,fg=button_fg, command=lambda:operate('divide'))
multiply_button = tkinter.Button(button_frame, text='*', font=button_font,bg=button_bg,fg=button_fg, command=lambda:operate('multiply'))
subtract_button = tkinter.Button(button_frame, text='-', font=button_font,bg=button_bg,fg=button_fg, command=lambda:operate('subtract'))
add_button = tkinter.Button(button_frame, text='+', font=button_font, bg=button_bg,fg=button_fg,command=lambda:operate('add'))
equal_button = tkinter.Button(button_frame, text='=', font=button_font,bg=button_bg,fg=button_fg,command=equal)
decimal_button = tkinter.Button(button_frame, text='.', font=button_font, bg=button_bg,fg=button_fg, command=lambda:submit_number("."))
negate_button = tkinter.Button(button_frame, text='+/-', font=button_font, bg=button_bg,fg=button_fg, command=find_negative)
nine_button = tkinter.Button(button_frame, text='9', font=button_font, bg=button_bg,fg=button_fg, command=lambda:submit_number(9))
eight_button = tkinter.Button(button_frame, text='8', font=button_font, bg=button_bg,fg=button_fg, command=lambda:submit_number(8))
seven_button = tkinter.Button(button_frame, text='7', font=button_font, bg=button_bg,fg=button_fg, command=lambda:submit_number(7))
six_button = tkinter.Button(button_frame, text='6', font=button_font, bg=button_bg,fg=button_fg, command=lambda:submit_number(6))
five_button = tkinter.Button(button_frame, text='5', font=button_font, bg=button_bg,fg=button_fg, command=lambda:submit_number(5))
four_button = tkinter.Button(button_frame, text='4', font=button_font, bg=button_bg,fg=button_fg,command=lambda:submit_number(4))
three_button = tkinter.Button(button_frame, text='3', font=button_font,bg=button_bg,fg=button_fg, command=lambda:submit_number(3))
two_button = tkinter.Button(button_frame, text='2', font=button_font, bg=button_bg,fg=button_fg, command=lambda:submit_number(2))
one_button = tkinter.Button(button_frame, text='1', font=button_font,bg=button_bg,fg=button_fg, command=lambda:submit_number(1))
zero_button = tkinter.Button(button_frame, text='0', font=button_font, bg=button_bg,fg=button_fg, command=lambda:submit_number(0))


#First row
clear_button.grid(row=0, column=0, columnspan=2, pady=1, sticky="WE")
quit_button.grid(row=0, column=2, columnspan=2, pady=1, sticky="WE")
#Second row
inverse_button.grid(row=1, column=0, pady=1, sticky="WE")
square_button.grid(row=1, column=1, pady=1, sticky="WE")
exponent_button.grid(row=1, column=2, pady=1, sticky="WE")
divide_button.grid(row=1, column=3, pady=1, sticky="WE")
#Third row
seven_button.grid(row=2, column=0, pady=1, sticky="WE", ipadx=20)
eight_button.grid(row=2, column=1, pady=1, sticky="WE", ipadx=20)
nine_button.grid(row=2, column=2, pady=1, sticky="WE", ipadx=20)
multiply_button.grid(row=2, column=3, pady=1, sticky="WE", ipadx=20)
#Fourth row
four_button.grid(row=3, column=0, pady=1, sticky="WE")
five_button.grid(row=3, column=1, pady=1, sticky="WE")
six_button.grid(row=3, column=2, pady=1, sticky="WE")
subtract_button.grid(row=3, column=3, pady=1, sticky="WE")
#Fifth row
one_button.grid(row=4, column=0, pady=1, sticky="WE")
two_button.grid(row=4, column=1, pady=1, sticky="WE")
three_button.grid(row=4, column=2, pady=1, sticky="WE")
add_button.grid(row=4, column=3, pady=1, sticky="WE")
#Sixth row
negate_button.grid(row=5, column=0, pady=1, sticky="WE")
zero_button.grid(row=5, column=1, pady=1, sticky="WE")
decimal_button.grid(row=5, column=2, pady=1, sticky="WE")
equal_button.grid(row=5, column=3, pady=1, sticky="WE")


#Run the root window's main loop
root.mainloop()