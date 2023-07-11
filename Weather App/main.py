# Importing Libraries and Dependencies
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        
        timezone.config(text=result)
        day.config(text=local_time.strftime("%A"))
        long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

        # Weather
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a1fe52f10976aa85fe44098b91184502"

        
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=(wind,"m/s"))
        h.config(text=(humidity,"%"))
        d.config(text=description)
        p.config(text = (pressure,"hPa"))
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!!")

# Creating window
window = Tk()
window.title("Weather App by V")
image = PhotoImage(file="images\\weather_logo.png")
window.iconphoto(False,image)

window.geometry("900x500+300+200")
window.resizable(False,False)

# Search Box for entering city name
search_image = PhotoImage(file="images\\search.png")
myimage = Label(image=search_image)
myimage.place(x=20,y=20)

textfield = tk.Entry(window,justify="center",width=16,font=("poppins",25,"bold"),bg = "#404040",border =0,fg="white")
textfield.place(x=60,y=40)
textfield.focus()

search_icon = PhotoImage(file="images\\search_icon.png")
myimage_icon = Button(image=search_icon,border=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

# Logo
logo_image = PhotoImage(file="images\\weather_logo(1).png")
logo = Label(image = logo_image)
logo.place(x=210,y=130)


# Bottom Box
frame_image = PhotoImage(file="images\\box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

# Time
name = Label(window,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(window,font=("Helvetica",20,"bold"))
clock.place(x=30,y=130)
day = Label(window,font=("Helvetica",20,"bold"))
day.place(x=30,y=160)

# Timezone
timezone = Label(window,font=("Helvetica",20,"bold"),fg = "black")
timezone.place(x=570,y=70)

long_lat = Label(window,font=("Helvetica",10),fg = "black")
long_lat.place(x=595,y=100)

# Label
label_1 = Label(window,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef",borderwidth=2,relief="solid")
label_1.place(x=120,y=400)

label_2 = Label(window,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef",borderwidth=2,relief="solid")
label_2.place(x=250,y=400)

label_3 = Label(window,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef",borderwidth=2,relief="solid")
label_3.place(x=430,y=400)

label_4 = Label(window,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef",borderwidth=2,relief="solid")
label_4.place(x=650,y=400)

t = Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c = Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w = Label(text=" ... ",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=115,y=430)

h = Label(text=" ... ",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=262,y=430)

d = Label(text=" ... ",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=445,y=430)

p = Label(text=" ... ",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=675,y=430)



window.mainloop()

