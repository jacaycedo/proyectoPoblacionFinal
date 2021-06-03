import tkinter as tk
from time import time
import datetime as dt
from tkinter.constants import COMMAND
from typing import Collection
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Variable, ttk
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
import struct as st
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from numpy.core.fromnumeric import var
import ecuacionesFunciones as functions


#Definicion de arreglos con valores de cada funcion para graficar a lo largo del tiempo
global arrST
global arrET
global arrIT
global arrRT
global arrPT
global tiempo
arrST = []
arrET =[]
arrIT =[]
arrRT =[]
arrPT =[]
tiempo =[]

#Definicion de funciones Solucion de ecuaciones
def eulerAdelante():
    ajustarParametros()
    global arrST
    global arrET
    global arrIT
    global arrRT
    global arrPT
    arrST,arrET,arrIT,arrRT,arrPT = ecuaciones.eulerForward(0.01,float(inicial.get()),float(final.get()))
    grafica()

def eulerAtras():
    ajustarParametros()
    global arrST
    global arrET
    global arrIT
    global arrRT
    global arrPT
    arrST,arrET,arrIT,arrRT,arrPT = ecuaciones.eulerBackward(0.01,float(inicial.get()),float(final.get()))
    grafica()


def eulerModificado():
    ajustarParametros()
    global arrST
    global arrET
    global arrIT
    global arrRT
    global arrPT
    arrST, arrET, arrIT, arrRT, arrPT = ecuaciones.eulerMod(0.01, float(inicial.get()), float(final.get()))
    grafica()

def RK2():
    ajustarParametros()
    global arrST
    global arrET
    global arrIT
    global arrRT
    global arrPT
    arrST,arrET,arrIT,arrRT,arrPT = ecuaciones.RK2(0.01,float(inicial.get()),float(final.get()))
    grafica()

def RK4():
    ajustarParametros()
    global arrST
    global arrET
    global arrIT
    global arrRT
    global arrPT
    arrST,arrET,arrIT,arrRT,arrPT = ecuaciones.RK4(0.01,float(inicial.get()),float(final.get()))
    grafica()

def odeint():
    global arrST
    global arrET
    global arrIT
    global arrRT
    global arrPT
    variables = ecuaciones.scypi(0.01,float(inicial.get()),float(final.get()))
    arrST,arrET,arrIT,arrRT,arrPT = variables[:,0], variables[:,1],variables[:,2],variables[:,3],variables[:,4]
    grafica()
    


def ajustarParametros():
    ecuaciones.setk(float(valorK.get()))
    ecuaciones.setai(float(valorAlphai.get()))
    ecuaciones.setae(float(valorAlphae.get()))
    ecuaciones.setgamma(float(valorGamma.get()))
    ecuaciones.setb(float(valorBetha.get()))
    ecuaciones.setp(float(valorRho.get()))
    ecuaciones.setm(float(valorMiu.get())) 


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
    global tiempo
    tiempo = t
    if sT.get() :
        ax.plot(t,arrST, label='S(t)')
    if eT.get():
        ax.plot(t,arrET, label='E(t)')
    if iT.get():
        ax.plot(t,arrIT, label='I(t)')
    if rT.get():
        ax.plot(t,arrRT, label='R(t)')
    if pT.get():
        ax.plot(t,arrPT, label='P(t)')
    ax.legend()
    plt.close()
    plt.style.use('seaborn-darkgrid')
    Plot = FigureCanvasTkAgg(fig, master=window)
    Plot.draw()

    Plot.get_tk_widget().place(x=50,y=30)





#Definición del lienzo de ejecucion para proyecto final
window = tk.Tk()

#Tamanio de ventana
window.geometry('900x700')
window.title('Proyecto final cientifica')
window.config(background="#fff")


#Variables para parametros
valorK = tk.StringVar(value = 0.05)
valorAlphai = tk.StringVar(value = 0.005)
valorAlphae = tk.StringVar(value = 0.65)
valorGamma = tk.StringVar(value = 0)
valorBetha = tk.StringVar(value = 0.1)
valorRho = tk.StringVar(value = 0.08)
valorMiu = tk.StringVar(value = 0.02)

#Variable que contiene los valores y las ecuaciones para la resolucion de las ecuaciones
ecuaciones = functions.Ecuaciones(float(valorK.get()),
                                 float(valorAlphai.get()),
                                 float(valorAlphae.get()),
                                 float(valorGamma.get()),
                                 float(valorBetha.get()),
                                 float(valorRho.get()),
                                 float(valorMiu.get()))

#Frame de parametros
frame1 = tk.Frame(master=window)
frame1.place(x=550, y=25)
frame1.config(bg="#fff", width=300, height=250,highlightbackground="black", highlightthickness=4)
frame1.update()
frameParams = tk.Frame(master = frame1,bg='#fff')

labelK = tk.Label(frameParams,text="k",bg='#fff',font=('Times New Roman', 15)).grid(row=0, column=0,padx=50)  
labelAlphai = tk.Label(frameParams, text="\N{Greek Small Letter Alpha}" + u'\u1d62', bg='#fff',font=('Times New Roman', 15)).grid(row=1, column=0,padx=50)  
labelAlphae = tk.Label(frameParams, text="\N{Greek Small Letter Alpha}" + u'\u2091', bg='#fff',font=('Times New Roman', 15)).grid(row=2, column=0,padx=50)  
labelGamma = tk.Label(frameParams, text= u'\u03B3', bg='#fff',font=('Times New Roman', 15)).grid(row=3, column=0, padx=50)  
labelBeta = tk.Label(frameParams, text= u'\ua7b5', bg='#fff',font=('Times New Roman', 15)).grid(row=4, column=0,padx=50)  
labelRho = tk.Label(frameParams, text= u'\u03c1', bg='#fff',font=('Times New Roman', 15)).grid(row=5, column=0,padx=50)  
labelMiu = tk.Label(frameParams, text= u'\u2c99', bg='#fff',font=('Times New Roman', 15)).grid(row=6, column=0,padx=50)  

