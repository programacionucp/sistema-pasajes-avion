from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.wm_title("Programacion II - Lic. en Sistemas")
window.config(background = "#EEEEEE")
window.geometry("850x650+10+20")
window.resizable(0,0)
style = ttk.Style()
style.configure('TButton', foreground='Black', borderwidth=110,relief='groove', padding=10)

global lstPasajeros
lstPasajeros=list()

for i in range (20):
    lstPasajeros.append(list())


def nuevaVentana():
    global window2
    window2 = Tk()
    window2.wm_title("Venta")
    window2.config(background = "#EEEEEE")
    window2.geometry("200x200+10+20")
    window2.resizable(0,0)
    style = ttk.Style()
    style.configure('TButton', foreground='Black', borderwidth=110,relief='groove', padding=10)

    titulo=Label(window2,width=20, text="Datos Pasajero", font=("helvetica",14),relief="groove",anchor="center")
    titulo.place(x=0,y=0)

    lblNumeroAsiento=Label(window2,width=19, text="N° de Asiento:", font=("helvetica",12),anchor="w")
    lblNumeroAsiento.place(x=20,y=30)

    global elegirAsiento
    elegirAsiento=Spinbox(window2, from_=1, to=20, wrap=True,state='readonly')
    elegirAsiento.place(x=20,y=50)

    lblNombrePasajero=Label(window2,width=12, text="Nombre:", font=("helvetica",12),anchor="w")
    lblNombrePasajero.place(x=20,y=70)

    global entNombre
    entNombre=Entry(window2,width=20,justify="center")
    entNombre.place(x=20,y=90)

    lblCedula=Label(window2,width=12, text="Cedula:", font=("helvetica",12),anchor="w",)
    lblCedula.place(x=20,y=115)

    global entCedula
    entCedula=Entry(window2,width=20,justify="center")
    entCedula.place(x=20,y=135)

    btnConfirmarVenta=Button(window2,width=16, text="Confirmar",command=confirmarVenta)
    btnConfirmarVenta.place(x=28, y=160,height=29)


def confirmarVenta():
    for x in range(len(lstPasajeros)):
        lstPasajeros[int(elegirAsiento.get())-1]=str(elegirAsiento.get()),str(entNombre.get()),str(entCedula.get())

    if elegirAsiento.get()=="1":
        lblAsiento1["background"]="red"
    if elegirAsiento.get()=="2":
        lblAsiento2["background"]="red"
    if elegirAsiento.get()=="3":
        lblAsiento3["background"]="red"
    if elegirAsiento.get()=="4":
        lblAsiento4["background"]="red"
    if elegirAsiento.get()=="5":
        lblAsiento5["background"]="red"
    if elegirAsiento.get()=="6":
        lblAsiento6["background"]="red"
    if elegirAsiento.get()=="7":
        lblAsiento7["background"]="red"
    if elegirAsiento.get()=="8":
        lblAsiento8["background"]="red"
    if elegirAsiento.get()=="9":
        lblAsiento9["background"]="red"
    if elegirAsiento.get()=="10":
        lblAsiento10["background"]="red"
    if elegirAsiento.get()=="11":
        lblAsiento11["background"]="red"
    if elegirAsiento.get()=="12":
        lblAsiento12["background"]="red"
    if elegirAsiento.get()=="13":
        lblAsiento13["background"]="red"
    if elegirAsiento.get()=="14":
        lblAsiento14["background"]="red"
    if elegirAsiento.get()=="15":
        lblAsiento15["background"]="red"
    if elegirAsiento.get()=="16":
        lblAsiento16["background"]="red"
    if elegirAsiento.get()=="17":
        lblAsiento17["background"]="red"
    if elegirAsiento.get()=="18":
        lblAsiento18["background"]="red"
    if elegirAsiento.get()=="19":
        lblAsiento19["background"]="red"
    if elegirAsiento.get()=="20":
        lblAsiento20["background"]="red"

    window2.destroy()

def registrarPasajero():
    nuevaVentana()

def nuevaVentanaEliminar():
    global window3
    window3 = Tk()
    window3.wm_title("Venta")
    window3.config(background = "#EEEEEE")
    window3.geometry("200x200+10+20")
    window3.resizable(0,0)
    style = ttk.Style()
    style.configure('TButton', foreground='Black', borderwidth=110,relief='groove', padding=10)

    titulo=Label(window3,width=20, text="Cedula del pasajero:", font=("helvetica",12),anchor="center")
    titulo.place(x=0,y=0)

    global entNumeroAsiento
    entNumeroAsiento=Entry(window3, width=20)
    entNumeroAsiento.place(x=30,y=30)


    btnEliminar=Button(window3,width=16,text="Eliminar",command=confirmarEliminacionPasajero)
    btnEliminar.place(x=38,y=60)

def elimnarPasajero():
    nuevaVentanaEliminar()

def confirmarEliminacionPasajero():
    #print(lstPasajeros)
    for x in range(len(lstPasajeros)):
        print(lstPasajeros[x])
        for elem in lstPasajeros[x]:
            if (elem==int(entNumeroAsiento.get())):                     #No me aplica el if.
                lstPasajeros.pop(int(entNumeroAsiento.get()-1))
    #print(lstPasajeros)
    window3.destroy()

#def porcentajeOcupacion():
    #porcentajeOcu=(20/100)*contadorOcupados
    #messagebox.showinfo(message=f"Porcentaje de ocupacion: {porcentajeOcu} ", title="Ocupacion")

