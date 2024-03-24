import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import os
from random import randint

def write_log(date):
    with open('log.txt', 'a+') as f:
        f.writelines(date.strftime('%Y-%m-%d') + '\n')

def commit_github(date):
    commit_time = date + randomTime()
    if commit_time <= datetime.datetime.now():
        os.system(f'git add .')
        os.system(f'git commit --date="{commit_time}" -m "Update {date} at {commit_time}."')

def randomTime():
    random_seconds = randint(0, (datetime.datetime.now() - datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)).seconds)
    return datetime.timedelta(seconds=random_seconds)

def run_script():
    min_commit_count = min_commit_var.get()
    max_commit_count = max_commit_var.get()

    if min_commit_count <= 0 or max_commit_count <= 0 or min_commit_count > max_commit_count:
        messagebox.showerror("Error", "Invalid commit count range")
        return

    commit_count = randint(min_commit_count, max_commit_count)

    current_date = datetime.datetime.now()
    for _ in range(commit_count):
        commit_time = current_date + randomTime()
        write_log(current_date)
        commit_github(commit_time)

    messagebox.showinfo("Commits Info", f"{commit_count} commits have been made on {current_date.date()}.")

# Create main window
root = tk.Tk()
root.title("GitHub Commit Script")

# Create input fields
min_commit_var = tk.IntVar(root, value=5)
max_commit_var = tk.IntVar(root, value=15)

min_commit_label = ttk.Label(root, text="Minimum commit count:")
min_commit_entry = ttk.Entry(root, textvariable=min_commit_var)

max_commit_label = ttk.Label(root, text="Maximum commit count:")
max_commit_entry = ttk.Entry(root, textvariable=max_commit_var)

run_button = ttk.Button(root, text="Run Script", command=run_script)

# Layout input fields
min_commit_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
min_commit_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

max_commit_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
max_commit_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

run_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Run the main event loop
root.mainloop()
