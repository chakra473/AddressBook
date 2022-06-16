'''
    @Author: Chakravarthy
    @Date: 2022-06-16 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-05-30 14:13:15
    @Title : Python Code for Address Book System
'''
# Import
from address_book import *

print("\nWelcome to Address Book System")

records = Addressbook()
while True:
    print("\n1.Add a new Record\n2.Update Records\n3.Delete a Record\n4.Close the program")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        first_name = input("\nEnter your First Name : ")
        last_name = input("Enter your Last Name : ")
        address = input("Enter your Address : ")
        city = input("Enter your City Name : ")
        state = input("Enter your State Name : ")
        zip = input("Enter your Zip Code : ")
        phone_number = input("Enter your Phone Number : ")
        email = input("Enter your Email : ")
        records.add_records(first_name, last_name, address, city, state, zip, phone_number,
                            email)  # Calling a method of AddressBook class to add record in address book
        records.print_records()  # Calling a method of AddressBook class to display records of address book
    elif ch == 2:
        old_first_name = input("\nEnter your First Name : ")
        check = records.find_records(old_first_name)
        if check:
            new_first_name = input("\nEnter your new First Name : ")
            last_name = input("Enter your new Last Name : ")
            address = input("Enter your new Address : ")
            city = input("Enter your new City Name : ")
            state = input("Enter your new State Name : ")
            zip = input("Enter your new Zip Code : ")
            phone_number = input("Enter your new Phone Number : ")
            email = input("Enter your new Email : ")
            records.update_records(old_first_name, new_first_name, last_name, address, city, state, zip, phone_number, email)
        else:
            print("Record Not Found!!")
    elif ch == 3:
        f_name = input("Enter your First Name : ")
        records.delete_record(f_name)
        records.print_records()
    elif ch == 4:
        break
    else:
        print("Choice is invalid")
