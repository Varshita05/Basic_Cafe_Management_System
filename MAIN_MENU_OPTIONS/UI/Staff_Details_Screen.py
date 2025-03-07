from tkinter import *
import sqlite3
from tkinter import messagebox


class staff_details_screen:
    def __init__(self, main_window):
        self.details_win = Toplevel(main_window, bg="#EECEDA")
        self.details_win.title("Staff Details")
        self.details_win.geometry("500x500")
        self.details_window = Frame(self.details_win, bg="#FAE7EB")
        self.details_window.pack(fill="both", expand=True, padx=50, pady=50)
        self.conn = sqlite3.connect("Database.db")
        self.cursor = self.conn.cursor()
        # Create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS staff 
                       (id INTEGER PRIMARY KEY, staff_id INTEGER, staff_name TEXT, staff_phno INTEGER)''')
        self.conn.commit()

        self.list = Label(self.details_window, text="Working Staff", font=('copperplate gothic bold', 10), bg="#FAE7EB")
        self.list.pack(padx=5, pady=5)
        self.cursor.execute('SELECT * FROM staff')
        ans = self.cursor.fetchall()
        l = Label(self.details_window, text=" Staff Id - Staff Name - Staff Phone Number ", bg='#FAE7EB')
        l.pack()
        for index, i in enumerate(ans):
            s = " | " + str(i[1]) + " - " + i[2] + " - " + str(i[3]) + " | "
            l1 = Label(self.details_window, text=s, bg="#FAE7EB")
            l1.pack(side=TOP, padx=1, pady=1, anchor=S)
        new_win1 = Button(self.details_window, text="Add or Delete Staff", command=self.add_del)
        new_win1.pack(side=BOTTOM, anchor='center', pady=5)


    def add_del(self):
        self.add_del_screen = Toplevel(self.details_window, bg="#FAE7EB")
        self.add_del_screen.resizable(0, 0)
        self.staff_label = Label(self.add_del_screen, text="Enter Staff Id: ", bg="#FAE7EB")
        self.staff_label.pack(padx=10, pady=10)
        self.staff_id = Entry(self.add_del_screen)
        self.staff_id.pack(padx=10, pady=10)
        self.name_label = Label(self.add_del_screen, text="Enter Staff Name: ", bg="#FAE7EB")
        self.name_label.pack(padx=10, pady=10)
        self.staff_name = Entry(self.add_del_screen)
        self.staff_name.pack(padx=10, pady=10)
        self.phno_label = Label(self.add_del_screen, text="Enter Staff Phone Number: ", bg="#FAE7EB")
        self.phno_label.pack(padx=10, pady=10)
        self.staff_phno = Entry(self.add_del_screen)
        self.staff_phno.pack(padx=10, pady=10)
        self.add_button = Button(self.add_del_screen, text="Add Staff", command=self.add_staff)
        self.add_button.pack(padx=10, pady=10)
        self.staff_listbox = Listbox(self.add_del_screen, yscrollcommand=True, xscrollcommand=True)
        self.staff_listbox.pack(padx=10, pady=10)
        self.load_staff()
        self.delete_button = Button(self.add_del_screen, text="Delete Staff", command=self.delete_staff)
        self.delete_button.pack(padx=10, pady=10)
        self.load_staff()

    def add_staff(self):
        id1 = self.staff_id.get()
        name = self.staff_name.get()
        phno = self.staff_phno.get()
        if id:
            self.cursor.execute("INSERT INTO staff (staff_id,staff_name,staff_phno) VALUES (?,?,?)", (id1, name, phno))
            self.conn.commit()
            self.load_staff()
            messagebox.showinfo("Success", "Added Successfully")
            self.details_win.destroy()
        else:
            messagebox.showwarning("Warning", "Please input details.")

    def load_staff(self):
        self.staff_listbox.delete(0, END)
        self.cursor.execute("SELECT * FROM staff")
        list1 = self.cursor.fetchall()
        for row in list1:
            self.staff_listbox.insert(END, row[1])

    def delete_staff(self):
        selected_staff = self.staff_listbox.get(ACTIVE)
        if selected_staff:
            self.cursor.execute("DELETE FROM staff WHERE staff_id=?", (selected_staff,))
            self.conn.commit()
            self.load_staff()
            messagebox.showinfo("Success", "Deleted Successfully")
            self.details_win.destroy()
        else:
            messagebox.showwarning("Warning", "Please select staff to delete.")

    def __del__(self):
        self.conn.close()
