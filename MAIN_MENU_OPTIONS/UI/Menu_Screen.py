from tkinter import *
import sqlite3
from tkinter import messagebox


class menu_screen:
    def __init__(self, main_window):
        self.menu_window = Toplevel(main_window, bg="#EECEDA")
        self.menu_window.title("Menu")
        self.menu_window.geometry("500x500")
        self.menu_frame = Frame(self.menu_window, bg="#FAE7EB")
        self.menu_frame.pack(fill="both", expand=True, padx=50, pady=50)
        self.conn = sqlite3.connect("Database.db")
        self.cursor = self.conn.cursor()

        # Create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Menu 
                (Id INTEGER PRIMARY KEY, Item TEXT, Price INTEGER)''')
        self.conn.commit()

        self.list = Label(self.menu_frame, text="Menu", font=('copperplate gothic bold', 10), bg="#FAE7EB")
        self.list.pack(padx=5, pady=5)
        self.cursor.execute('SELECT Item,Price FROM Menu')
        ans = self.cursor.fetchall()
        l = Label(self.menu_frame, text=" Item - Price ", bg='#FAE7EB')
        l.pack()
        for index, i in enumerate(ans):
            s = " | " + i[0] + " - " + str(i[1]) + "/-" + " | "
            l1 = Label(self.menu_frame, text=s, bg="#FAE7EB")
            l1.pack(side=TOP, padx=1, pady=1, anchor=S)
        new_win1 = Button(self.menu_frame, text="Add or Delete item", command=self.add_del)
        new_win1.pack(side=BOTTOM, anchor='center', pady=5)

    def add_del(self):
        self.add_del_screen = Toplevel(self.menu_frame, bg="#FAE7EB")
        self.add_del_screen.resizable(0, 0)
        self.item_label = Label(self.add_del_screen, text="Enter Item: ", bg="#FAE7EB")
        self.item_label.pack(padx=10, pady=10)
        self.item_name = Entry(self.add_del_screen)
        self.item_name.pack(padx=10, pady=10)
        self.price = Label(self.add_del_screen, text="Price: ", bg="#FAE7EB")
        self.price.pack(padx=10, pady=10)
        self.price_details = Entry(self.add_del_screen)
        self.price_details.pack(padx=10, pady=10)
        self.add_button = Button(self.add_del_screen, text="Add Item", command=self.add_item)
        self.add_button.pack(padx=10, pady=10)
        self.menu_listbox = Listbox(self.add_del_screen)
        self.menu_listbox.pack(padx=10, pady=10)
        self.delete_button = Button(self.add_del_screen, text="Delete Item", command=self.delete_item)
        self.delete_button.pack(padx=10, pady=10)
        self.load_items()

    def add_item(self):
        name = self.item_name.get()
        price = self.price_details.get()
        if name:
            self.cursor.execute("INSERT INTO Menu (Item,Price) VALUES (?,?)", (name, price))
            self.conn.commit()
            self.load_items()
            messagebox.showinfo("Success", "Added Successfully")
            self.add_del_screen.destroy()
        else:
            messagebox.showwarning("Warning", "Please input an item.")

    def load_items(self):
        self.menu_listbox.delete(0, END)
        self.cursor.execute("SELECT Item FROM Menu")
        menu = self.cursor.fetchall()
        for row in menu:
            self.menu_listbox.insert(END, row)

    def delete_item(self):
        selected_item = self.menu_listbox.get(ACTIVE)
        if selected_item:
            self.cursor.execute("DELETE FROM Menu WHERE item=?", (selected_item,))
            self.conn.commit()
            self.load_items()
            messagebox.showinfo("Success", "Deleted Successfully")
            self.add_del_screen.destroy()
        else:
            messagebox.showwarning("Warning", "Please select an item to delete.")

    def __del__(self):
        self.conn.close()
