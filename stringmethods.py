course = "Python for Beginners" 
print(len(course))#length of a string
#uppercase
print(course.upper())#doesnt modify original string!!!
print(course)
print(course.lower())
#to find character or sequence of character
print(course.find("B"))#gives index and it is case sensitive !!! 
#replacing a charcter or sequnce of character
print(course.replace("Beginners","absolute beginners"))
print(course)
print("Python" in course)#boolean value

