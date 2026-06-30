guess=9

i=1

while i<=3 :
    g=input("Guess:")
    if guess == int(g) :
        print("YOU ARE CORRECT!!!")
        break #break is use to break the loop (i.e. the loop is terminated)
    
    i+=1
else :
       print("Sorry you failed")