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
from employ import *

# This class is where all of the information from employ.py is kept and organized into a neat little easy to read list of employees.

class empDB: 

# This is where the class named empDB gets from employ.py all of the employees stored there and sets the item lst to a global variable.
# The parameter lst is set to default as an empty list if there isn't anything that comes back from the database that it is accessing.

    def __init__(self, lst= []):                  # this is complete
        self.lst = lst

# This organizes all of the information into a neat list that after each employee puts in a new line and returns it so that each
# employee is on a separate list from the others.

    def __str__(self):
        result = ''
        for elem in self.lst:
            result += str(elem) + "\n"
        return result

# This looks at all of the information that is in the list and returns the length of that whole list.

    def __len__(self):
        return len(self.lst)

# This one looks at the list and then adds a new employee to the main database list at the end.

    def appendEmp(self, emp=Employee()):
        self.lst += [emp]

# This looks at the list of employees in the database and inserts a new employee at index cell of the list of all of the employees.        

    # Do not use slices: code this yourself
    def insertEmp(self, index, emp=Employee()):
        new_list = []
        for i in range(0, index):
            new_list += [self.lst[i]]
        new_list += [emp]
        for j in range(index, len(self.lst)):
            new_list += [self.lst[j]]
        self.lst = new_list


    # Three standard methods to overload
    # Allows for bracket operator to be used to return indexth element of the empDB
    def __getitem__(self, index):                  # this is complete
        return self.lst[index]

    # Allows for bracket operator to be used to modify indexth element of the empDB, setting it to val
    def __setitem__(self, index, emp=Employee()):  # this is complete
        self.lst[index] = emp

# This looks at the list of employees and deletes a specific employee from the main list of employees depending on the index number
# that is given to it, it doesn't return anything it just modifies the list that is imported from the database.

    # Do not use del operator, but you may slice or bracket operator 
    def __delitem__(self, index):
        new_list = []
        for i in range(len(self.lst)):
            if i != index:
                new_list += [self.lst[i]]
        self.lst = new_list
                
# This looks at each part of the list of employees and checks to see if any of the items in the list are the same as the val
# that is being searched for.  If the val is found within the list of employees it will return the cell number of the val that
# was found if the val is not found within the list of employees it will return a -1.
# I have modified the given sequential search to accept the attribute of anything that is passed in on the call for the function.
# The parameter called attrib takes in any attribute contained in Employee and performs the search on the attribute that is entered, then returns
# the cell number of the given attribute that is found in the list of employees that is passed through the search or -1 if the attribute
# is not found in the list of employees. The default attribute is set to lastName, so if nothing is entered it will resort to that.


    # For now search on the attribute "lastName", later we will search on any attribute using: getattr(object, attrib[, defaultAttrib]) 
    def sequentialSearch(self, val, attrib = "lastName"):
        for i in range(len(self.lst)):
            if getattr(self.lst[i], attrib) == val:
                return i
        if getattr(self.lst[i], attrib) != val:
            return -1
        

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

    # For now sort on the attribute "lastName", (ie: sort by last name)
    #   Later we will sort on any attribute using: getattr(object, attrib[, defaultAttrib])
    def mergeSort(self): # split in half  then in half all the way til there is just one card in each half.  with the extra one if odd number goes to the left always 
        pass

# This goes through a sorted list of employees and checks the attribute parameter that is entered in the call for it and checks the value that is
# entered as well to see if it is in the sorted list if so it will return the cell
# number that the searched attribute appears, if it does not appear in the list for that attribute it will return a -1.  
# The default attribute for the search is set to lastName.
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



## A start on testing :
empList = empDB()
NUM_EMPS = 10
for i in range(NUM_EMPS):
    SSstring =  "111-22-120" + str(i)
    empList.appendEmp(Employee(4000.00,"Employee", str(NUM_EMPS-i-1), SSstring, datetime.fromordinal(1), datetime.today() ))
    #print empList[i].lastName

##print empList
a = Manager(5000.00, "Tom", "Cruise", "000-00-1234", "1934-10-25", datetime.fromordinal(1), datetime.today())
b = Manager(2000.00, "Jane", "Tom", "000-00-1111", "1934-10-25", datetime.fromordinal(1), datetime.today())
c = Manager(00.00, "John", "Doe", "000-00-2222", "1934-10-25", datetime.fromordinal(1), datetime.today())

empList.insertEmp(2, a)
empList.insertEmp(1, b)
empList.insertEmp(9, c)
print empList

##del empList[2]
##print empList

print empList.sequentialSearch("111-22-1202", "ssID")

empList.selectionSort("ssID")
print empList

print empList.binarySearch("111-22-1203", "ssID")


employDB_backup = copy.deepcopy(empList)

## More testing after you fill in some methods:
##print empList[5]
##empList[5].salary = 2500.0
##print empList[5]
##print
##
##empList.selectionSort()
##print empList
##
##empList.selectionSort("startDate")
##print empList
##
##empList[9] = AdminAssistant(25, "Sarah", "James", "111-22-1234", datetime.fromordinal(1), datetime.today(), 'Hwang', "CS" )
##print empList[9]
##print
##
##empList.appendEmp(EmpHourly())
##print empList[10]
##print
##empList.appendEmp(Manager(4900, "Sophie", "Hwang", "111-22-1267", datetime.fromordinal(1), datetime.today() ) )
print empList[11]
print
##empList.appendEmp(AdminAssistant(25, "Juan", "Ortiz", "111-22-1239", datetime.fromordinal(1), datetime.today(), 'Hwang', "CS" ))
##print empList[12]
##print
##
##print employDB_backup
##print empList
##
