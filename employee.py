from validation import *
from utils import *

class Employee:
    def __init__(self, eid, name, email, sal, age, gender, contact, address, city, dob, doj, dept, designation, pan, adhaar, performance_rating):
        self.eid = eid
        self.name = name
        self.email = email
        self.sal = sal
        self.age = age
        self.gender = gender
        self.contact = contact
        self.address = address
        self.city = city
        self.dob = dob
        self.doj = doj
        self.dept = dept
        self.designation = designation
        self.pan = pan
        self.adhaar = adhaar
        self.performance_rating = performance_rating
    
    def display(self):
        print(self.eid, self.name, self.email, self.sal, self.age, self.gender, self.contact, self.address, self.city, self.dob, self.doj, self.dept, self.designation, self.pan, self.adhaar, self.performance_rating)

EmployeeList = []
    
while True:
    print("1. Press 1 to add Employee record ")
    print("2. Press 2 to display the record ")
    print("3. Press 3 to delete the record ")
    print("4. Press 4 to update the record ")
    print("5. Press 5 to search the record ")
    print("6. Press 6 to display the employee details with highest/lowest salary as per the input ") #merge both of these
    # print("7. Press 7 to display the employee details with lowest salary ") #isko hata
    print("7. Press 7 to display all Employees details from a specific department ")  #iska code likh
    print("8. Press 8 to display the best employees name from the entered department ") #yeh bhi
    print("9. Press 9 to exit ")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        eid = generateEmpID()
        name = input("Enter employee name: ")
        while True:
            if validateName(name):
                break
            else:
                print("Invalid name entered.")
        while True:
            email = input("Enter employee email: ")
            if(validateEmail(email)):
                break
            else:
                print("Invalid email entered.")
        while True:
            salary = int(input("Enter employee salary: "))
            if(validateSalary(salary)):
                break
            else:
                print("Invalid salary entered.")

                # age will automate
        while True:
            age = int(input("Enter employee age: "))
            if(validateAge(age)):
                break
            else:
                print("Invalid age entered.")

        while True:
            gender = input("Enter 'M' for male, 'F' for female or 'O' for others: ")
            if(validateGender(gender)):
                break
            else:
                print("Invalid gender entered.")

        while True:
            contact = int(input("Enter mobile number: "))
            if(validateContactNo(contact)):
                break
            else:
                print("Invalid mobile number entered.")

        address = input("Enter the address: ")

        while True:
            city = input("Enter city: ")
            if validateCity(city):
                break
            else:
                print("Invalid city entered.")

        while True:
            dob = input("Enter date of birth: ")
            if validateDOB(dob):
                break
            else:
                print("Invalid date entered.")
        while True:
            doj = input("Enter date of joining: ")
            if(validateDOJ(doj)):
                break
            else:
                print("Invalid date entered.")
        while True:
            dept = input("Enter the department: ")
            if(validateDeptName(dept, EmployeeList)): 
                break
            else:
                print("Invalid department entered.")
        while True:
            designation = input("Enter the designation: ")
            if(validateDesignation(designation, EmployeeList)): 
                break
            else:
                print("Invalid designation entered.")
        while True:
            pan = input("Enter the PAN ID: ")
            if(validatePan(pan)):
                break
            else:
                print("Invalid PAN ID entered.")
        while True:
            aadhaar = int(input("Enter the Aadhaar number: "))
            if(validateAadhaar(aadhaar)):
                break
            else:
                print("Invalid Aadhaar number entered.")
        while True:
            performance_rating = int(input("Enter the rating out of 5: "))
            if(validatePerformance(performance_rating)):
                break
            else:
                print("Invalid rating inserted.")

        print("Record inserted")
        obj = Employee(eid, name, email, salary, age, gender, contact, address, city, dob, doj, dept, designation, pan, aadhaar, performance_rating)
        EmployeeList.append(obj)


    elif choice == 2:
        for i in EmployeeList:
            i.display()


    elif choice == 3:
        inputID = int(input("Enter the employee ID for which the record has to be deleted: "))
        for i in EmployeeList:
            if i.id == inputID:
                EmployeeList.remove(i)
    elif choice == 4:
        while True:
            print("1. Enter 1 to update name of employee")
            print("2. Enter 2 to update address of employee")
            print("3. Enter 3 to update DOB of employee")
            print("4. Enter 4 to update salary of employee")
            print("5. Enter 5 to exit")
            updateChoice = int(input("Enter the option: "))
            inputID = int(input("Enter the id:"))
            if choice == 1:
                for i in EmployeeList:
                    if i.id == inputID:
                        updatedName = input("Enter the new name: ")
                        EmployeeList[i].name = updatedName
            elif choice == 2:
                for i in EmployeeList:
                    if i.id == inputID:
                        updatedAddress = input("Enter the new address: ")
                        EmployeeList[i].address = updatedAddress
            elif choice == 3:
                for i in EmployeeList:
                    if i.id == inputID:
                        updatedDOB = input("Enter the new date of birth: ")
                        EmployeeList[i].dob = updatedDOB
            elif choice == 4:
                print("1. Enter 1 to update the salary of specific employee by employee id.")
                print("2. Enter 2 to update the salary of all employees working ins specific department.")
                print("3. Enter 3 to update the salary of all employees")
                print("4. Enter 4 to exit")
                updateChoice = int(input("Enter the option: "))
                if choice == 1:
                    inputID = int(input("Enter the employee id: "))
                    for i in EmployeeList:
                        if i.id == inputID:
                            inputSalary = int(input("Enter the salary: "))
                            EmployeeList[i].salary = inputSalary
                elif choice == 2:
                    inputDept = input("Enter the department: ")
                    for i in EmployeeList:
                        if i.dept == inputDept:
                            inputSalary = int(input("Enter the salary: "))
                            EmployeeList[i].salary = inputSalary
                elif choice == 3:
                    inputSalary = int(input("Enter the salary: "))
                    for i in EmployeeList:
                        EmployeeList[i].salary = inputSalary
                elif choice == 4:
                    break
                else:
                    print("Invalid choice entered.")
            elif choice == 5:
                break
            else:
                print("Invalid choice")
    elif choice == 5:
        print("1. Enter 1 to search the details of specific employee by employee id")
        print("2. Enter 2 to search by employee name")
        print("3. Enter 3 to search by Department name")
        print("4. Enter 4 to exit")
        searchChoice = int(input("Enter the choice: "))
        if searchChoice == 1:
            inputID = int(input("Enter the employee ID: "))
            for i in EmployeeList:
                if i.id == inputID:
                    i.display()
                else:
                    print("Employee ID is invalid.")
        elif searchChoice == 2:
            inputName = input("Enter the employee name: ")
            for i in EmployeeList:
                if i.name == inputName:
                    i.display()
                else:
                    print("Employee name is invalid.")
        elif searchChoice == 3:
            inputDept = input("Enter the employee department: ")
            for i in EmployeeList:
                if i.dept == inputDept:
                    i.display()
                else:
                    print("Employee department is invalid.")
        elif searchChoice == 4:
            break
        else:
            print("Invalid search choice.")
    elif choice == 6:
        dept = input("Enter department name: ")
        print("Type 'min' to display the minimun salary: ")
        print("Type 'max' to display the minimun salary: ")
        sal = input("Enter your choice: ")
        SalaryList = []

        if sal == 'min':
            for i in EmployeeList:
                SalaryList.append(i.sal)
                minSal = min(SalaryList)
            print("Details of employees with minimum salary:")
            for i in EmployeeList:
                if i.sal == minSal:
                    i.display()
        elif sal == 'max':
            for i in EmployeeList:
                SalaryList.append(i.sal)
                maxSal = max(SalaryList)
            print("Details of employees with maximum salary:")
            for i in EmployeeList:
                if i.sal == maxSal:
                    i.display()
        else:
            print("invalid choice entered.")

    elif choice == 7:
        #print all dept name
        dept = input("Enter the department name: ")
        
        EmpDeptList = []
        for i in EmployeeList:
            if i.dept == dept:
                EmpDeptList.append(i.name)
        for i in EmpDeptList:
            print(EmpDeptList[i])


    elif choice == 8:
        dept = input("Enter the department name: ")
        print("Best Employee/s from ", dept, " department is/are: ")

        ratingList = []
        for i in EmployeeList:
            if i.dept == dept:
                ratingList.append(i.performance_rating)
        max_rating=max(ratingList)

        BestEmpList = [] #store name of best employees from a given dept
        for i in EmployeeList:
            if i.dept == dept and i.performance_rating == max_rating:
                BestEmpList.append(i.name)
        
        for i in BestEmpList:
            print(BestEmpList[i])

    
    elif choice == 9:
        print("Program terminated successfully.")
        break
    else:
        print("Invalid choice entered.")