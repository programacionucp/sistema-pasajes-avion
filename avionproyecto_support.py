#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 18, 2020 08:12:38 PM -03  platform: Windows NT
#    Apr 18, 2020 11:38:17 PM -03  platform: Windows NT
#    Apr 19, 2020 03:51:05 PM -03  platform: Windows NT
#    Apr 19, 2020 03:57:14 PM -03  platform: Windows NT

import sys
from tkinter import messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk



try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def init(top, gui, *args, **kwargs):
    global w, top_level, root,lista_ejecutiva,lista_economica,asiento,listapasajeros, colorlbl,pasajeros,asiento_v_EJ,asiento_p_EJ,asiento_c_E,colorlbl,asiento_v_E,asiento_p_E
    w = gui
    top_level = top
    root = top
    lista_ejecutiva=[[w.asiento1,w.asiento5,w.asiento4,w.asiento8],[w.asiento2,w.asiento6,w.asiento3,w.asiento7]]
    lista_economica=[[w.asiento9,w.asiento15,w.asiento14,w.asiento20],[w.asiento10,w.asiento16,w.asiento13,w.asiento19,],[w.asiento11,w.asiento17,w.asiento12,w.asiento18]]
    asiento_v_EJ=0
    asiento_p_EJ = 0
    #-------Indices clase Economico
    asiento_v_E=0
    asiento_c_E = 0
    asiento_p_E=0
    #--------------------indiceborrarpasajero
    borrarind=0
    listapasajeros=list()
def set_Tk_var():
    global clasesP
    clasesP = tk.StringVar()
    global ubicacionP
    ubicacionP = tk.StringVar()
    global ubicacion_p
    ubicacion_p = tk.StringVar()
    global cedulapasajero
    cedulapasajero = tk.StringVar()
    global nombre_pasajero
    nombre_pasajero = tk.StringVar()
    global ventanaU
    ventanaU = tk.IntVar()
    global clasesvuelos
    clasesvuelos = tk.StringVar()

def buscar_pasajero():
    def buscar():
      for pasajero in listapasajeros:
          if pasajero["cedula"]==cedulaing.get():
              messagebox.showinfo("pasajeros"," Los datos del pasajero son los siguientes:""\nnombre:"+ pasajero["nombre"]+"\nClase : "+pasajero["clase"]+"\nUbicacion :"+pasajero["ubicacion"])


    window = tk.Tk()
    window.title("Buscar pasajero")
    window.geometry("200x100")
    window.resizable(0,0)
    btnCambiar = tk.Button(window, width="14", height="1", text="Aceptar", command=buscar)
    btnCambiar.place(x=20, y=70)
    cedulaing = tk.Entry(window)
    cedulaing.configure(width="11")
    cedulaing.place(x=40, y=30)
    tk.Label(window, text="cedula: ", font=("Arial black  ", 10), fg="white", relief="groove", bg="black").place(x=10, y=5)


def eliminar_pasajero():
    def eliminarP():
      global borrarind
      borrarind=0
      for pasajero in listapasajeros:
          if pasajero["cedula"]==cedulaing.get():
              listapasajeros.pop(borrarind)
              messagebox.showinfo("eliminar pasajero", " pasajero Eliminado correctamente")
              borrarind+=1
              if pasajero["clase"]=="ejecutiva":
                  pasajero["colorlbl"].config(background="#efe136")

              if pasajero["clase"]=="economica":
                pasajero["colorlbl"].config(background="#472ce0")

          else:
            messagebox.showerror("eliminar pasajero", " no se encuentra el pasajero")









    window = tk.Tk()
    window.title("Eliminar Pasajero")
    window.geometry("200x100")
    window.resizable(0,0)
    btnCambiar = tk.Button(window, width="14", height="1", text="ELIMINAR", command=eliminarP)
    btnCambiar.place(x=20, y=70)
    cedulaing = tk.Entry(window)
    cedulaing.configure(width="11")
    cedulaing.place(x=40, y=30)
    tk.Label(window, text="cedula: ", font=("Arial black  ", 10), fg="white", relief="groove", ).place(x=10, y=5)

    print('avionproyecto_support.eliminar_pasajero')
    sys.stdout.flush()
def datos_pasajero(nombre,cedula,clase,ubicacion,colorlbl):
    global dicDatospasajeros,todos
    dicDatospasajeros=dict()
    dicDatospasajeros["nombre"]=nombre
    dicDatospasajeros["cedula"] = cedula
    dicDatospasajeros["clase"] = clase
    dicDatospasajeros["ubicacion"] = ubicacion
    dicDatospasajeros["colorlbl"] =colorlbl
    listapasajeros.append(dicDatospasajeros)

def porcentaje_ocupacion():
    porcentajeOcupacion=str(len(listapasajeros)*100/20)
    messagebox.showinfo("Porcentaje ocupación", "el porcentaje de ocupación es de:"+porcentajeOcupacion)

    sys.stdout.flush()

asiento_v_EJ=0
def registrar_pasajeros():
    global asiento, colorlbl,pasajeros, asiento_v_EJ,asiento_p_EJ,asiento_c_E,colorlbl, asiento_v_E, asiento_p_E
    for pasajero in listapasajeros:
        if pasajero["cedula"]!=cedulapasajero.get():
            datos_pasajero(nombre_pasajero.get(),cedulapasajero.get(),clasesvuelos.get(),ubicacionP.get(),colorlbl)
        else:
            messagebox.showerror(["error"], ["puede haber un pasajero con el mismo dni"])
    if clasesvuelos.get()== "ejecutiva"and ubicacionP.get()=="ventana" :
        lista_ejecutiva[0][asiento_v_EJ].config(background="red")
        colorlbl = lista_ejecutiva[0][asiento_v_EJ]
        asiento_v_EJ+= 1

    if clasesvuelos.get()=="ejecutiva"and ubicacionP.get()=="pasillo":
        lista_ejecutiva[1][asiento_p_EJ].config(background="red")
        colorlbl = lista_ejecutiva[1][asiento_p_EJ]
        asiento_p_EJ += 1
    #claseECONOMICA
    if clasesvuelos.get() == "economica" and ubicacionP.get() == "ventana":
        lista_economica[0][asiento_v_E].config(background="red")
        colorlbl = lista_economica[0][asiento_v_E]
        asiento_v_E += 1
    if clasesvuelos.get() == "economica" and ubicacionP.get() == "centro":
        lista_economica[1][asiento_c_E].config(background="red")
        colorlbl = lista_economica[1][asiento_c_E]
        asiento_c_E += 1
    if clasesvuelos.get() == "economica" and ubicacionP.get() == "pasillo":
        lista_economica[2][asiento_p_E].config(background="red")
        colorlbl = lista_economica[2][asiento_p_EJ]
        asiento_p_E += 1
    for pasajero in listapasajeros:
        if pasajero["cedula"]!=cedulapasajero.get():
            datos_pasajero(nombre_pasajero.get(),cedulapasajero.get(),clasesvuelos.get(),ubicacionP.get(),colorlbl)
        else:
            messagebox.showerror(["error"], ["puede haber un pasajero con el mismo dni"])

    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import avionproyecto
    avionproyecto.vp_start_gui()





