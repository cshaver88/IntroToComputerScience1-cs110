# Cayla Shaver
# This project is working with classes and how to code programs that modify information within a database.
# The programs also enable the user to search for something within the database and have it return the necessary information.
#
# Project 3 Option A: complete employ.py and also this module (empDB.py).
# Any method that is commented:  "# this is complete" requires no further code, you may use as is.
# selectionSort is provided so you can use it as a model for sorting and searching by any parameter
# It may be easier to code without the attrib parameter first, searching by last name
# For empDB.py
# Document each method with a description of what it accomplishes and returns, and how each parameter is used.

# For each method, also state what its big-Oh runtime is and justify your claim
# You may use the following in your runtime justifications:
# The run-time of adding an element to the end of a list is constant time
# The run-time of most string operations are linear, except indexing and len, which are constant time.
# The run-time of a slice operation is proportional to the length of the output, but independent of the size of the input.

# Restrictions on use of built-in functions are listed above some of the methods you will code

import copy
from employ2 import *


# done ## This class is where all of the information from employ.py is kept and organized into a neat little easy to read list of employees.


class empDB:


# done ## This is where the class named empDB gets the employee list from employ.py, all of the employees stored there and sets the item lst to a global variable.
# The parameter lst is set to default as an empty list if there isn't anything that comes back from the database that it is accessing.
# Big Oh notation == O(1) because this function only does this operation once.


    def __init__(self, lst= []):                  # this is complete
        self.lst = lst


# done ## This organizes all of the information into a neat list that after each employee puts in a new line and returns it so that each
# employee is on a separate line from the others.
# Big Oh notation == O(n) because the for loop will go through the length of the list and inside the for loop it will use
# constant time to add the elements onto the result list.


    def __str__(self):
        result = ''
        for elem in self.lst:
            result += str(elem) + "\n"
        return result


# done ## This looks at all of the information that is in the list and returns the length of that whole list.
# Big Oh notation == O(1) because this only counts each element in the list and returns the total length which is
# constant time.


    def __len__(self):
        return len(self.lst)


# done ## This one looks at the list and then adds a new employee to the main database list at the end.
# Big Oh notation == O(1) because it looks at the list and regardless of how long the list is it automatically
# goes to the end of the list and adds emp onto it using constant time.


    def appendEmp(self, emp=Employee()):
        self.lst += [emp]


# done ## This looks at the list of employees in the database and inserts a new employee at index cell of
# the list of all of the employees.       
# Big Oh notation == O(n) because there are two for loops that each use constant time to add things to the list so
# it will go n times for each loop.


    # Do not use slices: code this yourself
    def insertEmp(self, index, emp=Employee()):
        new_list = []
        for i in range(0, index):
            new_list += [self.lst[i]]
        new_list += [emp]
        for j in range(index, len(self.lst)):
            new_list += [self.lst[j]]
        self.lst = new_list


# done ## This function will return the index of an element that is in the employee database.
# Big Oh notation == O(1) because it only looks at the list once at an index space so it doesn't take any extra time only uses
# constant time.


    # Three standard methods to overload
    # Allows for bracket operator to be used to return indexth element of the empDB
    def __getitem__(self, index):                  # this is complete
        return self.lst[index]

   
# done ## This function will look at the database and change the index of the list to the employee that is in the parameter list
# and change val to the element that is at index of the employee.
# Big Oh notation == O(1) because there are no loops to go through it only goes to the list and at index space adds an employee
# to the list which is only constant time 


    # Allows for bracket operator to be used to modify indexth element of the empDB, setting it to val
    def __setitem__(self, index, emp=Employee()):  # this is complete
        self.lst[index] = emp


# done## This looks at the list of employees and deletes a specific employee from the main list of employees depending on the index number
# that is given to it, it doesn't return anything it just mutates the list that is imported from the database.
# Big Oh notation == O(n) because there is a for loop that goes through the whole list but everything inside the loop is
# using constant time.


    # Do not use del operator, but you may slice or bracket operator
    def __delitem__(self, index):
        new_list = []
        for i in range(len(self.lst)):
            if i != index:
                new_list += [self.lst[i]]
        self.lst = new_list

               
