from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

#Creacion de Tk y Toplevel
root = Tk()
root.withdraw()
root.overrideredirect(1)
root.geometry('300x205+400+350')
root.configure(bg='black')
root.resizable(0,0)
window = Toplevel()
window.geometry('704x437')
window.resizable(False,False)
window.title('Reserva de Pasajes')
window.protocol('WM_DELETE_WINDOW',root.destroy)
window.configure(bg='black')

#Variables Globales
Disponibilidad=True
Botonera=0
Nombres_Pasajeros = [""]
Cedulas_Pasajeros = [""]
Buttons = [0,[240,20],[280,20],[385,20],[425,20],[240,50],[280,50],[385,50],[425,50],[220,100],
           [260,100],[300,100],[365,100],[405,100],[445,100],[220,130],[260,130],[300,130],[365,130],
           [405,130],[445,130],[220,160],[260,160],[300,160],[365,160],[405,160],[445,160],[220,190],
           [260,190],[300,190],[365,190],[405,190],[445,190],[220,220],[260,220],[300,220],[365,220],
           [405,220],[445,220],[220,250],[260,250],[300,250],[365,250],[405,250],[445,250],[220,280],
           [260,280],[300,280],[365,280],[405,280],[445,280]]
Asiento_Status = [""]
for i in range(50):
    Asiento_Status.append(1)
    Nombres_Pasajeros.append("")
    Cedulas_Pasajeros.append("")

#Funciones
def sillas():
    global Buttons,Asiento_Status,Nombres_Pasajeros,Cedulas_Pasajeros          
    for i in range(1,51):
        if i in (1,2,3,4,5,6,7,8) and Asiento_Status[i]==1:
            bg_="yellow"
        if i in (1,2,3,4,5,6,7,8) and Asiento_Status[i]==0:
            bg_="red"
        if i not in (1,2,3,4,5,6,7,8) and Asiento_Status[i]==1:
            bg_="light blue"
        if i not in (1,2,3,4,5,6,7,8) and Asiento_Status[i]==0:
            bg_="red"
        btn_silla  = Button(window, text=str(i),width=2,bg=bg_)
        btn_silla.place(x=Buttons[i][0],y=Buttons[i][1])
def Limpiar_root_y_toplevel(x):
    global Botonera
    if x==1:
        for child in root.winfo_children():
            if child != window:
                child.destroy()
    elif x==2:
        for child in root.winfo_children():
            if child != window:
                child.destroy()
        for child in window.winfo_children():
            if child != Botonera:
                child.destroy
