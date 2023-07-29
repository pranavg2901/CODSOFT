import datetime
import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Connect to the MySQL database
db_connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="todo_db")
db_cursor = db_connection.cursor()

# Function to add a new task to the database
def add_task():
    task_name = task_entry.get()
    due_date = due_date_entry.get()

    if task_name.strip() == '' or due_date.strip() == '':
        messagebox.showwarning("Error", "Please enter both, Task Name and Date.")
        return

    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showwarning("Error", "Invalid Date format. Please use YYYY-MM-DD.")
        return

    # Insert the task into the database
    sql_query = "INSERT INTO tasks (task_name, due_date) VALUES (%s, %s)"
    values = (task_name, due_date)
    db_cursor.execute(sql_query, values)
    db_connection.commit()

    task_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    update_task_list()

# Function to update the task list displayed in the GUI
def update_task_list():
    task_list.delete(0, tk.END)

    # Retrieve tasks from the database
    sql_query = "SELECT task_name, due_date FROM tasks ORDER BY due_date"
    db_cursor.execute(sql_query)
    tasks = db_cursor.fetchall()

    for task in tasks:
        task_name, due_date = task
        task_list.insert(tk.END, f"{due_date.strftime('%Y-%m-%d')} - {task_name}")

# Set up the GUI
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500+515+160")
root.configure(bg='#cce6ff')
icon = PhotoImage(file='icon.png')
root.iconphoto(False,icon)

task_title = tk.Label(root,text="TO-DO List",font=("Times New Roman",23,"bold"),bg='#cce6ff')
task_title.pack(pady=5)

task_label = tk.Label(root, text="Task",font=("Times New Roman",13,"bold"),bg='#cce6ff')
task_label.pack(pady=1)

task_entry = tk.Entry(root,width=30)
task_entry.pack(pady=5)

due_date_label = tk.Label(root, text="Date (YYYY-MM-DD)",font=("Times New Roman",13,"bold"),bg='#cce6ff')
due_date_label.pack(pady=1)

due_date_entry = tk.Entry(root,width=30)
due_date_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task,font=('Times New Roman',13))
add_button.pack(pady=10)

task_list = tk.Listbox(root, width=50,bg='white',font=("Times New ROman",12))
task_list.pack(pady=5)

update_task_list()

root.mainloop()
