'''
    @Author: Chakravarthy
    @Date: 2022-05-30 19:10:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-05-30 19:30:15
    @Title : Address Book System Testing
'''

import unittest
from create_contacts import *
from address_book import *


class TestArithmeticOperation(unittest.TestCase):

    # def test_create_contacts(self):
    #     """
    #     Description:
    #         This function is testing person_input method
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     obj = CreateContacts()
    #     self.assertEquals(obj.person_input() ,(obj.first_name,obj.last_name,obj.address,obj.city,obj.state,obj.zip,obj.phone_number,obj.email ))

    def test_add_records(self):
        person = Addressbook()
        # per = CreateContacts('abc','xyz','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
        ab = person.add_records('abc', 'xyz', 'pqr', 'kmn', 'uvw', '123', '1234567890', 'mk@gmail.com')
        self.assertEqual(ab[0].first_name, 'abc')
        self.assertEqual(ab[0].last_name, 'xyz')
        self.assertEqual(ab[0].address, 'pqr')
        self.assertEqual(ab[0].city, 'kmn')
        self.assertEqual(ab[0].state, 'uvw')
        self.assertEqual(ab[0].zip, '123')
        self.assertEqual(ab[0].phone_number, '1234567890')
        self.assertEqual(ab[0].email, 'mk@gmail.com')
        # self.assertListEqual(list(ab[0]),per)


if __name__ == "__main__":
    unittest.main()