def Requerimientos():
    global Asiento_Status, Disponibilidad, Nombres_Pasajeros, Cedulas_Pasajeros,Buttons,Botonera
    Botonera = Frame(window,width=680,height=100,relief=SUNKEN,bd=10)
    Botonera.place(x=0,y=390)
    #Requerimiento 1
    def Registrar_Pasajero():
        root.deiconify()
        root.title('Registro de Reserva')
        lbl_Nombre= Label(root, text='Nombre:',bg='black',fg='orange').pack()
        Nombre = StringVar()
        Entry_Nombre = Entry(root, textvariable=Nombre)
        Entry_Nombre.pack()
        lbl_Cedula= Label(root, text='Cédula:',bg='black',fg='orange').pack()
        Cedula = IntVar()
        Entry_Cedula = Entry(root, textvariable=Cedula)
        Entry_Cedula.pack()
        Clase= IntVar()
        Ubicacion_ = IntVar()
        centro = Checkbutton(root, text='Centro',variable=Ubicacion_, onvalue=3,bg='black',fg='orange')
        def Ubicacion(x):
            centro.place(x=-5000,y=-5000)
            Label_ubicacion = Label(root, text='Ubicación:',bg='black',fg='orange').place(x=120,y=125)
            ventana = Checkbutton(root, text='Ventana',variable=Ubicacion_, onvalue=1,bg='black',fg='orange')
            ventana.place(x=70,y=145)
            pasillo = Checkbutton(root, text='Pasillo',variable=Ubicacion_, onvalue=2,bg='black',fg='orange')
            pasillo.place(x=140,y=145)
            if x==1:
                centro.place(x=200,y=145)  
        def Disponibilidad_Asiento(x,y):
            disponibilidad_asiento=0
            for i in range(x,y):
                disponibilidad_asiento+=Asiento_Status[i]
            return disponibilidad_asiento
        def Reservar():
            global Disponibilidad
            def Modificar_Status_Asiento(tupla_asientos):
                asiento=""
                asientos=[]
                for i in tupla_asientos:
                    if Asiento_Status[i]==1:
                        asiento=i
                        break
                for i in tupla_asientos:
                    asientos.append(Asiento_Status[i])
                if sum(asientos)==0:
                    messagebox.showinfo('Falta de disponibilidad','No hay asientos con esta ubicación disponibles.')
                elif sum(asientos)!=0:
                        Nombres_Pasajeros[asiento]=Nombre.get()
                        Cedulas_Pasajeros[asiento]=Cedula.get()
                        Asiento_Status[asiento]=0
                        Asiento_Status[0]=str(asiento)
            if Clase.get()==1:
                if Disponibilidad_Asiento(1,8)==0:
                    messagebox.showinfo('Falta de disponibilidad','No hay asientos disponibles.')
                    Disponibilidad=False
                elif Disponibilidad_Asiento(1,8)!=0:
                    if Ubicacion_.get()==1:
                        Modificar_Status_Asiento((1,4,5,8))
                    elif Ubicacion_.get()==2:
                        Modificar_Status_Asiento((2,3,6,7))
            elif Clase.get()==2:
                if Disponibilidad_Asiento(9,50)==0:
                    messagebox.showinfo('Falta de disponibilidad','No hay asientos disponibles.')
                    Disponibilidad=False
                elif Disponibilidad_Asiento(9,50)!=0:
                    if Ubicacion_.get()==1:
                        Modificar_Status_Asiento((9,14,15,20,21,26,27,32,33,38,39,44,45,50))
                    elif Ubicacion_.get()==2:
                        Modificar_Status_Asiento((11,12,17,18,23,24,29,30,35,36,41,42,47,48))
                    elif Ubicacion_.get()==3:
                        Modificar_Status_Asiento((10,13,16,19,22,25,28,31,34,37,40,43,46,49))
            if Disponibilidad==True:
                string = 'Su asiento ha sido asignado\nNumero de asiento: {0}'.format(Asiento_Status[0])
                messagebox.showinfo('Reserva exitosa', string)
                Limpiar_root_y_toplevel(1)
                root.withdraw()
                sillas()
        Label_Clase = Label(root, text='Clase:',bg='black',fg='orange').pack()  
        Ejecutiva = Checkbutton(root, text='Ejecutiva', variable=Clase, onvalue=1, command= lambda: Ubicacion(0),bg='black',fg='orange')
        Ejecutiva.place(x=70,y=100)
        Economica = Checkbutton(root, text='Económica', variable=Clase, onvalue=2, command= lambda: Ubicacion(1),bg='black',fg='orange')
        Economica.place(x=150,y=100)
        Btn_Reservar = Button(root, text='Reservar pasaje', command=Reservar,bg='black',fg='orange',font=('Open Sans',11)).place(x=85,y=175)    
    btn_Registrar = Button(Botonera, text='Registrar pasajero', command=Registrar_Pasajero,width=24,bg='black',fg='orange').pack(side=LEFT)
    def Eliminar_Pasajero():
        root.deiconify()
        root.title('Eliminación de Reserva')
        lbl_Cedula= Label(root, text='Cédula:',bg='black',fg='orange',font=('Open Sans',11)).pack()
        Cedula_ = IntVar()
        Entry_Cedula = Entry(root, textvariable=Cedula_)
        Entry_Cedula.pack()
        def Confirmar():
                for i in range(len(Cedulas_Pasajeros)):
                    if Cedula_.get()==Cedulas_Pasajeros[i]:
                        Cedulas_Pasajeros[i]=""
                        Nombres_Pasajeros[i]=""
                        Asiento_Status[i]=1
                        break
                Limpiar_root_y_toplevel(1)
                root.withdraw()
                sillas()
                messagebox.showinfo('Reserva eliminada','La reserva ha sido eliminada.')
        btn_Confirmar = Button(root, text='Confirmar',command=Confirmar,bg='black',fg='orange',font=('Open Sans',11)).pack()
    btn_Eliminar = Button(Botonera, text='Eliminar pasajero', command = Eliminar_Pasajero, width=24,bg='black',fg='orange').pack(side=LEFT)
    def Buscar_Pasajero():
        root.deiconify()
        root.title('Busca de Reserva')
        lbl_Cedula= Label(root, text='Cédula:',bg='black',fg='orange',font=('Open Sans',11)).pack()
        Cedula_2 = IntVar()
        Entry_Cedula = Entry(root, textvariable=Cedula_2)
        Entry_Cedula.pack()
        def Buscar():
                if Cedula_2.get() in Cedulas_Pasajeros:
                    pasajero_=0
                    for i in range(len(Cedulas_Pasajeros)):
                        if Cedula_2.get()==Cedulas_Pasajeros[i]:
                            pasajero_=i
                            break
                    string = 'Pasajero con cédula: {0}\nNombre: {1}\nAsiento: {2}'.format(Cedulas_Pasajeros[pasajero_],Nombres_Pasajeros[pasajero_],pasajero_)
                    messagebox.showinfo('Pasajero Encontrado',string)
                else:
                    messagebox.showinfo('Pasajero no Registrado','No se ha encontrado un pasajero con esa Cédula.')
                Limpiar_root_y_toplevel(2)
                root.withdraw()
        btn_Buscar = Button(root, text='Confirmar',command=Buscar,bg='black',fg='orange',font=('Open Sans',11)).pack()
    btn_Buscar = Button(Botonera, text='Buscar pasajero',width=24,command=Buscar_Pasajero,bg='black',fg='orange').pack(side=LEFT)
    def Porcentaje_Ocupacion():
        def percentage(part, whole):
            return 100 * float(part)/float(whole)
        ocupacion_=0
        for i in range(1,51):
            ocupacion_+=Asiento_Status[i]
        Asientos_R = Asiento_Status.count(0)
        Asientos_L = Asiento_Status.count(1)
        porcentaje_ocup=100.0-percentage(ocupacion_,50)
        string='Asientos Reservados: {0}\nAsientos Libres: {1}\nPorcentaje de Ocupación: {2}%'.format(Asientos_R,Asientos_L,porcentaje_ocup)
        messagebox.showinfo('Datos de Ocupacion',string)
    btn_Porcentaje_Ocup = Button(Botonera, text='Porcentaje Ocupacion',width=20,command=Porcentaje_Ocupacion,bg='black',fg='orange').pack(side=LEFT)
#GUI
plane = ImageTk.PhotoImage(Image.open(r'C:\Users\Agus\Downloads\planeres.jpg'))
panel = Label(window, image = plane)
panel.place(x=0,y=0)
panel.image = plane
sillas()
Requerimientos()

root.mainloop()
