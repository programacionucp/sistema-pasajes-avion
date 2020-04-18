from tkinter import *
import tkinter as tk
from tkinter import ttk


master = tk.Tk()
master.geometry("640x420")
master.title("Pasajes de avion")




def regPas(pasaj,dni,clase,lugar):
    cont=0
    if int(clase) == 0:
        clase="tur"
    else:
        clase="eje"
    if int(lugar) == 0:
        lugar = "ven"
    elif int(lugar) == 1:
        lugar="cen"
    elif int(lugar) == 2:
        lugar="pas"
    for i in asientos:
        if i[2] == clase:
            if i[3] == lugar:
                    if i[1] == "lib":
                        asientos[cont]=[str(cont+1),"ocup",clase,lugar,dni,pasaj]
                        barrProg['value'] = progreso()
                        lblProg.configure(text=str(progreso()) + "/50  %"+str(round((progreso()/50)*100,1)))
                        if clase == "tur":
                            btnAsientos[cont].configure(background="#ff4747")
                        else:
                            btnAsientos[cont].configure(background="#fca644")
                        break
        cont+= 1

def elimPas(dni):
    dni=str(dni)
    cont=0
    for i in asientos:
        if i[4] == dni:
            asientos[cont][1]="lib"
            barrProg['value'] = progreso()
            lblProg.configure(text=str(progreso()) + "/50  %"+str(round((progreso()/50)*100,1)))
            asientos[cont].pop()
            asientos[cont].pop()
            if i[2] == "tur":
                btnAsientos[cont].configure(background="#42bcf5")
            else:
                btnAsientos[cont].configure(background="#e6f542")
            break
        cont+=1

def progreso():
    ocupados=0
    for i in asientos:
        if i[1] == "ocup":
            ocupados+=1
    return ocupados

def busPas(dni):
    dni = str(dni)
    for i in asientos:
        if i[4] == dni:
            if i[2] == "tur":
                i[2]="Turista"
            else:
                i[2] = "Ejecutiva"
            if i[3] == "ven":
                i[3] = "Ventana"
            elif i[3] == "cen":
                i[3] = "Centro"
            else:
                i[3] = "Pasillo"
            lblNomb.configure(text=i[5])
            lblAsiento.configure(text=i[0])
            lblClase.configure(text=i[2])
            lblLugar.configure(text=i[3])
            break

asientos=[]
for i in range(50):
    asientos.append([str(i+1),"lib"])
    if i < 8:
        asientos[i].append("eje")
        if i == 0 or i == 3 or i == 4 or i == 7:
            asientos[i].append("ven")
        else:
            asientos[i].append("pas")
    else:
        asientos[i].append("tur")
        if i == 8 or i == 13 or i == 14 or i == 19 or i == 20 or i == 25 or i == 26 or i == 31 or i == 32 or i == 37 or i == 38 or i == 43 or i == 44 or i == 49:
            asientos[i].append("ven")
        elif i == 9 or i == 12 or i == 15 or i == 18 or i == 21 or i == 24 or i == 27 or i == 30 or i == 33 or i == 36 or i == 39 or i == 42 or i == 45 or i == 48 :
            asientos[i].append("cen")
        else:
            asientos[i].append("pas")
    asientos[i].append("")
    asientos[i].append("")

#master.grid_rowconfigure(2, weight=1)
#master.grid_columnconfigure(1, weight=1)

frmReg=Frame(master,width=200,height=400,highlightbackground = "black",highlightthickness = 1)
frmReg.place(x=10,y=10)
frmPasaj=Frame(master,width=200,height=400,highlightbackground = "black",highlightthickness = 1)
frmPasaj.place(x=220,y=10)
frmPasajAsientos=Frame(frmPasaj,width=100,height=300,highlightbackground = "black",highlightthickness = 1)
frmPasajAsientos.place(x=50,y=50)
frmElim=Frame(master,width=200,height=100,highlightbackground = "black",highlightthickness = 1)
frmElim.place(x=430,y=10)
frmPorc=Frame(master,width=200,height=100,highlightbackground = "black",highlightthickness = 1)
frmPorc.place(x=432,y=125)
frmBusc=Frame(master,width=200,height=194,highlightbackground = "black",highlightthickness = 1)
frmBusc.place(x=430,y=217)


frmReg.grid_rowconfigure(5,weight=0)
frmReg.grid_columnconfigure(3,weight=0)

#espacio en blanco#
Label(frmReg,text="",width=15).grid(row=0,columnspan=3)
#espacio en blanco#
Label(frmReg,text="Nombre y Apellido:",width=15).grid(row=1,column=0)
entPasaj=Entry(frmReg,width=15)
entPasaj.grid(row=1,column=1)

#espacio en blanco#
Label(frmReg,text="",width=15).grid(row=2,columnspan=3)
#espacio en blanco#

