from tkinter import filedialog
from tkinter import * 
from tkinter.ttk import *
import tkinter.messagebox
import matplotlib.pyplot as plt
import os
import matplotlib
import loading


class PARAM:

    
    def __init__(self, master):
   
        
        
        self.my_var = IntVar()
        self.valuesdata6 = StringVar()
        self.valuesdata3 = StringVar()
        self.valuesdata4 = StringVar()
        self.valuesdata5 = StringVar()
        self.file = open('temp.txt','w') 
        
        ttk.Style().configure('green/black.TLabel', foreground='#000040', background='#8080ff')
        ttk.Style().configure('gb.TLabel', foreground='#000040', background='#dbdbdb')
        ttk.Style().configure('green/black.TButton', foreground='#000040', background='black')
        
        self.master = master
        self.master.title(" MACHINE LEARNING BASED CLASSIFICATION TOOL ")
        self.master.config(bg="#dbdbdb")
        self.master.geometry("800x680")
        self.can = Canvas(master, width=800, height=100, bg='#8080ff')
        
        self.can.place(x=1, y=1)

        self.l = ttk.Label(master, text="MACHINE LEARNING BASED CLASSIFICATION TOOL ",
                       font=('times new roman', 15, 'bold italic'),style='green/black.TLabel')
        self.l.place(x=175, y=30)
        
        
        
        self.e3 = ttk.Label(master,text="Select The Algorithm",style="gb.TLabel")
        self.e3.place(x=350, y=130, width=880)
        
        self.rb1 = ttk.Radiobutton(master, text='Artificial Neural Network', variable=self.my_var, value=5, command=self.selected)
        self.rb1.place(x=200, y=180)
        self.rb2 = ttk.Radiobutton(master, text='Convolutional Neural Network', variable=self.my_var, value=10, command=self.selected)
        self.rb2.place(x=420, y=180)
        
             
        self.e5 = ttk.Label(master,textvariable=self.valuesdata6,style='gb.TLabel')
        self.e5.place(x=235, y=255, width=350)
        
        self.e6 = ttk.Label(master,textvariable=self.valuesdata3,style='gb.TLabel')
        self.e6.place(x=235, y=335, width=350)
                      
        self.e7 = ttk.Label(master,textvariable=self.valuesdata4,style='gb.TLabel')
        self.e7.place(x=235, y=385, width=350)
        
        self.e8 = ttk.Label(master,textvariable=self.valuesdata5,style='gb.TLabel')
        self.e8.place(x=235, y=435, width=350)
        
        
        
        self.x1 =Entry(master)
        self.x1.place(x=485, y=335, width=80)
        
       
        
        self.x2 =Entry(master)
        self.x2.place(x=485, y=385, width=80)
        
        
        self.x3 =Entry(master)
        self.x3.place(x=485, y=435, width=80)
        
        self.b5 = ttk.Button(master, text='Load Data', cursor="plus", style='green/black.TButton', command=self.loadwindow)
        self.b5.place(x=50, y=580, width=110)
        
        
        
        self.x =Entry(master,style='gb.TLabel' )
        self.x.place(x=485, y=335, width=80,height=100)
        self.x.lift()
        
        self.xx =Entry(master,style='gb.TLabel')
        self.xx.place(x=485, y=435, width=80,height=50)
        self.xx.lift()
        
    
    def selected(self):
     if self.my_var.get()==5:
         self.valuesdata6.set("Define Parameters For Artificial Neural Network Classifier")
         self.valuesdata3.set("Enter Number Of Training Cycles")
         self.valuesdata4.set("Enter Number Of Training Classes")
         self.valuesdata5.set("Enter Number Of Hidden Neurons")
         self.x.lower()
         self.xx.lower()
         self.x1.delete(0,END)
         self.x2.delete(0,END)
         self.x3.delete(0,END)
         
         
         
     elif self.my_var.get()==10:
        self.valuesdata6.set("Define Parameters For Convolutional Neural Network Classifier")
        self.valuesdata3.set("Enter Number Of Training Cycles")
        self.valuesdata4.set("Enter Number Of Training Classes")
        self.valuesdata5.set("")
        self.x.lower()
        self.xx.lift()
        self.x1.delete(0,END)
        self.x2.delete(0,END)
        self.x3.delete(0,END)
        
        
     else:
        self.valuesdata6.set("ERROR:Report the Bug")
        
        
        
        
    def loadwindow(self):
        end='//null//'
        self.file.write('epoch:'+self.x1.get()+end)
        self.file.write('cls:'+self.x2.get()+end)
        if self.my_var.get()==5:
            self.file.write('neuron:'+self.x3.get()+end)
        else:
            self.file.write('neuron:'+'-999'+end)
        self.file.close()
       
        self.master.destroy()
        root3 = Tk()
        root3.resizable(0, 0)
        self.obj3 = loading.REG(root3)
        root3.mainloop()
        
        
    
        
if __name__ == '__main__':
        root = Tk()
        root.resizable(0, 0)
        obj = PARAM(root)
        root.mainloop()
    
        