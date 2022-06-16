'''
    @Author: Chakravarthy
    @Date: 2022-06-16 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-05-30 14:13:15
    @Title : Python Code for Address Book System
'''
# Import
from create_contacts import *

print("Welcome to Address Book System")

p1 = CreateContacts()  # Creating object of CreateContacts Class
p1.person_input()  # Calling Method of class
print(p1.first_name)
print(p1)
