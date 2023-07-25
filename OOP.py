## Python Object-Oriented Programming

## Creating a class!
## But why? - They allow us to logically use our data! (Not much clear!)

# class Employee:
#     pass ## this will tell python to pass it for now

## new one
## init method is initialize method...
## 
## link to the python module: https://docs.python.org/3/reference/datamodel.html#special-method-names
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@milliman.com'

    def fullname(self): ## this is a method!
        return f'{self.first} {self.last}'
    

#difference b/w class and instance of a class:
emp_1 = Employee('Yash', 'Bhatt', 10) ## this will be instance of a class
emp_2 = Employee('Deepanshi', 'Jain', 10) ## --> these are attributes of our class

# print(emp_1)
# print(emp_2)

##Instance variables:
# emp_1.first = 'Yash'
# emp_1.last = 'Bhatt'
# emp_1.email = 'Yash.Bhatt@milliman.com'
# emp_1.pay = 10

# emp_2.first = 'Deepanshi'
# emp_2.last = 'Jain'
# emp_2.email = 'Deepanshi.Jain@milliman.com'
# emp_2.pay = 10

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname()) ##Since this is a method it will require parentheses
## Now we don't want to do all this information so we will make some changes to our class (commenting out above one)

## Now we will be adding methods in our class! 

## Following two things are same!
emp_1.fullname()
print(Employee.fullname(emp_1))


