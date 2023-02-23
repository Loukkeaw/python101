from tkinter import *
from tkinter import ttk
from tkinter import messagebox



GUI = Tk()
GUI.title ('I want to code')
GUI.geometry('500x500')

L1=Label(GUI, text='Learning journey')
L1.place(x=30, y=20)
#######################
def Button1():
    text = 'python'
    messagebox.showinfo('coding language', text) #showifo.showerror.showwarning

FB1 = ttk.Label(GUI)
FB1.place(x=100, y=80)
B1 = ttk.Button(FB1, text= 'what coding language do you want to learn?', command=Button1)
B1.pack(ipadx=10, ipady=10, pady=10)
############

def Button2():
    text = 'Uncle Engineer'
    messagebox.showinfo('teacher name', text)

FB2 = LabelFrame(GUI)
FB2.place(x=100, y=150)
B2 = ttk.Button(FB1, text= 'what is your teacher name?', command=Button2)
B2.pack(ipadx=10, ipady=10, pady=10)


############
import datetime

def Button3():
    today = datetime.datetime.today().date()
    text = 'Today is' 
    messagebox.showinfo('Today is',today)
    
FB3 = Label(GUI)
FB3.place(x=160, y=210)
B3 = ttk.Button(FB3, text= 'What is today date?', command=Button3)
B3.pack(ipadx=10, ipady=10, pady=10)

###########

def Button4():
    text = 'WE SHOW ERROR'
    messagebox.showwarning('Error', text)
        

FB4 = Label(GUI)
FB4.place(x=180, y=270)
B4 = ttk.Button(FB4, text="Show Info", command=Button4)
B4.pack(ipadx=10, ipady=10, pady=10)

    
GUI.mainloop()

