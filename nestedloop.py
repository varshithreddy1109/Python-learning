for x in range(5) :
    for y in range(3) :       #inner loop
        print(f'({x},{y})')

'''
                 to print this pattern 
                 *****
                 **
                 *****
                 **
                 **
'''

list = [5,2,5,2,2]

for i in list :
    for j in range(i) :
        print("X" ,end=" ")
    print()

#in first loop i will store the value of list[0] and so on 