# done ## This looks at each part of the list of employees and checks to see if any of the items in the list are the same as the val
# that is being searched for.  If the val is found within the list of employees it will return the cell number of the val that
# was found if the val is not found within the list of employees it will return a -1.
# I have modified the given sequential search to accept the attribute of anything that is passed in on the call for the function.
# The parameter called attrib takes in any attribute contained in Employee and performs the search on the attribute that is entered, then returns
# the cell number of the given attribute that is found in the list of employees that is passed through the search or -1 if the attribute
# is not found in the list of employees.
# Big Oh notation == O(n) because there is a for loop that looks at everything in the list so n times it looks at everything
# then uses constant time to do everything else inside the loop.
# EXTRA CREDIT DONE!!!


    # For now search on the attribute "lastName", later we will search on any attribute using: getattr(object, attrib[, defaultAttrib])
    def sequentialSearch(self, val, attrib = "lastName"):
        for i in range(len(self.lst)):
            if getattr(self.lst[i], attrib) == val:
                return i
        if getattr(self.lst[i], attrib) != val:
            return -1

       
# done ## This sort function goes through the list of every employee that is in the database of employees and sorts them one after the other and
# mutates the list that is given to it to make it into a sorted list.  This has the extra credit where any attribute for the employee can be taken
# into account and sorted accordingly. If no attribute is entered it will use the lastName as a default attribute to sort with.
# Big Oh notation == O(n)**2 because there is a nested for loop within a for loop which for the outer loop it goes through O(n) times but
# again another O(n) times for the inner loop as well.
# EXTRA CREDIT DONE!!!


    # Sorts on any attribute using: getattr(object, attrib[, defaultAttrib])
    def selectionSort(self, attrib="lastName"):         # this is complete
        minIndex = 0
        for i in range (len(self.lst)):
            minIndex = i
            for j in range(i+1, len(self.lst)):
                # This is how to sort by lastName if there was no parameter attrrib
                #if self.lst[minIndex].lastName > self.lst[j].lastName: 
                # This is how to sort by parameter attribute with "lastName" as the default
                if getattr(self.lst[minIndex], attrib) > getattr(self.lst[j],attrib):
                    minIndex = j
            temp = self.lst[minIndex]
            self.lst[minIndex] = self.lst[i]
            self.lst[i] = temp


# This sort function looks at the employee list and sorts using the two helper functions
# mergeSort calls the mergeSortR function and uses that to split up the whole list into the right side the
# left side and gets a midpoint these sides break up the whole list into individually sorted parts
# of the whole list.  The other function merge takes all of the pieces from mergeSortR and looks at each
# of the individual pieces and compares them against each other then returns them to the mergeSortR function that
# then takes those new pieces and puts them all together then that returns the changed list to mergeSort and that
# mutates the database list to the merge sorted version.
# Big Oh notation == O(nlgn) because the loop will be completed O(n) times but when it gets to the recursive call it will take the length of
# the list and cut it by a constant number changing the amount of times that the loop will be completed each time through the loop.
# this is why it needs the lg in the big oh notation.
# EXTRA CREDIT DONE!!!


    # For now sort on the attribute "lastName", (ie: sort by last name)   EXTRA CREDIT ATTRIBUTE!!!!
    #   Later we will sort on any attribute using: getattr(object, attrib[, defaultAttrib])
    def merge(self, lt, rt, attrib):
        result = []
        i = 0
        j = 0
        while i < len(lt) and j < len(rt):
            if getattr(lt[i], attrib) <= getattr(rt[j], attrib):
                result.append(lt[i])
                i += 1
            else:
                result.append(rt[j])
                j += 1
        result += lt[i:]
        result += rt[j:]
        return result


    def mergeSortR(self, lst, attrib):
        if len(lst) <= 1:
            return lst
        mid = int(len(lst) / 2)
        lt = self.mergeSortR(lst[:mid], attrib)
        rt = self.mergeSortR(lst[mid:], attrib)
        return self.merge(lt, rt, attrib)


    def mergeSort(self, attrib = "lastName"): # split in half  then in half all the way til there is just one card in each half.  with the extra one if odd number goes to the left always
        self.lst = self.mergeSortR(self.lst, attrib)


