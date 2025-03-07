from datetime import date
from time import localtime, strftime, time
from tkinter import *

from Recipe_Book_Screen import recipe_book_screen
from Menu_Screen import menu_screen
from Billing_Screen import Billing_Screen
from Staff_Details_Screen import staff_details_screen
from Sales_Screen import Sales_Screen
# Recipe book method creates a window from recipe book screen file
# after method for recipe book button to be released

class main_screen:
    def __init__(self,login_screen):
        login_screen.destroy()
        # Creating main screen window
        self.main_screen = Tk()

        width = self.main_screen.winfo_screenwidth()
        height = self.main_screen.winfo_screenheight()

        # Window appears in full screen
        self.main_screen.geometry("%dx%d" % (width, height))
        self.main_screen.state('zoomed')

        image = PhotoImage(file=r"C:\Users\JANARDHANA RAO\Downloads\coffee.png")
        self.main_screen.iconphoto(False,image)
        # Customising main screen window
        self.main_screen.title("Cafe Management System")
        self.main_screen.configure(bg="#EECEDA")

        # Creating a frame and adding all options in one frame only
        self.main_frame = Frame(self.main_screen, bg='#FAE7EB')
        self.main_frame.pack(fill="both", expand=True, padx=50, pady=50)

        # Date and time
        today = date.today()
        date_l = Label(self.main_frame, text=today.strftime("%B %d, %Y"), fg="black", background='#FAE7EB',
                       font=("Times", 10))
        date_l.pack(side=RIGHT, anchor=N, padx=10,pady=10)
        time_now = strftime("%H:%M:%S", localtime())
        time_l = Label(self.main_frame, text=time_now, fg="black", background='#FAE7EB', font=("Times", 10))
        time_l.pack(side=LEFT, anchor=NW, padx=10,pady=10)

        page_title = Label(self.main_frame, text="Home Page", font=("copperplate gothic bold", 20), fg="black",
                           background='#FAE7EB', anchor="center")
        page_title.pack(pady=10)

        label = Label(self.main_frame, text="Cafe Management System", font=("Times", 18),
                      anchor="center", background='#FAE7EB', fg='black')
        label.pack(pady=10)

        # Buttons
        button1 = Button(self.main_frame, text="Recipe Book", command=self.recipe_book, height=6, width=12, background="#EECEDA", fg="black")
        button1.pack(pady=10, padx=10)
        button1.place(x=width // 2 - 150, y=height // 2, anchor="center")

        button2 = Button(self.main_frame, text="Menu", command=self.menu, height=6, width=12, background="#EECEDA", fg="black")
        button2.pack(pady=10, padx=10)
        button2.place(x=width // 2-50, y=height // 2 - 150, anchor="center")

        # billing_photo = PhotoImage(file= r"C:\Users\JANARDHANA RAO\Downloads\billing.png")
        '''billing_photo.zoom(15)
        billing_photo.subsample(21)
        billing_image = billing_photo.subsample(3, 2) '''

        button3 = Button(self.main_frame, text="Billing", command=self.billing, height=6, width=12, background="#EECEDA", fg="black")
        button3.pack(pady=10, padx=10)
        button3.place(x=width // 2 + 150, y=height // 2 - 150, anchor="center")

        # staff_photo = PhotoImage(file= r"C:\Users\JANARDHANA RAO\Downloads\staff.png")
        # (275x183) image # x = 18(183/10)/height, y= 27(275/10)/width
        '''staff_photo.zoom(18)
        staff_photo.subsample(27)
        staff_image = staff_photo.subsample(3, 2)'''

        button4 = Button(self.main_frame, command=self.staff, text="Staff Details", height=6, width=12, background="#EECEDA", fg="black")
        button4.pack(padx=10, pady=10)
        button4.place(x=width // 2 - 250, y=height // 2 - 150, anchor="center")

        button5 = Button(self.main_frame, command=self.sales, text="Sales", height=6, width=12, background="#EECEDA", fg="black")
        button5.pack(padx=10, pady=10)
        button5.place(x=width // 2 + 50, y=height // 2, anchor="center")

        logout = Button(self.main_frame, text="Logout", command=self.logout, background="#EECEDA", fg="black")
        logout.pack(side=BOTTOM, padx=10, pady=10)
        logout.place(x=width // 2-50, y=height-200, anchor="center")

        # Running the main screen window
        self.main_screen.mainloop()
    def recipe_book(self):
        self.main_screen.after(1, lambda: recipe_book_screen(self.main_screen))

    def menu(self):
        self.main_screen.after(1, lambda: menu_screen(self.main_screen))

    def billing(self):
        self.main_screen.after(1, lambda: Billing_Screen(self.main_screen))

    def staff(self):
        self.main_screen.after(1, lambda: staff_details_screen(self.main_screen))

    def sales(self):
        self.main_screen.after(1,lambda: Sales_Screen(self.main_screen))
    def logout(self):
        self.main_screen.destroy()

