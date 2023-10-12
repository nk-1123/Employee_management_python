import re
from datetime import datetime


DeptList = ['HR', 'IT', 'Sales', 'Finance']
DesigList = ['Manager', 'Vice President', 'Secratory', 'Intern', 'Software Devloper']

def validateName(name):
    temp = name.split(" ")

    for i in temp:
        if i.isalpha() and i.istitle():  #to check if name is alphabets and is capitalised
            return True
        return False


def validateEmail(email):
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$'
    if (re.fullmatch(regex, email)):
        return True
    return False

def validateSalary(salary):
    if salary>0:
        return True
    return False


def validateAge(age):
    if age>=18 and age<=60:
        return True
    return False

def validateGender(gender):
    if gender == 'M' or gender == 'F' or gender == 'O':
        return True
    return False

def validateContactNo(contact):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}") #compile returns the specified source as a code object, ready to be executed
    if Pattern.match(contact) != None:
        return True
    return False 

def validateCity(city):
    if city.isalpha():
        return True
    return False

def validateDOB(dob):
    format = "%d-%m-%Y"
 
    try:
        datetime.strptime(dob, format)
        return True
    except ValueError:
        return False
    

def validateDOJ(doj):
    return validateDOB(doj) #to reduce code redundancy

def validateDeptName(dept):
    for i in DeptList:
        if i == dept:
            return True
    return False 

def validateDesignation(designation): 
    for i in DesigList:
        if i == designation:
            return True
    return False 

def validatePan(pan):
    if len(pan)!=10:
        return False
    else: 
        for i in range(10):
            if(i<5 or i==9):
                if pan[i].isalpha() == False:
                    return False
            elif(i>=5 and i<9):
                if pan[i].isdigit() == False:
                    return False
    return True

def validateAadhaar(adhaar):
    if len(adhaar)!=12 and adhaar.isdigit() == False:
        return False
    return True

def validatePerformance(rating):
    if rating < 11:
        return True
    return False
