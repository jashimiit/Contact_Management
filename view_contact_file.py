def view_all_contact(contact_book):
    for contact in contact_book:
        print(
            contact["name"],
            contact["email"],
            contact["phone"],
            contact["address"],
            sep='|'
        )