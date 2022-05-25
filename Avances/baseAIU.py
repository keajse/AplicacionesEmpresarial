from tkinter import *
from tkinter import messagebox as msg

vnta = Tk()


def baseAiu():
    adm = admon.get()
    imp = impre.get()
    uti = util.get()
    iva = iv.get()
    tot = total.get()
    rtaFin = rtaFinal.get()

    adm = adm /100
    imp = imp / 100
    uti = uti /100
    iva = iva /100

    base = tot / (1+ (adm + imp + uti + iva))

    rtaFin = rtaFinal.set(base)

    return rtaFin
   


vnta.geometry("400x520")
vnta.config(bg="#C7F9F4")
vnta.title("Base del AIU")
vnta.maxsize(width=400, height=520)

admon = DoubleVar
util = DoubleVar
impre = DoubleVar
iv = DoubleVar
total = DoubleVar
rtaFinal = DoubleVar

espacio = Label(vnta,bg="#C7F9F4").pack()
lblDescripcion = Label(vnta,bg="#C7F9F4", text="Plantilla para calcular base del AIU", font=("Arial",14), fg="red").pack()

lblTotal = Label(vnta,bg="#C7F9F4", text="Total", font=("Arial",14)).place(x=30, y=80)
totalF = Entry(vnta, textvariable= total, width=10, fg="black", font=("Arial",20, "bold")).place(x=200, y=80)

lblAdm = Label(vnta,bg="#C7F9F4", text="Administración", font=("Arial",14)).place(x=30, y=140)
administracion = Entry(vnta, textvariable= admon, width=10, fg="black", font=("Arial",20, "bold")).place(x=200, y=140)

lblImp= Label(vnta,bg="#C7F9F4", text="Imprevistos", font=("Arial",14)).place(x=30, y=180)
imprevistos = Entry(vnta, textvariable= impre, width=10, fg="black", font=("Arial",20, "bold")).place(x=200, y=180)

lblUti = Label(vnta,bg="#C7F9F4", text="Utilidad", font=("Arial",14)).place(x=30, y=220)
utilidad = Entry(vnta, textvariable= util, width=10, fg="black", font=("Arial",20, "bold")).place(x=200, y=220)

lblIva = Label(vnta,bg="#C7F9F4", text="IVA", font=("Arial",14)).place(x=30, y=260)
IVA = Entry(vnta, textvariable= iv, width=10, fg="black", font=("Arial",20, "bold")).place(x=200, y=260)

boton = Button(vnta, text="Calcular", font=("Arial", 14), command=lambda: baseAiu).place(x=100, y=400)

baseA = Label(vnta,bg="#C7F9F4", text="Base AIU", font=("Arial",14, "bold"), fg="red").place(x=30, y=320)
rta = Entry(vnta, textvariable= rtaFinal, width=10, fg="black", font=("Arial",20, "bold")).place(x=200, y=320)

realizado = Label(vnta, text="Realizado por Laura Juliana Serrano García - Makeajse 2022", bg="#C7F9F4").pack(side="bottom")

vnta.mainloop()