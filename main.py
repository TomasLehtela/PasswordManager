import tkinter as tk
from tkinter import messagebox
import string
import random
import os
import json

# Constants
FONT_TEXT = ("Arial", 12, "bold")
BG_COLOR = "#F1E0AC"
ENTRY_COLOR = "#EEEDDE"
SYMBOLS = "!#%&=?_-*"


def gen_pw():

    generated_password = "".join(
        [
            random.choice(string.ascii_letters + string.digits + SYMBOLS)
            for _ in range(10)
        ]
    )

    pw_entry.delete(0, tk.END)
    pw_entry.insert(0, generated_password)

    window.clipboard_clear()
    window.clipboard_append(generated_password)


def add_to_db():

    app_name = app_var.get()
    username = username_var.get()
    pw = pw_var.get()
    data_dict = {app_name: {"username": username, "password": pw}}

    if len(app_name) == 0 or len(username) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Error", message="Fields cant be empty")

    else:
        # data_dict = f"{app_name} | {username} | {pw}"

        # Pop-up in a warning window
        # popup = messagebox.askokcancel(
        #     title="Are you sure?",
        #     message=f"Do you want to add the following data?\n\nApplication: {app_name}\nUsername/E-mail: {username}\nPassword: {pw}",
        # )
        try:
            with open("pwdb.json", "r") as f:
                json_data = json.load(f)
                json_data.update(data_dict)

        except FileNotFoundError:
            print("Exception: File not found! Creating file..")
            json_data = data_dict

        finally:
            with open("pwdb.json", "w") as f:
                json.dump(json_data, f, indent=4)

            # Pop-up in a new window
            # final_text = f"Following data has been added:\nApplication: {app_name}\nUsername/E-mail: {username}\nPassword: {pw}"
            # popup = tk.Toplevel(window)
            # popup.geometry("300x85")
            # popup.title("Succesfully added!")
            # popup.config(padx=10, pady=10)
            # popup_text = tk.Label(popup, text=final_text, justify="left")
            # popup_text.pack(side="left")

            app_entry.delete(0, tk.END)
            pw_entry.delete(0, tk.END)
            if username_entry != "name@gmail.com":
                username_entry.delete(0, tk.END)
                username_entry.insert(0, "name@gmail.com")


def open_db():

    os.startfile(r"pwdb.json")


# Window
window = tk.Tk()
window.title("Password Manager Skii")
window.config(padx=20, pady=20, bg=BG_COLOR)

# Canvas
canvas = tk.Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
BG_IMG = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=BG_IMG)
canvas.grid(column=1, row=0)

# Entry StringVar()
app_var = tk.StringVar()
username_var = tk.StringVar()
pw_var = tk.StringVar()

# Text
app_text = tk.Label(text="Application:", font=FONT_TEXT, bg=BG_COLOR)
app_text.grid(column=0, row=1)

username_text = tk.Label(text="Username/E-mail:", font=FONT_TEXT, bg=BG_COLOR)
username_text.grid(column=0, row=2)

pw_text = tk.Label(text="Password:", font=FONT_TEXT, bg=BG_COLOR)
pw_text.grid(column=0, row=3)

# Entries
app_entry = tk.Entry(textvariable=app_var, font=FONT_TEXT, width=32, bg=ENTRY_COLOR)
app_entry.grid(column=1, row=1)
app_entry.focus()

username_entry = tk.Entry(
    textvariable=username_var, font=FONT_TEXT, width=45, bg=ENTRY_COLOR
)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "name@gmail.com")

pw_entry = tk.Entry(textvariable=pw_var, font=FONT_TEXT, width=32, bg=ENTRY_COLOR)
pw_entry.grid(column=1, row=3, columnspan=1)

# Generate PW Button
gen_pw_button = tk.Button(text="Generate Password", command=gen_pw, bg=ENTRY_COLOR)
gen_pw_button.grid(column=2, row=3)

# Add button
add_button = tk.Button(
    text="Add to database", command=add_to_db, width=57, bg=ENTRY_COLOR
)
add_button.grid(column=1, row=4, columnspan=2)

# Open db button
open_button = tk.Button(text="Open database", command=open_db, width=57, bg=ENTRY_COLOR)
open_button.grid(column=1, row=5, columnspan=2)

# Search button
search_button = tk.Button(text="Search", command=open_db, width=15, bg=ENTRY_COLOR)
search_button.grid(column=2, row=1)

window.mainloop()
