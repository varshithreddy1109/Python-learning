weight=input("Enter weight")
typee=input("IN (K)g's or (P)ounds")

if typee == 'k' or typee == 'K':
    print(f'you are {int(weight)*2.205} pounds')
elif typee == 'p' or typee == 'P' :
    print(f"you are {0.45*int(weight)} Kg's")

72