import json

#File to store contacts 
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts form the JSON file."""
    try:
        with open(CONTACTS_FILE,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE,'w') as file:
        json.dump(contacts,file,indent=4)

def add_contacts(contacts):
    """Add a new cotact to the list.""" 
    name = input("Enter the contacts name :").strip() 
    phone = input("Enter the contacts phone number:").strip()       
    email = input("Enter the contacts email :").strip()       
    address = input("Enter the contacts address :").strip() 

    contacts[name]={
        'phone':phone,
        'email':email,
        'address':address
    }      
    print(f"Contact '{name}'added successfully!!")

def view_contacts(contacts):
    """Display all saved contacts."""
    if not contacts :
        print("No contacts found .")
        return
    print("\ncontact List:")
    for name,details in contacts.items():
        print(f"Name :{name}")
        print(f"Phone :{details['phone']}")
        print(f"Email :{details['email']}")
        print(f"Address :{details['address']}\n")
        found=True

    if not found:
        print("NO contact found with that name or phone number .")
def update_conatact(contacts):
    """Update contact details."""
    name=input("Enter the name of the conatct to upadate :").strip()

    if name in contacts :
        print(f"Current details for '{name}':")
        print(f"Phone :{contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address :{contacts[name]['address']}\n")

        phone = input("Enter the new phone number(leave blank to keep current):").strip()
        email= input("Enter the new email (leave blank to keep currrent):").strip()
        address= input("Enter the new address(leave blank to keep current):").strip()

        if phone :
            contacts[name]['phone']=phone
        if email:
            contacts[name]['email']=email   
        if address :
            contacts[name]['address']= address
            print(f"Contact'{name}'updated successfully!")
        else:
            print(f"No contact found with the name '{name}'.") 

def delete_contact(contacts):
    """Delete a contact from the list."""
    name = input("Enter the name of the contact to delete :").strip()

    if name in contacts:
        del contacts[name]
        print(f"Contact  '{name}'deleted successfully!")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    """Main function to run the contact management system.""" 
    contacts= load_contacts()

    while True:
        print("\nContact Management System") 
        print("1.Add contact")       
        print("2.View contacts")       
        print("3.Search contact")       
        print("4.Update contact")       
        print("5.Delete contact")       
        print("6.Exit")       

        choice=input("Enter your choice(1-6):").strip()

        if choice =='1':
            add_contacts(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_conatact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Exiting..!!")
            break
        else :
            print("Invalid choice.PLease enter a number 1 and 6.")
if __name__ == "__main__":
    main()

      




