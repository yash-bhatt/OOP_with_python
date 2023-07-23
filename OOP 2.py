## Lesson 2:
## Class variables:
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

print(f'Number of Employee instances at time 0 is {Employee.num_of_emps}')
#difference b/w class and instance of a class:
emp_1 = Employee('Yash', 'Bhatt', 10) ## this will be instance of a class
emp_2 = Employee('Deepanshi', 'Jain', 10) ## --> these are attributes of our class

print(f'Number of Employee instances at time after emp_1 and emp_2 is {Employee.num_of_emps}')
## Now we are going to add some more things to our class for example : raise!
# there are different ways to access the raise!
print(Employee.raise_amount)
print(emp_1.raise_amount) ## this is also going and getting raise_amount from the class!
print(emp_2.raise_amount)

print(Employee.__dict__)
print(emp_1.__dict__)

## But let's say if I assign instance something, it will become it's attribute!
## eg:
emp_1.raise_amount = 1.05
print(emp_1.__dict__)

print(Employee.raise_amount)
print(f'emp_1 raise amount after we changed it {emp_1.raise_amount}')
print(emp_1.raise_amount)

## Now we will add something which will tell us number of instances!

## Next we will learn about the Methods! there are static and class methods...