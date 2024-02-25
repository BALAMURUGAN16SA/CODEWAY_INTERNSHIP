import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
import requests
import datetime as dt
from datetime import datetime, timedelta
import time
from PIL import ImageTk, Image

windows = ttk.Window(themename = 'solar')
windows.title('WEATHER FORECAST')
windows.geometry('800x300')

main_lst = ['Clear','Clouds','Rain','Drizzle','Thuderstorm','Snow','Mist','Smoke','Haze','Dust','Fog']

img1 = Image.open('Clear.png').resize((75,75))
img2 = Image.open('Clouds.png').resize((75,75))
img3 = Image.open('Rain_2.png').resize((75,75))
img4 = Image.open('Drizzle.png').resize((75,75))
img5 = Image.open('Thunderstorm.png').resize((75,75))
img6 = Image.open('Snow.png').resize((75,75))
img7 = Image.open('Mist.png').resize((75,75))
img8 = Image.open('Fog.png').resize((75,75))
img9 = Image.open('Haze.png').resize((75,75))
img10 = Image.open('Dust.png').resize((75,75))
img11 = Image.open('Fog.png').resize((75,75))
weathers = {
    'Clear' : ImageTk.PhotoImage(img1),
    'Clouds' : ImageTk.PhotoImage(img2),
    'Rain' : ImageTk.PhotoImage(img3),
    'Drizzle' : ImageTk.PhotoImage(img4),
    'Thunderstorm' : ImageTk.PhotoImage(img5),
    'Snow' : ImageTk.PhotoImage(img6),
    'Mist' : ImageTk.PhotoImage(img7),
    'Smoke' : ImageTk.PhotoImage(img8),
    'Haze' : ImageTk.PhotoImage(img9),
    'Dust' : ImageTk.PhotoImage(img10),
    'Fog' : ImageTk.PhotoImage(img11)
}
    
tlst = []
wlst = []
def func(city):

    try:
        API = '2f44aef9a2277fe209f75cfbaa66025a'
        CITY = city

        BASE2 =  "http://api.openweathermap.org/data/2.5/weather?"
        url2 = BASE2 + 'appid=' + API + '&q=' + CITY
        response2 = requests.get(url2).json()
        now = response2['main']['temp']
        tlst.append(now)

        BASE1 =  "http://api.openweathermap.org/data/2.5/forecast?"
        url1 = BASE1 + 'appid=' + API + '&q=' + CITY
        response1 = requests.get(url1).json()
        inc = 1
        target_d = datetime.today().date() + timedelta(days = inc)
              
        for day in range(4):
        
            target_d = datetime.today().date() + timedelta(days = inc)
            time_now = datetime.now().strftime("%H:%M:%S")
            va = (((str(time_now)).split(':')))
            v = ''
            for i in range(3,25,3):
                if(int(va[0]) < i):
                    x = i-3
                    break
            if(len(str(x)) == 2):
                v += str(x) + ':' + '00' + ':' + '00'
            else:
                v += '0' + str(x) + ':' + '00' + ':' + '00'

            target_t = v

            for i in response1['list']:
                if((str(target_d) in i['dt_txt']) and (str(target_t) in i['dt_txt'])):
                    tlst.append(i['main']['temp'])
                    
            inc += 1
        #3
        label3['text'] = str(round(tlst[0] - 273.15, 3)) + ' ' + chr(176) + str('C')
        label6['text'] = str(round(tlst[1] - 273.15, 3)) + ' ' + chr(176) + str('C')
        label9['text'] = str(round(tlst[2] - 273.15, 3)) + ' ' + chr(176) + str('C')
        label12['text'] = str(round(tlst[3] - 273.15, 3)) + ' ' + chr(176) + str('C')
        label15['text'] = str(round(tlst[4] - 273.15, 3)) + ' ' + chr(176) + str('C')
        tlst.clear()

        #2
        tod = datetime.now().date()
        label2['text'] = 'Today'
        label5['text'] = 'Tomorrow'
        tom = tod + timedelta(days = 2)
        dow = tom.strftime('%A')
        label8['text'] = str(dow)
        tom = tod + timedelta(days = 3)
        dow = tom.strftime('%A')
        label11['text'] = str(dow)
        tom = tod + timedelta(days = 4)
        dow = tom.strftime('%A')
        label14['text'] = str(dow)

        #1
        def img(a):
            target_d = datetime.today().date() + timedelta(days = a)
            for i in response1['list']:
                if((str(target_d) in i['dt_txt']) and (str(target_t) in i['dt_txt'])):
                    k = i['weather']
                    wlst.append(k[0]['main'])
                    return weathers[k[0]['main']], k[0]['main']

        label1['image'] = (img(0))[0]
        label4['image'] = (img(1))[0]
        label7['image'] = (img(2))[0]
        label10['image'] = (img(3))[0]
        label13['image'] = (img(4))[0]

        label1a['text'] = (img(0))[1]
        label4a['text'] = (img(1))[1]
        label7a['text'] = (img(2))[1]
        label10a['text'] = (img(3))[1]
        label13a['text'] = (img(4))[1]

        wlst.clear()
        
    except:
        tv.set('Invalid Place / Poor Internet')
                   
#OUTLINE
main_box1 = ttk.Frame(windows, borderwidth = 1, relief = 'solid')
main_box1.place(relx = 0.5, rely = 0.5,relwidth = 0.95, relheight = 0.9, anchor = 'center')

