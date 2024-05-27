import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        self.save_contacts()
        return f"Contact '{name}' added successfully."

    def view_contacts(self):
        return self.contacts

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if name.lower() in contact['name'].lower()]
        return found_contacts

    def update_contact(self, old_name, new_name, phone, email, address):
        for contact in self.contacts:
            if contact['name'].lower() == old_name.lower():
                contact.update({
                    'name': new_name,
                    'phone': phone,
                    'email': email,
                    'address': address
                })
                self.save_contacts()
                return f"Contact '{old_name}' updated successfully."
        return f"No contact found with the name '{old_name}'."

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                return f"Contact '{name}' deleted successfully."
        return f"No contact found with the name '{name}'."

class ContactBookApp:
    def __init__(self, root):
        self.book = ContactBook()
        self.root = root
        self.root.title("Contact Book")

        self.frame = tk.Frame(root, bg='yellow')
        self.frame.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact, bg='yellow', fg='black', font=('Helvetica', 12, 'bold'))
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.view_button = tk.Button(self.frame, text="View Contacts", command=self.view_contacts, bg='yellow', fg='black', font=('Helvetica', 12, 'bold'))
        self.view_button.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tk.Button(self.frame, text="Search Contact", command=self.search_contact, bg='yellow', fg='black', font=('Helvetica', 12, 'bold'))
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.update_button = tk.Button(self.frame, text="Update Contact", command=self.update_contact, bg='yellow', fg='black', font=('Helvetica', 12, 'bold'))
        self.update_button.grid(row=0, column=3, padx=5, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact, bg='yellow', fg='black', font=('Helvetica', 12, 'bold'))
        self.delete_button.grid(row=0, column=4, padx=5, pady=5)

        self.output_text = tk.Text(self.frame, width=80, height=20, bg='yellow', fg='black', font=('Helvetica', 12))
        self.output_text.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        phone = simpledialog.askstring("Input", "Enter phone:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")

        if name and phone and email and address:
            result = self.book.add_contact(name, phone, email, address)
            messagebox.showinfo("Add Contact", result)
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def view_contacts(self):
        self.output_text.delete(1.0, tk.END)
        contacts = self.book.view_contacts()
        if contacts:
            for contact in contacts:
                self.output_text.insert(tk.END, f"Name: {contact['name']}\n")
                self.output_text.insert(tk.END, f"Phone: {contact['phone']}\n")
                self.output_text.insert(tk.END, f"Email: {contact['email']}\n")
                self.output_text.insert(tk.END, f"Address: {contact['address']}\n")
                self.output_text.insert(tk.END, "-"*40 + "\n")
        else:
            self.output_text.insert(tk.END, "No contacts found.\n")

    def search_contact(self):
        name = simpledialog.askstring("Input", "Enter name to search:")
        if name:
            self.output_text.delete(1.0, tk.END)
            found_contacts = self.book.search_contact(name)
            if found_contacts:
                for contact in found_contacts:
                    self.output_text.insert(tk.END, f"Name: {contact['name']}\n")
                    self.output_text.insert(tk.END, f"Phone: {contact['phone']}\n")
                    self.output_text.insert(tk.END, f"Email: {contact['email']}\n")
                    self.output_text.insert(tk.END, f"Address: {contact['address']}\n")
                    self.output_text.insert(tk.END, "-"*40 + "\n")
            else:
                self.output_text.insert(tk.END, "No contacts found with that name.\n")
        else:
            messagebox.showwarning("Input Error", "Name is required.")

    def update_contact(self):
        old_name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
        if old_name:
            new_name = simpledialog.askstring("Input", "Enter new name (leave blank to keep current):")
            new_phone = simpledialog.askstring("Input", "Enter new phone (leave blank to keep current):")
            new_email = simpledialog.askstring("Input", "Enter new email (leave blank to keep current):")
            new_address = simpledialog.askstring("Input", "Enter new address (leave blank to keep current):")

            for contact in self.book.contacts:
                if contact['name'].lower() == old_name.lower():
                    new_name = new_name or contact['name']
                    new_phone = new_phone or contact['phone']
                    new_email = new_email or contact['email']
                    new_address = new_address or contact['address']

                    result = self.book.update_contact(old_name, new_name, new_phone, new_email, new_address)
                    messagebox.showinfo("Update Contact", result)
                    return

            messagebox.showwarning("Update Error", f"No contact found with the name '{old_name}'.")
        else:
            messagebox.showwarning("Input Error", "Old name is required.")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        if name:
            result = self.book.delete_contact(name)
            messagebox.showinfo("Delete Contact", result)
        else:
            messagebox.showwarning("Input Error", "Name is required.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
