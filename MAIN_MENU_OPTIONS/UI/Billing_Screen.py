from tkinter import *
import sqlite3
from tkinter import messagebox

class Billing_Screen:
    def __init__(self, main_window):
        self.billing_win = Toplevel(main_window,bg="#EECEDA")
        self.billing_win.title("Billing")
        self.billing_window = Frame(self.billing_win, bg="#FAE7EB")
        self.billing_window.pack(fill="both", padx=50, pady=50)
        self.conn = sqlite3.connect("Sales.db")
        self.cursor = self.conn.cursor()

        #Create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS January_Sales_2025 (Order_Id INTEGER PRIMARY KEY,
         Order_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, Order_Items STRING, Quantity INTEGER, Total INTEGER)''')
        self.conn.commit()

        self.current_order = []
        # Create GUI elements
        self.details = Label(self.billing_window, text="--Billing--", font=('copperplate gothic bold', 10), bg="#FAE7EB")
        self.details.pack(padx=5, pady=5)
        self.menu = sqlite3.connect("Database.db")
        self.m_cursor = self.menu.cursor()
        self.m_cursor.execute("SELECT * FROM Menu")
        self.menu.commit()
        self.list = self.m_cursor.fetchall()
        self.items_list = []
        for i in self.list:
            self.items_list.append(i[1])
        self.click, self.clicked = StringVar(), StringVar()
        self.clicked.set(self.items_list[0])
        self.drop = OptionMenu(self.billing_window,self.clicked,*self.items_list)
        self.drop.pack(padx=10,pady=10)
        values = ['1','2','3']
        self.click.set(values[0])
        self.drop1 = OptionMenu(self.billing_window,self.click,*values)
        self.drop1.pack(padx=10,pady=10)
        self.order_add = Button(self.billing_window,text="Add item to order",command=self.add_order,anchor=NE)
        self.order_add.pack(padx=10,pady=10)
        self.order_place = Button(self.billing_window, text="Place order", command=self.place_order, anchor=NE)
        self.order_place.pack(padx=10,pady=10)

    def place_order(self):
        self.billing_win.destroy()
        self.receipt_win = Tk()
        self.receipt_win.title("Receipt")
        self.receipt_frame = Frame(self.receipt_win)
        self.receipt_frame.pack()
        l = Label(self.receipt_frame, text="Item Name - Quantity - Price")
        l.pack()
        self.order_total = 0
        self.total_quantity = 0
        self.items = ""
        for index,i in enumerate(self.current_order):
            s = " | "+i[0]+" - "+i[1]+" - "+str(i[2])+" | "
            self.order_total+=i[2]
            self.total_quantity+=int(i[1])
            if index<len(self.current_order)-1:
                self.items += i[0] + ", "
            else:
                self.items+=i[0]
            i_l = Label(self.receipt_frame,text=s)
            i_l.pack()
        pay = "Total Payment to be done : "+str(self.order_total)+"/-"
        pay_label = Label(self.receipt_frame,text=pay)
        pay_label.pack(padx=10,pady=10)
        pay_done = Button(self.receipt_frame,text="Payment Done",command=self.payment_done)
        pay_done.pack(padx=10,pady=10)

    def payment_done(self):
        self.cursor.execute('''INSERT INTO January_Sales_2025 (Order_Items, Quantity, Total) 
        VALUES (?,?,?)''',(self.items,self.total_quantity,self.order_total))
        self.conn.commit()
        messagebox.showinfo("Done","Order Placed")
        self.receipt_win.destroy()
    def add_order(self):
        self.name = self.clicked.get()
        self.quant = self.click.get()
        index = self.items_list.index(self.name)
        price = int(self.quant)*int(self.list[index][2])
        self.current_order.append([self.name,self.quant,price])
        l = Label(self.billing_window,text="Added the item to order !",fg='red',bg="#FAE7EB")
        l.pack()
        l.after(2000,l.destroy)
    def __del__(self):
        self.conn.close()