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
        print(
            "Eid: ", self.eid,
            "Name: ", self.name,
            "Email: ", self.email,
            "Salary: ", self.sal, 
            "Age: ", self.age,
            "Gender: ", self.gender,
            "Contact: ", self.contact,
            "Address: ", self.address,
            "City: ", self.city,
            "DOB: ", self.dob,
            "DOJ: ", self.doj,
            "Department: ", self.dept,
            "Designation: ", self.designation,
            "PAN: ", self.pan,
            "Adhaar: ", self.adhaar,
            "Performance rating: ", self.performance_rating
            )

EmployeeList = []
    
while True:
    print("1. Press 1 to add Employee record ")
    print("2. Press 2 to display the record ")
    print("3. Press 3 to delete the record ")
    print("4. Press 4 to update the record ")
    print("5. Press 5 to search the record ")
    print("6. Press 6 to display the employee details with highest/lowest salary as per the input ") 
    print("7. Press 7 to display all Employees details from a specific department ")  
    print("8. Press 8 to display the best employees name from the entered department ") 
    print("9. Press 9 to exit ")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        eid = generateEmpID()
        while True:
            name = input("Enter employee name: ")
            if validateName(name):
                break
            else:
                print("Invalid name entered.")
                print("")
        while True:
            email = input("Enter employee email: ")
            if(validateEmail(email)):
                break
            else:
                print("Invalid email entered.")
                print("")
        while True:
            salary = int(input("Enter employee salary: "))
            if(validateSalary(salary)):
                break
            else:
                print("Invalid salary entered.")
                print("")

                
        while True:
            age = int(input("Enter employee age: "))
            if(validateAge(age)):
                break
            else:
                print("Invalid age entered.")
                print("")

        while True:
            gender = input("Enter 'M' for male, 'F' for female or 'O' for others: ")
            if(validateGender(gender)):
                break
            else:
                print("Invalid gender entered.")
                print("")

        while True:
            contact = input("Enter mobile number: ")
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
                print("")

        while True:
            dob = input("Enter date of birth: ")
            if validateDOB(dob):
                break
            else:
                print("Invalid date entered.")
                print("")
        while True:
            doj = input("Enter date of joining: ")
            if(validateDOJ(doj)):
                break
            else:
                print("Invalid date entered.")
                print("")
        while True:
            dept = input("Enter the department: ")
            if(validateDeptName(dept)): 
                break
            else:
                print("Invalid department entered.")
                print("")
        while True:
            designation = input("Enter the designation: ")
            if(validateDesignation(designation)): 
                break
            else:
                print("Invalid designation entered.")
                print("")
        while True:
            pan = input("Enter the PAN ID: ")
            if(validatePan(pan)):
                break
            else:
                print("Invalid PAN ID entered.")
                print("")
        while True:
            aadhaar = input("Enter the Aadhaar number: ")
            if(validateAadhaar(aadhaar)):
                break
            else:
                print("Invalid Aadhaar number entered.")
                print("")
        while True:
            performance_rating = int(input("Enter the rating out of 10: "))
            if(validatePerformance(performance_rating)):
                break
            else:
                print("Invalid rating inserted.")
                print("")

        print("Record inserted")
        obj = Employee(eid, name, email, salary, age, gender, contact, address, city, dob, doj, dept, designation, pan, aadhaar, performance_rating)
        EmployeeList.append(obj)


    elif choice == 2:
        for i in EmployeeList:
            i.display()


    elif choice == 3:
        inputID = int(input("Enter the employee ID for which the record has to be deleted: "))
        for i in EmployeeList:
            if i.eid == inputID:
                EmployeeList.remove(i)

    elif choice == 4:
        while True:
            print("1. Enter A to update name of employee")
            print("2. Enter B to update address of employee")
            print("3. Enter C to update DOB of employee")
            print("4. Enter D to update salary of employee")
            print("5. Enter E to go back")
            updateChoice = input("Enter the option: ")

            if updateChoice == 'A':
                inputID = int(input("Enter the id:"))
                for i in EmployeeList:
                    if i.eid == inputID:
                        updatedName = input("Enter the new name: ")
                        i.name = updatedName
                        print("Name successfully updated.")
                        print("")
                        
            elif updateChoice == 'B':
                inputID = int(input("Enter the id:"))
                for i in EmployeeList:
                    if i.eid == inputID:
                        updatedAddress = input("Enter the new address: ")
                        i.address = updatedAddress
                        print("Address successfully updated.")
                        print("")
                        
            elif updateChoice == 'C':
                inputID = int(input("Enter the id:"))
                for i in EmployeeList:
                    if i.eid == inputID:
                        updatedDOB = input("Enter the new date of birth: ")
                        i.dob = updatedDOB
                        print("DOB successfully updated.")
                        print("")
                        
            elif updateChoice == 'D':
                inputID = int(input("Enter the id:"))
                for i in EmployeeList:
                    if i.eid == inputID:
                        inputSalary = int(input("Enter the salary: "))
                        i.salary = inputSalary
                        print("Salary successfully updated.")
                        print("")
                        
            elif updateChoice == 'E':
                break
            else:
                print("Invalid choice")
                print('')

    elif choice == 5:
        print("1. Enter A to search the details of a employee by employee id")
        print("2. Enter B to search by employee name")
        print("3. Enter C to search by Department name")
        print("4. Enter D to exit")
        searchChoice = input("Enter the choice: ")
        if searchChoice == 'A':
            inputID = int(input("Enter the employee ID: "))
            for i in EmployeeList:
                if i.eid == inputID:
                    i.display()
                else:
                    print("Employee ID is invalid.")
                    print("")
        elif searchChoice == 'B':
            inputName = input("Enter the employee name: ")
            for i in EmployeeList:
                if i.name == inputName:
                    i.display()
                else:
                    print("Employee name is invalid.")
                    print("")
        elif searchChoice == 'C':
            inputDept = input("Enter the employee department: ")
            for i in EmployeeList:
                if i.dept == inputDept:
                    i.display()
                else:
                    print("Employee department is invalid.")
                    print("")
        elif searchChoice == 'D':
            break
        else:
            print("Invalid search choice.")
            print("")

    elif choice == 6:
        dept = input("Enter department name: ")
        print("Type 'min' to display the minimun salary: ")
        print("Type 'max' to display the minimun salary: ")
        sal = int(input("Enter your choice: "))
        SalaryList = []

        if sal == 'min':
            for i in EmployeeList:
                SalaryList.append(i.sal) 
                minSal = min(SalaryList)
            print("Details of employees with minimum salary:")
            for i in EmployeeList:
                if i.sal == minSal:
                    i.display()
                    print('')
        elif sal == 'max':
            for i in EmployeeList:
                SalaryList.append(i.sal) 
                maxSal = max(SalaryList)
            print("Details of employees with maximum salary:")
            for i in EmployeeList:
                if i.sal == maxSal:
                    i.display()
                    print('')
        else:
            print("invalid choice entered.")
            print('')

    elif choice == 7:
        #print all dept name
        dept = input("Enter the department name: ")
        
        EmpDeptList = []
        for i in EmployeeList:
            if i.dept == dept:
                EmpDeptList.append(i.name)
        if len(EmpDeptList) != 0:
            for i in EmpDeptList:
                print(i)
        else:
            print("NO employees present in this department")
        print('')


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
        if(len(BestEmpList) != 0):
            for i in BestEmpList:
                print(i)
        else:
            print("No Employees present in this department")
            print("")

    elif choice == 9:
        print("Program terminated successfully.")
        break
    
    else:
        print("Invalid choice entered.")
