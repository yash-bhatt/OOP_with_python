## In this video we will learn python class inheritance.
## Inheritance allows us to inherit attributes and methods from parent class
## We can add new functionalities without modifying our parent class!

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
    
## Creating a new inheritance class
class Developer(Employee):
    raise_amount = 1.5  ##50%

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) ## this will help us take first, last and pay using the employee class
        self.programming_lang = prog_lang

## Again creating a new class called Manager!
class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    ## add few methods here!
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    

    def print_emps(self):
        for emp in self.employees:
            print('----->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])


print(mgr_1.email)
mgr_1.print_emps()

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

## Now we have follwing in emps under mgr_1
mgr_1.print_emps()


# help(Developer)
# print(dev_1.email)
# print(dev_2.email)


print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.email)
print(dev_1.programming_lang)

## isinstance tells us if an object is instance of a class or not?
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

## issubclass tells is a class is subclass of another class?
      
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

## Http execption? look into this!
## library is python whisky library exception module.
