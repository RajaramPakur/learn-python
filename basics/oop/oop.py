# class
import datetime


class Employee:

    # class variables
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last + '@company.com'
        # super().__init__()
        Employee.num_of_emps += 1

    # dunder methods

    def __repr__(self):
        # this methods is used to debugging logging
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        #  used to display for end user
        return "{} - {}".format(self.fullname(), self.email)

    # Dunder method to add
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # cls as class variable
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # can use as constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split(',')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if(day.weekday() == 5 or day.weekday() == 6):
            return False
        return True


# Inheritance - inherit from employee class


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_language):
        self.programming_language = programming_language
        super().__init__(first, last, pay)


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        super().__init__(first, last, pay)

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--->", emp.fullname())


emp_1 = Employee('Rajaram', 'Pakur', 50000)
emp_2 = Employee('Shyam', 'Pakur', 60000)

# called dunder method automatically
print(emp_1 + emp_2)
print(len(emp_1))

# print(emp_1.__repr__())

# instance variables
dev_1 = Developer('Rajaram', 'Pakur', 50000, "Python")
dev_2 = Developer('Shyam', 'Shrestha', 60000, "Java")

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.add_emp(dev_2)

# print(isinstance(mgr_1, Manager))
# print(issubclass(Developer, Employee))


print(mgr_1.email)
print(mgr_1.print_emps())
mgr_1.remove_emp(dev_1)
print(mgr_1.print_emps())


# my_date = datetime.date(2020, 3, 28)
# print(Employee.is_workday(my_date))

# emp_1.set_raise_amt(1.05)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)

# print(emp_1.fullname())
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.num_of_emps)

# emp_str_1 = 'John,Doe,10000'
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.first)
