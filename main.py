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
    def __init__(self, operators):
        self.operators = operators

    def calculate(self, operation, operand1, operand2):
        for operator in self.operators:
            if operation == operator.SYMBOL:
                return operator.calculate(operand1, operand2)
        
        raise Exception("Invalid operation")

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


def main():
    input_getter = InputGetter()
    add_operator = Add()
    sub_operator = Sub()
    calculator = Calculator(
        operations=[
            add_operator,
            sub_operator,
        ]
    )
    answer = calculator.calculate(
        operation=input_getter.get_operation_symbol(),
        operand1=input_getter.get_operator1(),
        operand2=input_getter.get_operator2(),
    )
    print("Answer:", answer)


if __name__ == "__main__":
    main()
