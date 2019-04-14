class InputGenerator(object):

    def gererate_string_input(self, order) -> str:
        return str(input('Please, provide your {0} string input. \n'.format(order)))