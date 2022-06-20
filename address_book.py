"""
    @Author: Chakravarthy
    @Date: 2022-06-16 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-05-30 14:13:15
    @Title : Python Code for Address Book System
"""

from create_contacts import CreateContacts


class Addressbook:
    addressbook_name = []  # Creating List having CreateContacts Class Object Datatype

    addressbook_dict = {}

    def create_addressbook(self, name):
        self.addressbook_name.append(name)  # Add address book name which is provided by user  in address book list
        if len(self.addressbook_dict) == 0:  # Checking that dictionary is empty or not
            self.addressbook_dict[
                name] = []  # creating key value pair where address book name is key and all the record of address
            # book as value
        else:
            if name in self.addressbook_dict.keys():  # Checking that address book given by user is already present
                # in dictionary or not
                print("This AddressBook is also present")
            else:
                self.addressbook_dict[
                    name] = []  # creating key value pair where address book name is key and all the record of
                # address book as value
        return self.addressbook_name, self.addressbook_dict

    temp = 0

    def display_list_of_addressBook(self):
        """
        Description:
            This function is displaying only list of address book available
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        if len(self.addressbook_name) == 0:  # Checking that address book list is empty or not
            print("\nThere is no address book available")
            self.temp = 1
        else:
            print("\n\nList of existing Address Book Are : ")
            for name in self.addressbook_name:  # Accessing all the names in address book
                print(name)

    def add_records(self, ab_name, first_name, last_name, address, city, state, zip, phone_number, email):
        """
        Description:
            This function is getting user input and store it in list
        Parameter:
            It takes self and all the details with book name as argument
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
        for content in self.addressbook_dict.keys():  # Accessing all the address book name of dictionary
            if content == ab_name:  # Checking that address book name provided by user is matching with
                # dictionary address book or not
                self.addressbook_dict[ab_name].append(person)
            else:
                print(f"\n{content} Address Book not found")
        return self.addressbook_dict

    def print_records(self):
        """
        Description:
            This function is printing address book records
        Parameter:
            It takes self argument
        Return:
            returns none
        """
        print("\n\nRecords Present in Multiple Address Book : ")

        for ab_name in self.addressbook_dict.keys():  # Accessing all the address book name of dictionary
            print(f"\n\nAddress Book : " + ab_name)
            i = 1
            for record in self.addressbook_dict[ab_name]:  # Accessing all the records of list one by one using
                # foreach loop
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

    def find_records(self, ab_name, first_name):
        """
        Description:
            This function is finding address book records based on first name
        Parameter:
            It takes self and first name as argument
        Return:
            returns True or False
        """
        for content in self.addressbook_dict.keys():
            if content == ab_name:
                for record in self.addressbook_dict[ab_name]:
                    if record.first_name == first_name:
                        return True
                    else:
                        print("\nRecord Not Found")
            else:
                print("Address book not found")
        return False

    def update_records(self, ab_name, old_first_name, new_first_name, last_name, address, city, state, zip,
                       phone_number,
                       email):
        """
        Description:
            This function is updating address book records
        Parameter:
            It takes self and first name as argument
        Return:
            returns list of records
        """
        for content in self.addressbook_dict.keys():  # Accessing all the address book name of dictionary
            if content == ab_name:  # Checking that address book name provided by user is matching with
                # dictionary address book or not
                for record in self.addressbook_dict[ab_name]:
                    if record.first_name == old_first_name:  # Checking that first name provided by user is
                        # matching with Existing Record or not
                        record.first_name = new_first_name
                        record.last_name = last_name
                        record.address = address
                        record.city = city
                        record.state = state
                        record.zip = zip
                        record.phone_number = phone_number
                        record.email = email
                        print("\nRecord Updated Successfully !!")

        return self.addressbook_dict

    def delete_record(self, ab_name, first_name):
        """
        Description:
            This function is deleting address book record by first name
        Parameter:
            It takes self first name as argument
        Return:
            returns none
        """
        for content in self.addressbook_dict.keys():
            if content == ab_name:
                for record in self.addressbook_dict[ab_name]:
                    if record.first_name == first_name:
                        self.addressbook_dict[ab_name].remove(
                            record)  # Deleting all the details of one user in Address Book
                        print("\nRecord Deleted Successfully")
        return self.addressbook_dict

    def remove_duplicate(self, ab_name):
        for content in self.addressbook_dict.keys():
            if content == ab_name:
                for record in self.addressbook_dict[ab_name]:
                    for i in range(len(self.addressbook_dict)):
                        if record.first_name[i] == record.first_name[i + 1]:
                            self.addressbook_dict[ab_name].remove(
                                record)  # Deleting all the details of one user in Address Book
                            print("\nDuplicate Record Deleted Successfully")
