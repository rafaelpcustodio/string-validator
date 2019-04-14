import unittest
from string_validator.StringValidator import StringValidator

class OverlapTest(unittest.TestCase):

    def test_bigger_first_value_success(self):
        first_value = "1.2"
        second_value = "1.0"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 1.2 is bigger than the last one 1.0')

    def test_smaller_first_value_success(self):
        first_value = "1.0"
        second_value = "1.2"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 1.0 is smaller than the last one 1.2')

    def test_equals_first_value_and_second_value_success(self):
        first_value = "1.0"
        second_value = "1.0"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'First(1.0) and second(1.0) value are equal')

    def test_equals_big_first_value_and_big_second_value_success(self):
        first_value = "1.000000000000"
        second_value = "1.000000000000"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'First(1.0) and second(1.0) value are equal')

    def test_int_format_smaller_success(self):
        first_value = "1"
        second_value = "2"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 1.0 is smaller than the last one 2.0')

    def test_int_format_bigger_success(self):
        first_value = "2"
        second_value = "1"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 2.0 is bigger than the last one 1.0')

    def test_random_values_first_success(self):
        first_value = "298.98"
        second_value = "298.00"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 298.98 is bigger than the last one 298.0')

    def test_random_values_second_success(self):
        first_value = "628172.56"
        second_value = "789820.10"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 628172.56 is smaller than the last one 789820.1')

    def test_random_negative_values_first_success(self):
        first_value = "628172.56"
        second_value = "-789820.10"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 628172.56 is bigger than the last one -789820.1')

    def test_random_negative_values_second_success(self):
        first_value = "-628172.56"
        second_value = "-789820.10"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value -628172.56 is bigger than the last one -789820.1')

    def test_random_negative_values_third_success(self):
        first_value = "214.01"
        second_value = "214.001"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 214.01 is bigger than the last one 214.001')

    def test_random_negative_values_fourth_success(self):
        first_value = "214.00001"
        second_value = "214.000001"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 214.00001 is bigger than the last one 214.000001')

    def test_both_wrong_format_error(self):
        first_value = "one"
        second_value = "two"
        self.assertRaises(ValueError, StringValidator.validate_string(StringValidator(), first_value, second_value))

    def test_one_wrong_format_error(self):
        first_value = "a"
        second_value = "1.0"
        self.assertRaises(ValueError, StringValidator.validate_string(StringValidator(), first_value, second_value))

    def test_one_wrong_format_int_error(self):
        first_value = "--1"
        second_value = "0"
        self.assertRaises(ValueError, StringValidator.validate_string(StringValidator(), first_value, second_value))

    def test_two_wrong_format_int_first_success(self):
        first_value = "001"
        second_value = "010"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 1.0 is smaller than the last one 10.0')

    def test_two_wrong_format_int_second_success(self):
        first_value = "0000000100"
        second_value = "0000010"
        result_string = StringValidator.validate_string(StringValidator(), first_value, second_value)
        self.assertEquals(result_string, 'The first value 100.0 is bigger than the last one 10.0')


if __name__ == '__main__':
    unittest.main()