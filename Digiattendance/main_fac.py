from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import openpyxl
from tkinter.simpledialog import askinteger  # Import askinteger from simpledialog
import mysql.connector
from PIL import Image, ImageTk
import time
import qrcode
import sys

main = Tk()
main.geometry("925x500+300+200")
main.config(bg="#fff")
main.resizable(False, False)
main.title("Main main !")
try:
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="root@123", database="qr") #change database name accordingly
    mycur = mydb.cursor()
except:
    messagebox.showerror("Error", "Connection is not established. Try again !!")


def log_out():
    messagebox.showinfo("Logout", "Logout Successfully !!")
    main.destroy()
    import log_stu


def curtime():
    timeVar = time.strftime("%I:%M:%S %p\n %A \n %x")
    clock.config(text=timeVar)
    clock.after(200, curtime)


def generate_qr_code():
    global qr_label, time_limit, qr_code_data, selected_course
    qr_code_data = user.get()
    if qr_code_data == "Enter the code to make a QR":
        messagebox.showerror("error", "Input Some unique text !")
        return
    selected_course = final_course.get()
    if selected_course == "Select a Course":
        messagebox.showerror("error", "Input Some Course Code !")
        return
    else:
        qr_data_db(qr_code_data, selected_course)
        time_limit = askinteger(
            "Time Limit", "Enter the time limit (in seconds):", initialvalue=10
        )
        if time_limit is None:
            return
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_code_data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        img = ImageTk.PhotoImage(image=qr_img)
        if qr_label is not None:
            qr_label.destroy()
        qr_label = Label(main, image=img, bg="white")
        qr_label.image = img
        qr_label.pack()
        main.after(time_limit * 1000, close_qr_window)


def qr_data_db(qr_code_data, selected_course):
    if selected_course == "CM201G":
        mycur.execute("insert into cm201g (qr_code) values (%s)", ([qr_code_data]))
        mydb.commit()
    elif selected_course == "CM202G":
        mycur.execute("insert into cm202g (qr_code) values (%s)", ([qr_code_data]))
        mydb.commit()
    elif selected_course == "CM203G":
        mycur.execute("insert into cm203g (qr_code) values (%s)", ([qr_code_data]))
        mydb.commit()
    elif selected_course == "CM204G":
        mycur.execute("insert into cm204g (qr_code) values (%s)", ([qr_code_data]))
        mydb.commit()
    elif selected_course == "CM205G":
        mycur.execute("insert into cm205g (qr_code) values (%s)", ([qr_code_data]))
        mydb.commit()
    else:
        messagebox.showerror("Error", "Select Proper Course Code !!")


def close_qr_window():
    global qr_label
    if qr_label is not None:
        qr_label.destroy()
        qr_label = None


img = PhotoImage(file="images/welcome_main.png")
Label(main, image=img, bg="white").place(x=1, y=5)
clock = Label(main, font=("Calibri", 13), bg="#57a1f8", fg="white")
clock.place(x=820, y=5)
course_codes = ["CM201G", "CM202G", "CM203G", "CM204G", "CM205G"]
final_course = StringVar()
course_dropdown = ttk.Combobox(main, textvariable=final_course)
course_dropdown["values"] = course_codes
course_dropdown.place(x=620, y=150)
course_dropdown.set("Select a Course")


def on_enter(e):
    user.delete(0, "end")


def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "Enter the code to make a QR")


user = Entry(
    main,
    width=35,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UILight", 10),
)
user.place(x=620, y=210)
user.insert(0, "Enter the code to make a QR")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(main, width=200, height=2, bg="black").place(x=620, y=235)
qr_label = None
time_limit = 10  # Default time limit in seconds
submit_button = Button(
    main,
    width=39,
    pady=7,
    text="Submit",
    bg="#57a1f8",
    fg="white",
    border=0,
    command=generate_qr_code,
)
submit_button.place(x=620, y=290)
curtime()
Button(
    main,
    width=9,
    pady=7,
    text="Log Out",
    bg="#57a1f8",
    fg="white",
    border=0,
    command=log_out,
).place(x=800, y=450)
main.mainloop()
