import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

windows = ttk.Window(themename = 'superhero')
windows.geometry('550x350')
windows.title('CALCULATOR')

def func():
    i1 = v1.get()
    i2 = v2.get()
    o = v3.get()
    a = 0
    try:
        match o:
            case '+':
                a += i1 + i2
            case '-':
                a += i1 - i2
            case '*':
                a += i1 * i2
            case '/':
                a += i1 / i2
            case '//':
                a += i1 // i2
            case '^':
                a += i1 ** i2
            case '%':
                a += (i1*i2)/100
        v4.set(a)
        
    except:
         v4.set('ERROR')   
    
label1 = ttk.Label(windows, text = '', borderwidth = 1, relief = 'solid')
label2 = ttk.Label(windows, text = '', borderwidth = 1, relief = 'solid')
windows.rowconfigure(0, weight = 4)
windows.rowconfigure(1, weight = 1)
windows.columnconfigure(0, weight = 1)
label1.grid(row = 0, column = 0, sticky = 'news')
label2.grid(row = 1, column = 0, sticky = 'news')

frame1 = ttk.Frame(label1, borderwidth = 3, relief = 'solid')
frame2 = ttk.Frame(label2, borderwidth = 3, relief = 'solid')
frame1.place(relx = 0.5, rely = 0.5, relwidth = 0.8, relheight = 0.8, anchor = 'center')
frame2.place(relx = 0.5, rely = 0.5, relwidth = 0.8, relheight = 0.8, anchor = 'center')

v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.StringVar()
input1 = ttk.Label(frame1, text = 'INPUT 1  : ')
input2 = ttk.Label(frame1, text = 'INPUT 2  : ')
operat = ttk.Label(frame1, text = 'OPERATOR : ')

sp1 = ttk.Spinbox(frame1, from_ = -9999999999, to = 999999999, textvariable = v1)
sp2 = ttk.Spinbox(frame1, from_ = -9999999999, to = 999999999, textvariable = v2)
cb = ttk.Combobox(frame1, values = ('+', '-', '*', '/', '//', '^', '%'), textvariable = v3)
ev = ttk.Button(frame1, text = 'EVAL', command = func)
def on_enter(event=None):
    ev.invoke()
windows.bind("<Return>", on_enter)

input1.place(relx = 0.2, rely = 0.2, relwidth = 0.5, relheight = 0.1)
input2.place(relx = 0.2, rely = 0.4, relwidth = 0.5, relheight = 0.1)
operat.place(relx = 0.2, rely = 0.6, relwidth = 0.5, relheight = 0.1)
sp1.place(relx = 0.4, rely = 0.2, relwidth = 0.4, relheight = 0.15)
sp2.place(relx = 0.4, rely = 0.4, relwidth = 0.4, relheight = 0.15)
cb.place(relx = 0.4, rely = 0.6, relwidth = 0.4, relheight = 0.15)
ev.place(relx = 0.82, rely = 0.6, relwidth = 0.15, relheight = 0.16)

v4 = tk.StringVar()
label3 = ttk.Label(frame2, borderwidth = 2, relief = 'solid', textvariable = v4)
label3.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 0.5, anchor = 'center')

windows.mainloop()