tv = tk.StringVar()
search = ttk.Entry(main_box1, textvariable =tv)
search.place(relx = 0.715, rely = 0.07, relwidth = 0.27, relheight = 0.1)

def on_enter(event=None):
    go.invoke()
go = ctk.CTkButton(search, text = 'GO', command = lambda : func(search.get()))
go.place(relx = 0.8, rely = 0.0, relwidth = 0.2, relheight = 1, anchor = 'nw')
search.bind("<Return>", on_enter)


today = ttk.Frame(main_box1, borderwidth = 2, relief = 'solid')
today.place(relx = 0.15, rely = 0.5, relwidth = 0.20, relheight = 0.9, anchor = 'center')



label1 = ttk.Label(today, image = '', borderwidth =1, relief = 'solid', anchor = 'center' ,justify = 'center')
label1a = ttk.Label(today, text = '', borderwidth = 1, relief = 'solid', anchor = 'center' ,justify = 'center')
label2 = ttk.Label(today, text = '', borderwidth = 1, relief = 'solid', anchor = 'center' ,justify = 'center')
label3 = ttk.Label(today, text = '', borderwidth = 1, relief = 'solid', anchor = 'center' ,justify = 'center')
today.rowconfigure(0, weight = 3)
today.rowconfigure(1, weight = 1)
today.rowconfigure(2, weight = 1)
today.rowconfigure(3, weight = 1)
today.columnconfigure(0, weight = 1)
label1.grid(row = 0, column = 0, sticky = 'news')
label1a.grid(row = 1, column = 0, sticky = 'news')
label2.grid(row = 2, column = 0, sticky = 'news')
label3.grid(row = 3, column = 0, sticky = 'news')

day_n1 = ttk.Frame(main_box1, borderwidth = 2, relief = 'solid')
day_n1.place(relx = 0.37, rely = 0.6, relwidth = 0.15, relheight = 0.65, anchor = 'center')
label4 = ttk.Label(day_n1,image = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label4a = ttk.Label(day_n1, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label5 = ttk.Label(day_n1, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label6 = ttk.Label(day_n1, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
day_n1.rowconfigure(0, weight = 3)
day_n1.rowconfigure(1, weight = 1)
day_n1.rowconfigure(2, weight = 1)
day_n1.rowconfigure(3, weight = 1)
day_n1.columnconfigure(0, weight = 1)
label4.grid(row = 0, column = 0, sticky = 'news')
label4a.grid(row = 1, column = 0, sticky = 'news')
label5.grid(row = 2, column = 0, sticky = 'news')
label6.grid(row = 3, column = 0, sticky = 'news')

day_n2 = ttk.Frame(main_box1, borderwidth = 2, relief = 'solid')
day_n2.place(relx = 0.55, rely = 0.6, relwidth = 0.15, relheight = 0.65, anchor = 'center')
label7 = ttk.Label(day_n2, image = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label7a = ttk.Label(day_n2, text = '', borderwidth = 2, relief = 'solid',anchor = 'center' ,justify = 'center')
label8 = ttk.Label(day_n2, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label9 = ttk.Label(day_n2, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
day_n2.rowconfigure(0, weight = 3)
day_n2.rowconfigure(1, weight = 1)
day_n2.rowconfigure(2, weight = 1)
day_n2.rowconfigure(3, weight = 1)
day_n2.columnconfigure(0, weight = 1)
label7.grid(row = 0, column = 0, sticky = 'news')
label7a.grid(row = 1, column = 0, sticky = 'news')
label8.grid(row = 2, column = 0, sticky = 'news')
label9.grid(row = 3, column = 0, sticky = 'news')


day_n3 = ttk.Frame(main_box1, borderwidth = 2, relief = 'solid')
day_n3.place(relx = 0.73, rely = 0.6, relwidth = 0.15, relheight = 0.65, anchor = 'center')
label10 = ttk.Label(day_n3, image = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label10a = ttk.Label(day_n3, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label11 = ttk.Label(day_n3, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label12 = ttk.Label(day_n3, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
day_n3.rowconfigure(0, weight = 3)
day_n3.rowconfigure(1, weight = 1)
day_n3.rowconfigure(2, weight = 1)
day_n3.rowconfigure(3, weight = 1)
day_n3.columnconfigure(0, weight = 1)
label10.grid(row = 0, column = 0, sticky = 'news')
label10a.grid(row = 1, column = 0, sticky = 'news')
label11.grid(row = 2, column = 0, sticky = 'news')
label12.grid(row = 3, column = 0, sticky = 'news')


day_n4 = ttk.Frame(main_box1, borderwidth = 2, relief = 'solid')
day_n4.place(relx = 0.91, rely = 0.6, relwidth = 0.15, relheight = 0.65, anchor = 'center')
label13 = ttk.Label(day_n4, image = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label13a = ttk.Label(day_n4, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label14 = ttk.Label(day_n4, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
label15 = ttk.Label(day_n4, text = '', borderwidth = 2, relief = 'solid', anchor = 'center' ,justify = 'center')
day_n4.rowconfigure(0, weight = 3)
day_n4.rowconfigure(1, weight = 1)
day_n4.rowconfigure(2, weight = 1)
day_n4.rowconfigure(3, weight = 1)
day_n4.columnconfigure(0, weight = 1)
label13.grid(row = 0, column = 0, sticky = 'news')
label13a.grid(row = 1, column = 0, sticky = 'news')
label14.grid(row = 2, column = 0, sticky = 'news')
label15.grid(row = 3, column = 0, sticky = 'news')


windows.mainloop()