def start():
    titulo=Label(window,width=30, text="Venta de pasajes", font=("helvetica",14))
    titulo.place(x=20,y=0)

    recuadro01 = Canvas(window, width=700,
                height=400,
                borderwidth=2,
                relief='groove')
    recuadro01.place(x=50, y=70)

    recuadro02 = Canvas(window, width=80,
                height=380,
                borderwidth=2,
                background='gray',
                relief='groove')
    recuadro02.place(x=350, y=80)

    #Referencias
    lblEjecutivo=Label(window,width=10, text="Ejecutivo", font=("Helvetica",10), relief="groove", background="yellow",anchor="center")
    lblEjecutivo.place(x=250, y=30,height=40)
    lblEconomica=Label(window,width=10, text="Ejecutivo", font=("Helvetica",10), relief="groove", background="blue",anchor="center")
    lblEconomica.place(x=350, y=30,height=40)
    lblEconomica=Label(window,width=10, text="Ocupado", font=("Helvetica",10), relief="groove", background="red",anchor="center")
    lblEconomica.place(x=450, y=30,height=40)


    #ASIENTOS

    #PRIMERA CLASE
    global lblAsiento1
    lblAsiento1=Label(window,width=4, text="1", font=("Helvetica",12), relief="groove", background="yellow",anchor="center")
    lblAsiento1.place(x=170, y=120,height=40)
    global lblAsiento2
    lblAsiento2=Label(window,width=4, text="2", font=("Helvetica",12), relief="groove", background="yellow",anchor="center")
    lblAsiento2.place(x=250, y=120,height=40)
    global lblAsiento3
    lblAsiento3=Label(window,width=4, text="3", font=("Helvetica",12), relief="groove", background="yellow",anchor="center")
    lblAsiento3.place(x=500, y=120,height=40)
    global lblAsiento4
    lblAsiento4=Label(window,width=4, text="4", font=("Helvetica",12), relief="groove", background="yellow",anchor="center")
    lblAsiento4.place(x=580, y=120,height=40)

    global lblAsiento5
    lblAsiento5=Label(window,width=4, text="5", font=("Helvetica",12), relief="groove", background="yellow",anchor="center")
    lblAsiento5.place(x=170, y=200,height=40)
    global lblAsiento6
    lblAsiento6=Label(window,width=4, text="6", font=("Helvetica",12), relief="groove", background="yellow",anchor="center")
    lblAsiento6.place(x=250, y=200,height=40)
    global lblAsiento7
    lblAsiento7=Label(window,width=4, text="7", font=("Helvetica",12), relief="groove", background="yellow",anchor="center")
    lblAsiento7.place(x=500, y=200,height=40)
    global lblAsiento8
    lblAsiento8=Label(window,width=4, text="8", font=("Helvetica",12), relief="groove", background="yellow",anchor="center")
    lblAsiento8.place(x=580, y=200,height=40)

    #CLASE ECONOMICA
    global lblAsiento9
    lblAsiento9=Label(window,width=4, text="9", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento9.place(x=90, y=280,height=40)
    global lblAsiento10
    lblAsiento10=Label(window,width=4, text="10", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento10.place(x=170, y=280,height=40)
    global lblAsiento11
    lblAsiento11=Label(window,width=4, text="11", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento11.place(x=250, y=280,height=40)
    global lblAsiento12
    lblAsiento12=Label(window,width=4, text="12", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento12.place(x=500, y=280,height=40)
    global lblAsiento13
    lblAsiento13=Label(window,width=4, text="13", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento13.place(x=580, y=280,height=40)
    global lblAsiento14
    lblAsiento14=Label(window,width=4, text="14", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento14.place(x=660,y=280,height=40)

    global lblAsiento15
    lblAsiento15=Label(window,width=4, text="15", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento15.place(x=90, y=360,height=40)
    global lblAsiento16
    lblAsiento16=Label(window,width=4, text="16", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento16.place(x=170, y=360,height=40)
    global lblAsiento17
    lblAsiento17=Label(window,width=4, text="17", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento17.place(x=250, y=360,height=40)
    global lblAsiento18
    lblAsiento18=Label(window,width=4, text="18", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento18.place(x=500, y=360,height=40)
    global lblAsiento19
    lblAsiento19=Label(window,width=4, text="19", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento19.place(x=580, y=360,height=40)
    global lblAsiento20
    lblAsiento20=Label(window,width=4, text="20", font=("Helvetica",12), relief="groove", background="blue",anchor="center")
    lblAsiento20.place(x=660,y=360,height=40)

    #Botones

    btnRegistrarPasajero = Button(window,width=20, text="Registrar pasajero",command=registrarPasajero)
    btnRegistrarPasajero.place(x=80, y=480,height=29)
    btnEliminarPasajero = Button(window,width=20, text="Eliminar pasajero",command=elimnarPasajero)
    btnEliminarPasajero.place(x=240, y=480,height=29)
    btnBuscarPasajero = Button(window,width=20, text="Buscar Pasajero")
    btnBuscarPasajero.place(x=400, y=480,height=29)
    btnPorcentajeOcupacion = Button(window,width=24, text="Porcenetaje de Ocupacion")
    btnPorcentajeOcupacion.place(x=560, y=480,height=29)



start()
window.mainloop()



