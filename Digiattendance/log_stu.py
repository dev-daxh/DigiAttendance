from tkinter import *
from tkinter import messagebox
import mysql.connector
import bcrypt
from PIL import ImageTk

root = Tk()
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(False, False)
root.title("Login Page !")


def db():
    try:
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="root@123", database="daksh" #change database name accordingly
        )
        mycur = mydb.cursor()
    except:
        messagebox.showerror("Error", "Connection is not established. Try again!")
        return

    username = user.get()
    password = passw.get()

    if not username or not password:
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    query = "SELECT password FROM user_info WHERE username=%s"
    mycur.execute(query, (username,))
    row = mycur.fetchone()

    if row is None:
        messagebox.showerror("Error", "Invalid Username or Password!")
    else:
        stored_password = row[0].encode("utf-8")

        if bcrypt.checkpw(password.encode("utf-8"), stored_password):
            messagebox.showinfo("Welcome", "Login Successful")
            root.destroy()
            query = "SELECT name, enroll FROM user_info WHERE username=%s"
            mycur.execute(query, (username,))
            row = mycur.fetchone()

            if row:
                name, enroll = row
                # Here, you can handle the logic to pass `name` and `enroll` to the next window or module
                import main_stu
        else:
            messagebox.showerror("Error", "Invalid Username or Password!")

    mydb.close()


def signUp():
    root.destroy()
    import SignUp_Student


def forg():
    root.destroy()
    import forg_stu


img = PhotoImage(file="images/log_student.png")
Label(root, image=img, bg="white").place(x=30, y=30)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(
    root,
    text="Sign In",
    fg="#57a1f8",
    bg="white",
    font=("Microsoft YaHei UI Light", 23, "bold"),
)
heading.place(x=600, y=100)


###################### Username #################################
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


###################### Password #################################
def on_enter(e):
    passw.delete(0, "end")


def on_leave(e):
    name = passw.get()
    if name == "":
        passw.insert(0, "Password")


passw = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
passw.place(x=30, y=150)
passw.insert(0, "Password")
passw.bind("<FocusIn>", on_enter)
passw.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(
    frame,
    width=39,
    pady=7,
    text="Sign In",
    bg="#57a1f8",
    fg="white",
    border=0,
    command=db,
).place(x=34, y=214)
label = Label(
    frame,
    text="Don't have an account?",
    fg="black",
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
label.place(x=75, y=270)

sign_up = Button(
    frame,
    width=6,
    text="Sign Up",
    border=0,
    fg="#57a1f8",
    bg="white",
    cursor="hand2",
    command=signUp,
)
sign_up.place(x=245, y=273)
forgot = Button(
    frame,
    width=0,
    text="Forgot password?",
    border=0,
    fg="#57a1f8",
    bg="white",
    cursor="hand2",
    command=forg,
)
forgot.place(x=245, y=183)

root.mainloop()
