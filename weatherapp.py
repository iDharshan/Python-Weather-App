import tkinter as tk

import requests

HEIGHT= 500
WIDTH= 600

#d1529082aa9e27fbe1923128093a9bf2
#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={your api key}
def get_weather(city):
    weather_key='d1529082aa9e27fbe1923128093a9bf2'
    url='https://pro.openweathermap.org/data/2.5/forecast/weather
    '
    params={'appid': weather_key,'q':city,'units':'metric'}
    response= requests.get(url, params=params)
    print(response.json())

root = tk.Tk()

canvas= tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image= tk.PhotoImage(file='landscape.png')
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)


frame = tk.Frame(root,bg="#b3b3b3",bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

button = tk.Button(frame,text="Get Weather",font=40, command= lambda: get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

entry=tk.Entry(frame,font=40,bg="white")
entry.place(relwidth=0.65,relheight=1)

lower_frame=tk.Frame(root,bg='#b3b3b3',bd=5)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label= tk.Label(lower_frame)
label.place(relwidth=1,relheight=1)


root.mainloop()
