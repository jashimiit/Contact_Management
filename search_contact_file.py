def search_contact_by_name(contact_book):
    search_term=input('Enter the name to search contact: ')
    search_result=[]

    for contact in contact_book:
        if any(search_term.lower() in name.lower() for name in contact["name"]):
            search_result.append(contact)

    if search_result:
        for contact in search_result:
            print(f'Name:{contact["name"]}, email:{contact["email"]}, Phone Number:{contact["phone"]}, Address:{contact["address"]}')
    else:
        print('Search text not matching with any contact name!')        