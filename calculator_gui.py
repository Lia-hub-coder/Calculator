import tkinter as tk
window=tk.Tk()
window.title("CALCULATOR")
display=tk.Entry(window)
one=tk.Button(window,text='1')
display.pack()
one.pack()
window.mainloop()