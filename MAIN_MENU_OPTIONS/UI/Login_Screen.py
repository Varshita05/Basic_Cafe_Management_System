from tkinter import *
import sqlite3
from tkinter import messagebox
from Main_Screen import main_screen

class Login_Screen:
    def __init__(self):
        self.login_screen = Tk()

        # Customising
        self.login_screen.title("Login/Register")
        self.login_screen.configure(bg="#EECEDA")
        image = PhotoImage(file=r"C:\Users\JANARDHANA RAO\Downloads\coffee.png")
        self.login_screen.iconphoto(False, image)
        main_frame = Frame(self.login_screen, bg="#FAE7EB")
        main_frame.pack(fill="both", expand=True, padx=50, pady=50)

        self.conn = sqlite3.connect("Database.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Login_Credentials(Gmail TEXT, Username TEXT, Password TEXT)")
        self.conn.commit()

        page_title = Label(main_frame, text="Login Page", font=("copperplate gothic bold", 20), fg="black",
        background='#FAE7EB', anchor="center")
        page_title.pack(pady=10)
        l1 = Label(main_frame, text="Username", background='#FAE7EB')
        l1.pack(padx=10, pady=10)
        self.username = Entry(main_frame)
        self.username.pack(padx=10, pady=10)
        l2 = Label(main_frame, text="Password", background='#FAE7EB')
        l2.pack(padx=10, pady=10)
        self.password = Entry(main_frame)
        self.password.pack(padx=10, pady=10)
        login = Button(main_frame, text="Login", command=self.login, background='#EECEDA')
        login.pack(padx=10, pady=10)
        b1 = Button(main_frame, text="Forgot Password?", command=self.forgot_password)
        b1.pack(padx=10, pady=10)
        b2 = Button(main_frame, text="New User? Register", command=self.register)
        b2.pack(padx=10, pady=10)
        self.login_screen.mainloop()
    def login(self):
        username = self.username.get()
        password = self.password.get()
        self.cursor.execute("SELECT Username,Password FROM Login_Credentials")
        self.users = self.cursor.fetchall()
        for i in self.users:
            if i[0]==username:
                if i[1]==password:
                    self.login_screen.after(1, lambda: main_screen(self.login_screen))
                else:
                    messagebox.showwarning("Incorrect","Incorrect Password")
                    break
        else:
             messagebox.showwarning("Doesn't exist","Username doesn't exist")

    def reset_password(self):
        register_window = Toplevel(self.login_screen, bg="#EECEDA")
        register_window.resizable(0, 0)
        register_frame = Frame(register_window, background="#FAE7EB")
        register_frame.pack(padx=10, pady=10)
        label1 = Label(register_frame, text="Enter your Gmail Address/Username", background='#FAE7EB')
        label1.pack(padx=10, pady=10)
        detail = (Entry(register_frame))
        detail.pack(padx=10, pady=10)
        l3 = Label(register_frame, text="Enter your new password", background='#FAE7EB')
        l3.pack(padx=10, pady=10)
        Password = (Entry(register_frame))
        Password.pack(padx=10, pady=10)
        l31 = Label(register_frame, text="Enter your new password again", background='#FAE7EB')
        l31.pack(padx=10, pady=10)
        password1 = Entry(register_frame)
        password1.pack(padx=10, pady=10)
        b = Button(register_frame, text="Change Password")
        b.pack(padx=10, pady=10)


    def register(self):
        self.register_window = Toplevel(self.login_screen, bg="#EECEDA")
        self.register_window.resizable(0, 0)
        register_frame = Frame(self.register_window, background='#FAE7EB')
        register_frame.pack(padx=10, pady=10)
        label1 = Label(register_frame, text="Enter your gmail address", background='#FAE7EB')
        label1.pack(padx=10, pady=10)
        self.Gmail = Entry(register_frame)
        self.Gmail.pack(padx=10, pady=10)
        label2 = Label(register_frame, text="Enter your username", background='#FAE7EB')
        label2.pack(padx=10, pady=10)
        self.Username = Entry(register_frame)
        self.Username.pack(padx=10, pady=10)
        l3 = Label(register_frame, text="Enter your password", background='#FAE7EB')
        l3.pack(padx=10, pady=10)
        self.Password = Entry(register_frame)
        self.Password.pack(padx=10, pady=10)
        l31 = Label(register_frame, text="Enter your password again", background='#FAE7EB')
        l31.pack(padx=10, pady=10)
        self.password1 = Entry(register_frame)
        self.password1.pack(padx=10, pady=10)
        b = Button(register_frame, text="Register",command=self.check)
        b.pack(padx=10, pady=10)
    def check(self):
        self.mail = self.Gmail.get()
        self.user = self.Username.get()
        self.pass1 = self.Password.get()
        self.pass2 = self.Password.get()
        if self.pass1==self.pass2:
            self.cursor.execute("INSERT INTO Login_Credentials(Gmail, Username, Password) VALUES (?,?,?)"
                                 , (self.mail,self.user,self.pass1))
            self.conn.commit()
            messagebox.showinfo("Success","Registered Successfully, Login to continue!")
            self.register_window.destroy()
        else:
            messagebox.showwarning("Password Error","Type Same Password twice")
    def forgot_password(self):
        password_window = Toplevel(self.login_screen, bg="#EECEDA")
        password_window.resizable(0,0)
        password_frame = Frame(password_window, background='#FAE7EB')
        password_frame.pack(fill="both", expand=True, padx=50, pady=50)
        label1 = Label(password_frame, text="Enter your gmail address or Username", background='#FAE7EB')
        label1.pack(padx=10, pady=10)
        detail = (Entry(password_frame))
        detail.pack(padx=10, pady=10)
        label2 = Label(password_frame, text="Enter the OTP", background='#FAE7EB')
        label2.pack(padx=10, pady=10)
        otp = (Entry(password_frame))
        otp.pack(padx=10, pady=10)
        b = Button(password_frame, text="Verify", command=self.reset_password)
        b.pack(padx=10, pady=10)

# Class call
Login_Screen()

