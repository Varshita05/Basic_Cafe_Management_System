from tkinter import *
import sqlite3
class Sales_Screen:
    def __init__(self, main_window):
        self.sales_window = Toplevel(main_window, bg="#EECEDA")
        self.sales_window.title("Sales")
        self.sales_window.geometry("500x500")
        self.sales_frame = Frame(self.sales_window, bg="#FAE7EB")
        self.sales_frame.pack(fill="both", expand=True, padx=50, pady=50)
        self.conn = sqlite3.connect("Sales.db")
        self.cursor = self.conn.cursor()

        self.list = Label(self.sales_frame, text="2025 Sales", font=('copperplate gothic bold', 10), bg="#FAE7EB")
        self.list.pack(padx=5, pady=5)
        self.list = Label(self.sales_frame, text="January Sales", font=('Times', 10), bg="#FAE7EB")
        self.list.pack(padx=5, pady=5)
        self.cursor.execute('SELECT * FROM January_Sales_2025')
        ans = self.cursor.fetchall()
        l = Label(self.sales_frame, text=" Order_Id - Date - Order_Items - Quantity - Total ", bg='#FAE7EB')
        l.pack()
        for index, i in enumerate(ans):
            s = " | " + str(i[0]) + " - " + str(i[1]) + " - " + i[2] + " - " + str(i[3]) + " - " + str(i[4]) + "/-" + " | "
            l1 = Label(self.sales_frame, text=s, bg="#FAE7EB")
            l1.pack(side=TOP, padx=1, pady=1, anchor=S)

        self.sales_window.mainloop()