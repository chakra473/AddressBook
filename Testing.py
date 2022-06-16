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
    person = Addressbook()
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

    # def test_add_records(self):
    #     # per = CreateContacts('abc','xyz','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
    #     ab = self.person.add_records('abc', 'xyz', 'pqr', 'kmn', 'uvw', '123', '1234567890', 'chakra@gmail.com')
    #     self.assertEqual(ab[0].first_name, 'abc')
    #     self.assertEqual(ab[0].last_name, 'xyz')
    #     self.assertEqual(ab[0].address, 'pqr')
    #     self.assertEqual(ab[0].city, 'kmn')
    #     self.assertEqual(ab[0].state, 'uvw')
    #     self.assertEqual(ab[0].zip, '123')
    #     self.assertEqual(ab[0].phone_number, '1234567890')
    #     self.assertEqual(ab[0].email, 'chakra@gmail.com')
    #     # self.assertListEqual(list(ab[0]),per)

    def test_find_records(self):
        """
        Description:
            This function is testing find records method of Addressbook Class
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        ab = self.person.add_records('abc', 'xyz', 'pqr', 'kmn', 'uvw', '123', '1234567890', 'chakra@gmail.com')
        self.assertFalse(self.person.find_records('def'))

    def test_update_records(self):
        """
        Description:
            This function is testing update records method of Addressbook Class
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        #a = self.person.add_records('abc', 'xyz', 'pqr', 'kmn', 'uvw', '123', '1234567890', 'chakra@gmail.com')
        ab = self.person.update_records('abc', 'chakra', 'murali', 'pqr', 'kmn', 'uvw', '123', '1234567890',
                                        'chakra@gmail.com')
        self.assertEqual(ab[0].first_name, 'chakra')
        self.assertEqual(ab[0].last_name, 'murali')
        self.assertEqual(ab[0].address, 'pqr')
        self.assertEqual(ab[0].city, 'kmn')
        self.assertEqual(ab[0].state, 'uvw')
        self.assertEqual(ab[0].zip, '123')
        self.assertEqual(ab[0].phone_number, '1234567890')
        self.assertNotEqual(ab[0].email, 'm.chakra473@gmail.com')


if __name__ == "__main__":
    unittest.main()
