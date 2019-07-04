from tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
class Castorena:
    def save_file(self): 
        list = []                
        list = self.get_Values()         
        Texto= "Nombre :  "+self.txtnombre.get()+"\n"+"Edad :  "+str(self.Edad.get())+"\n"+"Sexo :  "+str(self.Sexo.get())+"\n"+"Peso :  "+str(self.Peso.get())+"kg"+"\n"+"Estatura :  "+str(self.Estatura.get())+"cm"+"\n"+"Imc :  "+str(list[0])+" - "+list[2]+"\n"+"pesoideal :  "+str(list[1])+"kg" + "\n"

        archivo = open("/Users/Castorena/Desktop/Paco.txt", 'w')

        archivo.write(Texto)
        archivo.close()

    def get_Values(self):
        list = []
        peso = float(self.Peso.get())
        estatura = float(self.Estatura.get())
        imc = (peso / (estatura* estatura))
        list.append(imc)
        pesoideal = 0.75*(estatura-150)+50
        list.append(pesoideal)

        if(imc<18.5):
         list.append("Peso inferior al normal")
       
        if(imc>18.5 and imc <24.9):
         list.append("Normal")
        
        if(imc>25.0 and imc <29.9):
         list.append( "Peso superior al normal")
         
        if(imc >30.0):
         list.append("Obesidad")

        return list


    def calcular(self):
         
         if(str(self.Edad.get()).isdigit()==True):
          list = []
          list = self.get_Values()

          lb= Label(self.instancia_de_Tk, text="Nombre :  "+self.txtnombre.get(),font=("Agency fb",14)).place(x=10,y=210)
          lb= Label(self.instancia_de_Tk, text="Edad :  "+str(self.Edad.get()),font=("Agency fb",14)).place(x=10,y=250)
          lb= Label(self.instancia_de_Tk, text="Sexo :  "+str(self.Sexo.get()),font=("Agency fb",14)).place(x=10,y=290)
          lb= Label(self.instancia_de_Tk, text="Peso :  "+str(self.Peso.get()),font=("Agency fb",14)).place(x=10,y=330)
          lb= Label(self.instancia_de_Tk, text="Estatura :  "+str(self.Estatura.get()),font=("Agency fb",14)).place(x=10,y=370)
          lb= Label(self.instancia_de_Tk, text="Imc :  "+str(list[0])+" - "+list[2],font=("Agency fb",14)).place(x=10,y=330)
          lb= Label(self.instancia_de_Tk, text="pesoideal :  "+str(list[1])+"kg",font=("Agency fb",14)).place(x=10,y=370)

         if(str(self.Edad.get()).isdigit()==False):
          messagebox.showinfo(message="El campo de edad esta incorrecto", title="BUGS")
         


    def __init__(self, instancia_de_Tk): 

        self.instancia_de_Tk= instancia_de_Tk;

        instancia_de_Tk.geometry("400x600+100+100")
        instancia_de_Tk.title ("Calculador del Índice de Masa Corporal")

        lb= Label(instancia_de_Tk, text="Nombre",font=("Agency fb",14)).place(x=10,y=10)
        self.txtnombre= StringVar() 
        entry1= tk.Entry(instancia_de_Tk,textvariable=self.txtnombre).place(x=70,y=20)



        lb= Label(text="Edad",font=("Agency fb",14)).place(x=10,y=50)
        self.Edad = StringVar()
        txtEdad = Entry(instancia_de_Tk,textvariable=self.Edad).place(x=70,y=60)


        lb= Label(text="Sexo",font=("Agency fb",14)).place(x=10,y=90)
        self.Sexo = StringVar()
        ComboSexo = Combobox(instancia_de_Tk,textvariable = self.Sexo , state="readonly",values=["Masculino", "Femenino"]).place(x=70, y=100)


        lb = Label(text="Estatura (cm) ",font=("Agency fb",14)).place(x=10,y=130)
        self.Estatura = DoubleVar()
        txtEstatura = Entry(instancia_de_Tk,textvariable=self.Estatura).place(x=110,y=140)

        lb= Label(text="Peso (kg) ",font=("Agency fb",14)).place(x=10,y=170)
        self.Peso = DoubleVar()
        txtPeso= Entry(instancia_de_Tk,textvariable=self.Peso).place(x=100,y=180)
        
        button1 = Button(instancia_de_Tk, text="Calcular", command=self.calcular).place(x=70, y = 500)
        button2 = Button(instancia_de_Tk, text="Guardar", command=self.save_file).place(x=280, y = 500)

ventana = Tk()
Castorena(ventana)
ventana.title("Calculadora IMC")
ventana.mainloop()