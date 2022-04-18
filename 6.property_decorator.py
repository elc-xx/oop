# Property decorator allows to define Class methods that we can access like attributes.
# This allows us to implement getters, setters and deleters.

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Doe')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)  # Refers to John before the email function and property decorator
print(emp_1.fullname)
print()

emp_1.fullname = 'Steve Smith'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()
