name=input("What is your name:")
colour=input("Your favorite colour")
print("Hi "+name)#concatination of the two strings "hi" and name
print("Hi ",name)#results in same output as that in concatination
print(name+" likes "+colour)

#input() always returns the value as string so it is important to mention the datatype in ehich we want input
birth_year=input("Enter date of birth: ")
#age=2026-birth_year  here birth_year is a string and 2026 is an int so error occurs
age=2026-int(birth_year)
print(birth_year)
print(age)
print(type(age))#print the type



