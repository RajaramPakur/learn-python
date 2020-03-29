class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # method as attribute
    # work as getter
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # setter method for fullname
    @fullname.setter
    def fullname(self, fullname):
        first, last = fullname.split(' ')
        self.first = first
        self.last = last

    # deleter method
    @fullname.deleter
    def fullname(self):
        print("Delete name")
        self.first = None
        self.last = None

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)


emp_1 = Employee('Rajaram', 'Pakur', 50000)


print(emp_1.first)

emp_1.fullname = "Shyam Shrestha"
print(emp_1.first)

del emp_1.fullname

print(emp_1.fullname)
print(emp_1.email)

