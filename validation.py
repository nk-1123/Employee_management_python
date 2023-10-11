import re

def validateName(name):
    temp = name.split(" ")

    for i in temp:
        if i.isalpha() and i.istitle():  #to check if name is string and capitalised
            return True
        return False


def validateEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
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
    temp=re.fullmatch('[7-9][0-9]{9}',contact) #returns match object only if full pattern matches else returns none.
    if temp!=None:
        return True
    return False

def validateCity(city):
    if city.isalpha():
        return True
    return False

def validateDOB(dob):
    pattern_str = r'^\d{2}-\d{2}-\d{4}$'
    if re.match(pattern_str, dob):
        return True
    return False

def validateDOJ(doj):
    return validateDOB(doj) #to reduce code redundancy

def validateDeptName(dept, EmpList):
    for i in EmpList:
        if i.dept == dept:
            return True
    return False 

def validateDesignation(designation, EmpList): 
    for i in EmpList:
        if i.designation == designation:
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
    if rating.isdigit() and int(rating) < 6:
        return True
    return False
