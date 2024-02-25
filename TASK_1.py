import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

ind = 0

windows = ttk.Window(themename = 'c2')
windows.geometry('1000x600')
windows.title('TO-DO-LIST')

windows.rowconfigure(0, weight = 1)
windows.columnconfigure(0, weight = 1)
frame_tab = ttk.Frame(windows, borderwidth = 2, relief = 'solid')
frame_tab.grid(row = 0, column = 0, sticky = 'news')
tab = ttk.Notebook(frame_tab, bootstyle = 'danger')
tab1 = ttk.Frame(tab)
tab2 = ttk.Frame(tab)
tab3 = ttk.Frame(tab)

tab.add(tab1, text = 'ADD')
tab.add(tab2, text = 'COMPLETED')
tab.add(tab3, text = 'DELETED')
tab.place(relx = 0.5, rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')

#tab1
frame_enter = ttk.Frame(tab1, borderwidth = 2, relief = 'solid')
frame_avail_1 = ttk.Frame(tab1, borderwidth = 2, relief = 'solid')
frame_action = ttk.Frame(tab1, borderwidth = 2, relief = 'solid')

tab1.rowconfigure(0, weight = 2)
tab1.rowconfigure(1, weight = 3)
tab1.rowconfigure(2, weight = 2)
tab1.columnconfigure(0, weight = 1)

frame_enter.grid(row = 0, column = 0, sticky = 'news')
frame_avail_1.grid(row = 1, column = 0, sticky = 'news')
frame_action.grid(row = 2, column = 0, sticky = 'news')

#tab2
lab2 = ttk.Label(tab2, text = 'COMPLETED TASKS', borderwidth = 2, relief = 'solid', justify = 'center', anchor = 'center',font = ("Verdana", 16))
frame_avail_2 = ttk.Frame(tab2, borderwidth = 2, relief = 'solid')
tab2.rowconfigure(0, weight = 2)
tab2.rowconfigure(1, weight = 10)
tab2.columnconfigure(0, weight = 1)
lab2.grid(row = 0, column = 0, sticky = 'news')
frame_avail_2.grid(row = 1, column = 0, sticky = 'news')

#tab3
lab3 = ttk.Label(tab3, text = 'DELETED TASKS', borderwidth = 2, relief = 'solid', justify = 'center', anchor = 'center', font = ("Verdana", 16))
frame_avail_3 = ttk.Frame(tab3, borderwidth = 2, relief = 'solid')
tab3.rowconfigure(0, weight = 2)
tab3.rowconfigure(1, weight = 10)
tab3.columnconfigure(0, weight = 1)
lab3.grid(row = 0, column = 0, sticky = 'news')
frame_avail_3.grid(row = 1, column = 0, sticky = 'news')

def add():
    global ind
    ind = ind+1
    task = entry1_value.get()
    status = 'INCOMPLETE'

    table_down_1.insert(parent = '', index = tk.END, values = (ind, task, status))

t3i = 1
def delete():
    global ind
    global t3i
    j = 1
    
    for i in table_down_1.selection():
        row = list(table_down_1.item(i,'values'))
        row[0] = t3i
        t3i += 1
        table_down_3.insert(parent = '', index = tk.END, values = row)
        
        table_down_1.delete(i)
        ind -= 1
        
    ii = table_down_1.get_children()
    for i in ii:
        row = (table_down_1.item(i,'values'))
        updated = (j, row[1], row[2])
        table_down_1.item(i, values = updated)
        
        j += 1

t2i = 1
def complete():
    global t2i
    ii = table_down_1.selection()
    
    for i in ii:
        row = table_down_1.item(i, 'values')
        updated = (row[0], row[1], 'COMPLETED')
        table_down_1.item(i, values = updated)

    updated_new = (t2i, row[1], 'COMPLETED')
    table_down_2.insert(parent = '', index = tk.END, values = updated_new)
    t2i += 1

    sf = table_down_1.focus()
    if(table_down_1.item(sf)['values'][2] == 'COMPLETED'):
        button_cmp.configure(state = tk.DISABLED)

def on_select(event):
    try:
        sf = table_down_1.focus()
        if(table_down_1.item(sf)['values'][2] == 'INCOMPLETE'):
            button_cmp.configure(state = tk.NORMAL)

        elif(table_down_1.item(sf)['values'][2] == 'COMPLETED'):
            button_cmp.configure(state = tk.DISABLED)
    except:
        None
        
entry1_value = tk.StringVar()
entry1 = ctk.CTkEntry(frame_enter, textvariable = entry1_value)
entry1.place(relx = 0.5, rely = 0.3, relwidth = 0.5, relheight = 0.3, anchor = 'center')
button1 = ctk.CTkButton(frame_enter, text = 'ADD', command = add, fg_color= '#008262')
button1.place(relx = 0.5, rely = 0.7, relwidth = 0.1, relheight = 0.3, anchor = 'center')
def on_enter(event=None):
    button1.invoke()
windows.bind("<Return>", on_enter)

table_down_1 = ttk.Treeview(frame_avail_1, columns = ('SNO', 'TASK', 'STATUS'), show = 'headings', bootstyle = 'danger')
table_down_1.column("SNO", anchor = tk.CENTER)
table_down_1.column("TASK",  anchor = tk.CENTER)
table_down_1.column("STATUS", anchor = tk.CENTER)

table_down_1.heading('SNO', text = 'SERIAL_NUMBER')
table_down_1.heading('TASK', text = 'TASKS')
table_down_1.heading('STATUS', text = 'STATUS')
table_down_1.pack(fill = 'both', expand = 'True')

table_down_1.bind("<<TreeviewSelect>>", on_select)

button_del = ctk.CTkButton(frame_action, text = 'DELETE', command = delete, fg_color= '#008262')
button_del.place(relx = 0.3, rely = 0.5, relwidth = 0.2, relheight = 0.3, anchor = 'center')
button_cmp = ctk.CTkButton(frame_action, text = 'COMPLETED', command = complete, fg_color= '#008262')
button_cmp.place(relx = 0.7, rely = 0.5, relwidth = 0.2, relheight = 0.3, anchor = 'center')

table_down_2 = ttk.Treeview(frame_avail_2, columns = ('SNO', 'TASK', 'STATUS'), show = 'headings', bootstyle = 'danger')
table_down_2.column("SNO", anchor = tk.CENTER)
table_down_2.column("TASK",  anchor = tk.CENTER)
table_down_2.column("STATUS", anchor = tk.CENTER)

table_down_2.heading('SNO', text = 'SERIAL_NUMBER')
table_down_2.heading('TASK', text = 'TASKS')
table_down_2.heading('STATUS', text = 'STATUS')
table_down_2.pack(fill = 'both', expand = 'True')

table_down_3 = ttk.Treeview(frame_avail_3, columns = ('SNO', 'TASK', 'STATUS'), show = 'headings', bootstyle = 'danger')
table_down_3.column("SNO", anchor = tk.CENTER)
table_down_3.column("TASK",  anchor = tk.CENTER)
table_down_3.column("STATUS", anchor = tk.CENTER)

table_down_3.heading('SNO', text = 'SERIAL_NUMBER')
table_down_3.heading('TASK', text = 'TASKS')
table_down_3.heading('STATUS', text = 'STATUS')
table_down_3.pack(fill = 'both', expand = 'True')
windows.mainloop()
