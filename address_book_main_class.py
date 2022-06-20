"""
    @Author: Chakravarthy
    @Date: 2022-06-16 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-05-30 14:13:15
    @Title : Python Code for Address Book System
"""
# Import
from address_book import *

print("\nWelcome to Address Book System")

records = Addressbook()
while True:
    print("\n1.Add a new Record\n2.Update Records\n3.Delete Records\n4.Display By City\n5.Display By State\n6.Exit")
    ch = int(input("\nEnter your choice : "))
    if ch == 1:
        ans = input("\nDo you want to add records in new Address Book ? If yes then press 1 : ")
        if ans == "1":
            name_of_ab = input("\nEnter name of address book which you want to create : ")
            records.create_addressbook(name_of_ab)  # Calling a method to Create a new Address Book
            num = int(input("\nHow many contacts you want to add in address book : "))
            for i in range(num):
                print(f"\nEnter details for contact {i + 1} : \n")
                first_name = input("\nEnter your First Name : ")
                last_name = input("Enter your Last Name : ")
                address = input("Enter your Address : ")
                city = input("Enter your City Name : ")
                state = input("Enter your State Name : ")
                zip = input("Enter your Zip Code : ")
                phone_number = input("Enter your Phone Number : ")
                email = input("Enter your Email : ")
                records.add_records(name_of_ab, first_name, last_name, address, city, state, zip, phone_number, email)
            records.print_records()
        else:
            records.display_list_of_addressBook()  # Displaying existing address book name
            if records.temp == 1:  # Checking that address book is empty or not
                print("\nPlease Add Address Book First by entering choice 1")
            else:
                name_of_ab = input("\nSelect any one address book from above list : ")
                num = int(input("\nHow many contacts you want to add in address book : "))
                for i in range(num):
                    print(f"\nEnter details for contact {i + 1} : \n")
                    first_name = input("\nEnter your First Name : ")
                    last_name = input("Enter your Last Name : ")
                    address = input("Enter your Address : ")
                    city = input("Enter your City Name : ")
                    state = input("Enter your State Name : ")
                    zip = input("Enter your Zip Code : ")
                    phone_number = input("Enter your Phone Number : ")
                    email = input("Enter your Email : ")
                    records.add_records(name_of_ab, first_name, last_name, address, city, state, zip, phone_number,
                                        email)
            records.print_records()
    elif ch == 2:
        records.display_list_of_addressBook()  # Displaying existing address book name
        if records.temp == 1:  # Checking that address book is empty or not
            print("\nPlease Add Address Book First by entering choice 1")
        else:
            name_of_ab = input("\nSelect any one address book from above list : ")
            old_first_name = input("\nEnter your First Name : ")
            check = records.find_records(name_of_ab, old_first_name)
            if check:
                new_first_name = input("\nEnter your new First Name : ")
                last_name = input("Enter your new Last Name : ")
                address = input("Enter your new Address : ")
                city = input("Enter your new City Name : ")
                state = input("Enter your new State Name : ")
                zip = input("Enter your new Zip Code : ")
                phone_number = input("Enter your new Phone Number : ")
                email = input("Enter your new Email : ")
                records.update_records(name_of_ab, old_first_name, new_first_name, last_name, address, city, state, zip,
                                       phone_number, email)
        records.print_records()
    elif ch == 3:
        records.display_list_of_addressBook()  # Displaying existing address book name
        if records.temp == 1:  # Checking that address book is empty or not
            print("\nPlease Add Address Book First by entering choice 1")
        else:
            name_of_ab = input("\nSelect any one address book from above list : ")
            first_name = input("\nEnter your First Name : ")
            check = records.find_records(name_of_ab, first_name)
            if check:
                records.delete_record(first_name)
        records.print_records()
    elif ch == 4:
        city_name = input("\nEnter city name : ")
        total_records = records.display_persons_by_city(city_name)
        print(f"\nTotal records present where city is {city_name}  : {total_records}")
    elif ch == 5:
        state_name = input("\nEnter state name : ")
        total_records = records.display_persons_by_state(state_name)
        print(f"\nTotal records present where state is {state_name} : {total_records}")
    elif ch == 6:
        break
    else:
        print("Choice is invalid")
