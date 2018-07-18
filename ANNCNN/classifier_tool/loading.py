from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import matplotlib.pyplot as plt
import os
import matplotlib
import parameters
from tkinter.scrolledtext import ScrolledText
import ann
#import cnn
import filereader
import tempreader


class REG:

    def __init__(self, master):
        
        
        self.valuesdata = StringVar()
        self.valuesdata1 = StringVar()
        self.valuesdata2 = StringVar()
        self.yaxis=IntVar()
        #self.cls=IntVar()
        self.yaxis=100
        self.epochs,self.cls,self.neuron=tempreader.main()
        print(self.epochs)
        print(self.cls)
        print(self.neuron)
        self.data=[]
        ttk.Style().configure('green/black.TLabel', foreground='#000040', background='#8080ff')
        ttk.Style().configure('green/black.TButton', foreground='#000040', background='black')
        ttk.Style().configure('gb/black.TLabel', foreground='#000040', background='#dbdbdb')
        ttk.Style().configure('add.TButton', foreground='green', background='black')
        ttk.Style().configure('remove.TButton', foreground='red', background='black')
        self.master = master
        self.master.title(" MACHINE LEARNING BASED CLASSIFICATION TOOL ")
        self.master.config(bg="#dbdbdb")
        self.master.geometry("1000x680")
        self.can = Canvas(master, width=1200, height=100, bg='#8080ff')
        
        self.can.place(x=1, y=1)

        self.l = ttk.Label(master, text="MACHINE LEARNING BASED CLASSIFICATION TOOL",
                       font=('times new roman', 15, 'bold italic'),style='green/black.TLabel')
        self.l.place(x=350, y=30)
        
        #self.row,self.col,self.band=filereader.main(self.head)
        
        self.b1 = ttk.Button(master, text='Select ImageFile', cursor="plus", style='green/black.TButton' , command=self.callback)
        self.b1.place(x=35, y=150, width=110)
        self.e1 = ttk.Label(master,textvariable=self.valuesdata,relief="sunken" )
        self.e1.place(x=175, y=153, width=275)
        
        self.b2 = ttk.Button(master, text='Select HeaderFile', cursor="plus", style='green/black.TButton' , command=self.callback1)
        self.b2.place(x=35, y=250, width=110)
        self.e2 = ttk.Label(master,textvariable=self.valuesdata1,relief="sunken")
        self.e2.place(x=175, y=253, width=275)
        
        
        self.b12 = ttk.Button(master, text='+', cursor="plus", style='add.TButton' , command=self.calladd)
        self.b12.place(x=175, y=400, width=25)
        
        
        self.b13 = ttk.Button(master, text='-', cursor="plus", style='remove.TButton' , command=self.calldel)
        self.b13.place(x=215, y=400, width=25)
        
        self.e13 = ttk.Label(master,text="Load Training Data",style='gb/black.TLabel')
        self.e13.place(x=35, y=403, width=125)
            
        self.e19 = ttk.Label(master,text="Training Data",style='gb/black.TLabel')
        self.e19.place(x=650, y=175, width=125)
        
        
        self.b7 = ttk.Button(master, text='Classify', cursor="plus", style='green/black.TButton',command=lambda: ann.main(self.row,self.col,self.band,self.data,self.img) if self.neuron  == -999 else ann.main(self.row,self.col,self.band,self.data,self.img))#the first parameter is set to ann.main as there are errors in loading cnn module
        self.b7.place(x=35, y=570, width=110)
      
        
        self.b8 = ttk.Button(master, text='exit', cursor="plus", style='green/black.TButton',command=self.savedone)
        self.b8.place(x=235, y=570, width=110)
        
        
        self.T =Text(master, height=self.cls, width=65)
        self.T.pack()
        self.T.place(x=600,y=200)
        self.T.config({"background": "#dbdbdb"})
        self.T.config({"border": 0})
        
        

    
    def callback(self):
        filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Text file","*.txt")))
        self.valuesdata.set(filename)
        self.img=filename
        print(self.img)
        #self.createtemp(filename)
        #print (root.filename)
        
    def callback1(self):
        filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Header file","*.hdr"),("all files","*.*")))
        self.valuesdata1.set(filename)
        self.head=filename
        print(self.head)
        self.row,self.col,self.band=filereader.main(self.head)
        #self.createtemp(filename)
        #print (root.filename)
        
        
    def calladd(self):
        add =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Text file","*.txt")))
        #self.datax.set(add)
        self.data.append(add)
        self.T.config(state="normal")
        self.T.delete('1.0', END)
        for ent in self.data:
            self.T.insert(END, ent+'\n')
        self.T.config(state="disabled")
        if len(self.data)>=(self.cls-1):
            self.b12.config(state="disabled")
        elif len(self.data)<(self.cls-1):
            self.b12.config(state="normal")
        print(len(self.data))
        print(self.cls)
        #self.createtemp(filename)
        #print (root.filename)
        
        
        
    def calldel(self):
        self.data=self.data[:-1]
        self.T.config(state="normal")
        self.T.delete('1.0', END)
        for ent in self.data:
            self.T.insert(END, ent+'\n')
        self.T.config(state="disabled")
        if len(self.data)<self.cls:
            self.b12.config(state="normal")
            
    def savedone(self):
        self.master.destroy()
    