#Cayla Shaver
#This is a Class project that displays the use of classes and inheritance within classes.
#from datetime import tzinfo, timedelta, datetime  #http://docs.python.org/library/datetime.html
from datetime import *
import string

class Employee(object):

    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today()):
        # set all attributes from the parameter list
        self.salary = salary
        self.firstName = firstName
        self.lastName = lastName
        self.ssID = ssID
        self.DOB = DOB
        self.startDate = startDate
    def __str__(self):
        return str(self.firstName) + ', ' + str(self.lastName) + ', ' + str(self.ssID) + ', ' + str(self.DOB) + ', ' + str(self.startDate) + ', ' + str(self.salary)


class EmpSalaried(Employee):
    # salary is for the pay period
    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today()):      #keep
        # fill in call to superclass --init--
        super(EmpSalaried, self).__init__(salary, firstName, lastName, ssID, DOB, startDate)
                 
    # hrsWorkedThisPeriod is for uniformity with other Employees and is not used       
    def calc_Salary(self,hrsWorkedThisPeriod = 0):
        return self.salary

class Manager(EmpSalaried):
    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today(), manage=[]):
        super(Manager, self).__init__(salary, firstName, lastName, ssID, DOB, startDate)
        self.manage = manage

    def __str__(self):
        return super(Manager, self).__str__() + ', ' + str(self.manage)

       
class EmpHourly(Employee):
    # salary is per hour wage
    # __init__ is complete:
    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today(), manager=''):
        # Employee.__init__(self, salary, firstName, lastName, ssID, DOB, startDate)  #  <- alternative to next line
        super(EmpHourly, self).__init__(salary, firstName, lastName, ssID, DOB, startDate)
        self.manager =  manager
       
    def __str__(self):
        return super(EmpHourly, self).__str__() + ', ' + str(self.manager)
       
    def calc_Salary(self, hrsWorkedThisPeriod = 0):
        salary = self.salary
        hours = hrsWorkedThisPeriod
        pay = salary * hours
        return pay

class AdminAssistant(EmpHourly):
    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today(), manager='', department=''):
        super(AdminAssistant, self).__init__(salary, firstName, lastName, ssID, DOB, startDate, manager)
        self.department = department

    def __str__(self):
        return super(AdminAssistant, self).__str__() + ', ' + str(self.department)


class FactoryWorker(EmpHourly):
    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today(), manager='', assemblyLine=''):
        super(FactoryWorker, self).__init__(salary, firstName, lastName, ssID, DOB, startDate, manager)
        self.assemblyLine = assemblyLine
 
    def __str__(self):
        return super(FactoryWorker, self).__str__() + ', ' + str(self.assemblyLine)

class MaintenanceWorker(EmpHourly):
    def __init__(self, salary=0.0, firstName="", lastName="", ssID="", DOB=datetime.fromordinal(1), startDate=datetime.today(), manager='', buildings=[]):
        super(MaintenanceWorker, self).__init__(salary, firstName, lastName, ssID, DOB, startDate, manager)
        self.buildings = buildings

    def __str__(self):
        return super(MaintenanceWorker, self).__str__() + ', ' + str(self.buildings)



##TESTCASES THESE ARE ALL THE CALLS FOR EACH CLASS AS WELL AS THE SALARY CALCULATION WHEN APPLICABLE.


emp1 = Employee(5.00, "Jim", "Le", "111-11-1111", "1995-04-24", datetime.today())
print emp1

emp2 = EmpSalaried(20.00, "Jane", "Lee", "123-45-6789", "1989-12-03")
print emp2

emp2sal = emp2.calc_Salary(40)
print emp2sal

emp3 = Manager(4200.00, "Jordan", "Goldin", "333-22-1111", "1985-12-25", "2012-04-01")

emp4 = EmpHourly(15.00, "Bobby", "Green", "111-22-3333", "1987-09-10", datetime.today(), [emp3.firstName + ' ' + emp3.lastName])
print emp4

emp4sal = emp4.calc_Salary(35)
print emp4sal

emp5 = AdminAssistant(50.00, "Cayla", "Shaver", "999-88-7777", "1988-08-10", datetime.today(), [emp3.firstName + ' ' + emp3.lastName], "Main Office")
print emp5

emp5sal = emp5.calc_Salary(25)
print emp5sal

emp6 = FactoryWorker(15.00, "Billy", "James", "777-88-9999", "2000-05-03", datetime.today(), [emp3.firstName + ' ' + emp3.lastName], "Line Alpha")
print emp6

emp6sal = emp6.calc_Salary(45)
print emp6sal

emp7 = MaintenanceWorker(11.00, "Janie", "Wilson", "444-55-6666", "1964-02-24", datetime.today(), [emp3.firstName + ' ' + emp3.lastName], ["Alpha", "Bravo", "Charlie"])
print emp7

emp7sal = emp7.calc_Salary(20)
print emp7sal

emp8 = Manager(4200.00, "Jordan", "Goldin", "333-22-1111", "1985-12-25", "2012-04-01", [emp4.firstName + ' ' + emp4.lastName, emp5.firstName + ' ' + emp5.lastName, emp6.firstName + ' ' + emp6.lastName, emp7.firstName + ' ' + emp7.lastName])
print emp8

emp8sal = emp8.calc_Salary(60)
print emp8sal
