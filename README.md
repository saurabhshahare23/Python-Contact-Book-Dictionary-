📒 Contact Book (Python CLI App)
A simple command-line contact book written in Python using lists and dictionaries. This app allows users to add, view, search, and delete contacts by interacting through a terminal interface.

🔧 Features
✅ Add new contacts (Name, Phone, Email)

📋 Display all saved contacts

🔍 Search contacts by name

❌ Delete contacts by name

🚪 Exit the application

🖼️ Screenshots
Add Contact	Search Contact	Delete Contact	Display Contacts	Main Menu
				

(Replace yourusername, your-repo-name, and your-image-id after uploading to GitHub)

📝 How to Use
Clone the repository:

git clone https://github.com/yourusername/contact-book.git
cd contact-book
Run the program:
python contact_book_dict.py
Follow on-screen menu to interact with the contact book.

🧠 Code Overview
The program includes:

A contacts list storing contact dictionaries.

Functions for each action: add_contact(), display_contacts(), search_contact(), and delete_contact().

A main loop in main() providing a text-based UI.

⚠️ Known Issue
In both search_contact() and delete_contact(), the "Contact not found" message prints within the loop and may appear multiple times if not the first match. This can be fixed by moving the print statement outside the loop.

✅ Example Fix (Improved search_contact()):
def search_contact():
    name = input("Enter name to search:")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Name: {contact['name']},Phone: {contact['phone']},Email: {contact['email']}")
            return
    print("Contact not found.")

🛠 Requirements
Python 3.x
