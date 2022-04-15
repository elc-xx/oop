# Special methods are also called magic or dunder methods.
# These methods allow us to emulate built-in types or implement operator overloading.
# Official list: https://docs.python.org/3/reference/datamodel.html (section and subsections from 3.3)

class Employee:
    raise_amt = 1.04

    # init is a special method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    # return sum of salaries
    def __add__(self, other):
        return self.pay + other.pay

    # return length of name
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1) # calls str(emp_1)
# initially it returned "<__main__.Employee object at 0x000001B5F1807FD0>"
print()

# repr is an unambiguous representantion of the object, used for debugging,logging; meant for developers
print(repr(emp_1))   # same as print(emp_1.__repr__())
# str is a readable representation of an object, how it displays in screen; meant for end-users
print(str(emp_1))    # same as print(emp_1.__str__())
print()

print(emp_1 + emp_2)   # same as print(emp_1.__add__(emp_2))
print()

print(len(emp_1))     # same as print(emp_1.__len__())
print()
