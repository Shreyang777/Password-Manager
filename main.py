from tkinter import *
from tkinter import messagebox
import random
import pyperclip
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]+[random.choice(symbols) for char in range(nr_symbols)]+[random.choice(numbers) for char in range(nr_numbers)]


    random.shuffle(password_list)

    password="".join(password_list)

    print(f"Your password is: {password}")

    password_input.insert(0,f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global website_input
    global password_input
    global email_input
    # write--------------------------------------------
    if len(website_input.get())==0 or len(password_input.get())==0 or len(email_input.get())==0:
        messagebox.showerror(title="Error",message="One or other fields empty")
    else:
        is_ok=messagebox.askokcancel(title="Save Password" ,message=f"These are details\nWebsite:{website_input.get()}\nEmail:{email_input.get()}\nPassword:{password_input.get()}")
        if is_ok:
            with open("data.txt", mode='a') as file:
                file.write(f"{website_input.get()}|{email_input.get()}|{password_input.get()}\n")

    #delete------------------------------------------
    website_input.delete(0,'end')
    password_input.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")

canvas=Canvas(width=200,height=200,bg="white",highlightthickness=0)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
#----------------------------------------Label------------------------------------------------------------------
website_label=Label(text="Website:" ,font=(FONT_NAME,12),bg="white")

website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:" ,font=(FONT_NAME,12),bg="white")
email_label.grid(row=2,column=0)

password_label=Label(text="Password:" ,font=(FONT_NAME,12),bg="white")
password_label.grid(row=3,column=0)

#-------------------------------------------Input---------------------------------------------------------------

website_input=Entry(width=48)
website_input.focus()
website_input.grid(row=1,column=1,columnspan=2,sticky="e")

email_input=Entry(width=48)
email_input.insert(0,"angela@gmail.com")
email_input.grid(row=2,column=1,columnspan=2,sticky="e")

password_input=Entry(width=25)
password_input.grid(row=3,column=1,columnspan=1)

#-------------------------------------Buttons--------------------------------------------------

generate=Button(text="Generate Password",width=15,command=generate_password)
generate.grid(row=3,column=2)

add=Button(text="Add",width=41,command=save)
add.grid(row=5,column=1,columnspan=2,sticky="e",ipadx=0)











window.mainloop()
