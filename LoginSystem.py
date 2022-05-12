import re
from tkinter import *
import os


# variables

# functions
def reg_submit():
    un = username.get()
    pw = password.get()
    all_accounts = os.listdir()
    notif.config(text='')
    notif_un.config(text='')
    notif_pw.config(text='')

    if un == '' or pw == '':
        notif.config(text='All fields are required *', fg="red")
        return

    for name_check in all_accounts:
        if un == name_check:
            notif_un.config(text='Account already exists with the same Username', fg="red")
            return
        else:
            if re.search('@' and '.com', un):
                notif_un.config(text='Username invalid ("@",".com")*')
                return
            elif len(pw) < 8:
                notif_pw.config(text='Password should be atleast 8 characters long*', fg='red')
                return
            elif re.search('[0-9]', pw) and re.search('[a-z]', pw) and re.search('[A-Z]', pw) and re.search('!'or'@'or'-'or'#'or'$', pw):
                pass
            else:
                notif_pw.config(text='Password must contain atleast one number, one lowercase, one uppercase and a special character(!@#$-)*', fg='red')
                return



    file = open(un, 'w')
    file.write(un + '\n')
    file.write(pw + '\n')
    file.close()
    notif.config(text='Account has been created', fg="green")


def register():
    global notif
    global notif_un
    global notif_pw
    global username
    global password
    username = StringVar()
    password = StringVar()
    reg_screen = Toplevel()
    reg_screen.title('Registration')
    Label(reg_screen, text='Register yourself here!', font=('Arial', 14)).grid(row=0, pady=10)
    Label(reg_screen, text='Username: ', font=('Arial', 12)).grid(row=1, column=1, pady=5)
    Label(reg_screen, text='Password: ', font=('Arial', 12)).grid(row=3, column=1, pady=5)

    Entry(reg_screen, textvariable=username).grid(row=1, column=2)
    notif_un = Label(reg_screen)
    notif_un.grid(row=2, column=2)
    Entry(reg_screen, textvariable=password, show='*').grid(row=3, column=2)
    notif_pw = Label(reg_screen)
    notif_pw.grid(row=4, column=2)

    Button(reg_screen, text='Submit', command=reg_submit).grid(row=5, column=2)
    notif = Label(reg_screen)
    notif.grid(row=6, column=1, sticky=N)


def login():
    ul = user_login.get()
    pl = pass_login.get()
    if ul == '' or pl == '':
        login_notif.config(text='Username or Password incorrect!', fg='red')
        return

    all_accounts = os.listdir()
    for name_check in all_accounts:
        if ul == name_check:
            new_file = open(ul, 'r')
            file = new_file.read()
            details = file.split('\n')
            if ul == details[0] and pl == details[1]:
                login_screen = Toplevel()
                login_screen.title(ul)
                Label(login_screen, text='Welcome ' + ul, font=('Arial', 15)).grid(row=0)
                Label(login_screen, text='Login successful!', font=('Arial', 10)).grid(row=1)
                login_notif.config(text='Login successful', fg='green')
            else:
                login_notif.config(text='Username or Password incorrect!', fg='red')


mainpage = Tk()
mainpage.geometry('300x250')
user_login = StringVar()
pass_login = StringVar()
mainpage.title('Login page')
Label(mainpage, text='Welcome!', font=('Arial', 14)).grid(row=0, sticky=N, pady=15, column=3)
Label(mainpage, text='Username', font=('Arial', 14)).grid(row=4, column=2, sticky=W)
Entry(mainpage, textvariable=user_login).grid(row=4, column=3, padx=20, sticky=E)

Label(mainpage, text='Password', font=('Arial', 14)).grid(row=5, column=2, sticky=W)
Entry(mainpage, textvariable=pass_login, show="*").grid(row=5, column=3, padx=20, sticky=E)
Button(mainpage, text='Login', command=login, font=('Arial', 10), width= 15).grid(row=6, sticky=W, pady=5, column=3)
Button(mainpage, text='Sign up', command=register, font=('Arial', 10), width=15).grid(row=7, sticky=W, column=3)
login_notif = Label(mainpage)
login_notif.grid(row=6)

mainpage.mainloop()