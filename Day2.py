def Procces():
    print("Welcome to Tip Calculater!")
    total=float(input("How much total?\n"))
    tip=float(input("How much tip do you want to pay?\n"))
    person=float(input("How many people will pay?\n"))
    calculatedTip=(total/100.0)*tip
    total+=calculatedTip
    sum=total/person
    print("Every one must pay"+str(sum))
    retry=input("Do you wish to retry?y/n")
    if retry=="y":
        Procces()
    else:
        quit()    
Procces()
