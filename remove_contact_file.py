def remove_contact(contact_book):
    search_term=input('Enter the contact name to remove: ')
    search_result=[]

    for contact in contact_book:
        #if any(search_term.lower() in name.lower() for name in contact["name"]):
        if search_term.lower() in contact["name"].lower():
            search_result.append(contact)

    if search_result:
        for index, contact in enumerate(search_result):
            print(f'{index+1}. Name:{contact["name"]}, email:{contact["email"]}, Phone Number:{contact["phone"]}, Address:{contact["address"]}')
    if not search_result:
        print('This contact name is not available to remove!')
        return contact_book

    while True:
        try:
            select_index=int(input('Enter the contact index number to remove: '))
            if select_index<1 or select_index>len(search_result):
                print(f'{select_index} is invalid input, please enter value within 1 to {len(search_result)}')
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid index number.")

    contact_book.pop(select_index-1)
    print('Contact is removed successfully')
    return contact_book
