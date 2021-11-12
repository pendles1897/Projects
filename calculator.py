class Calculator:

    def __init__(self, firstValue, operation, secondValue):
        self.firstValue = firstValue
        self.operation = operation
        self.secondValue = secondValue
    
    # Addition
    def add(self):
        print(self.firstValue + self.secondValue)
    
    # Subtraction
    def subtract(self):
        print(self.firstValue - self.secondValue)
    
    # Multiplication
    def multiply(self):
        print(self.firstValue * self.secondValue)

    # Division
    def divide(self,a,b):
        print(self.firstValue / self.secondValue)
    

while True:
    a = int(input("Enter first value: "))
    b = str(input("\nEnter operation: "))
    c = int(input("\nEnter second value: "))
    if b == '+':
        calculation = Calculator(a,b,c)
        calculation.add()
        break
    elif b == '-' or b == '–':
        calculation = Calculator(a,b,c)
        calculation.subtract()
        break
    elif b == 'x' or b == 'X':
        calculation = Calculator(a,b,c)
        calculation.multiply()
        break
    elif b == '/':
        calculation = Calculator(a,b,c)
        calculation.divide()
        break
    else:
        print('Invalid operator. Try again: ')
        continue