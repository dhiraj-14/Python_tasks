import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('700x600')
root.config(bg='#d3f3f5')
root.title('Contact Book')
root.resizable(0, 0)

contactlist = [
    ['Siddharth Nigam', '369854712', 's1@gmail.com'],
    ['Gaurav Patil', '521155222', 'g2@gmail.com'],
    ['Abhishek Nikam', '78945614', 'a3@gmail.com'],
    ['Sakshi Gaikwad', '58745246', 'sa11@gmail.com'],
    ['Mohit Paul', '5846975', 'mo11@gmail.com'],
    ['Karan Patel', '5647892', 'kr10@gmail.com'],
    ['Sam Sharma', '89685320', 'sam13@gmail.com'],
    ['John Maheshwari', '98564785', 'jo11@gmail.com'],
    ['Ganesh Pawar', '85967412', 'ga16@gmail.com']
]

Name = tk.StringVar()
Number = tk.StringVar()
Email = tk.StringVar()  # Corrected variable name for email

frame = tk.Frame(root)
frame.pack(side=tk.RIGHT)

scroll = tk.Scrollbar(frame, orient=tk.VERTICAL)
select = tk.Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16),
                    bg="#f0fffc", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
select.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


def AddContact():
    if Name.get() != "" and Number.get() != "" and Email.get() != "":  # Ensure all fields are filled
        contactlist.append([Name.get(), Number.get(), Email.get()])  # Include email in contactlist
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        messagebox.showerror("Error", "Please fill in all the information")


def UpdateDetail():
    if Name.get() and Number.get() and Email.get():  # Ensure all fields are filled
        contactlist[Selected()] = [Name.get(), Number.get(), Email.get()]  # Update with email
        messagebox.showinfo("Confirmation", "Successfully Updated Contact")
        EntryReset()
        Select_set()
    else:
        messagebox.showerror("Error", "Please fill in all the information or select a contact")


def search():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Contact Not Found")
    else:
        NAME, PHONE, EMAIL = contactlist[Selected()]  # Retrieve email as well
        Name.set(NAME)
        Number.set(PHONE)
        Email.set(EMAIL)


def Delete_Entry():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please select a Contact")
    else:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result:
            del contactlist[Selected()]
            Select_set()


def View():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        NAME, PHONE, EMAIL = contactlist[Selected()]  # Retrieve email as well
        Name.set(NAME)
        Number.set(PHONE)
        Email.set(EMAIL)


def EXIT():
    root.destroy()


def Select_set():
    contactlist.sort()
    select.delete(0, tk.END)
    for name, phone, email in contactlist:
        select.insert(tk.END, name)


def EntryReset():
    Name.set('')
    Number.set('')
    Email.set('')  # Clear email field as well


# Labels and Entry fields
tk.Label(root, text='Name', font=("Times new roman", 18, "bold"), bg='SlateGray3').place(x=30, y=20)
tk.Entry(root, textvariable=Name, width=30).place(x=200, y=30)
tk.Label(root, text='Contact No.', font=("Times new roman", 18, "bold"), bg='SlateGray3').place(x=30, y=70)
tk.Entry(root, textvariable=Number, width=30).place(x=200, y=80)
tk.Label(root, text='Email', font=("Times new roman", 18, "bold"), bg='SlateGray3').place(x=30, y=130)
tk.Entry(root, textvariable=Email, width=30).place(x=200, y=130)

# Buttons
tk.Button(root, text="ADD Contact", font='Helvetica 14 bold', bg='#e8c1c8', command=AddContact, padx=20).place(x=50, y=180)
tk.Button(root, text="Update", font='Helvetica 14 bold', bg='#e8c1c8', command=UpdateDetail, padx=20).place(x=50, y=240)
tk.Button(root, text="Search", font='Helvetica 14 bold', bg='#e8c1c8', command=search, padx=20).place(x=50, y=310)
tk.Button(root, text="DELETE", font='Helvetica 14 bold', bg='#e8c1c8', command=Delete_Entry, padx=20).place(x=50, y=370)
tk.Button(root, text="VIEW", font='Helvetica 14 bold', bg='#e8c1c8', command=View).place(x=50, y=440)
tk.Button(root, text="EXIT", font='Helvetica 22 bold', bg='tomato', command=EXIT).place(x=190, y=500)

# Initialize the listbox
Select_set()

root.mainloop()