Label(frmReg,text="DNI:",width=15).grid(row=3,column=0)
entDni=Entry(frmReg,width=15)
entDni.grid(row=3,column=1)

#espacio en blanco#
Label(frmReg,text="",width=15).grid(row=4,columnspan=3)
#espacio en blanco#

Label(frmReg,text="Clase:",width=15).grid(row=5,columnspan=3)
clase=IntVar()
rdbtnClasTur=Radiobutton(frmReg,text="Turista",variable=clase,value=0)
rdbtnClasEjec=Radiobutton(frmReg,text="Ejecutivo",variable=clase,value=1)
rdbtnClasTur.grid(row=6,column=0)
rdbtnClasEjec.grid(row=6,column=1)

#espacio en blanco#
Label(frmReg,text="",width=15).grid(row=7,columnspan=3)
#espacio en blanco#

Label(frmReg,text="Lugar:",width=15).grid(row=8,columnspan=3)
lugar=IntVar()
rdbtnLugVent=Radiobutton(frmReg,text="Ventana",variable=lugar,value=0)
rdbtnLugCentro=Radiobutton(frmReg,text="Centro",variable=lugar,value=1)
rdbtnLugPas=Radiobutton(frmReg,text="Pasillo",variable=lugar,value=2)
rdbtnLugVent.grid(row=9,column=0)
rdbtnLugCentro.grid(row=9,column=1)
rdbtnLugPas.grid(row=10,columnspan=2)

#espacios en blanco
Label(frmReg,text="",width=15).grid(rowspan=4,columnspan=3)
Label(frmReg,text="",width=15).grid(rowspan=4,columnspan=3)
Label(frmReg,text="",width=15).grid(rowspan=4,columnspan=3)
Label(frmReg,text="",width=15).grid(rowspan=4,columnspan=3)
Label(frmReg,text="",width=15).grid(rowspan=4,columnspan=3)

#Frame de asientos
btnAsientos=[]
for i in range(50):
    btnAsientos.append(Button(frmPasajAsientos,text=i+1,width=1))
    if i < 8:
        btnAsientos[i].configure(background="#e6f542")
    else:
        btnAsientos[i].configure(background="#42bcf5")


btnReg=Button(frmReg,text="Registrar pasajero",width=20,command=lambda:regPas(entPasaj.get(),entDni.get(),clase.get(),lugar.get()))
btnReg.grid(rowspan=7,columnspan=3)

Label(frmReg,text="",width=15).grid(rowspan=4,columnspan=3)


frmPasajAsientos.grid_rowconfigure(4,weight=1)
frmPasajAsientos.grid_columnconfigure(8,weight=1)



fila=0
btnAsientos[0].grid(row=fila,column=0)
Label(frmPasajAsientos,text="").grid(row=fila,column=1)
btnAsientos[1].grid(row=fila,column=2)
Label(frmPasajAsientos,text="").grid(row=fila,column=3)
Label(frmPasajAsientos,text="").grid(row=fila,column=4)
btnAsientos[2].grid(row=fila,column=5)
Label(frmPasajAsientos,text="").grid(row=fila,column=6)
btnAsientos[3].grid(row=fila,column=7)

fila=1
btnAsientos[4].grid(row=fila,column=0)
Label(frmPasajAsientos,text="").grid(row=fila,column=1)
btnAsientos[5].grid(row=fila,column=2)
Label(frmPasajAsientos,text="").grid(row=fila,column=3)
Label(frmPasajAsientos,text="").grid(row=fila,column=4)
btnAsientos[6].grid(row=fila,column=5)
Label(frmPasajAsientos,text="").grid(row=fila,column=6)
btnAsientos[7].grid(row=fila,column=7)

fila=2
btnAsientos[8].grid(row=fila,column=0)
btnAsientos[9].grid(row=fila,column=1)
btnAsientos[10].grid(row=fila,column=2)
Label(frmPasajAsientos,text="").grid(row=fila,column=3)
Label(frmPasajAsientos,text="").grid(row=fila,column=4)
btnAsientos[11].grid(row=fila,column=5)
btnAsientos[12].grid(row=fila,column=6)
btnAsientos[13].grid(row=fila,column=7)

fila=3
btnAsientos[14].grid(row=fila,column=0)
btnAsientos[15].grid(row=fila,column=1)
btnAsientos[16].grid(row=fila,column=2)
Label(frmPasajAsientos,text="").grid(row=fila,column=3)
Label(frmPasajAsientos,text="").grid(row=fila,column=4)
btnAsientos[17].grid(row=fila,column=5)
btnAsientos[18].grid(row=fila,column=6)
btnAsientos[19].grid(row=fila,column=7)

fila=4
btnAsientos[20].grid(row=fila,column=0)
btnAsientos[21].grid(row=fila,column=1)
btnAsientos[22].grid(row=fila,column=2)
Label(frmPasajAsientos,text="").grid(row=fila,column=3)
Label(frmPasajAsientos,text="").grid(row=fila,column=4)
btnAsientos[23].grid(row=fila,column=5)
btnAsientos[24].grid(row=fila,column=6)
btnAsientos[25].grid(row=fila,column=7)

