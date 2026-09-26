i=1
while i<5:
    j=1
    count=0
    while(j<5):
        if j>=i :
            break

        if j%2==0 :
            j+=1
            continue
        print(i*j,end=" ")
        count+=1
        j+=1

    print(count,"printed")
    i+=1