# classes: without init function defined, an empty object will be instantiated.
#   If init is defined, it will be invoked upon instantiation of an object of the class
# The first parameter of any method/function in the class is always self, the name self is used by convention.
#  The object that the method was called on is auto passed in for the first param, so the function call param list has one less arg than the function definition.


# Project 3 Option A: complete this module (employ.py) and also module empDB.py.
#  __init__ for class EmpHourly is completed for you so you can use it as a model for calling of superclass methods

# For employ.py:
#   Fill in the class definitions where they are incomplete. 
#   Code __init__ methods so that each type of employee is correctly instantiated and each attribute coded once only.
#   Code __str__ methods so that each type of employee has all attibutes printed on one line, in csv format (attributes separated by commas only), in the order they appear in the __init__ parameter list.
#   Code calc_salary so that each type of employee has salary calculated correctly. (You may pass hours worked as a parameter.)
#   Call on superclass __init__ and __str__ where appropriate. Call on superclass calc_salary where appropriate.


#from datetime import tzinfo, timedelta, datetime   # http://docs.python.org/library/datetime.html
from datetime import *
import string

class Employee(object):

    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today()):
        # set all attributes from the parameter list
        pass

    def __str__(self):
        pass


class EmpSalaried(Employee):
    # salary is for the pay period
    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today()):      #keep
        # fill in call to superclass --init--
        # set the additional attribute
        pass
                  
    # hrsWorkedThisPeriod is for uniformity with other Employees and is not used        
    def calc_Salary(self,hrsWorkedThisPeriod = 0):
        pass

class Manager(EmpSalaried):
    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today(), manage=[]):
        pass

    def __str__(self):
        pass

        
class EmpHourly(Employee):
    # salary is per hour wage
    # __init__ is complete:
    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today(), manager='',):
        # Employee.__init__(self, salary, firstName, lastName, ssID, DOB, startDate)  #  <- alternative to next line 
        super(EmpHourly, self).__init__(salary, firstName, lastName, ssID, DOB, startDate)
        self.manager =  manager
        
    def __str__(self):
        pass
        
    def calc_Salary(self, hrsWorkedThisPeriod = 0):
        pass

class AdminAssistant(EmpHourly):
    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today(), manager='', department=''):
        pass

    def __str__(self):
        pass

class FactoryWorker(EmpHourly):
        pass

class MaintenanceWorker(EmpHourly):
        pass




emp1 = Employee(25, "jim", "Le", "111-11-1111", "1995-04-24", datetime.today())
emp2 = EmpSalaried(28, "jane", "Le", "123-45-6789", "1989-12-03")
print emp2
