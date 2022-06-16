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
        person = CreateContacts()  # Creating an object of CreateContacts Class
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

    def find_records(self, first_name):
        """
        Description:
            This function is finding address book records based on first name
        Parameter:
            It takes self and first name as argument
        Return:
            returns True or False
        """
        for record in self.addressbook:
            if record.first_name == first_name:
                return True
        return False

    def update_records(self, old_first_name, new_first_name, last_name, address, city, state, zip, phone_number, email):
        """
        Description:
            This function is updating address book records
        Parameter:
            It takes self and first name as argument
        Return:
            returns list of records
        """
        for record in self.addressbook:
            if record.first_name == old_first_name:
                record.first_name = new_first_name
                record.last_name = last_name
                record.address = address
                record.city = city
                record.state = state
                record.zip = zip
                record.phone_number = phone_number
                record.email = email
                print("\nRecord Updated Successfully !!")
        return self.addressbook

    def delete_record(self, first_name):
        """
        Description:
            This function is deleting address book record by first name
        Parameter:
            It takes self first name as argument
        Return:
            returns none
        """
        for record in self.addressbook:
            if record.first_name == first_name:  # Checking that first name provided by user is matching with
                # Existing Record or not
                self.addressbook.remove(record)  # Deleting all the details of one user in Address Book
                print("\nRecord Deleted Successfully")
            else:
                print("record not found")
        return self.addressbook
