from tkinter import *
from tkinter import messagebox
import mysql.connector
import bcrypt

win = Tk()
win.title("Sign Up")
win.geometry("950x600+300+100")
win.resizable(False, False)
win.config(bg='white')

global password

def db():
    if passw.get() == '':
        messagebox.showerror('Error', 'Fill All fields !!')
        return
    
    mydb = mysql.connector.connect(host='localhost', user='root', password='root@123', database='daksh') #change database name accordingly
    cursor = mydb.cursor()
    
    name = nam.get()
    enroll = roll.get()
    phone_no = phone.get()
    email = email_id.get()
    username = user.get()
    password = passw.get()
    
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    cursor.execute('INSERT INTO user_info (name, enroll, phone_no, email, username, password) VALUES (%s, %s, %s, %s, %s, %s)', 
                   (name, enroll, phone_no, email, username, hashed_password))
    
    mydb.commit()
    messagebox.showinfo('Sign Up', 'Thanks For Signing Up !!')
    mydb.close()
    win.destroy()
    import log_stu

def signIn():
    win.destroy()
    import log_stu

img = PhotoImage(file='images/SignUp_Student.png')
Label(win, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(win, width=350, height=490, bg='white')
frame.place(x=490, y=50)

heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=0)

###################### Name #################################
def on_enter(e):
    nam.delete(0, 'end')
def on_leave(e):
    name = nam.get()
    if name == '':
        nam.insert(0, 'Name')

nam = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
nam.place(x=30, y=65)
nam.insert(0, 'Name')
nam.bind('<FocusIn>', on_enter)
nam.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=90)

###################### Enrollment #################################
def on_enter(e):
    roll.delete(0, 'end')
def on_leave(e):
    name = roll.get()
    if name == '':
        roll.insert(0, 'Enrollment No.')

roll = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
roll.place(x=29, y=117)
roll.insert(0, 'Enrollment No.')
roll.bind('<FocusIn>', on_enter)
roll.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=29, y=151)

###################### Phone No #################################
def on_enter(e):
    phone.delete(0, 'end')
def on_leave(e):
    name = phone.get()
    if name == '':
        phone.insert(0, 'Phone No.')

phone = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
phone.place(x=30, y=180)
phone.insert(0, 'Phone No.')
phone.bind('<FocusIn>', on_enter)
phone.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=210)

###################### Email #################################
def on_enter(e):
    email_id.delete(0, 'end')
def on_leave(e):
    name = email_id.get()
    if name == '':
        email_id.insert(0, 'Email Id')

email_id = Entry(frame, width=35, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
email_id.place(x=30, y=245)
email_id.insert(0, 'Email Id')
email_id.bind('<FocusIn>', on_enter)
email_id.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=275)

###################### Username #################################
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=305)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=335)

###################### Password #################################
def on_enter(e):
    passw.delete(0, 'end')
def on_leave(e):
    name = passw.get()
    if name == '':
        passw.insert(0, 'Password')

passw = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
passw.place(x=30, y=365)
passw.insert(0, 'Password')
passw.bind('<FocusIn>', on_enter)
passw.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=395)

Button(frame, width=39, pady=7, text='Sign Up', bg="#57a1f8", fg='white', border=0, command=db).place(x=25, y=421)

label = Label(frame, text="Already have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 11))
label.place(x=55, y=470)

sign_up = Button(frame, width=8, height=1, text='Sign In', border=0, fg='#57a1f8', bg='white', cursor='hand2', command=signIn)
sign_up.place(x=235, y=473)

win.mainloop()
