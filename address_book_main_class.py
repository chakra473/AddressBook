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
print("\n1. Add a new Record\n")
ch = int(input("\nEnter your choice : "))
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
else:
    print("Choice is invalid")
