from back_up_contact_file import back_up_contact

def add_contact(contact_book):
    name=input('Enter your name: ')
    email=input('Enter your email id: ')
    phone=input('Enter your phone number: ')
    for contact in contact_book:
        if contact["phone"] == phone:
            print("Error: A contact with this phone number already exists.")
            return contact_book
    address=input('Enter your address: ')

    contact={
        "name":name,
        "email": email,
        "phone": phone,
        "address": address
    }
    contact_book.append(contact)
    from back_up_contact_file import back_up_contact
    back_up_contact(contact_book)
    
    print('Contact added successfully')
    return contact_book