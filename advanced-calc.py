# Code 1: Advanced Calculator with History

class AdvancedCalculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"Add: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"Subtract: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"Multiply: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            result = "Error! Division by zero."
        else:
            result = a / b
        self.history.append(f"Divide: {a} / {b} = {result}")
        return result

    def show_history(self):
        return "\n".join(self.history) if self.history else "No calculations performed yet."

if __name__ == "__main__":
    # Test Advanced Calculator
    calc = AdvancedCalculator()
    calc.add(5, 10)
    calc.subtract(20, 8)
    print(calc.show_history())