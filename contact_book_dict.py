#Contact book using lists and dictionaries
contacts=[]

#Add contact
def add_contact():
    name = input("Enter name:")
    phone = input("Enter phone number:")
    email =input("Enter email:")
    contacts.append({"name":name,"phone":phone,"email":email})
    print("Contact added succesfully!")
    
#Display all contacts
def display_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"Name: {contact['name']},Phone: {contact['phone']},Email: {contact['email']}")
        
#Search contact
def search_contact():
    name=input("Enter name to search:")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            print(f"Name: {contact['name']},Phone: {contact['phone']},Email: {contact['email']}")
            return
        print("Contact not found.")
        
#Delete contact
def delete_contact():
    name=input("Enter name to delete:")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
        print("Contact not found.")
        
#Main menu
def main():
    while True:
        print("\n1.Add Contact\n2.Display Contacts\n3.Search Contact\n4.Delete Contact\n5.Exit")
        choice=input("Enter choice:")
        if choice == '1':
            add_contact()
        elif choice == '2':
            display_contacts()
        elif choice =='3':
            search_contact()
        elif choice =='4':
            delete_contact()
        elif choice=='5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
            
main()