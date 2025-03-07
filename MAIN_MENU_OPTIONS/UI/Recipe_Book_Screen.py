from tkinter import messagebox
import sqlite3
from tkinter import *


class recipe_book_screen:
    def __init__(self, main_window):
        self.recipe_book_win = Toplevel(main_window, bg="#EECEDA")
        self.recipe_book_win.title("Recipe Book")
        self.recipe_book_win.geometry("500x500")
        self.recipe_book_window = Frame(self.recipe_book_win, bg="#FAE7EB")
        self.recipe_book_window.pack(fill="both", expand=True, padx=50, pady=50)
        self.conn = sqlite3.connect("Database.db")
        self.cursor = self.conn.cursor()

        self.list = Label(self.recipe_book_window, text="Available Recipes", font=('copperplate gothic bold', 10), bg="#FAE7EB")
        self.list.pack(padx=5, pady=5)
        self.cursor.execute('SELECT * FROM Recipes')
        ans = self.cursor.fetchall()
        # Create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes 
                (Id INTEGER PRIMARY KEY, Recipe_name TEXT, Recipe TEXT)''')
        self.conn.commit()


        l = Label(self.recipe_book_window, text=" Recipe Name - Recipe ", bg='#FAE7EB')
        l.pack()
        for index, i in enumerate(ans):
            s = " | " + i[1] + " - " + i[2] + " | "
            l1 = Label(self.recipe_book_window, text=s, bg="#FAE7EB")
            l1.pack(side=TOP, padx=1, pady=1, anchor=S)
        new_win1 = Button(self.recipe_book_window, text="Add or Delete Recipe", command=self.add_del)
        new_win1.pack(side=BOTTOM, anchor='center',pady=5)
        # new_win = Button(self.recipe_book_window,text="Add Recipe",command=self.addi)
        # new_win.pack(side=BOTTOM,anchor='center',pady=5)


        '''self.name1 = Label(self.recipe_book_window, text="Recipe Name")
        self.name1.pack()
        self.name2 = Label(self.recipe_book_window, text="Recipe")
        self.name2.pack()'''


    def add_del(self):
        self.add_del_screen = Toplevel(self.recipe_book_window, bg="#FAE7EB")
        self.add_del_screen.resizable(0,0)
        # self.add_screen = Frame(self.add_del_screen, bg="#FAE7EB")
        # self.add_screen.pack()
        self.recipe_label = Label(self.add_del_screen, text="Enter Recipe Name: ", bg="#FAE7EB")
        self.recipe_label.pack(padx=10, pady=10)
        self.recipe_name = Entry(self.add_del_screen)
        self.recipe_name.pack(padx=10, pady=10)
        self.details = Label(self.add_del_screen, text="Enter Recipe Details: ",bg="#FAE7EB")
        self.details.pack(padx=10, pady=10)
        self.recipe_details = Entry(self.add_del_screen)
        self.recipe_details.pack(padx=10, pady=10)
        self.add_button = Button(self.add_del_screen, text="Add Recipe", command=self.add_recipe)
        self.add_button.pack(padx=10, pady=10)
        # self.del_win = Toplevel(self.recipe_book_window, bg="#FAE7EB")
        # self.del_win.resizable(0, 0)
        # self.del_screen = Frame(self.del_win, bg="#FAE7EB")
        # self.del_screen.pack()
        self.recipe_listbox = Listbox(self.add_del_screen)
        self.recipe_listbox.pack(padx=10, pady=10)
        self.delete_button = Button(self.add_del_screen, text="Delete Recipe", command=self.delete_recipe)
        self.delete_button.pack(padx=10, pady=10)
        self.load_recipes()

    def add_recipe(self):
        name = self.recipe_name.get()
        detail = self.recipe_details.get()
        if name:
            self.cursor.execute("INSERT INTO Recipes (Recipe_Name,Recipe) VALUES (?,?)", (name, detail))
            self.conn.commit()
            self.load_recipes()
            messagebox.showinfo("Success","Added Successfully")
            self.recipe_book_win.destroy()
        else:
            messagebox.showwarning("Warning", "Please input a name.")

    def load_recipes(self):
        self.recipe_listbox.delete(0, END)
        self.cursor.execute("SELECT * FROM Recipes")
        recipes = self.cursor.fetchall()
        for row in recipes:
            self.recipe_listbox.insert(END, row[1])

    def delete_recipe(self):
        selected_recipe = self.recipe_listbox.get(ACTIVE)
        if selected_recipe:
            self.cursor.execute("DELETE FROM recipes WHERE recipe_name=?", (selected_recipe,))
            self.conn.commit()
            self.load_recipes()
            messagebox.showinfo("Success", "Deleted Successfully")
            self.add_del_screen.destroy()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def __del__(self):
        self.conn.close()
