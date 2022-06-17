'''
    @Author: Chakravarthy
    @Date: 2022-06-16 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-05-30 14:13:15
    @Title : Python Code for Address Book System
'''


class CreateContacts:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.address = None
        self.city = None
        self.state = None
        self.zip = None
        self.phone_number = None
        self.email = None

    def person_input(self):  # Creating class method
        """
        Description:
            This function is getting details from user and store it in variables
        Parameter:
            It takes one self argument
        Return:
            returns tuple of all details
        """
        self.first_name = input("Enter your First Name : ")
        self.last_name = input("Enter your Last Name : ")
        self.address = input("Enter your Address : ")
        self.city = input("Enter your City Name : ")
        self.state = input("Enter your State Name : ")
        self.zip = int(input("Enter your Zip Code : "))
        self.phone_number = int(input("Enter your Phone Number : "))
        self.email = input("Enter your Email Address: ")
        return self.first_name, self.last_name, self.address, self.city, self.state, self.zip, self.phone_number, self.email
