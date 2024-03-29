from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def find_password():
    search = web_entry.get()
    try:
        with open("Password_Manager.json", "r") as data:
            file = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found.")
    else:
        if search in file:
            email = file[search]["email"]
            password = file[search]["password"]
            messagebox.showinfo(title=f"{search}", message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Ooops", message="No details for the website exist")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_lett = [random.choice(letters) for _ in range(nr_letters)]
    password_symb = [random.choice(symbols) for _ in range(nr_symbols)]
    password_num = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_lett + password_num + password_symb

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, f"{password}")
    pyperclip.copy(password)
    messagebox.showinfo(title="Password", message="Password copied to clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(title="Ooops", message="Please don't leave any field empty")
    else:
        try:
            with open("Password_Manager.json", "r") as files:
                # read data
                data = json.load(files)
        except FileNotFoundError:
            with open("Password_Manager.json", "w") as files:
                json.dump(new_data, files, indent=4)
        else:
            data.update(new_data)
            with open("Password_Manager.json", "w") as files:
                json.dump(data, files, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Website
web_label = Label(text="Website", font=("Arial", 13))
web_label.grid(column=0, row=1)
web_entry = Entry(width=24)
web_entry.focus()
web_entry.grid(column=1, row=1)
website_search = Button(text="Search", command=find_password)
website_search.grid(column=2,row=1)

# Email/Username
email_label = Label(text="Email/Username", font=("Arial", 13))
email_label.grid(column=0, row=2)
email_entry = Entry(width=42)
email_entry.insert(0, "asdasdw@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password
pass_label = Label(text="Password", font=("Arial", 13))
pass_entry = Entry(width=24)
pass_generate = Button(text="Generate Password", command=generate_pass)
pass_label.grid(column=0, row=3)
pass_entry.grid(column=1, row=3)
pass_generate.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, padx=0, command=add)
add_button.grid(column=1, row=5, columnspan=2, )

# Image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

window.mainloop()
