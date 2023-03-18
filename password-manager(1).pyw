from tkinter import *
import csv

def submit():
    username = entry.get()
    password = entry2.get()
    platforms = platform.get()
    re_password = entry3.get()
    #platformi= "PLATFORM"
    #usernamei = "USERNAME"
    #passwordi = "PASSWORD"
    #add_data(platformi,usernamei,passwordi)
               
    # if platforms == "" or " ":
    #     lbl5.config(text="Platform Box can't be blank!")
    # else:
        
    #     if username == "" or " ":
    #         lbl5.config(text="Username Box can't be blank!")  
    #     else:  
    #         if password == "" or " ":
    #             lbl5.config(text="Password Box can't be blank!") 
            
    #         else:
    
    if re_password != password:
        lbl5.config(text="Passwords do not match!")
        entry2.delete(0,END) 
        entry3.delete(0,END)
    else :
        add_data(platforms,username,password)
        platform.delete(0,END)
        entry.delete(0,END)
        entry2.delete(0,END) 
        entry3.delete(0,END) 
        lbl5.config(text="Saved Successfully!")
                               
def delete():
    platform.delete(0,END)
    entry.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

def add_data(platforms, username, password):
    with open("passwords.csv","a+") as file:
        writing = csv.writer(file)
        writing.writerow([platforms, username, password])

window = Tk()
window.title("Password Manager")
window.config(background='black')
window.geometry("400x270")

lbl = Label(window,text="Enter Platform:",
            anchor="center",
            fg="white",
            bg="black",
            pady=5)
lbl.pack()

platform = Entry(window,
            font=("Comic Sans",15),
            fg="white",
            bg="black",
            width=35,
            justify="center"            
            )

platform.configure(insertbackground="white")
platform.pack(side=TOP)

lbl2 = Label(window,text="Enter Your Username:",
            anchor="center",
            fg="white",
            bg="black",
            pady=5)
lbl2.pack()

entry = Entry(window,
            font=("Comic Sans",15),
            fg="white",
            bg="black",
            width=35,
            justify="center"
            
            )
entry.configure(insertbackground="white")
entry.pack(side=TOP)

lbl3 = Label(window,text="Enter Your Password:",
            anchor="center",
            fg="white",
            bg="black",
            pady=5)
lbl3.pack()

entry2 = Entry(window,
            font=("Comic Sans",15),
            fg="white",
            bg="black",
            show="*",
            width=35,
            justify="center"
            )
entry2.configure(insertbackground="white")
entry2.pack(side=TOP)


lbl4 = Label(window,text="Re-enter Your Password:",
            anchor="center",
            fg="white",
            bg="black",
            pady=5)
lbl4.pack()

entry3 = Entry(window,
            font=("Comic Sans",15),
            fg="white",
            bg="black",
            show="*",
            width=35,
            justify="center"
            )
entry3.configure(insertbackground="white")
entry3.pack(side=TOP)




submit_button = Button(window,
                text="Save",
                command=submit,
                background="black",
                foreground="white",
                padx=3,
                pady=3,
                width=7)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                text="Clear",
                command=delete,
                background="black",
                foreground="white",
                padx=3,
                pady=3,
                width=7)
delete_button.pack(side=RIGHT)

lbl5 = Label(window,
            text ="",
            fg="white",
            bg="black",
            padx=10)
lbl5.pack(side=LEFT)

window.mainloop()



