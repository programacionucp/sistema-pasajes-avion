import principal as pr
from tkinter import *
import tkinter as tk


master = tk.Tk()
master.geometry("640x420")
master.title("Pasajes de avion")

#master.grid_rowconfigure(2, weight=1)
#master.grid_columnconfigure(1, weight=1)

frmReg=Frame(master,width=200,height=400,highlightbackground = "black",highlightthickness = 1)
frmReg.place(x=10,y=10)
frmPasaj=Frame(master,width=200,height=400,highlightbackground = "black",highlightthickness = 1)
frmPasaj.place(x=220,y=10)
frmPasajAsientos=Frame(frmPasaj,width=100,height=300,highlightbackground = "black",highlightthickness = 1)
frmPasajAsientos.place(x=50,y=50)
#frmElim=Frame(master,width=200,height=100,highlightbackground = "black",highlightthickness = 1)
#frmElim.place(x=430,y=10)
#frmPorc=Frame(master,width=200,height=100,highlightbackground = "black",highlightthickness = 1)
#frmPorc.place(x=430,y=111)
#frmBusc=Frame(master,width=200,height=198,highlightbackground = "black",highlightthickness = 1)
#frmBusc.place(x=430,y=212)


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




btnReg=Button(frmReg,text="Registrar pasajero",width=20,command=lambda:pr.resPas(entPasaj.get(),entDni.get(),clase.get(),lugar.get()))
btnReg.grid(rowspan=7,columnspan=3)

Label(frmReg,text="",width=15).grid(rowspan=4,columnspan=3)


frmPasajAsientos.grid_rowconfigure(4,weight=1)
frmPasajAsientos.grid_columnconfigure(8,weight=1)

#Frame de asientos
btnAsientos=[]
for i in range(50):
    btnAsientos.append(Button(frmPasajAsientos,text=i+1,width=1))
    if i < 8:
        btnAsientos[i].configure(background="#e6f542")
    else:
        btnAsientos[i].configure(background="#42bcf5")

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

fila=7
btnAsientos[44].grid(row=fila,column=0)
btnAsientos[45].grid(row=fila,column=1)
btnAsientos[46].grid(row=fila,column=2)
Label(frmPasajAsientos,text="").grid(row=fila,column=3)
Label(frmPasajAsientos,text="").grid(row=fila,column=4)
btnAsientos[47].grid(row=fila,column=5)
btnAsientos[48].grid(row=fila,column=6)
btnAsientos[49].grid(row=fila,column=7)


master.mainloop()