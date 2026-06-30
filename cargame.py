i = 0

while i!=3 :
    x=input()
    x=x.lower()
    if x=="help" :
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif x=="start" :
        print("Car started ... Ready to go !")
    elif x == "stop" :
        print("Car stopped.")
    elif x == "quit" :
        print(" ")
        i=3
    else :
        print("I don't understand that...")
