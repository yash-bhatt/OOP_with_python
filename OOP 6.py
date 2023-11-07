## Property decorators - Getters, Setters and Deleters 

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.'+ last + '@milliman.com'
    
    @property 
    def email(self): ## this is a method!
        return f'{self.first}.{self.last}@milliman.com'

    @property
    def fullname(self): ## this is a method!
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    

emp_1 = Employee('John', 'Smith', 10)
# emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

## what if we want to change the first name?
emp_1.first = 'Jim'

## So we will do the use of property decorators since if we use a method it will break someone's code.

## if we use a method we have to change code from emp_1.email to emp_1.email()!

print(emp_1.email)

## applying a setter on full name!

emp_1.fullname = 'Corey Schafer'
print(emp_1.first)
print(emp_1.email)

## We can make a deleter in the same way if we want to delete something!
del emp_1.fullname
print(emp_1.email)
print(emp_1.pay)