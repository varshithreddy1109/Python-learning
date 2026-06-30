names=['john','smith','dhoni','kohli']
print(names) #o/p: ['john', 'smith', 'dhoni', 'kohli']
print(names[0]) #john
print(names[1:3]) #['smith', 'dhoni']
print(names[-2])  #dhoni
print(names[:])   #['john', 'smith', 'dhoni', 'kohli']

#   modification of list

names[0]="king"
print(names)  #['king', 'smith', 'dhoni', 'kohli']

# Example largest number in the list

number = [3,1,4,8,10.5,2.5,10.55]
max=number[0]
for i in number :
    if i > max :
        max=i
print(f"the largest number is {max} i  this list {number}")

