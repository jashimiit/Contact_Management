def back_up_contact(contact_book):
    with open('contacts.csv', 'w') as fp:
        for index, contact in enumerate(contact_book):
            line=f'{contact["name"]}, {contact["email"]}, {contact["phone"]},{contact["address"]}\n '
            fp.write(line)