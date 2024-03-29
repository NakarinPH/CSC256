# Nakarin Philangam
# CSC256.0001

import datetime
import unittest

import datetemp
from datetemp import DateTemp


class TestDateTemp(unittest.TestCase):

    # set up the value for date and temperature
    def setUp(self):
        self.datetemp = DateTemp((2022, 9, 11), 80.00)


# ----------------------------------------------------------------------
# Init Test does not need becauce it is equivalents to date and temperature
# ----------------------------------------------------------------------
# # test the init if have the correct value
# class TestInit(TestDateTemp):
#
#     # test date if the input equals to 0000, 00, 00
#     def test_initial_date(self):
#         self.assertEqual(self.datetemp.date, (0000, 00, 00))
#
#     # test tempereture if the input equals to 0.00F
#     def test_initial_temp(self):
#         self.assertEqual(self.datetemp.temperature, 0.00)


class TestDate(TestDateTemp):

    # test date if the input equals to 0000, 00, 00
    def test_date(self):
        self.assertEqual(self.datetemp.date, (2022, 9, 11))

    # test date if is in year, month, day format
    def test_valid_date(self):
        self.assertTrue(self.datetemp.date, datetime.date)

    # test date if it does not return datetime.date format
    def test_invalid_date(self):
        self.assertNotEqual(self.datetemp.date, int)


class TestTemp(TestDateTemp):

    # test if temperature equals to 0.00F
    def test_temp(self):
        self.assertEqual(self.datetemp.temperature, 80.00)

    # test if temperature is valid when the user enter a float value
    def test_valid_temp_with_float(self):
        self.assertIsInstance(self.datetemp.temperature, float)

    # test if temperature is invalid when the user enter a string value
    def test_invalid_temp_with_str(self):
        self.assertNotIsInstance(self.datetemp.temperature, str)

    # test if temperature is invalid when the user enter an int value
    def test_invalid_temp_with_int(self):
        self.assertNotIsInstance(self.datetemp.temperature, int)


class TestString(TestDateTemp):

    # test the output of the __str__
    def test_str(self):
        actual = self.datetemp.__str__()
        expected = 'The temperature on (2022, 9, 11) was 80.0 F'
        self.assertEqual(actual, expected)


class TestSortedByDateOrTemp(TestDateTemp):

    # create DateTemp objects
    datetemp1 = DateTemp((2022, 9, 11), 70)
    datetemp2 = DateTemp((2011, 1, 2), 55)
    datetemp3 = DateTemp((2022, 8, 30), 89)

    # add each DateTemp Objects into the list
    datetemp_list = [datetemp1, datetemp2, datetemp3]

    # test if the output is sorted by date
    def test_sorted_date(self):
        actual = datetemp.sorted_by_date(self.datetemp_list)
        expected = [self.datetemp2, self.datetemp3, self.datetemp1]
        self.assertEqual(actual, expected)

    # test if the output is sorted by temperature
    def test_sorted_temp(self):
        actual = datetemp.sorted_by_temp(self.datetemp_list)
        expected = [self.datetemp2, self.datetemp1, self.datetemp3]
        self.assertEqual(actual, expected)

# ----------------------------------------------------------------------
# 5 tests that are not necessary because they are in an equivalence class that is already being tested
#
# 1. the init test of date because it is tested with the date test (is equivalent to date)
# 2. the init test of temperature because it is equivalent to temperature
# 3. set_date_from_ints because it is equivalent to test_valid_date
# 4. __repr__ because it is equivalent to __str__
# 5. date with the decorator @property because it is test with the date test
# ----------------------------------------------------------------------


