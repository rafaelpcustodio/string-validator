
class Printer(object):

    def print_bigger(self, first_value, second_value) -> str:
        print_value = 'The first value {0} is bigger than the last one {1}'.format(first_value, second_value)
        print(print_value)
        return print_value

    def print_equal(self, first_value, second_value) -> str:
        print_value = 'First({0}) and second({1}) value are equal'.format(first_value, second_value)
        print(print_value)
        return print_value

    def print_smaller(self, first_value, second_value) -> str:
        print_value = 'The first value {0} is smaller than the last one {1}'.format(first_value, second_value)
        print(print_value)
        return print_value
