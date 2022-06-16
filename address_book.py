'''
    @Author: Chakravarthy
    @Date: 2022-06-16 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-05-30 14:13:15
    @Title : Python Code for Address Book System
'''

from create_contacts import CreateContacts


class Addressbook:
    addressbook = []  # Creating List having CreateContacts Class Object Datatype

    def add_records(self, first_name, last_name, address, city, state, zip, phone_number, email):
        """
        Description:
            This function is getting user input and store it in list
        Parameter:
            It takes self and all the details as argument
        Return:
            returns list of address book
        """
        person = CreateContacts()  # Creating a object of CreateContacts Class
        person.first_name = first_name
        person.last_name = last_name
        person.address = address
        person.city = city
        person.state = state
        person.zip = zip
        person.phone_number = phone_number
        person.email = email
        self.addressbook.append(person)
        return self.addressbook

    def print_records(self):
        """
        Description:
            This function is printing address book records
        Parameter:
            It takes self argument
        Return:
            returns none
        """
        i = 1
        print("Records Present in Address Book : ")
        for record in self.addressbook:  # Accessing all the records of list one by one using foreach loop
            print(f"\n\nRecord - {i}")
            print(f"First Name : {record.first_name}")
            print(f"Last Name : {record.last_name}")
            print(f"Address : {record.address}")
            print(f"City : {record.city}")
            print(f"State : {record.state}")
            print(f"Email : {record.email}")
            print(f"Zip code : {record.zip}")
            print(f"Phone Number : {record.phone_number}")
            i += 1
