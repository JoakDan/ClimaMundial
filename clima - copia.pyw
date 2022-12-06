from tkinter import *
import requests
#b3071c93b59a876745e3622b20f8b140
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
def mostrar_respuesta(clima):
    nombre_ciudad = clima["name"]
    desc = clima["weather"][0]["description"]
    temp = clima["main"]["temp"]
    
    
    ciudad["text"] = nombre_ciudad
    temperatura["text"] = temp
    descripcion["text"] = desc
    
    
   
def clima_JSON(ciudad):
    API_key = "b3071c93b59a876745e3622b20f8b140"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {"APPID": API_key, "q": ciudad, "units": "metric"}
    response =requests.get(URL, params = parametros)
    clima = response.json()   
    print(response.json())
    
    mostrar_respuesta(clima)
   
    print(clima["name"])
    print(clima["weather"][0]["description"])
    print(clima["main"]["temp"])
def click(event):
    texto_ciudad.config(state=NORMAL)
    texto_ciudad.delete(0,END)    
ventana = Tk()
ventana.title("Clima Mundial")
ventana.iconbitmap(r"C:\Users\PC\Desktop\developer\sol.ico")
ventana.geometry("350x400")
ventana.config(bg="lightblue")
texto_ciudad = Entry(ventana, font=("Courier", 20, "normal"), justify= "center")
texto_ciudad.insert(0,"Ciudad")
texto_ciudad.config(state=DISABLED)
texto_ciudad.bind("<Button-1>",click)
texto_ciudad.pack(padx = 30, pady = 30)


obtener_clima = Button(ventana,cursor="hand2", bg="beige",fg="lightcoral", text= "Obtener Clima", font=("Courier", 20, "normal"), command= lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad= Label(background=("lightblue"),font= ("Courier", 20, "normal"))
ciudad.pack(padx=20, pady=20)

temperatura= Label(background=("lightblue"), font= ("Courier", 50, "normal"))
temperatura.pack(padx=10, pady=10)

descripcion= Label(background=("lightblue"), font= ("Courier", 20, "normal"))
descripcion.pack(padx=10, pady=10)
ventana.mainloop()