# the Hermon of drinking water
angll = input("is Angll active?\nyes\tno\n")

# check if you are thirsty
if angll == "yes":
    print("_"*34)
    print()
    print("Search for water around you\n")
    do_find = input("Do you find water?\nyes\tno\n")
    if do_find == "yes":
        print("_"*34)
        print()
        print("Say besm Allah and drink water")
    else:
        print("_"*34)
        print()
        print("Go to the kitchen and get some water.")
else:
    print("_"*34)
    print()
    print("No need to drink.water")


