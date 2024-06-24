from tkinter import *
from tkinter import messagebox
import mysql.connector
#import pymysql
#from PIL import ImageTk
root= Tk()
root.geometry('925x500+300+200')
root.config(bg='#fff')
root.resizable(False,False)
root.title("Welcome Page !")
def student():
    messagebox.showwarning('Confirmation','Are you Sure !!')
    root.destroy()
    import log_stu

def teacher():
    messagebox.showwarning('Confirmation','Are you Sure !!')
    root.destroy()
    import log_fac


heading = Label(root,text='Click on your Identity',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',13,'bold'))
heading.place(x=370,y=270) 
img = PhotoImage(file='images/welcome_faculty.png')
Button(root,border=0,image=img,bg='white',command=teacher).place(x=300,y=320)

img1 = PhotoImage(file='images/welcome_student.png')
Button(root,border=0,image=img1,bg='white',command=student).place(x=480,y=325)



logo= PhotoImage(file='images/welcome_logo.png')
Button(root,border=0,image=logo,bg='white',command=student).place(x=300,y=10)

root.mainloop()