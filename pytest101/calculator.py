from numbers import Number
class CalculatorError(Exception):
    pass

class Calculator(object):
    def add(self, a, b):
        self._check(a)
        self._check(b)
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise CalculatorError('Can\'t divide by zero')

    def _check(self, operand):
        if not isinstance(operand, Number):
            raise CalculatorError(f'{operand} was not a number')

if __name__ == '__main__':
    print('Let\'s calculate')
    calculator = Calculator()
    operations = [
        calculator.add,
        calculator.subtract,
        calculator.multiply,
        calculator.division,
    ]

    while True:
        for i, operation in enumerate(operations, start=1):
            print(f'{i}: {operation.__name__}')
        print('q: quit\n')
        operation = int(input('Pick an operation: '))
        a = float(input('What is a: '))
        b = float(input('What is b: '))
        print(operations[operation - 1](a, b))
        if operation == 'q':
            import sys
            sys.exit()