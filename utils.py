from datetime import date
import random

def generateEmpID(): #to generate emp id
    return random.randrange(100, 199)

def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))