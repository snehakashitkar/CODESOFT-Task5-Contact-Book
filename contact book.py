import tkinter as tk
from tkinter import messagebox, simpledialog

# Contact Book Dictionary to store contact information
contact_book = {}

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter contact name:")
    if not name:
        return
    if name in contact_book:
        messagebox.showerror("Error", "Contact already exists!")
        return
    
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email address:")
    address = simpledialog.askstring("Input", "Enter address:")
    
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    messagebox.showinfo("Success", "Contact added successfully!")
    update_contact_list()

# Function to display all contacts
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contact_book.items():
        contact_list.insert(tk.END, f"{name}: {details['phone']}")

# Function to search a contact by name or phone
def search_contact():
    search_term = simpledialog.askstring("Search", "Enter contact name or phone number to search:")
    if not search_term:
        return
    
    found_contacts = []
    for name, details in contact_book.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            found_contacts.append(f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n")
    
    if found_contacts:
        messagebox.showinfo("Search Result", "\n\n".join(found_contacts))
    else:
        messagebox.showerror("Not Found", "No matching contact found!")

# Function to update an existing contact
def update_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
    if name not in contact_book:
        messagebox.showerror("Error", "Contact not found!")
        return
    
    phone = simpledialog.askstring("Input", f"Enter new phone number for {name} (current: {contact_book[name]['phone']}):")
    email = simpledialog.askstring("Input", f"Enter new email for {name} (current: {contact_book[name]['email']}):")
    address = simpledialog.askstring("Input", f"Enter new address for {name} (current: {contact_book[name]['address']}):")
    
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    messagebox.showinfo("Success", "Contact updated successfully!")
    update_contact_list()

# Function to delete a contact
def delete_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
    if name in contact_book:
        del contact_book[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        update_contact_list()
    else:
        messagebox.showerror("Error", "Contact not found!")

# Create the main window
window = tk.Tk()
window.title("Contact Book")

# Add a title label
title_label = tk.Label(window, text="Contact Book", font=("Arial", 20))
title_label.pack(pady=10)

# Contact list display
contact_list = tk.Listbox(window, width=50, height=10)
contact_list.pack(pady=10)

# Buttons for different actions
add_button = tk.Button(window, text="Add Contact", width=20, command=add_contact)
add_button.pack(pady=5)

view_button = tk.Button(window, text="View Contacts", width=20, command=update_contact_list)
view_button.pack(pady=5)

search_button = tk.Button(window, text="Search Contact", width=20, command=search_contact)
search_button.pack(pady=5)

update_button = tk.Button(window, text="Update Contact", width=20, command=update_contact)
update_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Contact", width=20, command=delete_contact)
delete_button.pack(pady=5)

# Start the GUI loop
window.mainloop()
