from tkinter import *
from tkinter import ttk
import tkcalendar


root = Tk()
root.title("Fager Employee Form")
root.geometry("700x500")
title_labal = ttk.Label(root, text="Employee Form", font="inter")
title_labal.grid(row=0, column=0, columnspan=4, pady=10)


#name
fname = ttk.Label(root, text="First name:")
fname.grid(row=1, column=0, pady=10, padx=5, sticky="nw")

fnameentry = ttk.Entry(root, width=25)
fnameentry.focus_set()
fnameentry.grid(row=1, column=1, pady=10, padx=10)

lname = ttk.Label(root, text="Last name:")
lname.grid(row=1, column=2, pady=10, sticky="nw")

lnameentry = ttk.Entry(root, width=25)
lnameentry.grid(row=1, column=3, pady=10)


#Date of birth
dateofbirth= ttk.Label(root, text="Date Of Birth:")
dateofbirth.grid(row=2, column=0, pady=10, padx=5, sticky="nw")

dateofbirth = tkcalendar.DateEntry(root)
dateofbirth.grid(row=2, column=1, columnspan=3, pady=10, sticky="we")


#Gender
gender = StringVar()
gender.set("none")

gender_lable = ttk.Label(root, text="Gender:") 
gender_lable.grid(row=3, column=0, pady=10, padx=5, sticky="nw")

male = ttk.Radiobutton(root, text="Male", variable=gender, value="male")
male.grid(row=3, column=1, pady=10)

female = ttk.Radiobutton(root, text="Female", variable=gender, value="female")
female.grid(row=3, column=2, pady=10)
 

#Country
country_lable = ttk.Label(root, text="Country:")
country_lable.grid(row=4, column=0, pady=10, padx=5, sticky="nw")

country = ttk.Combobox(root, values=["Sudan", "UAE", "Egypt", "Moroco"])
country.grid(row= 4, column=1, columnspan=3, pady=10, padx=5, sticky="we")


#Address
Address_lable = ttk.Label(root, text="Address:")
Address_lable.grid(row=5, column=0, pady=10, padx=5, sticky="nw")

address = Text(root, height=5)
address.grid(row= 5, column=1, columnspan=4, pady=10, sticky="we")


#Buttons
def record():
    firstname = fnameentry.get()
    lastname = lnameentry.get()
    birth = dateofbirth.get()
    gender_ = gender.get()
    country_ = country.get()
    address_ = address.get("1.0", "end -1c")
    text = f"{firstname}, {lastname}, {birth}, {gender_}, {country_}, {address_}.\n"
    with open("employee form/employee.csv", "a") as file:
        file.write(text)
    clearAll()


def clearAll():
    fnameentry.delete("0", "end")
    lnameentry.delete("0", "end")
    dateofbirth.delete("0", "end")
    gender.set("none")
    country.delete("0", "end")
    address.delete("1.0", "end")
    fnameentry.focus_set()


save = ttk.Button(root, text="Save", command=record)
save.grid(row=6, column=1, pady=10, ipadx=10, ipady=3)

clear = ttk.Button(root, text="Clear", command=clearAll)
clear.grid(row=6, column=3, pady=10, ipadx=10, ipady=3)

exit_ = ttk.Button(root, text="Exit", width=20, command=exit)
exit_.grid(row=7, column=2, pady=10, rowspan=3, sticky="we", ipadx=10, ipady=3)


root.mainloop()
