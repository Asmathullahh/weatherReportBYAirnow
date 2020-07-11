from tkinter import *
from PIL import ImageTk,Image
import requests
import json


root=Tk()
root.title("WEATHER REPORT")
root.iconbitmap("Martz90-Hex-Weather.ico")
root.geometry("1080x120")
def clear():
    root.configure(background="black")
    mylabel.destroy()
    
def zipsearch():
    z=zip.get()
    try:
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(z) + "&distance=15&API_KEY=2C331F17-791F-40BC-8ED2-C6F245FC1276")
        api=json.loads(api_request.content)
        date=api[0]['DateObserved']
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        global category
        category=api[0]['Category']['Name']
        hour=api[0]['HourObserved']
        timezone=api[0]['LocalTimeZone']
    except Exception as e:
        api="Error.. reload page again!"
        mylabel2=Label(root,text="Enter a valid AMERICAN zipcode",font=("monospace",50),fg="red",bg="black").grid(row=2,column=1,columnspan=2)
    global x
    global y
    if category=="Good":
        x="#00e400"
        y="black"
    elif category=="Moderate":
        y="black"
        x="#ffff00"
    elif category=="Unhealthy for Sensitive Groups":
        y="black"
        x="#ff7e00"
    elif category=="Unhealthy":
        y="black"
        x="#ff0000"
    elif category=="Very Unhealthy":
        y="red"
        x="#8f3f97"
    elif category=="Hazarduos":
        y="red"
        x="#7e0023"
    elif category=="Unavailable":
        y="red"
        x="black"
    else:
        y="black"
        x="black"
        Label(root,text="404 Error occured...!",font=("monospace",50),fg="#00e400",bg="black").grid(row=1,column=1,columnspan=2)

    stringe=str(city + "  " + "AirQuality is " + str(quality)+"  "+ category+"  on  "+date+" "+str(hour)+":00 "+ timezone)
    global mylabel
    mylabel=Label(root,text=stringe,font=("monospace",20),fg=y,bg=x)
    mylabel.grid(row=2,column=1)

    root.configure(background=x)
    menu=Button(root,text="Clear Screen",bg="black",fg="red",bd=5,command=clear).grid(row=0,column=4)
zip=Entry(root,width=50,bd=5,fg="#00e400",bg="black")
zip.grid(row=0,column=0,columnspan=2)
exits=Button(root,text="EXIT!",fg="red",bg="black",bd=5,command=root.destroy).grid(row=0,column=3)
zipbutton=Button(root,text="search for a zipcode",bg="black",fg="red",bd=5,command=zipsearch).grid(row=0,column=2)
root.configure(background="black")
root.mainloop()
