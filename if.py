spiecies = "cat"

if spiecies == "cat":
    print("Yep, it's a cat.")

spiecies2 = "dog"

if spiecies2 == "cat":
    print("Yep, it's a cat.")
elif spiecies2 == "dog":
    print("Yep, it's a dog.")

full_name = "Billy Joel"

if full_name == "Billy" + " " + "Joel":
    print ("full name is in fact: " + full_name)
else:
    print ("full name is not Billy Joel.")

number = 3

if number == 1:
    print("number is 1")
elif number != 1:
    print("number equals 3")
else:
    print("NaN")