# done This sort goes through the list of employees and performs a sort on the given attribute in the function call if no attribute
# is specified the default attribute to sort with will be lastName.  This sort goes through the list of employees looks at the
# attribute saves a temp variable for each part of the list then it checks to see if that temp is greater or less that those around it
# then puts it into it's proper place depending on the check of greater or less. This mutates the list by moving each of the temp variables
# into their proper sorted place.
# Big Oh notation == O(n)**2 because there are two loops one inside the other, the outer loop will be completed O(n) times but the inner loop
# will also be completed O(n) times. 
# EXTRA CREDIT DONE!!!


    # Sort on the attribute "lastName" (ie: sort by last name).
    # For extra credit sort on any attribute using: getattr(object, attrib[, defaultAttrib]).=
    def insertionSort(self, attrib = "lastName"):
        for i in range(1, len(self.lst)):
            temp = self.lst[i]
            j = i - 1
            while j >= 0:
                if getattr(self.lst[j], attrib) >= getattr(temp, attrib):
                    self.lst[j + 1] = self.lst[j]
                    j -= 1
                else:
                    break
            self.lst[j + 1] = temp


# This goes through a sorted list of employees and checks the attribute parameter that is entered in the call for it and checks the value that is
# entered as well to see if it is in the sorted list if so it will return the cell number for the searched attribute appears, if it does not
# appear in the list for that attribute it will return a -1.  The helper function binSearch does most of the searching for binarySearch.
# The default for the attribute is set to lastName so if no attribute is given it will default to that instead of something else.
# Big Oh notation == O(nlgn) because there are recursive calls in the functions that make it loop around O(n) times but it
# decreases the size of the list at a set number multiple times.
# EXTRA CREDIT DONE!!!


    # For now search on the attribute "lastName", (ie: return index of employee with last name == val)
    #   Later we will search on any attribute using: getattr(object, attrib[, defaultAttrib])
    def binSearch(self, val, low, high, attrib = "lastName"): # dictionary search from class low and high changes each time
        mid = (low + high) / 2
        if val == getattr(self.lst[mid], attrib):
            return mid
        if low >= high:
            return -1
        if val < getattr(self.lst[mid], attrib):
            return self.binSearch(val, low, mid - 1, attrib)
        if val > getattr(self.lst[mid], attrib):
            return self.binSearch(val, mid + 1, high, attrib)


    def binarySearch(self, val, attrib = "lastName"):
        return self.binSearch(val, 0, len(self) - 1, attrib)



# My testing is before your given start to testing.


                  
## A start on testing :
empList = empDB()


NUM_EMPS = 10
for i in range(NUM_EMPS):
    SSstring =  "111-22-120" + str(i)
    empList.appendEmp(Employee(4000.00,"Employee", str(NUM_EMPS-i-1), SSstring, datetime.fromordinal(1), datetime.today() ))
    #print empList[i].lastName

##print empList
emp1 = Manager(5000.00, "Tom", "Cruise", "000-00-1234", "1934-10-25", datetime.today())
emp2 = Employee(2000.00, "Jane", "Tom", "000-00-1111", "1934-10-25", datetime.today())
emp3 = Manager(100.00, "John", "Doe", "000-00-2222", "1934-10-25", datetime.today())
emp4 = Employee(7500.00, "Reinhard", "Cate", "000-00-3333", "1934-10-25", datetime.today())
emp5 = AdminAssistant(50.00, "Cayla", "Shaver", "999-88-7777", "1988-08-10", datetime.today(), [emp3.firstName + ' ' + emp3.lastName], "Office A")
emp6 = FactoryWorker(25.00, "Billy", "James", "777-88-9999", "2000-05-03", datetime.today(), [emp3.firstName + ' ' + emp3.lastName], "Line Bravo")
emp7 = MaintenanceWorker(20.00, "Janie", "Wilson", "444-55-6666", "1964-02-24", datetime.today(), [emp1.firstName + ' ' + emp1.lastName], ["Foxtrot", "Delta", "Charlie"])
emp8 = FactoryWorker(15.00, "Alyssa", "Hess", "000-00-4444", "2000-12-13", "2001-12-15", [emp3.firstName + ' ' + emp3.lastName], "Line Alpha")


# testing done ## Insert Testing
##print empList

