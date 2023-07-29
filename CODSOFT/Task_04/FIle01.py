from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests



#api_key='42950206f34d6dd7f5953585694bda18'
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


config_file= 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['weather']['api']

def get_weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        json = result.json()
        
        city = json['name']
        country = json['sys']['country']
        temp_kel = json['main']['temp']
        temp_cel = temp_kel-273.15
        temp_fah = (temp_kel-273.15)*9/5+32
        weather = json['weather'][0]['main']
        final = (city,country,temp_kel,temp_cel,temp_fah,weather)
        return final
    else:
        return None
    

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{},{}'.format(weather[0],weather[1])
        temp_lbl['text'] = 'Celcius : {:.2f}°C      Farenheit : {:.2f}°F'.format(weather[3],weather[4])
        weather_lbl['text']= weather[5]
    else:
        messagebox.showerror("Error","Cannot Find City {}".format(city))

#Start
app = Tk()
app.title("Weather Forecasting")
app.geometry('800x400+370+190')
app.configure(bg="#cce6ff")


Heading= Label(app, text="Weather Forecasting", font=('Helvetica', 25, 'bold'), bg="#cce6ff")
Heading.pack(pady=5)

city_text=StringVar()
city_entry= Entry(app,textvariable=city_text,width=29)
city_entry.pack(padx=20, pady=15)

search_button = Button(app,text="Search", width=15,command=search, font=('Helvetica', 8))
search_button.pack()

location_lbl= Label(app, text="", font=('Helvetica', 20, 'bold'),bg='#cce6ff')
location_lbl.pack(pady=5)

temp_lbl = Label(app,text="",font=('Arial', 13, 'bold'),bg='#cce6ff')
temp_lbl.pack(pady=4)

weather_lbl = Label(app,text="",font=('Arial', 10),bg='#cce6ff')
weather_lbl.pack()

app.mainloop()

