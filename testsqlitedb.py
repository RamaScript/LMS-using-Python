#GUI Tkinter Python Program to insert show and delete data with sqlite database

import tkinter as tk
import sqlite3
from tkinter import messagebox

def add_task():
        id1 = id_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        if id1 and name and age:
            cursor.execute("INSERT INTO user (id,name,age) VALUES (?,?,?)", (id1,name,age))
            conn.commit()
            load_tasks()
            id_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please input ID.")

def load_tasks():
    data_listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    for row in data:
        data_listbox.insert(tk.END, row[0],row[1],row[2])

def delete_task():
    selected_task = data_listbox.get(tk.ACTIVE)
    if selected_task:
        cursor.execute("DELETE FROM user WHERE id=?", (selected_task,))
        conn.commit()
        load_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")
def __del__(self):
    conn.close()

root = tk.Tk()

root.title("Python Tkinter Program with Sqlite Database Connection")
# Create a database or connect to an existing one
conn = sqlite3.connect("bca.db")
cursor = conn.cursor()
# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT,age TEXT)''')
conn.commit()
# Create GUI elements
label_1 = tk.Label(root, text="Enter ID:")
label_1.pack()
id_entry = tk.Entry(root)
id_entry.pack()
label_2 = tk.Label(root, text="Enter Name:")
label_2.pack()
name_entry = tk.Entry(root)
name_entry.pack()
label_3 = tk.Label(root, text="Enter Age:")
label_3.pack()
age_entry = tk.Entry(root)
age_entry.pack()
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()
data_listbox = tk.Listbox(root)
data_listbox.pack()
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()
load_tasks()


            
root.mainloop()