entradaK = tk.Entry(master=frameParams, textvariable =valorK, highlightbackground="black", highlightthickness=1).grid(row=0, column=1)
entradaAlphai = tk.Entry(master=frameParams, textvariable =valorAlphai, highlightbackground="black", highlightthickness=1).grid(row=1, column=1)
entradaAlphae = tk.Entry(master=frameParams, textvariable =valorAlphae, highlightbackground="black", highlightthickness=1).grid(row=2, column=1)
entradaGamma = tk.Entry(master=frameParams, textvariable =valorGamma, highlightbackground="black", highlightthickness=1).grid(row=3, column=1)
entradaBetha = tk.Entry(master=frameParams, textvariable =valorBetha, highlightbackground="black", highlightthickness=1).grid(row=4, column=1)
entradaRho = tk.Entry(master=frameParams, textvariable =valorRho, highlightbackground="black", highlightthickness=1).grid(row=5, column=1)
entradaMiu = tk.Entry(master=frameParams, textvariable =valorMiu, highlightbackground="black", highlightthickness=1).grid(row=6, column=1)


frameParams.config(width=300, height=225)
frameParams.place(x=15, y =35)
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
btnRunge4 = tk.Button(btnColumn, text="Odeint", width=25, height=1, bg='black', fg='white', command= odeint)
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
final = tk.StringVar(value=150)
resta = tk.StringVar(value=float(final.get())-float(inicial.get()))

def botonDias():
    resta.set(float(final.get())-float(inicial.get()))

frameSimulacion = tk.Frame(window, width=400, height=100, bg = '#fff')
entradaInicio = tk.Entry(master=frameSimulacion, textvariable =inicial, highlightbackground="black", highlightthickness=1).grid(row=0, column=0)
flecha = tk.Label(master = frameSimulacion, font=(20), text = "\N{RIGHTWARDS BLACK ARROW}", bg='#fff').grid(row=0, column=2)
entradaFin = tk.Entry(master=frameSimulacion, textvariable =final, highlightbackground="black", highlightthickness=1 ).grid(row=0, column=3)
dias = tk.Label(master = frameSimulacion, font=(20), text = "Dias", bg='#fff').grid(row=0, column=4)
botonActivar = tk.Button(master = frameSimulacion, font=(20), textvariable=resta, command = botonDias).grid(row=0, column=5)
frameSimulacion.place(x=110, y = 550)       


def cargarDatos():
    nombreCarpeta = tk.filedialog.askdirectory(parent = window, title='Directorio para leer datos')
    if nombreCarpeta == '':
        messagebox.showinfo(message="No has seleccionado una carpeta", title="Advertencia")
    carpetaReal = Path(nombreCarpeta)
    datosSt = leerArchivoDir(carpetaReal, '.s')
    datosEt = leerArchivoDir(carpetaReal, '.e')
    datosIt = leerArchivoDir(carpetaReal, '.i')
    datosRt = leerArchivoDir(carpetaReal, '.r')
    datoPt = leerArchivoDir(carpetaReal, '.p')
    datosT = leerArchivoDir(carpetaReal, '.t')
    global arrST
    global arrET
    global arrIT
    global arrRT
    global arrPT
    global tiempo
    arrST = datosSt
    arrET = datosEt
    arrIT = datosIt
    arrRT = datosRt
    arrPT = datoPt
    final.set(datosT[-1]+0.01)
    inicial.set(datosT[0])
    grafica()

def leerArchivoDir(directorio, tipo):
    exte = '*'+tipo
    archivo = [f.absolute() for f in directorio.glob(exte) if f.is_file()][0]
    datosLeidos = open(archivo, 'rb').read()
    unpacked = np.array(st.unpack('d'*(len(datosLeidos)//8),datosLeidos))
    return unpacked

def persistirDatos():
    tiempoActual = time()
    fecha = dt.datetime.utcfromtimestamp(tiempoActual).strftime("%Y-%m-%d_%H-%M-%S")
    carpeta = 'DatosDe-'+ fecha
    directorioNombre = filedialog.askdirectory(parent = window,title="Directorio de guardado de datos") 
    if directorioNombre == '':
        messagebox.showinfo(message="No has seleccionado una carpeta", title="Advertencia")
    rutaCarpeta = Path(directorioNombre)
    carpetaReal = rutaCarpeta.joinpath(str(carpeta))
    carpetaReal.mkdir(parents=True, exist_ok=True)
    guardarArchivo(carpetaReal,'.s', np.array(arrST))
    guardarArchivo(carpetaReal,'.e', np.array(arrET))
    guardarArchivo(carpetaReal,'.i', np.array(arrIT))
    guardarArchivo(carpetaReal,'.r', np.array(arrRT))
    guardarArchivo(carpetaReal,'.p', np.array(arrPT))
    guardarArchivo(carpetaReal,'.t', np.array(tiempo))

def guardarArchivo(directorio, ext, datos):
    datosPacked = st.pack('d'*len(datos), *datos)
    archivo = open(directorio.joinpath("datos"+ext).absolute(),'wb')
    archivo.write(datosPacked)

btnEulerMod = tk.Button(window, text="Importar", width=15, height=1, bg='white', fg='black', command=cargarDatos).place(x=80, y= 0)
btnEulerMod = tk.Button(window, text="Exportar", width=15, height=1, bg='white', fg='black', command=persistirDatos).place(x=200, y= 0)



window.mainloop()    