import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
import struct as st
import numpy as np



def cargarDatos():
    nombreCarpeta = tk.filedialog.askdirectory()
    if nombreCarpeta == '':
        messagebox.showinfo(message="No has seleccionado una carpeta", title="Advertencia")
    carpetaReal = Path(nombreCarpeta)


def leerArchivoDir(directorio, tipo):
    exte = '*'+tipo
    archivo = [f.absolute() for f in directorio.glob(exte) if f.is_file()][0]
    datosLeidos = open(archivo, 'rb').read()
    unpacked = np.array(st.unpack('d'*(len(datosLeidos)/8),datosLeidos))




cargarDatos()