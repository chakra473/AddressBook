"""
    @Author: Chakravarthy
    @Date: 2022-05-30 19:10:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-05-30 19:30:15
    @Title : Address Book System Testing
"""

import unittest
from create_contacts import *
from address_book import *


class TestArithmeticOperation(unittest.TestCase):
    person = Addressbook()

    # def test_create_addressbook(self):
    #     """
    #     Description:
    #         This function is testing create address book method
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     ab_name, dict_ele = self.person.create_addressbook("MyBook")
    #     self.assertEqual(ab_name[0], 'MyBook')
    #     self.assertEqual(len(dict_ele), 1)

    # def test_add_records(self):
    #     """
    #     Description:
    #         This function is testing add records method of Addressbook Class
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook', 'abc', 'xyz', 'pqr', 'kmn', 'tamilnadu', '123', '1234567890',
    #                                       'mk@gmail.com')
    #     self.assertEqual(len(ab_dict['MyBook']), 1)

    # def test_find_records(self):
    #     """
    #     Description:
    #         This function is testing find records method of Addressbook Class
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook', 'abc', 'xyz', 'pqr', 'kmn', 'tamilnadu', '123', '1234567890',
    #                                       'mk@gmail.com')
    #     ab_dict = self.person.add_records('MyBook', 'chakra', 'xyz', 'pqr', 'kmn', 'tamilnadu', '123', '1234567890',
    #                                       'mk@gmail.com')
    #     self.assertTrue(self.person.find_records('MyBook', 'abc'))
    #
    # def test_update_records(self):
    #     """
    #     Description:
    #         This function is testing update records method of Addressbook Class
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     ab_dict = self.person.update_records('MyBook', 'abc', 'abc', 'murali', 'pqr', 'kmn', 'tamilnadu', '123',
    #                                          '1234567890', 'mk@gmail.com')
    #     self.assertEqual(ab_dict['MyBook'][0].first_name, 'abc')
    #     self.assertEqual(len(ab_dict['MyBook']), 2)
    #
    # def test_delete_records(self):
    #     """
    #     Description:
    #         This function is testing delete records method of Addressbook Class
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     ab_dict = self.person.delete_record('MyBook', 'abc')
    #     self.assertEqual(len(ab_dict), 0)

    # def test_display_persons_by_state(self):
    #     """
    #     Description:
    #         This function is testing count the records display by state
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook', 'chakra', 'm', 'pqr', 'chennai', 'tamilnadu', '123', '1234567890',
    #                                       'mc@gmail.com')
    #     ab_dict = self.person.add_records('MyBook', 'jay', 'm', 'pqr', 'trichy', 'tamilnadu', '123', '8451238945',
    #                                       'mc@gmail.com')
    #     result = self.person.display_persons_by_state('tamilnadu')
    #     self.assertEqual(result, 2)
    #
    # def test_add_persons_in_dictionary_by_city_name(self):
    #     """
    #     Description:
    #         This function is testing add_persons_in_dictionary_by_city_name method
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook', 'jay', 'm', 'pqr', 'chennai', 'tamilnadu', '123', '1234567890',
    #                                       'mk@gmail.com')
    #     ab_dict = self.person.add_records('MyBook', 'chakra', 'm', 'pqr', 'kovai', 'tamilnadu', '123', '8451238945',
    #                                       'mk@gmail.com')
    #     city_dict = self.person.add_persons_in_dictionary_by_city_name()
    #     self.assertEqual(len(city_dict), 2)
    #
    # def test_add_persons_in_dictionary_by_state_name(self):
    #     """
    #     Description:
    #         This function is testing add_persons_in_dictionary_by_state_name method
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook', 'jay', 'm', 'pqr', 'selam', 'tamilnadu', '123', '1234567890',
    #                                       'mk@gmail.com')
    #     ab_dict = self.person.add_records('MyBook', 'chakra', 'm', 'pqr', 'trichi', 'mno', '123', '8451238945',
    #                                       'mk@gmail.com')
    #     state_dict = self.person.add_persons_in_dictionary_by_state_name()
    #     self.assertEqual(len(state_dict), 2)

    # def test_sort_by_person_name(self):
    #     """
    #     Description:
    #         This function is testing sort_by_person_name method
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook', 'zab', 'm', 'pqr', 'kmn', 'uvw', '123', '1234567890',
    #                                       'i@gmail.com')
    #     ab_dict = self.person.add_records('MyBook', 'abc', 'm', 'pqr', 'abc', 'mno', '123', '8451238945',
    #                                       't@gmail.com')
    #     ab_dict = self.person.add_records('MyBook', 'moses', 'm', 'pqr', 'abc', 'mno', '123', '8451238945',
    #                                       'mc@gmail.com')
    #     ab_dict = self.person.sort_by_person_name()
    #     self.assertEqual(ab_dict['MyBook'][1].first_name, 'moses')
    #     self.assertEqual(ab_dict['MyBook'][0].first_name, 'abc')
    #     self.assertEqual(ab_dict['MyBook'][-1].first_name, 'zab')

    def test_sort_method(self):
        """
        Description:
            This function is testing all sort  method
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        self.person.create_addressbook("MyBook")
        ab_dict = self.person.add_records('MyBook', 'z', 'britto', 'pqr', 'banglore', 'karnataka', 501234, 12345678,
                                          'mk@gmail.com')
        ab_dict = self.person.add_records('MyBook', 'a', 'm', 'pqr', 'ahmedabad', 'gujarat', 331203, 845123895,
                                          'mk@gmail.com')
        ab_dict = self.person.add_records('MyBook', 'b', 'm', 'pqr', 'chennai', 'tamilnadu', 131203, 845123895,
                                          'mk@gmail.com')
        ab_dict_by_city = self.person.sort_by_city()
        self.assertEqual(ab_dict_by_city['MyBook'][0].city, 'ahmedabad')
        ab_dict_by_state = self.person.sort_by_state()
        self.assertEqual(ab_dict_by_state['MyBook'][0].state, 'gujarat')
        ab_dict_by_zip = self.person.sort_by_zip()
        self.assertEqual(ab_dict_by_zip['MyBook'][0].zip, 131203)

    def test_txt_file_write(self):
        """
        Description:
            This function is testing that text file write operation is working properly or not
        Parameter:
            It takes one self as argument
        Return:
            returns Nothing
        """
        self.person.create_addressbook("MyBook")
        ab_dict = self.person.add_records('MyBook', 'chakra', 'm', 'pqr', 'kmn', 'uvw', 321, 12345678,
                                          'mchakra@gmail.com')
        self.person.txt_file_write()
        with open("txt_test_file.txt") as myfile:
            line = myfile.readlines()[5]
        self.assertEqual(line, 'First Name : chakra\n')


if __name__ == "__main__":
    unittest.main()
