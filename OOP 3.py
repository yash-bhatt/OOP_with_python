## In this video we will learn regular, class and static methods.

## Regular methoods in a class automatically take the instance as the first argument (we called it 'self')
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

emp_1 = Employee('Yash', 'Bhatt', 10) ## this will be instance of a class
emp_2 = Employee('Deepanshi', 'Jain', 10)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amt(1.05) ## this is same as saying Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

## Now add a classmethod which will convert an string into a employee class automatically!

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1) ## So when people say they used classmethods as alternative mean this is what they mean
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)

## Now we will talk about the static methods
## When working with the classes regular methods put instance as the first method (self)
## and Classmethods automatically pass class (cls) as the first argument

## Static method don't pass anything automatically.

## eg: 
## 
import datetime
my_date = datetime.date(2016, 7, 11)
print(f'For the above date the day is a workday? -> {Employee.is_workday(my_date)}')
