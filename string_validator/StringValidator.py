from utils.Parser import Parser
from printer.Printer import Printer

class StringValidator(object):

    def validate_string(self, first_string, second_string) -> str:
        try:
            float_first_value = self.parse_string(first_string)
            float_second_value = self.parse_string(second_string)
            return self.compare_values(float_first_value, float_second_value)
        except ValueError:
            print('Sorry, you must provide a number value.')

    def parse_string(self, string_value):
       return Parser.string_to_float_parser(string_value)

    def compare_bigger(self, first_float, second_float) -> bool:
        return first_float > second_float

    def compare_equal(self, first_float, second_float) -> bool:
        return first_float == second_float

    def compare_values(self, float_first_value, float_second_value) -> str:
        if self.compare_bigger(float_first_value, float_second_value):
            return Printer.print_bigger(Printer(), float_first_value, float_second_value)
        elif self.compare_equal(float_first_value, float_second_value):
            return Printer.print_equal(Printer(), float_first_value, float_second_value)
        else:
            return Printer.print_smaller(Printer(), float_first_value, float_second_value)
