first="john"
last="smoth"
msg=f'{first} [{last}] is a coder'
print(msg)
  

# ==============================
# FORMATTED STRINGS (f-strings)
# ==============================
# RULE:
# Add 'f' before the string
# Put variables or expressions inside {}

# Syntax:
# f"normal text {variable/expression}"



# --------------------------------
# 1. Basic Variable Printing
# --------------------------------

name = "Varshith"
age = 19
branch = "CSE"

print(f"My name is {name}")
print(f"My age is {age}")
print(f"I am from {branch} branch")


# --------------------------------
# 2. Multiple Variables
# --------------------------------

cgpa = 9.5

print(f"{name} from {branch} has CGPA {cgpa}")


# --------------------------------
# 3. Expressions Inside {}
# --------------------------------

a = 10
b = 5

print(f"Addition = {a + b}")
print(f"Subtraction = {a - b}")
print(f"Multiplication = {a * b}")
print(f"Division = {a / b}")


# --------------------------------
# 4. Functions Inside {}
# --------------------------------

text = "python"

print(f"Uppercase = {text.upper()}")
print(f"Length = {len(text)}")


# --------------------------------
# 5. Float Formatting
# --------------------------------

pi = 3.1415926535

print(f"Pi value = {pi:.2f}")   # 2 decimal places
print(f"Pi value = {pi:.4f}")   # 4 decimal places


# --------------------------------
# 6. Adding Commas
# --------------------------------

salary = 1500000

print(f"Salary = ₹{salary:,}")


# --------------------------------
# 7. Leading Zeros
# --------------------------------

roll_no = 7

print(f"Roll Number = {roll_no:03}")


# --------------------------------
# 8. Text Alignment
# --------------------------------

word = "Python"

print(f"{word:<10} Left Align")
print(f"{word:>10} Right Align")
print(f"{word:^10} Center Align")


# --------------------------------
# 9. Multiline f-string
# --------------------------------

print(f"""
======== STUDENT DETAILS ========

Name   : {name}
Age    : {age}
Branch : {branch}
CGPA   : {cgpa}

=================================
""")


# --------------------------------
# 10. Debug Style
# --------------------------------

x = 100
y = 200

print(f"{x=}, {y=}")


# --------------------------------
# 11. Real Example
# --------------------------------

loan_amount = 500000
interest_rate = 8.5

print(f"""
======== LOAN DETAILS ========

Customer Name : {name}
Loan Amount   : ₹{loan_amount:,}
Interest Rate : {interest_rate}%

==============================
""")


# --------------------------------
# MEMORY TRICK
# --------------------------------

# f-string = Full sentence + variables inside {}

# Formula:
# f"normal sentence {variable}"

# Example:
# f"My name is {name}"
#
# Python replaces {} with variable values automatically.


