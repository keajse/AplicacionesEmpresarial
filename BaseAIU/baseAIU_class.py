from dataclasses import replace
from tkinter import StringVar, Tk,Label,Button,Entry, Frame
from tkinter import messagebox
from tokenize import Double, String
import locale
locale.setlocale(locale.LC_ALL, '')



class FrBaseAIU(Frame):

    def __init__(self, master=None):
        super().__init__(master,width=320, height=500)
        self.master = master
        self.pack()
        self.create_widgets()
        

    def fBaseAIU(self):

        total=self.txtTotal.get()
        adm=self.txtAdmon.get()
        imp=self.txtImpr.get()
        uti=self.txtUtil.get()
        iva=self.txtIva.get()

        if adm == "":
            adm = 0

        if imp == "":
            imp = 0
        
        if uti == "":
            uti = 0
        
        if iva == "":
            iva = 0

        if total == "":
            messagebox.showinfo("FALTA DATO", "Paz y bien, falta ingresar el valor que contiene el AIU")
            total = 0       
    

        adm1 = float(adm)
        imp1 = float(imp)
        uti1 = float(uti)
        iva1 = float(iva)
        tot = float(total)

        utili = uti1 /100

        vrIva = utili * iva1 /100

        base = tot / (1+ ((adm1/100) + (imp1/100) + utili + vrIva))


        self.txtBase.delete(0,'end')
        self.txtBase.insert(0, locale.format_string("%f",base, grouping=True))   

        millares = locale.format_string("%.2f",tot, grouping=True)
        self.millares.set(millares)

        

    def limpiar(self):
        total=self.txtTotal.get()
        adm=self.txtAdmon.get()
        imp=self.txtImpr.get()
        uti=self.txtUtil.get()
        iva=self.txtIva.get()
        base = self.txtBase.get()

        total = ""
        adm = ""
        imp = ""
        uti = ""
        iva = ""
        base = ""

        self.txtTotal.delete(0,'end')
        self.txtTotal.insert(0, total)  

        self.txtAdmon.delete(0,'end')
        self.txtAdmon.insert(0, adm)  

        self.txtImpr.delete(0,'end')
        self.txtImpr.insert(0, imp)  

        self.txtUtil.delete(0,'end')
        self.txtUtil.insert(0, uti)  

        self.txtIva.delete(0,'end')
        self.txtIva.insert(0, iva)  

        self.txtBase.delete(0,'end')
        self.txtBase.insert(0, base)  

        self.millares.set("")

        self.txtTotal.focus()


    def create_widgets(self):

        self.millares = StringVar()

        self.lblTotal = Label(self,text="Valor con AIU incluido: ",font=("Arial",12, "bold"))
        self.txtTotal=  Entry(self,bg="pink", font=("Arial",12), justify="center",borderwidth=1,  relief="sunken")
        self.lblValor = Label(self,text="$ ",font=("Arial",12))
        self.lblmillares = Label(self,font=("Arial",11, "bold"), textvariable= self.millares, fg="red")

        self.lblAdmon = Label(self,text="Administración: ",font=("Arial",12))
        self.txtAdmon=Entry(self,bg="pink", font=("Arial",12), justify="center")
        
        self.lblImpr = Label(self,text="Imprevistos: ",font=("Arial",12))
        self.txtImpr=Entry(self,bg="pink", font=("Arial",12), justify="center")
        
        self.lblUtil = Label(self,text="Utilidad: ",font=("Arial",12))
        self.txtUtil=Entry(self,bg="pink", font=("Arial",12), justify="center")
        
        self.lblIva = Label(self,text="Iva / Utilidad: ",font=("Arial",12))
        self.txtIva=Entry(self,bg="pink", font=("Arial",12), justify="center")
        
        self.btn1=Button(self,text="Calcular", font=("Arial",12), command=self.fBaseAIU)
        self.btn2=Button(self,text="Reiniciar", font=("Arial",12), command=self.limpiar)
        
        self.lblBase = Label(self,text="Base AIU: ", font=("Arial",12, "bold"), fg="red")
        self.txtBase=Entry(self,bg="cyan", font=("Arial",12, "bold"), justify="center")

        #self.lblRealizado = Label(self,text="Realizado por Laura Juliana Serrano García - MaKeajse 2022",font=("Arial",8))
        #self.lblFrase = Label(self,text="Recuerda Hacer de lo Ordinario, algo Extraordinario",font=("Arial",8, "italic"), fg="black", justify="right")
        
        self.lblTotal.place(x=20,y=20,width=280, height=30)
        self.txtTotal.place(x=40,y=60,width=260, height=30)
        self.lblValor.place(x=20,y=60,width=20, height=30)
        self.lblmillares.place(x=100,y=100,width=185, height=30)


        self.lblAdmon.place(x=50,y=140,width=120, height=30)
        self.txtAdmon.place(x=200,y=140,width=50, height=30)
        self.lblImpr.place(x=50,y=180,width=120, height=30)
        self.txtImpr.place(x=200,y=180,width=50, height=30)
        self.lblUtil.place(x=50,y=220,width=120, height=30)
        self.txtUtil.place(x=200,y=220,width=50, height=30)
        self.lblIva.place(x=50,y=260,width=120, height=30)
        self.txtIva.place(x=200,y=260,width=50, height=30)
        self.btn1.place(x=50,y=400,width=100, height=30)
        self.btn2.place(x=170,y=400,width=100, height=30)
        self.lblBase.place(x=10,y=310,width=120, height=30)
        self.txtBase.place(x=20,y=350,width=280, height=30)

        #self.lblRealizado.place(x=10,y=450, height=30)
        #self.lblFrase.place(x=10,y=470, height=20)
        #self.lblFrase.pack(side="bottom")

        

root = Tk()
root.wm_title("Base de AIU")
root.maxsize(width=320, height=500)



root.lblFrase = Label(root,text="""Realizado por Laura Juliana Serrano García - MaKeajse 2022.
Recuerda: 'Hacer de lo Ordinario, algo Extraordinario'.
""",font=("Arial",7 , "italic"), fg="black", justify="right").pack(side="bottom")

app = FrBaseAIU(root) 
app.mainloop()
