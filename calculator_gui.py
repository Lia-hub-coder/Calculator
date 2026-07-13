import tkinter as tk
window=tk.Tk()
window.title("CALCULATOR")
display=tk.Entry(window)
display.pack()
def click_one():
    display.insert(tk.END, '1')
one=tk.Button(window,text='1', command=click_one)

one.pack()
window.mainloop()