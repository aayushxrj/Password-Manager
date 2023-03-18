from tkinter import *
import csv



def submit():
    username = entry.get()
    password = entry2.get()
    platforms = platform.get()

    add_data(platforms,username,password)

    platform.delete(0,END)
    entry.delete(0,END)
    entry2.delete(0,END)   

    

def delete():
    platform.delete(0,END)
    entry.delete(0,END)
    entry2.delete(0,END)


def add_data(platforms, username, password):
    with open("data.csv","a+") as file:
        
        writing = csv.writer(file)
        writing.writerow([platforms, username, password])




window = Tk()

window.title("Password Manager")
window.config(background='black')

platform = Entry(window,
            font=("Comic Sans",25),
            fg="white",
            bg="black",
            
            )

platform.configure(insertbackground="white")
platform.pack(side=TOP)


entry = Entry(window,
            font=("Comic Sans",25),
            fg="white",
            bg="black",
            
            )
entry.configure(insertbackground="white")
entry.pack(side=TOP)

entry2 = Entry(window,
            font=("Comic Sans",25),
            fg="white",
            bg="black",
            show="*"
            )
entry2.configure(insertbackground="white")
entry2.pack(side=TOP)

label = Label(window,
            text="Write your \n Platform: \n Username: \n Password:",
            font=("Arial",8,"bold"),
            fg="white",
            bg="black",
            bd=10,
            padx=20,
            pady=20,
            compound="left")

label.pack(side=LEFT)














submit_button = Button(window,
                text="Save",
                command=submit,
                )
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                text="Clear",
                command=delete)
delete_button.pack(side=RIGHT)


window.mainloop()
