#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 15, 2020 07:05:06 PM -03  platform: Windows NT

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

import TPPasajeros_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    TPPasajeros_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    TPPasajeros_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("603x579+627+140")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.btnRegistrarP = tk.Button(top)
        self.btnRegistrarP.place(relx=0.1, rely=0.604, height=33, width=206)
        self.btnRegistrarP.configure(activebackground="#ececec")
        self.btnRegistrarP.configure(activeforeground="#000000")
        self.btnRegistrarP.configure(background="#d9d9d9")
        self.btnRegistrarP.configure(command=TPPasajeros_support.registrarPasajero)
        self.btnRegistrarP.configure(disabledforeground="#a3a3a3")
        self.btnRegistrarP.configure(foreground="#000000")
        self.btnRegistrarP.configure(highlightbackground="#d9d9d9")
        self.btnRegistrarP.configure(highlightcolor="black")
        self.btnRegistrarP.configure(pady="0")
        self.btnRegistrarP.configure(text='''Registrar Pasajero''')

        self.btnEliminarP = tk.Button(top)
        self.btnEliminarP.place(relx=0.564, rely=0.604, height=33, width=206)
        self.btnEliminarP.configure(activebackground="#ececec")
        self.btnEliminarP.configure(activeforeground="#000000")
        self.btnEliminarP.configure(background="#d9d9d9")
        self.btnEliminarP.configure(command=TPPasajeros_support.eliminarPasajero)
        self.btnEliminarP.configure(disabledforeground="#a3a3a3")
        self.btnEliminarP.configure(foreground="#000000")
        self.btnEliminarP.configure(highlightbackground="#d9d9d9")
        self.btnEliminarP.configure(highlightcolor="black")
        self.btnEliminarP.configure(pady="0")
        self.btnEliminarP.configure(text='''Eliminar Pasajero''')

        self.btnPorcentaje = tk.Button(top)
        self.btnPorcentaje.place(relx=0.1, rely=0.691, height=33, width=206)
        self.btnPorcentaje.configure(activebackground="#ececec")
        self.btnPorcentaje.configure(activeforeground="#000000")
        self.btnPorcentaje.configure(background="#d9d9d9")
        self.btnPorcentaje.configure(command=TPPasajeros_support.porcentajeOcup)
        self.btnPorcentaje.configure(disabledforeground="#a3a3a3")
        self.btnPorcentaje.configure(foreground="#000000")
        self.btnPorcentaje.configure(highlightbackground="#d9d9d9")
        self.btnPorcentaje.configure(highlightcolor="black")
        self.btnPorcentaje.configure(pady="0")
        self.btnPorcentaje.configure(text='''Porcentaje Ocupación''')

        self.btnBuscarP = tk.Button(top)
        self.btnBuscarP.place(relx=0.564, rely=0.691, height=33, width=206)
        self.btnBuscarP.configure(activebackground="#ececec")
        self.btnBuscarP.configure(activeforeground="#000000")
        self.btnBuscarP.configure(background="#d9d9d9")
        self.btnBuscarP.configure(command=TPPasajeros_support.buscarPasajero)
        self.btnBuscarP.configure(disabledforeground="#a3a3a3")
        self.btnBuscarP.configure(foreground="#000000")
        self.btnBuscarP.configure(highlightbackground="#d9d9d9")
        self.btnBuscarP.configure(highlightcolor="black")
        self.btnBuscarP.configure(pady="0")
        self.btnBuscarP.configure(text='''Buscar Pasajero''')

        self.asiento1 = tk.Label(top)
        self.asiento1.place(relx=0.217, rely=0.173, height=25, width=42)
        self.asiento1.configure(activebackground="#f9f9f9")
        self.asiento1.configure(activeforeground="black")
        self.asiento1.configure(background="#f3e743")
        self.asiento1.configure(disabledforeground="#b3ae93")
        self.asiento1.configure(foreground="#000000")
        self.asiento1.configure(highlightbackground="#d9d9d9")
        self.asiento1.configure(highlightcolor="black")
        self.asiento1.configure(relief="ridge")
        self.asiento1.configure(text='''1''')

        self.asiento2 = tk.Label(top)
        self.asiento2.place(relx=0.3, rely=0.173, height=25, width=42)
        self.asiento2.configure(activebackground="#f9f9f9")
        self.asiento2.configure(activeforeground="black")
        self.asiento2.configure(background="#f3e743")
        self.asiento2.configure(disabledforeground="#a3a3a3")
        self.asiento2.configure(foreground="#000000")
        self.asiento2.configure(highlightbackground="#d9d9d9")
        self.asiento2.configure(highlightcolor="black")
        self.asiento2.configure(relief="ridge")
        self.asiento2.configure(text='''2''')

        self.asiento5 = tk.Label(top)
        self.asiento5.place(relx=0.217, rely=0.221, height=25, width=42)
        self.asiento5.configure(activebackground="#f9f9f9")
        self.asiento5.configure(activeforeground="black")
        self.asiento5.configure(background="#f3e743")
        self.asiento5.configure(disabledforeground="#a3a3a3")
        self.asiento5.configure(foreground="#000000")
        self.asiento5.configure(highlightbackground="#d9d9d9")
        self.asiento5.configure(highlightcolor="black")
        self.asiento5.configure(relief="ridge")
        self.asiento5.configure(text='''5''')

        self.asiento6 = tk.Label(top)
        self.asiento6.place(relx=0.3, rely=0.221, height=25, width=42)
        self.asiento6.configure(activebackground="#f9f9f9")
        self.asiento6.configure(activeforeground="black")
        self.asiento6.configure(background="#f3e743")
        self.asiento6.configure(disabledforeground="#a3a3a3")
        self.asiento6.configure(foreground="#000000")
        self.asiento6.configure(highlightbackground="#d9d9d9")
        self.asiento6.configure(highlightcolor="black")
        self.asiento6.configure(relief="ridge")
        self.asiento6.configure(text='''6''')

        self.asiento3 = tk.Label(top)
        self.asiento3.place(relx=0.6, rely=0.173, height=25, width=42)
        self.asiento3.configure(activebackground="#f9f9f9")
        self.asiento3.configure(activeforeground="black")
        self.asiento3.configure(background="#f3e743")
        self.asiento3.configure(disabledforeground="#a3a3a3")
        self.asiento3.configure(foreground="#000000")
        self.asiento3.configure(highlightbackground="#d9d9d9")
        self.asiento3.configure(highlightcolor="black")
        self.asiento3.configure(relief="ridge")
        self.asiento3.configure(text='''3''')

        self.asiento7 = tk.Label(top)
        self.asiento7.place(relx=0.6, rely=0.221, height=25, width=42)
        self.asiento7.configure(activebackground="#f9f9f9")
        self.asiento7.configure(activeforeground="black")
        self.asiento7.configure(background="#f3e743")
        self.asiento7.configure(disabledforeground="#a3a3a3")
        self.asiento7.configure(foreground="#000000")
        self.asiento7.configure(highlightbackground="#d9d9d9")
        self.asiento7.configure(highlightcolor="black")
        self.asiento7.configure(relief="ridge")
        self.asiento7.configure(text='''7''')

        self.asiento4 = tk.Label(top)
        self.asiento4.place(relx=0.68, rely=0.173, height=24, width=42)
        self.asiento4.configure(activebackground="#f9f9f9")
        self.asiento4.configure(activeforeground="black")
        self.asiento4.configure(background="#f3e743")
        self.asiento4.configure(disabledforeground="#a3a3a3")
        self.asiento4.configure(foreground="#000000")
        self.asiento4.configure(highlightbackground="#d9d9d9")
        self.asiento4.configure(highlightcolor="black")
        self.asiento4.configure(relief="ridge")
        self.asiento4.configure(text='''4''')

        self.asiento8 = tk.Label(top)
        self.asiento8.place(relx=0.68, rely=0.221, height=25, width=42)
        self.asiento8.configure(activebackground="#f9f9f9")
        self.asiento8.configure(activeforeground="black")
        self.asiento8.configure(background="#f3e743")
        self.asiento8.configure(disabledforeground="#a3a3a3")
        self.asiento8.configure(foreground="#000000")
        self.asiento8.configure(highlightbackground="#d9d9d9")
        self.asiento8.configure(highlightcolor="black")
        self.asiento8.configure(relief="ridge")
        self.asiento8.configure(text='''8''')

        self.asiento9 = tk.Label(top)
        self.asiento9.place(relx=0.182, rely=0.295, height=25, width=43)
        self.asiento9.configure(activebackground="#f9f9f9")
        self.asiento9.configure(activeforeground="black")
        self.asiento9.configure(background="#70c7c7")
        self.asiento9.configure(disabledforeground="#a3a3a3")
        self.asiento9.configure(foreground="#000000")
        self.asiento9.configure(highlightbackground="#d9d9d9")
        self.asiento9.configure(highlightcolor="black")
        self.asiento9.configure(relief="ridge")
        self.asiento9.configure(text='''9''')

        self.asiento10 = tk.Label(top)
        self.asiento10.place(relx=0.267, rely=0.295, height=25, width=42)
        self.asiento10.configure(activebackground="#f9f9f9")
        self.asiento10.configure(activeforeground="black")
        self.asiento10.configure(background="#70c7c7")
        self.asiento10.configure(disabledforeground="#a3a3a3")
        self.asiento10.configure(foreground="#000000")
        self.asiento10.configure(highlightbackground="#d9d9d9")
        self.asiento10.configure(highlightcolor="black")
        self.asiento10.configure(relief="ridge")
        self.asiento10.configure(text='''10''')

        self.asiento11 = tk.Label(top)
        self.asiento11.place(relx=0.35, rely=0.295, height=25, width=42)
        self.asiento11.configure(activebackground="#f9f9f9")
        self.asiento11.configure(activeforeground="black")
        self.asiento11.configure(background="#70c7c7")
        self.asiento11.configure(disabledforeground="#a3a3a3")
        self.asiento11.configure(foreground="#000000")
        self.asiento11.configure(highlightbackground="#d9d9d9")
        self.asiento11.configure(highlightcolor="black")
        self.asiento11.configure(relief="ridge")
        self.asiento11.configure(text='''11''')

        self.asiento15 = tk.Label(top)
        self.asiento15.place(relx=0.182, rely=0.344, height=25, width=43)
        self.asiento15.configure(activebackground="#f9f9f9")
        self.asiento15.configure(activeforeground="black")
        self.asiento15.configure(background="#70c7c7")
        self.asiento15.configure(disabledforeground="#a3a3a3")
        self.asiento15.configure(foreground="#000000")
        self.asiento15.configure(highlightbackground="#d9d9d9")
        self.asiento15.configure(highlightcolor="black")
        self.asiento15.configure(relief="ridge")
        self.asiento15.configure(text='''15''')

        self.asiento16 = tk.Label(top)
        self.asiento16.place(relx=0.267, rely=0.344, height=25, width=42)
        self.asiento16.configure(activebackground="#f9f9f9")
        self.asiento16.configure(activeforeground="black")
        self.asiento16.configure(background="#70c7c7")
        self.asiento16.configure(disabledforeground="#a3a3a3")
        self.asiento16.configure(foreground="#000000")
        self.asiento16.configure(highlightbackground="#d9d9d9")
        self.asiento16.configure(highlightcolor="black")
        self.asiento16.configure(relief="ridge")
        self.asiento16.configure(text='''16''')

        self.asiento17 = tk.Label(top)
        self.asiento17.place(relx=0.35, rely=0.344, height=25, width=42)
        self.asiento17.configure(activebackground="#f9f9f9")
        self.asiento17.configure(activeforeground="black")
        self.asiento17.configure(background="#70c7c7")
        self.asiento17.configure(disabledforeground="#a3a3a3")
        self.asiento17.configure(foreground="#000000")
        self.asiento17.configure(highlightbackground="#d9d9d9")
        self.asiento17.configure(highlightcolor="black")
        self.asiento17.configure(relief="ridge")
        self.asiento17.configure(text='''17''')

        self.asiento12 = tk.Label(top)
        self.asiento12.place(relx=0.551, rely=0.295, height=25, width=42)
        self.asiento12.configure(activebackground="#f9f9f9")
        self.asiento12.configure(activeforeground="black")
        self.asiento12.configure(background="#70c7c7")
        self.asiento12.configure(disabledforeground="#a3a3a3")
        self.asiento12.configure(foreground="#000000")
        self.asiento12.configure(highlightbackground="#d9d9d9")
        self.asiento12.configure(highlightcolor="black")
        self.asiento12.configure(relief="ridge")
        self.asiento12.configure(text='''12''')

        self.asiento13 = tk.Label(top)
        self.asiento13.place(relx=0.633, rely=0.295, height=25, width=42)
        self.asiento13.configure(activebackground="#f9f9f9")
        self.asiento13.configure(activeforeground="black")
        self.asiento13.configure(background="#70c7c7")
        self.asiento13.configure(disabledforeground="#a3a3a3")
        self.asiento13.configure(foreground="#000000")
        self.asiento13.configure(highlightbackground="#d9d9d9")
        self.asiento13.configure(highlightcolor="black")
        self.asiento13.configure(relief="ridge")
        self.asiento13.configure(text='''13''')

        self.asiento14 = tk.Label(top)
        self.asiento14.place(relx=0.713, rely=0.294, height=25, width=42)
        self.asiento14.configure(activebackground="#f9f9f9")
        self.asiento14.configure(activeforeground="black")
        self.asiento14.configure(background="#70c7c7")
        self.asiento14.configure(disabledforeground="#a3a3a3")
        self.asiento14.configure(foreground="#000000")
        self.asiento14.configure(highlightbackground="#d9d9d9")
        self.asiento14.configure(highlightcolor="black")
        self.asiento14.configure(relief="ridge")
        self.asiento14.configure(text='''14''')

        self.asiento18 = tk.Label(top)
        self.asiento18.place(relx=0.551, rely=0.344, height=25, width=42)
        self.asiento18.configure(activebackground="#f9f9f9")
        self.asiento18.configure(activeforeground="black")
        self.asiento18.configure(background="#70c7c7")
        self.asiento18.configure(disabledforeground="#a3a3a3")
        self.asiento18.configure(foreground="#000000")
        self.asiento18.configure(highlightbackground="#d9d9d9")
        self.asiento18.configure(highlightcolor="black")
        self.asiento18.configure(relief="ridge")
        self.asiento18.configure(text='''18''')

        self.asiento19 = tk.Label(top)
        self.asiento19.place(relx=0.633, rely=0.344, height=25, width=42)
        self.asiento19.configure(activebackground="#f9f9f9")
        self.asiento19.configure(activeforeground="black")
        self.asiento19.configure(background="#70c7c7")
        self.asiento19.configure(disabledforeground="#a3a3a3")
        self.asiento19.configure(foreground="#000000")
        self.asiento19.configure(highlightbackground="#d9d9d9")
        self.asiento19.configure(highlightcolor="black")
        self.asiento19.configure(relief="ridge")
        self.asiento19.configure(text='''19''')

        self.asiento20 = tk.Label(top)
        self.asiento20.place(relx=0.713, rely=0.345, height=25, width=42)
        self.asiento20.configure(activebackground="#f9f9f9")
        self.asiento20.configure(activeforeground="black")
        self.asiento20.configure(background="#70c7c7")
        self.asiento20.configure(disabledforeground="#a3a3a3")
        self.asiento20.configure(foreground="#000000")
        self.asiento20.configure(highlightbackground="#d9d9d9")
        self.asiento20.configure(highlightcolor="black")
        self.asiento20.configure(relief="ridge")
        self.asiento20.configure(text='''20''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.116, rely=0.535, relwidth=0.779)

if __name__ == '__main__':
    vp_start_gui()