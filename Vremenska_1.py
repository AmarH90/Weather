import tkinter as tk
import time 
from tkinter import *
import tkinter.font as font
import requests
from bs4 import BeautifulSoup as B_soup

url = "https://freemeteo.com.hr/vrijeme/sarajevo/trenutno-vrijeme/mjesto/?gid=3191281&language=croatian&country=bosnia-and-herzegovina"
result = requests.get(url)
print(result.status_code)
data = result.content
soup = B_soup(data,"html.parser")
print(soup.prettify())

test = soup.find(id="current-weather")
print(test.text)
show_1 = test.text



window = tk.Tk()
window.attributes("-fullscreen", True)
window["background"]="#856ff8"
window.title("Vremenska prognoza")
label = tk.Label(window, text="vrjeme danas ")
label.pack()

myFont = font.Font(family="Helvetica")

btn = Button(window, text = "Close me!!!",bg="#0052cc", fg="#ffffff" ,bd = "5", command = window.destroy)
btn["font"] = myFont
btn.pack(side=BOTTOM)

def toggleText():
    if(btn_2["text"]=="Submit"):
        btn_2["text"]="Submitted"
        btn_2["fg"]="Yellow"
        bla = Label(text=show_1, fg="#0052cc")
        bla.place(x=500, y=200)
    else:
        btn_2["text"]="Submit"
        btn_2["fg"]="#ffffff"
        
            
        
btn_2 = Button(window, text="Submit", bg="#0052cc",fg="#ffffff", command = toggleText)
btn_2["font"]= myFont

btn_2.pack(side=BOTTOM)
window.mainloop()


    


