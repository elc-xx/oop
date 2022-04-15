# Regular methods take the instance as the first argument (self)
# Class methods take the class as first argument (cls). Can be used as alternative constructors.
# Static methods do not take instance or class as the first argument. They have some logical connection.

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # add decorator to convert a regular method to class method
    # we use cls because we can't pass the reserved word "class"
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)   # call the constructor

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)  # same as Employee.raise_amt = 1.05
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print()

# user case when they receive the new employee data in special format
# class method to create the instance
emp_str_3 = 'Kevin-Smith-70000'

emp_3 = Employee.from_string(emp_str_3)
print(emp_3.email)
print(emp_3.pay)
print()

# static methods don't use the class or instance to function
import datetime
my_date = datetime.date(2022, 4, 15)    # Friday
print(Employee.is_workday(my_date))

my_date = datetime.date(2022, 4, 16)    # Saturday
print(Employee.is_workday(my_date))