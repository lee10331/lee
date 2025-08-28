from tkinter import *

# Window setup
window = Tk()
window.geometry('300x400')
window.title('Calculator')

# Entry box
e = Entry(window, width=20, borderwidth=5, font=("Arial", 18), justify="right")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(num))

def clear():
    e.delete(0, END)

def calculate():
    try:
        result = eval(e.get())   # Evaluates the entered expression
        e.delete(0, END)
        e.insert(0, str(result))
    except:
        e.delete(0, END)
        e.insert(0, "Error")

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        Button(window, text=text, width=10, height=2, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(window, text=text, width=10, height=2, command=lambda t=text: click(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
Button(window, text="C", width=10, height=2, command=clear).grid(row=5, column=0, columnspan=4, pady=5)

mainloop()
