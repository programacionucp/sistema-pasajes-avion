#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 22, 2020 02:12:26 PM -03  platform: Windows NT
#    Apr 22, 2020 02:23:23 PM -03  platform: Windows NT

import sys

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

from tkinter import messagebox

def set_Tk_var():
    global dniEliminarBuscar
    dniEliminarBuscar = tk.StringVar()
    global nombre
    nombre = tk.StringVar()
    global dni
    dni = tk.StringVar()
    global clase
    clase = tk.StringVar()
    global ubicacion
    ubicacion = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    configInicial()

def registrarPasajero():
    #datos ingresados
    claseSel = ""
    ubicacionSel = ""
    dniSel = dni.get()
    nombreSel = nombre.get()

    for unAsiento in lstAsientos:
        if unAsiento[5].count(dniSel)==1:
            messagebox.showinfo("ERROR", "El dni ingresado ya se encuentra registrado. ")
            break
        else:
            if clase.get() == "Ejecutiva":
                claseSel = EJECUTIVA
            else:
                claseSel = ECONOMICO

            if ubicacion.get() == "Ventana":
                 ubicacionSel = VENTANA
            elif ubicacion.get() == "Centro":
                  ubicacionSel = CENTRO
            else:
                  ubicacionSel = PASILLO

            #recorrer la lista para asignar
            for unAsiento in lstAsientos:
                if unAsiento[1] == LIBRE \
                    and unAsiento[2] == claseSel  \
                    and unAsiento[3] == ubicacionSel:
                        unAsiento[1] = OCUPADO
                        unAsiento[4] = nombreSel
                        unAsiento[5] = dniSel
                        unAsiento[6].configure(background=asientoBgOcupado)
                        messagebox.showinfo("Registro exitoso.", f"Asiento N°: {unAsiento[0]}")
                        return

def configInicial():
    global lstAsientos
    global EJECUTIVA,ECONOMICO,VENTANA,PASILLO,CENTRO,LIBRE,OCUPADO
    global asientoBgDisponible
    global asientoBgOcupado
    global contador


    asientoBgDisponible,asientoBgOcupado = "#ffff00","#ff0000"

    EJECUTIVA,ECONOMICO = "eje","eco"
    VENTANA,PASILLO,CENTRO = "ven","pas","cen"
    LIBRE,OCUPADO = "libre","ocupado"

    """"
    0 - asiento ---> 1
    1 - estado ----> "libre","ocupado"
    2 - clase  ---->  ejecutiva - económica
    3 - ubicacion --- ventana - pasillo - centro
    4 - pasajero nombre
    5 - pasajero dni 
    6 - label 
    """

    lstAsientos = [
        [1,LIBRE,EJECUTIVA,VENTANA,"","",w.lblAsiento1],
        [2,LIBRE,EJECUTIVA,PASILLO,"","",w.lblAsiento2],
        [3,LIBRE,EJECUTIVA,PASILLO,"","",w.lblAsiento3],
        [4,LIBRE,EJECUTIVA,VENTANA,"","",w.lblAsiento4],
        [5,LIBRE,EJECUTIVA,VENTANA,"","",w.lblAsiento5],
        [6,LIBRE,EJECUTIVA,PASILLO,"","",w.lblAsiento6],
        [7,LIBRE,EJECUTIVA,PASILLO,"","",w.lblAsiento7],
        [8,LIBRE,EJECUTIVA,VENTANA,"","",w.lblAsiento8],
        [9,LIBRE,ECONOMICO,VENTANA,"","",w.lblAsiento9],
        [10,LIBRE,ECONOMICO,CENTRO,"","",w.lblAsiento10],
        [11,LIBRE,ECONOMICO,PASILLO,"","",w.lblAsiento11],
        [12,LIBRE,ECONOMICO,PASILLO,"","",w.lblAsiento12],
        [13,LIBRE,ECONOMICO,CENTRO,"","",w.lblAsiento13],
        [14,LIBRE,ECONOMICO,VENTANA,"","",w.lblAsiento14],
        [15,LIBRE,ECONOMICO,VENTANA,"","",w.lblAsiento15],
        [16,LIBRE,ECONOMICO,CENTRO,"","",w.lblAsiento16],
        [17,LIBRE,ECONOMICO,PASILLO,"","",w.lblAsiento17],
        [18,LIBRE,ECONOMICO,PASILLO,"","",w.lblAsiento18],
        [19,LIBRE,ECONOMICO,CENTRO,"","",w.lblAsiento19],
        [20,LIBRE,ECONOMICO,VENTANA,"","",w.lblAsiento20]
    ]

def buscarPasajero():
    dniSel = dniEliminarBuscar.get()
    #recorrer la lista para buscar un dni
    for unAsiento in lstAsientos:
         if unAsiento[5] == dniSel:
            messagebox.showinfo("Info. Pasajero", f"Nombre Pasajero: {unAsiento[4]}, "
                                               f" Numero de Asiento:  {unAsiento[0]} ")
            return
def eliminarPasajero():
    dniSel = dniEliminarBuscar.get()
    for unAsiento in lstAsientos:
         if unAsiento[5] == dniSel:
            unAsiento[1]=LIBRE
            unAsiento[4]=""
            unAsiento[5]=""
            unAsiento[6].configure(background=asientoBgDisponible)
            messagebox.showinfo("info. Pasajero", "Pasajero eliminado. ")
            return

def promedioOcupacion():
    for unAsiento in lstAsientos:
         if unAsiento[1] == OCUPADO:
             contador=+1
    promedio=(100/len(lstAsientos))*contador
    messagebox.showinfo("info. Ocupacion", f"Promedio de Ocupacion: {promedio}")

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import avionIrala
    avionIrala.vp_start_gui()





