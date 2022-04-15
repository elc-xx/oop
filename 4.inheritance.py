class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# new class inherits all Employee methods and attributes
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)  # call parent constructor to handle this
        self.prog_language = prog_language


class Manager(Employee):
    raise_amt = 1.20

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  # call parent constructor to handle this
        if employees is None:
            self.employees = []  # we don't pass the empty list as default argument
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('John', 'Doe', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# print(help(Developer))

print(dev_1.email)
print(dev_1.prog_language)
print(dev_2.email)
print(dev_2.prog_language)
print()

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print()

mgr_1 = Manager('Sue', 'Heck', 90000, [dev_1])
print(mgr_1.email)
print(mgr_1.employees)  # points to location of list in memory
mgr_1.print_emps()
print()

mgr_1.add_emp(dev_2)
mgr_1.print_emps()
print()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
print()

# validations
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print()

print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))