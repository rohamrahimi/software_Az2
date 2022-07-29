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

    def calculate(self, operand1, operand2):
        pass

class Add(Operator):
    pass

class Sub(Operator):
    SYMBOL = "-"
    def calculate(self, operand1, operand2):
        return operand1 - operand2

if __name__ == "__main__":
    pass