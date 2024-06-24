from tkinter import *
from tkinter import messagebox
import mysql.connector
import pymysql
from PIL import ImageTk


fg = Tk()
fg.geometry("925x550+300+200")
fg.config(bg="#fff")
fg.resizable(False, False)
fg.title("Forgot Password !")


def db():
    if passw.get() != passw1.get():
        messagebox.showerror("Error", "Password Mismatched !!")
    try:
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="root@123", database="daksh"
        ) #change database name accordingly
        mycur = mydb.cursor()
    except:
        messagebox.showerror("Error", "Connection is not established Try again !!")
        return
    query = "select * from stu_info where username=%s"
    mycur.execute(query, [user.get()])
    row = mycur.fetchone()
    if row == None:
        messagebox.showerror("Error", "Incorrect Username !!")
    else:
        query = "update stu_info set password=%s where username=%s"
        mycur.execute(query, (passw1.get(), user.get()))
        mydb.commit()
        messagebox.showinfo(
            "Password Changed", "Your Password Has been changed Sucessfully!!"
        )
        fg.destroy()
        import log_stu


img = PhotoImage(file="images/forg_image.png")
Label(fg, image=img, bg="white").place(x=10, y=10)

frame = Frame(fg, width=350, height=350, bg="white")
frame.place(x=550, y=70)

heading = Label(
    fg,
    text="Forgot Password ",
    fg="#57a1f8",
    bg="white",
    font=("Microsoft YaHei UI Light", 23, "bold"),
)
heading.place(x=600, y=50)


###################### username #################################
def on_enter(e):
    user.delete(0, "end")


def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "Username")


user = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


###################### New Password #################################
def on_enter(e):
    passw.delete(0, "end")


def on_leave(e):
    name = passw.get()
    if name == "":
        passw.insert(0, "New Password")


passw = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
passw.place(x=30, y=150)
passw.insert(0, "New Password")
passw.bind("<FocusIn>", on_enter)
passw.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)


###################### Confirm Password #################################
def on_enter(e):
    passw1.delete(0, "end")


def on_leave(e):
    name = passw1.get()
    if name == "":
        passw1.insert(0, "Confirm Password")


passw1 = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
passw1.place(x=30, y=210)
passw1.insert(0, "Confirm Password")
passw1.bind("<FocusIn>", on_enter)
passw1.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=237)

Button(
    frame,
    width=39,
    pady=7,
    text="Reset Password",
    bg="#57a1f8",
    fg="white",
    border=0,
    command=db,
).place(x=34, y=284)


fg.mainloop()
