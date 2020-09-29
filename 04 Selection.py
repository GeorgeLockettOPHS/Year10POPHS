#Selection
#selection uses if/elif and else
#things peole get wrong are:
#1.Forgetting the colon
#2.Forgetting indentation
#3.Not understanding comparison
#operators ==

skycolour = "grey"

if skycolour == ("grey"):
    print("the sky is grey today, its going to rain")

print("Good bye!!!")

baby = input("has the baby been born yet? y or n?")

if baby == ("y"):
    print("congratulations")
else:
    print("call us when you have news")
    
food = "kebab"

if food == "kebab":
    print("ummmmm, my favourite!")
    print("i feel like saying it 100 times ...")
    print(100 * (food + "! "))
else:
    print("im hungry")
