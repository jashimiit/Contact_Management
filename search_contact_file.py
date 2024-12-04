def search_contact_by_name(contact_book):
    search_term=input('Enter the name to search contact: ')
    search_result=[]

    for contact in contact_book:
        #if any(search_term.lower() in name.lower() for name in contact["name"]):
        if search_term.lower() in contact["name"].lower():
            search_result.append(contact)

    if search_result:
        for index, contact in enumerate(search_result):
            print(f'{index+1}. Name:{contact["name"]}, email:{contact["email"]}, Phone Number:{contact["phone"]}, Address:{contact["address"]}')
    else:
        print('Search text not matching with any contact name!')        