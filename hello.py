
# STUDENT PROFILE MANAGEMENT SYSTEM

# 1. Display application title
print("====================================")
print("   STUDENT PROFILE MANAGEMENT SYSTEM")
print("====================================")

# 2. Collect student information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
college = input("Enter your college name: ")

# 3. Display student information
print("\n========== STUDENT PROFILE ==========")

print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age)
# Calculate year of birth
current_year = 2026
birth_year = current_year - age

print("Year of Birth:", birth_year)
print("Course:", course)
print("College:", college)

print("====================================")
print("Student registration completed!")

# 4. Classify student by age

if age < 13:
    print("Age Category: Child")

elif age < 18:
    print("Age Category: Teenager")

elif age <= 25:
    print("Age Category: Young Adult")

elif age <= 59:
    print("Age Category: Adult")

else:
    print("Age Category: Senior Citizen")

# First Python function

def welcome_message():
    print("==============================")
    print("WELCOME TO STUDENT MANAGEMENT")
    print("==============================")

# Calling the function
welcome_message()

# Function with two parameters

def student_details(name, course):
    print("Student Name:", name)
    print("Student Course:", course)

# Calling the function
student_details("Ibrahim Kamani", "Computer Science")

# Function to calculate year of birth

def calculate_birth_year(age):
    current_year = 2026
    birth_year = current_year - age
    return birth_year

# Call the function
year = calculate_birth_year(21)

print("Student Birth Year:", year)