fila=5
btnAsientos[26].grid(row=fila,column=0)
btnAsientos[27].grid(row=fila,column=1)
btnAsientos[28].grid(row=fila,column=2)
Label(frmPasajAsientos,text="").grid(row=fila,column=3)
Label(frmPasajAsientos,text="").grid(row=fila,column=4)
btnAsientos[29].grid(row=fila,column=5)
btnAsientos[30].grid(row=fila,column=6)
btnAsientos[31].grid(row=fila,column=7)

fila=6
btnAsientos[32].grid(row=fila,column=0)
btnAsientos[33].grid(row=fila,column=1)
btnAsientos[34].grid(row=fila,column=2)
Label(frmPasajAsientos,text="").grid(row=fila,column=3)
Label(frmPasajAsientos,text="").grid(row=fila,column=4)
btnAsientos[35].grid(row=fila,column=5)
btnAsientos[36].grid(row=fila,column=6)
btnAsientos[37].grid(row=fila,column=7)

fila=7
btnAsientos[38].grid(row=fila,column=0)
btnAsientos[39].grid(row=fila,column=1)
btnAsientos[40].grid(row=fila,column=2)
Label(frmPasajAsientos,text="").grid(row=fila,column=3)
Label(frmPasajAsientos,text="").grid(row=fila,column=4)
btnAsientos[41].grid(row=fila,column=5)
btnAsientos[42].grid(row=fila,column=6)
btnAsientos[43].grid(row=fila,column=7)

fila=8
btnAsientos[44].grid(row=fila,column=0)
btnAsientos[45].grid(row=fila,column=1)
btnAsientos[46].grid(row=fila,column=2)
Label(frmPasajAsientos,text="").grid(row=fila,column=3)
Label(frmPasajAsientos,text="").grid(row=fila,column=4)
btnAsientos[47].grid(row=fila,column=5)
btnAsientos[48].grid(row=fila,column=6)
btnAsientos[49].grid(row=fila,column=7)

#elementos de frame eliminar pasajero
frmElim.grid_rowconfigure(2,weight=1)
frmElim.grid_columnconfigure(2,weight=1)

Label(frmElim,text="").grid(row=0,columnspan=2)
Label(frmElim,text="DNI a borrar:",width=15).grid(row=1,column=0)
entDniBorrar=Entry(frmElim,width=14)
entDniBorrar.grid(row=1,column=1)
Label(frmElim,text="").grid(row=2,columnspan=2)
btnBorrarPas=Button(frmElim,text="Borrar pasajero",width=25,command= lambda : elimPas(entDniBorrar.get()))
btnBorrarPas.grid(row=3,columnspan=2)
Label(frmElim,text="").grid(row=4,columnspan=2)



#elementos de frame porcentaje
frmPorc.grid_rowconfigure(2,weight=1)
frmPorc.grid_columnconfigure(2,weight=1)

Label(frmPorc,text="").grid(row=0,columnspan=3)
Label(frmPorc,text="Porcentaje de ocupacion:",width=27).grid(row=1,column=0)

barrProg=ttk.Progressbar(frmPorc,orient = HORIZONTAL,
              length = 150, mode = 'determinate', maximum=50)
barrProg.grid(row=2,columnspan=3)
barrProg['value']=progreso()
lblProg=Label(frmPorc,text=str(progreso())+"/50  %"+str(round((progreso()/50)*100,1)))
lblProg.grid(row=3,columnspan=3)

#elementos del frame buscar pasajero
dni = StringVar(master)
dni.set("DNI")

Label(frmBusc,text="").grid(row=0,columnspan=2)

Label(frmBusc,text="DNI a buscar:",width=15).grid(row=1,column=0)
entDniBuscar=Entry(frmBusc,width=14)
entDniBuscar.grid(row=1,column=1)
btnBuscar=Button(frmBusc,text="buscar",command= lambda : busPas(entDniBuscar.get()))
btnBuscar.grid(row=2,columnspan=2)

Label(frmBusc,text="Pasajero:").grid(row=3,column=0)
lblNomb=Label(frmBusc,text="")
lblNomb.grid(row=3,column=1)

Label(frmBusc,text="Asiento:").grid(row=4,column=0)
lblAsiento=Label(frmBusc,text="")
lblAsiento.grid(row=4,column=1)

Label(frmBusc,text="Clase:").grid(row=5,column=0)
lblClase=Label(frmBusc,text="")
lblClase.grid(row=5,column=1)

Label(frmBusc,text="Lugar:").grid(row=6,column=0)
lblLugar=Label(frmBusc,text="")
lblLugar.grid(row=6,column=1)

master.mainloop()