'''
    @Author: Chakravarthy
    @Date: 2022-05-30 19:10:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-05-30 19:30:15
    @Title : Address Book System Testing
'''
import unittest
from create_contacts import *


class TestArithmeticOperation(unittest.TestCase):

    def test_create_contacts(self):
        """
        Description:
            This function is testing person_input method
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        obj = CreateContacts()
        # assert (obj.person_input(), (
        #     obj.first_name, obj.last_name, obj.address, obj.city, obj.state, obj.zip, obj.phone_number, obj.email))
        assert obj.person_input() == (
            obj.first_name, obj.last_name, obj.address, obj.city, obj.state, obj.zip, obj.phone_number, obj.email)


if __name__ == "__main__":
    unittest.main()
