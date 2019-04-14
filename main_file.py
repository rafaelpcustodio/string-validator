from string_validator.StringValidator import StringValidator
from input_generator.InputGenerator import InputGenerator

if __name__ == '__main__':

    string_one = InputGenerator().gererate_string_input("first")
    string_two = InputGenerator().gererate_string_input("second")
    StringValidator.validate_string(StringValidator(), string_one, string_two)


