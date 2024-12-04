import add_contact_file
import view_contact_file
import search_contact_file


contact_book=[]

print('Welcome to the contact management system')

menu_text='''
1.Add Contact
2.View all Contact
3.Remove Contact
4.Search Contact
0.Exit
'''

while True:
    print(menu_text)
    choice=int(input('Enter your choice: '))

    if choice==1:
        contact_book=add_contact_file.add_contact(contact_book)
    elif choice==2:
        view_contact_file.view_all_contact(contact_book)
    elif choice==3:
        print('You want to remove contact')
    elif choice==4:
        search_result=search_contact_file.search_contact_by_name(contact_book)
    elif choice==0:
        print('Thank You for Using Contact Management System!')
        break
    else:
        print('You entered invalid input, Please enter correct input')
