import tkinter as tk
from tkinter.constants import COMMAND
from typing import Collection
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Variable, ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from numpy.core.fromnumeric import var



#Definicion de funciones Solucion de ecuaciones

def eulerAdelante():
    print("Euler Adelante")

def eulerAtras():
    print("Euler Atras")

def eulerModificado():
    print("Euler Modificado")

def RK2():
    print("Runge kunta 2")

def RK4():
    print("Runge kunta 4")

#Funcion para cerrar ventana
def CerrarAplicacion():
    MsgBox = tk.messagebox.askquestion ('Cerrar Aplicación','¿Está seguro que desea cerrar la aplicación?', icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()
    else:
        tk.messagebox.showinfo('Retornar','Será retornado a la aplicación')
        
def grafica():

    fig = plt.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(float(inicial.get()),float(final.get()), 0.01)
    ax = fig.add_subplot(111)
    ax.set_xlabel("days")
    ax.set_ylabel("Population Ratio")
    ax.plot() 

    if sT.get() :
        ax.plot(t,np.sin(t))
    if eT.get():
        ax.plot(t,np.cos(t))
    if iT.get():
        ax.plot(t,np.sin(t)+np.cos(t))
    if rT.get():
        ax.plot(t,np.sin(t)-np.cos(t))
    if pT.get():
        ax.plot(t,np.sin(t)+2*np.cos(t))

   
    plt.close()
    plt.style.use('seaborn-darkgrid')
    Plot = FigureCanvasTkAgg(fig, master=window)
    Plot.draw()

    #toolbar = NavigationToolbar2Tk(Plot, window)
    #toolbar.update()
    Plot.get_tk_widget().place(x=50,y=30)

    #def on_key_press(event):
    #    print("you pressed {}".format(event.key))
    #    key_press_handler(event, Plot, toolbar)
    #Plot.mpl_connect("key_press_event", on_key_press)




#Definición del lienzo de ejecucion para proyecto final
window = tk.Tk()

#Tamanio de ventana
window.geometry('900x700')
window.title('Proyecto final cientifica')
window.config(background="#fff")

#Frame de parametros
frame1 = tk.Frame(master=window)
frame1.place(x=550, y=25)
frame1.config(bg="#fff", width=300, height=250,highlightbackground="black", highlightthickness=4)
frame1.update()
lblTitulo1 = tk.Label(master=frame1,bg='#fff', font=('Times New Roman', 17), text=f"Parámetros")
lblTitulo1.place(x=frame1.winfo_width()/2, y=20,anchor="center")

#Frame métodos solucion
frame2 = tk.Frame(master=window)
frame2.place(x=550, y=350)
frame2.config(bg="#fff", width=300, height=325,highlightbackground="black", highlightthickness=4)
frame2.update()
lblTitulo2 = tk.Label(master=frame2,bg='#fff', font=('Times New Roman', 17), text=f"Métodos de solución")
lblTitulo2.place(x=frame2.winfo_width()/2, y=20,anchor="center")
#Columna de botones
btnColumn = tk.Frame(frame2, width=200, height=250, bg="#fff")
btnColumn.place(x=50, y=40)

#Boton euler
btnEulerAdelante = tk.Button(btnColumn, text="Euler adelante", width=25, height=1, bg='black', fg='white', command=eulerAdelante)
btnEulerAdelante.grid(row = 0, column = 0, pady = 10)
#Boton euler atras
btnEulerAtras = tk.Button(btnColumn, text="Euler atras", width=25, height=1, bg='black', fg='white', command=eulerAtras)
btnEulerAtras.grid(row = 1, column = 0, pady = 10)
#Boton euler modificado
btnEulerMod = tk.Button(btnColumn, text="Euler Modificado", width=25, height=1, bg='black', fg='white', command=eulerModificado)
btnEulerMod.grid(row = 2, column = 0, pady = 10)
#Boton Runge kutta 2
btnRunge2 = tk.Button(btnColumn, text="Runge-Kutta 2", width=25, height=1, bg='black', fg='white', command=RK2)
btnRunge2.grid(row = 3, column = 0, pady = 10)
#Boton Runge kutta 4
btnRunge4 = tk.Button(btnColumn, text="Runge-Kutta 4", width=25, height=1, bg='black', fg='white', command= RK4)
btnRunge4.grid(row = 4, column = 0, pady = 10)
#Boton nativos python
btnRunge4 = tk.Button(btnColumn, text="Odeint", width=25, height=1, bg='black', fg='white', command= RK4)
btnRunge4.grid(row = 5, column = 0, pady = 10)

#Boton cerrar
btnCerrar = tk.Button(master=window, text="X", width=6, height=1, bg='#c93e3e', fg='white',relief="flat", command = CerrarAplicacion).place(x=0,y=0)

#Variables para modelar graficado de valores
sT = tk.BooleanVar(value=1)
eT = tk.BooleanVar(value=1)
iT = tk.BooleanVar(value=1)
rT = tk.BooleanVar(value=1)
pT = tk.BooleanVar(value=1)

#Frame opciones grafica

frameOpciones = tk.Frame(window, width=400, height=50, bg = '#fff')
botonSt= tk.Checkbutton(frameOpciones, text="", variable=sT, command=grafica, bg='#fff').grid(row=0, column=0)
labelSt = tk.Label(frameOpciones,text="S(t)",bg='#fff').grid(row=1,column=0, padx=22)

botonEt= tk.Checkbutton(frameOpciones, text="", variable=eT, command=grafica, bg='#fff').grid(row=0, column=1)
labelEt = tk.Label(frameOpciones,text="E(t)", bg='#fff').grid(row=1,column=1, padx=22)

botonIt= tk.Checkbutton(frameOpciones, text="", variable=iT, command=grafica, bg='#fff').grid(row=0, column=2)
labelIt = tk.Label(frameOpciones,text="I(t)", bg='#fff').grid(row=1,column=2, padx=22)

botonRt= tk.Checkbutton(frameOpciones, text="", variable=rT, command=grafica, bg='#fff').grid(row=0, column=3)
labelRt = tk.Label(frameOpciones,text="R(t)", bg='#fff').grid(row=1,column=3, padx=22)

botonPt= tk.Checkbutton(frameOpciones, text="", variable=pT, command=grafica,bg='#fff').grid(row=0, column=4)
labelPt = tk.Label(frameOpciones,text="P(t)", bg='#fff').grid(row=1,column=4,padx=22)


frameOpciones.place(x=150,y=430)
#Label para frase tiempo de simulacion
labelGHorasSimulacion = tk.Label(width=55, height=1,text="Dias de simulacion", bg='#8080ff', fg="#fff")
labelGHorasSimulacion.place(x=110,y=510)

inicial = tk.StringVar(value =0)
final = tk.StringVar(value=5)
resta = tk.StringVar(value=float(final.get())-float(inicial.get()))

def botonDias():
    resta.set(float(final.get())-float(inicial.get()))
    grafica()

frameSimulacion = tk.Frame(window, width=400, height=100, bg = '#fff')
entradaInicio = tk.Entry(master=frameSimulacion, textvariable =inicial, highlightbackground="black", highlightthickness=1).grid(row=0, column=0)
flecha = tk.Label(master = frameSimulacion, font=(20), text = "\N{RIGHTWARDS BLACK ARROW}", bg='#fff').grid(row=0, column=2)
entradaFin = tk.Entry(master=frameSimulacion, textvariable =final, highlightbackground="black", highlightthickness=1 ).grid(row=0, column=3)
dias = tk.Label(master = frameSimulacion, font=(20), text = "Dias", bg='#fff').grid(row=0, column=4)
botonActivar = tk.Button(master = frameSimulacion, font=(20), textvariable=resta, command = botonDias).grid(row=0, column=5)

frameSimulacion.place(x=110, y = 550)       

grafica()
window.mainloop()    