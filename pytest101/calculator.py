
class CalculatorError(Exception):
    pass

class Calculator(object):
    def add(self, a, b):
        try:
            return a + b
        except TypeError:
            raise CalculatorError('Invalid value')

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b