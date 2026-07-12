import tkinter as tk
window=tk.Tk()
window.title("CALCULATOR")
display=tk.Entry(window)
one=tk.Button(window,text='1')
display.pack()
one.pack()
def click_one():
    display.insert(tk.END, "1",command=click_one)
window.mainloop()