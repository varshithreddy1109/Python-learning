try:
    age= int(input("age"))
    print(age)
except ValueError:
    print("invalid value")

    #using try expect see that the program do not crash due to error