from tkinter import *
import ressource

def tmenu():
    menu = Tk()

    frame_menu = Frame(menu, bg='#1468e8')

    menu.title("LoginPy by eden")
    menu.geometry("480x260")
    menu.minsize(700, 500)
    menu.maxsize(700, 500)
    menu.iconbitmap("app.ico")
    menu.config(background='#1468e8')

    calapp = Button(frame_menu, text='calculator' ,font=("Courrier", 20), bg='white', fg='#1468e8', command=calapp)

    calapp.pack(Pady=1 ,fill=X)

    frame_menu.pack(expend=YES)

    menu.mainloop()


def log():

    tmenu()

def regist():

    tmenu()

def tmaster():
    master = Tk()

    frame_or = Frame(master, bg='#1468e8')

    master.title("LoginPy by eden")
    master.geometry("480x260")
    master.minsize(700, 500)
    master.maxsize(700, 500)
    master.iconbitmap("app.ico")
    master.config(background='#1468e8')

    label_welcome = Label(frame_or, text="Welcome on LoginPy", font=('Courrier', 40), bg='#1468e8', fg='white')
    botton_login = Button(frame_or, text='login', font=("Courrier", 20), bg='white', fg='#1468e8', command=log)
    botton_register = Button(frame_or, text='register', font=("Courrier", 20), bg='white', fg='#1468e8', command=regist)
    input_password = Entry(frame_or, font=("Courrier", 15))
    input_log = Entry(frame_or, font=("Courrier", 15))
    notepass = Label(frame_or, text="Password :", font=("Courrier", 10), bg='#1468e8', fg='white')
    notelog = Label(frame_or, text="mail :", font=("Courrier", 10), bg='#1468e8', fg='white')

    label_welcome.pack(pady=25, fill=X)
    notelog.pack()
    input_log.pack(pady=25, fill=X)
    notepass.pack()
    input_password.pack(pady=25 ,fill=X)
    botton_login.pack(pady=1, fill=X)
    botton_register.pack(pady=1, fill=X)

    frame_or.pack(expand=YES)

    master.mainloop()

tmaster()
