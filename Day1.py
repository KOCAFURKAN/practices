def Procces():
    print("Welcome to Band Name Creator!")
    firstWord=input("Give me a mighty word! \n")
    print("Hıhı")
    secondWord=input("Give me a second mighty word mortal!\n")
    print("I decided! Here is your chosen band name!"+firstWord+" "+secondWord)
    retry=input("Do you wish to retry?y/n")
    if retry=="y":
        Procces()
    else:
        quit()    
Procces()
