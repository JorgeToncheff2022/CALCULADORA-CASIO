from tkinter import *

ventana=Tk()
def presionar(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)

def calculo():
    global operador
    try:
        oper=str(eval(operador))
        input_text.set(oper)
    except:
        input_text.set("ERROR")
    operador=""      


i = 0
def borrar(num):
    global i 

    input_text.delete(0,END)
    i = 0


 

input_text=StringVar()
operador=""

#Agregar formato a la ventana
ventana.title("CALCULADORA CASIO")
ventana.resizable(width=False, height=False)


#Agregamos una variable que va a contener el formato de los botones
anchoBoton=7
altoBoton=2
colorBoton=("#747f91")
color2=("#FF5733")

display=Entry(ventana, font=("arial",18, "bold"), bd=20, insertwidth=5, bg="#EFEBE9", justify="right", textvariable=input_text)
display.grid(row=0,column=0,columnspan=5)

#Agregamos los botones con numeros
Button(ventana,text=7, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(7)).grid(row=1,column=0)
Button(ventana,text=8, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(8)).grid(row=1,column=1)
Button(ventana,text=9, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(9)).grid(row=1,column=2)

Button(ventana,text=4, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(4)).grid(row=2,column=0)
Button(ventana,text=5, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(5)).grid(row=2,column=1)
Button(ventana,text=6, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(6)).grid(row=2,column=2)

Button(ventana,text=1, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(1)).grid(row=3,column=0)
Button(ventana,text=2, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(2)).grid(row=3,column=1)
Button(ventana,text=3, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(3)).grid(row=3,column=2)

Button(ventana,text=".", bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(".")).grid(row=4,column=0)
Button(ventana,text=0, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:presionar(0)).grid(row=4,column=1)
Button(ventana,text="=", bg=color2, width=anchoBoton, height=altoBoton, command=lambda:calculo()).grid(row=4,column=2)
Button(ventana,text="(", background=("#BDBDBD"), width=anchoBoton, height=altoBoton, command=lambda:presionar("(")).grid(row=4,column=3)
Button(ventana,text=")", background=("#BDBDBD"), width=anchoBoton, height=altoBoton, command=lambda:presionar(")")).grid(row=4,column=4)
#Agregamos los botones con los operadores

Button(ventana,text="C", bg=color2, width=anchoBoton, height=altoBoton, command=lambda:presionar("C")).grid(row=1,column=3)
Button(ventana,text="AC", bg=color2, width=anchoBoton, height=altoBoton, command=lambda:borrar("AC ")).grid(row=1,column=4)

Button(ventana,text="+", background=("#BDBDBD"),width=anchoBoton, height=altoBoton, command=lambda:presionar("+")).grid(row=2,column=3)
Button(ventana,text="-", background=("#BDBDBD"),width=anchoBoton, height=altoBoton, command=lambda:presionar("-")).grid(row=2,column=4)

Button(ventana,text="*", background=("#BDBDBD"),width=anchoBoton, height=altoBoton, command=lambda:presionar("*")).grid(row=3,column=3)
Button(ventana,text="/", background=("#BDBDBD"),width=anchoBoton, height=altoBoton, command=lambda:presionar("/")).grid(row=3,column=4)


ventana.mainloop()