from tkinter import *
import os
import topic


def login():
    global login_screen
    #login_screen = Toplevel(main_screen)
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Va rugam introduceti datele pentru login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir("/Users/Ioana/PycharmProjects/RC_P")
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Succes")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Autentificare reusita").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    login_screen.destroy()
    topic.Topics()



def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Succes")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Parola invalida ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Succes")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Neinregistrat").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def main_account_screen():
    #global main_screen
    #main_screen = Tk()
    login()
    login_screen.mainloop()


#main_account_screen()





