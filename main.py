from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    with open("Password_Manager.txt","a") as files:
        files.write(f"{website} | {email} | {password} \n")
        web_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Website
web_label = Label(text="Website", font=("Arial", 13))
web_label.grid(column=0, row=1)
web_entry = Entry(width=42)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

# Email/Username
email_label = Label(text="Email/Username", font=("Arial", 13))
email_label.grid(column=0, row=2)
email_entry = Entry(width=42)
email_entry.insert(0,"asdasdw@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password
pass_label = Label(text="Password",font=("Arial", 13))
pass_entry = Entry(width=24)
pass_generate = Button(text="Generate Password")
pass_label.grid(column=0, row=3)
pass_entry.grid(column=1, row=3)
pass_generate.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, padx=0, command=add)
add_button.grid(column=1, row=5, columnspan=2,)

# Image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=1, row=0)

window.mainloop()