from tkinter import *
import os

from topic import Topics


class Login:
    def __init__(self):
        global root
        self.v = []
        self.root = Tk()
        self.root.title('Login')
        self.root.geometry('750x750')
        Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        # create a register button
        Button(text="Register", height="2", width="30", command=self.register).pack()

        # create Login Button
        Button(text="Login", height="2", width="30", command=self.login).pack()

        self.root.mainloop()

    def register(self):
        global username
        global password
        global username_entry
        global password_entry

        # The Toplevel widget work pretty much like Frame,
        # but it is displayed in a separate, top-level window.
        # Such windows usually have title bars, borders, and other “window decorations”.
        # And in argument we have to pass global screen variable

        self.register_screen = Toplevel(self.root)
        self.register_screen.title("Register")
        self.register_screen.geometry("300x250")

        # Set text variables
        username = StringVar()
        password = StringVar()

        # Set label for user's instruction
        Label(self.register_screen, text="Please enter details below", bg="blue").pack()
        Label(self.register_screen, text="").pack()

        # Set username label
        username_lable = Label(self.register_screen, text="Username * ")
        username_lable.pack()

        # Set username entry
        # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

        username_entry = Entry(self.register_screen, textvariable=username)
        username_entry.pack()

        # Set password label
        password_lable = Label(self.register_screen, text="Password * ")
        password_lable.pack()

        # Set password entry
        password_entry = Entry(self.register_screen, textvariable=password, show='*')
        password_entry.pack()

        Label(self.register_screen, text="").pack()

        # Set register button
        Button(self.register_screen, text="Register", width=10, height=1, bg="blue", command=self.register_user).pack()

    def register_user(self):
        # get username and password
        username_info = username.get()
        password_info = password.get()

        # Open file in write mode
        file = open(username_info, "w")

        # write username and password information into file
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        # set a label for showing success information on screen

        Label(self.register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    # define login function
    def login(self):

        self.login_screen = Toplevel(self.root)
        self.login_screen.title("Login")
        self.login_screen.geometry("300x250")
        Label(self.login_screen, text="Please enter details below to login").pack()
        Label(self.login_screen, text="").pack()

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_login_entry
        global password_login_entry

        Label(self.login_screen, text="Username * ").pack()
        username_login_entry = Entry(self.login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Password * ").pack()
        password_login_entry = Entry(self.login_screen, textvariable=password_verify, show='*')
        password_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Button(self.login_screen, text="Login", width=10, height=1, command=self.login_verify).pack()

    def login_verify(self):
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.login_sucess()

            else:
                self.password_not_recognised()

        else:
            self.user_not_found()

    def login_sucess(self):
        global login_success_screen
        login_success_screen = Toplevel(self.login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=self.delete_login_success).pack()


    def password_not_recognised(self):
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(self.login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        Button(password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()

    # Designing popup for user not found

    def user_not_found(self):
        global user_not_found_screen
        user_not_found_screen = Toplevel(self.login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()

    # Deleting popups

    def delete_login_success(self):
        login_success_screen.destroy()
        self.login_screen.destroy()
        self.root.destroy()
        t=Topics()



    def delete_password_not_recognised(self):
        password_not_recog_screen.destroy()

    def delete_user_not_found_screen(self):
        user_not_found_screen.destroy()