empList.insertEmp(2, emp1)
empList.insertEmp(1, emp2)
empList.insertEmp(9, emp3)
empList.insertEmp(7, emp4)
empList.insertEmp(5, emp5)

##print empList

##
### testing done ## Append Testing
##
                  
empList.appendEmp(emp5)
empList.appendEmp(emp6)
empList.appendEmp(emp7)
empList.appendEmp(emp8)
empList.appendEmp(emp4)

##print empList
######
##
### testing done ## Getitem Testing
##

##print empList.__getitem__(10)
##print empList.__getitem__(1)
##print empList.__getitem__(5)
##print empList.__getitem__(0)
##print empList.__getitem__(-1)


### testing done ## Setitem Testing


##empList.__setitem__(0, Employee(5.00, "Jim", "Le", "111-11-1111", "1995-04-24", datetime.today()))
##print empList
##
##empList.__setitem__(7, Employee(15.00, "Bobby", "Green", "111-22-3333", "1987-09-10", datetime.today()))
##print empList
##
##empList.__setitem__(10, FactoryWorker(15.00, "Billy", "James", "777-88-9999", "2000-05-03", datetime.today(), [emp3.firstName + ' ' + emp3.lastName], "Line Alpha"))
##print empList
##
##empList.__setitem__(4, MaintenanceWorker(11.00, "Janie", "Wilson", "444-55-6666", "1964-02-24", datetime.today(), [emp3.firstName + ' ' + emp3.lastName], ["Alpha", "Bravo", "Charlie"]))
##print empList
##
##empList.__setitem__(-1, Employee(20.00, "Jane", "Lee", "123-45-6789", "1989-12-03"))
##print empList
##
##
### testing done ## Delitem Testing
##
##
##del empList[0]
##print empList
##                    
##del empList[5]
##print empList
##                    
##del empList[10]
##print empList
##                   
##del empList[11]
##print empList
##
##
### testing done ## SequentialSearch Testing
##
##
##print empList.sequentialSearch(2000.00, "salary")
##print empList.sequentialSearch(0.00, "salary")
##print empList.sequentialSearch("Tom", "firstName")
##print empList.sequentialSearch("Rufus", "firstName")
##print empList.sequentialSearch("Wilson", "lastName")
##print empList.sequentialSearch("Nguyen", "lastName")
##print empList.sequentialSearch("000-00-3333", "ssID")
##print empList.sequentialSearch("000-00-0000", "ssID")
##print empList.sequentialSearch("2000-05-03", "DOB")
##print empList.sequentialSearch("1963-10-02", "DOB")
##print empList.sequentialSearch("2001-12-15", "startDate")
##print empList.sequentialSearch("1964-10-01", "startDate")

##
### testing done ## MergeSort Testing
##

##empList.mergeSort("salary")
##print empList
##                    
##empList.mergeSort("firstName")
##print empList
##                    
##empList.mergeSort("lastName")
##print empList
##                    
##empList.mergeSort("ssID")
##print empList
##                    
##empList.mergeSort()
##print empList
####
##
### testing done ## InsertionSort Testing
##
##
##empList.insertionSort("salary")
##print empList
##                    
##print empList.insertionSort("firstName")
##print empList
##                    
##print empList.insertionSort("lastName")
##print empList
##                    
##print empList.insertionSort("ssID")
##print empList
##                    
##print empList.insertionSort()
##print empList

##
### testing done ## SelectionSort Testing
##
##
##empList.selectionSort("salary")
##print empList
##
##empList.selectionSort("firstName")
##print empList
##                    
####empList.selectionSort("lastName")
####print empList
######                    
##empList.selectionSort("ssID")
##print empList

empList.selectionSort()
print empList
##
##
### testing done ## BinarySearch Testing
##
####
##print empList.binarySearch(7500.00, "salary")
##print empList.binarySearch(0.00, "salary")
##
##print empList.binarySearch("Tom", "firstName")
##print empList.binarySearch("Rufus", "firstName")

##print empList.binarySearch("Wilson", "lastName")
##print empList.binarySearch("Nguyen", "lastName")
####
##print empList.binarySearch("000-00-3333", "ssID")
##print empList.binarySearch("000-00-0000", "ssID")
##


##                  
##  END OF TESTING  ##



employDB_backup = copy.deepcopy(empList)
