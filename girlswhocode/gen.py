#imports the ability to get a random number
from random import*

#create the list of words you want to choose from
aList = ["Stringy Sam", "Chatty Chad", "Strapping Strap", "Meaty Meat"]
response = input("Would you like a fun name? (Y/N)")
while response != "N":
    if response == "Y":
        aRandomIndex = randint(0, len(aList)-1)
        print(aList[aRandomIndex])
    else:
        print("{} is an invalid input".format(response))
    response = input("Would you like a fun name? (Y/N)")
