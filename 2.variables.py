# Instance variables are unique for each instance (first, last, pay)
# Class variables are shared among all instances of a class

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


print(f'{Employee.num_of_emps=}')

emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000)

# init is executed everytime an instance is created, it adds 1 to the num_of_emps class var
print(f'{Employee.num_of_emps=}')
print()

# raise_amount is the same for all instances
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay)
print()

# see how it works internally
print(emp_1.__dict__)  # no raise_amount
print()
print(Employee.__dict__)  # raise_amount is there
print()

emp_1.raise_amt = 1.05  # only instance is changed
print(Employee.raise_amt)
print(emp_1.raise_amt)  # access raise_amount through class
print(emp_2.raise_amt)  # access raise_amount through class
print(emp_1.__dict__)   # raise_amount added
print()

Employee.raise_amt = 1.06  # everything changes
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print()


