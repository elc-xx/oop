# Create class and instances

class Employee:

    # also called constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_2)
print()

print(emp_1.email)
print(emp_2.email)
print()

print(emp_1.fullname())
print(emp_2.fullname())
print()

# calling the object -Employee- and then the instance -emp_1-
print(Employee.fullname(emp_1))
