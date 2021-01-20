import ast
import os
import time


def convert_list_2_bin(contact_list):
    file = open('data.bin', 'wb')
    file.write(str(contact_list).encode('ascii'))
    file.close()


def convert_bin_2_list():
    file = open('data.bin', 'rb')
    line = file.read()
    if line:
        return ast.literal_eval(line.decode('ascii'))
    else:
        return []


def len_fit(text, length, char=' '):
    return str(text + char * (length - len(text)))


def header(title):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\n\n\n')
    print('             ╔══════════════════════════════════════════════════╗')
    print('             ║    {}║'.format(len_fit(title, 46)))
    print('             ╠══════════════════════════════════════════════════╣')


def menu_generator(message_text=None):
    header('Contact Book')
    print('             ║ 1. Add                                           ║')
    print('             ║ 2. List                                          ║')
    print('             ║ 3. Search                                        ║')
    print('             ║ 4. Sort                                          ║')
    print('             ║ 5. Delete                                        ║')
    print('             ║ 6. Exit                                          ║')
    print('             ╚══════════════════════════════════════════════════╝')
    if message_text:
        print('                  {}'.format(message_text))
        print()
    input_choice = input('                  Please enter your choice: ')
    return input_choice


def vcard(title, contact_info):
    first_name = contact_info['first_name']
    last_name = contact_info['last_name']
    phone = contact_info['phone']
    address = contact_info['address']
    postal_code = contact_info['postal_code']
    header(title)
    print('             ║ First name: {}║'.format(len_fit(first_name, 37)))
    print('             ║ Last name: {}║'.format(len_fit(last_name, 38)))
    print('             ║ Phone number: {}║'.format(len_fit(phone, 35)))
    print('             ║ Address: {}║'.format(len_fit(address, 40)))
    print('             ║ Postal code: {}║'.format(len_fit(postal_code, 36)))
    print('             ╚══════════════════════════════════════════════════╝')


def add():
    contact = {
        'first_name': '',
        'last_name': '',
        'phone': '',
        'address': '',
        'postal_code': '',
    }
    vcard('Add Contact', contact)
    contact['first_name'] = input('                  Please enter First name: ')
    vcard('Add Contact', contact)
    contact['last_name'] = input('                  Please enter Last name: ')
    vcard('Add Contact', contact)
    contact['phone'] = input('                  Please enter Phone number: ')
    vcard('Add Contact', contact)
    contact['address'] = input('                  Please enter Address: ')
    vcard('Add Contact', contact)
    contact['postal_code'] = input('                  Please enter Postal code: ')
    vcard('Add Contact', contact)
    confirmation = input('                  Do you confirm the information [Y/n]: ')
    if confirmation == '' or confirmation == 'Y' or confirmation == 'y':
        list_contact = convert_bin_2_list()
        list_contact.append(contact)
        convert_list_2_bin(list_contact)


def vcard_list(contact_list):
    for count, contact in enumerate(contact_list):
        first_name = contact['first_name']
        last_name = contact['last_name']
        phone = contact['phone']
        address = contact['address']
        postal_code = contact['postal_code']
        print('             ║ First name: {}║'.format(len_fit(first_name, 37)))
        print('             ║ Last name: {}║'.format(len_fit(last_name, 38)))
        print('             ║ Phone number: {}║'.format(len_fit(phone, 35)))
        print('             ║ Address: {}║'.format(len_fit(address, 40)))
        print('             ║ Postal code: {}║'.format(len_fit(postal_code, 36)))
        if count + 1 == len(contact_list):
            print('             ╚══════════════════════════════════════════════════╝')
        else:
            print('             ╠══════════════════════════════════════════════════╣')


def list_of_contact():
    list_contact = convert_bin_2_list()
    header('List of Contacts')
    vcard_list(list_contact)
    input('               Press Enter to return ')


def search():
    list_contact = convert_bin_2_list()
    len_list_contact = str(len(list_contact))
    header('Search in Contacts')
    print('             ║ Number of contacts: {}║'.format(len_fit(len_list_contact, 29)))
    print('             ║ Search based on First name                       ║')
    print('             ╚══════════════════════════════════════════════════╝')
    query = input('               Enter Fist name: ')
    try:
        result = next(item for item in list_contact if item["first_name"] == query)
        vcard('Contact Information', result)
        input('               Press Enter to return ')
    except:
        print('               Contact not found!')
        input('               Press Enter to return ')


def sort():
    list_contact = convert_bin_2_list()
    newlist = sorted(list_contact, key=lambda k: k['first_name'])
    header('Search in Contacts')
    vcard_list(newlist)
    input('               Press Enter to return ')


def delete():
    list_contact = convert_bin_2_list()
    len_list_contact = str(len(list_contact))
    header('Search in Contacts')
    print('             ║ Number of contacts: {}║'.format(len_fit(len_list_contact, 29)))
    print('             ║ Search based on First name                       ║')
    print('             ╚══════════════════════════════════════════════════╝')
    query = input('               Enter Fist name: ')
    try:
        result = next(item for item in list_contact if item["first_name"] == query)
        vcard('Delete Contact', result)
        confirmation = input('               Are you sure to delete this contact? [y/N] ')
        if confirmation == 'Y' or confirmation == 'y':
            for count, contact in enumerate(list_contact):
                if result['first_name'] == contact['first_name']:
                    list_contact.pop(count)
                    convert_list_2_bin(list_contact)

    except:
        print('               Contact not found!')
        input('               Press Enter to return ')


def about():
    header('Contact Book')
    print('             ║ Lesson: Save and recover data                    ║')
    print('             ║ Home work: HW1                                   ║')
    print('             ║ Teacher: Pr. Rasekh                              ║')
    print('             ║ Student: Amin Hemmati                            ║')
    print('             ║ Student number: 9672193                          ║')
    print('             ╚══════════════════════════════════════════════════╝')
    time.sleep(5)


def menu():
    should = True
    message = None
    while should:
        choice = menu_generator(message)
        message = None
        if choice == '1':
            add()
        elif choice == '2':
            list_of_contact()
        elif choice == '3':
            search()
        elif choice == '4':
            sort()
        elif choice == '5':
            delete()
        elif choice == '6':
            should = False
        else:
            message = 'You enter a wrong character!'


about()
menu()
os.system('cls' if os.name == 'nt' else 'clear')
print('\n\n\n\n\n                  github: https://github.com/AminHCE/Contact-Book')
input('                  Press Enter to Exit ')
os.system('cls' if os.name == 'nt' else 'clear')
