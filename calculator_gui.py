import tkinter as tk

window.title("CALCULATOR")
display=tk.Entry(window)
display.pack()
first_number = None
second_number=None
operator = None
def click(value):
    display.insert(tk.END, f"{value}")
zero=tk.Button(window,text='0', command=lambda:click(0))
one=tk.Button(window,text='1', command=lambda:click(1))
two=tk.Button(window,text='2', command=lambda:click(2))
three=tk.Button(window,text='3', command=lambda:click(3))
four=tk.Button(window,text='4', command=lambda:click(4))
five=tk.Button(window,text='5', command=lambda:click(5))
six=tk.Button(window,text='6', command=lambda:click(6))
seven=tk.Button(window,text='7', command=lambda:click(7))
eight=tk.Button(window,text='8', command=lambda:click(8))
nine=tk.Button(window,text='9', command=lambda:click(9))
zero.pack(); one.pack(); two.pack(); three.pack();four.pack();five.pack()
six.pack();seven.pack();eight.pack();nine.pack()
def operator_click(op):
    global first_number
    first_number=display.get()
    first_number=int(first_number)
    display.delete(0,tk.END)
    global operator
    operator=op
def equal_click():
    global second_number
    second_number=display.get()
    second_number=int(second_number)
    print(second_number)
equal=tk.Button(window, text="=", command=lambda:equal_click())
plus=tk.Button(window,text='+', command=lambda:operator_click ("+"))
plus.pack()
equal.pack()
window.mainloop()