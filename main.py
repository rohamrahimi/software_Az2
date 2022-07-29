import os
from decimal import Decimal


class InputGetter:
    def __init__(self) -> None:
        self.operator1 = None
        self.operator2 = None
        self.operation_symbol = None

    def get_input(self):
        self.operation_symbol = input("Please enter the operation symbol:")
        self.operator1 = input("Please enter the first operator:")
        self.operator2 = input("Please enter the second operator:")

    def get_operation_symbol(self):
        return self.operation_symbol

    def get_operator1(self):
        return self.operator1

    def get_operator2(self):
        return self.operator2


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
    SYMBOL = "+"

    def calculate(self, operand1, operand2):
        return operand1 + operand2

class Sub(Operator):
    SYMBOL = "-"
    def calculate(self, operand1, operand2):
        return operand1 - operand2

if __name__ == "__main__":
    pass