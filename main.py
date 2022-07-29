import os
from decimal import Decimal

class InputGetter:
    pass

class Calculator:
    def __init__(self, operations):
        self.operations = operations

    def calculate(self, operation, operand1, operand2):
        pass

class Operator:
    SYMBOL = ""

    def __init__(self):
        pass

    def calculate(self):
        pass

class Add(Operator):
    pass

class Sub(Operator):
    pass

if __name__ == "__main__":
    pass