def load_contact(contact_book):
    contact_book.clear()

    try:
        with open("contacts.csv", "r") as fp:
            for line in fp:
                if not line.strip():
                    continue
                line_split=line.strip().split(",")
                contact={
                    "name": line_split[0],
                    "email": line_split[1],
                    "phone": line_split[2],
                    "address": line_split[3]
                }
                contact_book.append(contact)
            print('Contact loaded Successfully')
        return contact_book
    
    except FileNotFoundError:
        print("No saved contacts found. Starting with an empty contact book.")
    except Exception as e:
        print(f"An error occurred while loading contacts: {e}")