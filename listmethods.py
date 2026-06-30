numbers = [5,2,1,7,4,4,7,99,5,66]
#adding at end of the list
numbers.append(20)
print(numbers)
#adding at a particular position
numbers.insert(1,55)
print(numbers)
#to remove a item
numbers.remove(55)
print(numbers)
#to clear entire list
#numbers.clear()
#to clear last element of the list
numbers.pop()
print(numbers)
#to check existence of a element
print(numbers.index(2)) #returns the index and if element ius not present then it will show a error
#or 
print(5 in numbers)
#to count how many times a element is present 
print(numbers.count(5))
#to sort the list
numbers.sort()
print(numbers)
#to keep in desending first sort then use revese()
#to get a copy of our list
numbers2=numbers.copy()
numbers.append(693)
print(numbers2)
print(numbers)

print(f'before deleting duplicates{numbers}')
#remove duplicates in a list(excerise)
for item in numbers:
    while numbers.count(item)!=1:
        numbers.remove(item)

print(f'after deleting duplicates{numbers}')