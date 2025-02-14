import tkinter
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk


#make the main window
root = tkinter.Tk()
root.title("Login form")
root.geometry('540x600')
root.configure(bg='#333333')

frame = tkinter.Frame(bg="#333333")

def login():
    """This is the login function"""
    username = username_entry.get()  # Access username entry
    password = password_entry.get()  # Access password entry
    # Simple validation
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome to the budget app!")
    else:
        messagebox.showerror("Login Error", "Invalid username or password!")
        
#load the background image
img = Image.open(r"\\wsl$\Ubuntu\home\mrholocker\workspace\github.com\ZHolocker\budgetapp\budgetapp\logo.png")
img = img.resize((400,200))
bg_image = ImageTk.PhotoImage(img)

#create all widgets here
background_label = tkinter.Label(frame, image=bg_image, bg="#333333")
#logo_label = tkinter.Label(frame, image="finsight_logo.png")
login_label = tkinter.Label(frame, text="Login", bg="#333333", fg="#FFFFFF", font=("Arial", 30) )
username_label = tkinter.Label(frame, text="Username",bg="#333333", fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg="#333333", fg="#FFFFFF",font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg="white", font=("Arial", 16), command=login)

#widget placements
background_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)
login_label.grid(row=1, column=0, columnspan=2, sticky="news", pady=10)
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, pady=20)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1, pady=20)
login_button.grid(row=4, column=0, columnspan=2, pady=30)



frame.pack()



root.mainloop()
