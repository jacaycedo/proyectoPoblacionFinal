import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
import struct as st
import numpy as np


datosLeidos = open('X:/Universidad/Prog Cientifica/ProyectoFinal/guardados/DatosDe-2021-06-03_02-31-21/datos.t', 'rb').read()
unpacked = np.array(st.unpack('d'*(len(datosLeidos)//8),datosLeidos))
print(unpacked)