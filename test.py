# test_all.py
from advanced_calc import AdvancedCalculator
from todo_list import TodoList
from bank_account import BankAccount
from library import Library
from weather_tracker import WeatherTracker

# Test Advanced Calculator
calc = AdvancedCalculator()
calc.add(5, 10)
calc.subtract(20, 8)
print("Calculator History:")
print(calc.show_history())
print("\n")

# Test Todo List
todo = TodoList()
print(todo.add_task("Complete Python Project"))
print("Tasks:")
print(todo.view_tasks())
print("\n")

# Test Banking System
account = BankAccount("Alice", 1000)
print(account.deposit(500))
print(account.withdraw(300))
print(account.check_balance())
print("\n")

# Test Library Management
library = Library()
library.add_book("1984", "George Orwell")
print("Library Books:")
print(library.view_books())
print("\n")

# Test Weather Tracker
tracker = WeatherTracker()
tracker.add_weather("2025-01-20", 25)
tracker.add_weather("2025-01-21", 28)
print(tracker.average_temperature())
