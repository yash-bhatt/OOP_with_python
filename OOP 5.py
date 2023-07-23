## In this lesson we will learn about the special methods or magic/dunder methods!
## dunder = __abc__ left right is dunder

## PRACTICE: LOOK AT THE DIFFERENT MODULES CODE AND UNDERSTAND IT! for example datetime module!
## looking into these libraries will def help me!

class Employee:

    num_of_emps = 0
    raise_amount = 1.04 ## this is the raise people will be getting

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@milliman.com'

        Employee.num_of_emps += 1 ## We haven't used self this time because we do not have any specific case for which we want an instance to have different value like we did for raise!

    def fullname(self): ## this is a method!
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  

    @classmethod
    def set_raise_amt(cls, amount): ## classmethods pass class automatically
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    ### adding a add special method:
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

    
## this two special methods allow us change how our objects are printed and displayed.


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)
print(str(emp_1)) # or print(emp_1.__repr__())
print(repr(emp_1)) # or print(emp_1.__str__())

print(emp_1+emp_2)
print(len(emp_1))