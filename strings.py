#we can use doth "" and '' to declare a string . if the string have any apostapy or something prefer"" orelse it will cause error
course="python course for beginners"
print(course)
course1="python course for begineer's"
print(course1)
course3='python for "beginerrs"'
print(course3)
#for multiple lines string '''  '''

course='''hello
welcome to microsoft'''
print(course)

course="python for beginners"
#index:  012345
#index..-4-3-2-1
print(course[0])
print(course[-3])
print(course[0:3])#print from index 0 to index 2 suppose from[a:b] then start from a till b-1
#if no end then till end will print
print(course[1:])

first="john"
last="smith"
message=first+'['+last+']'+'is a coder'
print(message)