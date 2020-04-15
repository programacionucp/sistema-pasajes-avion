from tkinter import *



vp = Tk()
vp.geometry("700x600")
vp.title("Reserva de asientos")

IzquierdaFrame = Frame(vp, width="300", height="400", bd=8, relief="raise")
IzquierdaFrame.place(x=50,y=0)
DerechaFrame = Frame(vp, width="300", height="400", bd=8, relief="raise")
DerechaFrame.place(x=350,y=0)
BaseFrame = Frame(vp, width="600", height="100", bd=8, relief="raise")
BaseFrame.place(x=50,y=450)
divisionFrame = Frame(vp, width="600", height="10", bd=8, relief="raise")
divisionFrame.place(x=50,y=120)

#Asientos ejercutivos/primera clase
A1=Label(vp,text="A1",bg="yellow", font=("Arial",12)).place(x=100,y=40)
A2=Label(vp,text="A2",bg="yellow", font=("Arial",12)).place(x=250,y=40)
A3=Label(vp,text="A3",bg="yellow", font=("Arial",12)).place(x=400,y=40)
A4=Label(vp,text="A4",bg="yellow", font=("Arial",12)).place(x=550,y=40)
A5=Label(vp,text="A5",bg="yellow", font=("Arial",12)).place(x=100,y=90)
A6=Label(vp,text="A6",bg="yellow", font=("Arial",12)).place(x=250,y=90)
A7=Label(vp,text="A7",bg="yellow", font=("Arial",12)).place(x=400,y=90)
A8=Label(vp,text="A8",bg="yellow", font=("Arial",12)).place(x=550,y=90)

#Asientos turistas
A9=Label(vp,text="A9",bg="deep sky blue", font=("Arial",12)).place(x=100,y=150)
A10=Label(vp,text="A10",bg="deep sky blue", font=("Arial",12)).place(x=250,y=150)
A11=Label(vp,text="A11",bg="deep sky blue", font=("Arial",12)).place(x=400,y=150)
A12=Label(vp,text="A12",bg="deep sky blue", font=("Arial",12)).place(x=550,y=150)
A13=Label(vp,text="A13",bg="deep sky blue", font=("Arial",12)).place(x=100,y=200)
A14=Label(vp,text="A14",bg="deep sky blue", font=("Arial",12)).place(x=250,y=200)
A15=Label(vp,text="A15",bg="deep sky blue", font=("Arial",12)).place(x=400,y=200)
A16=Label(vp,text="A16",bg="deep sky blue", font=("Arial",12)).place(x=550,y=200)
A17=Label(vp,text="A17",bg="deep sky blue", font=("Arial",12)).place(x=100,y=250)
A18=Label(vp,text="A18",bg="deep sky blue", font=("Arial",12)).place(x=250,y=250)
A19=Label(vp,text="A19",bg="deep sky blue", font=("Arial",12)).place(x=400,y=250)
A20=Label(vp,text="A20",bg="deep sky blue", font=("Arial",12)).place(x=550,y=250)

#botones
btn1 = Button(vp,text="Registrar Pasajero",bd=5, width=17,fg="gray25",bg="sky blue", font=("Arial",11)).place(x=70,y=460)
btn2 = Button(vp,text="Eliminar Pasajero",bd=5, width=17,fg="gray25",bg="sky blue", font=("Arial",11)).place(x=270,y=460)
btn3 = Button(vp,text="Buscar Pasajero",bd=5, width=17,fg="gray25",bg="sky blue", font=("Arial",11)).place(x=470,y=460)
btn4 = Button(vp,text="Porcentaje Ocupacion",bd=5, width=17,fg="gray25",bg="sky blue", font=("Arial",11)).place(x=70,y=500)
btn5 = Button(vp,text="Opcion 1",bd=5, width=17,fg="gray25",bg="sky blue", font=("Arial",11)).place(x=270,y=500)
btn6 = Button(vp,text="Opcion 2",bd=5, width=17,fg="gray25",bg="sky blue", font=("Arial",11)).place(x=470,y=500)

vp.mainloop()
