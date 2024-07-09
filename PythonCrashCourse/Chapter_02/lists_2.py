guests = ["Thomas Monson", "Chicho Arango", "Abraham Lincoln"]

for person in guests:
    print(f"Hello, {person}. My name is Kyle, I'd like to invite you to my fabulous dinner party.")

print(f"\n{guests[2]} cannot make it to the party.\n")
guests[2] = "Brandon Sanderson"

for person in guests:
    print(f"Hello, {person}. My name is Kyle, I'd like to invite you to my fabulous dinner party.")

print("\n A bigger table has become available we can invite more guests.\n")

guests.insert(0, "Benjamin Franklin")
guests.insert(2, "Captain Moroni")
guests.append("Bruce Wayne")

for person in guests:
    print(f"Hello, {person}. My name is Kyle, I'd like to invite you to my fabulous dinner party.")

print("\n We can actually now only invite two people to dinner.\n")

# Using a for i in range from 0 to the length of the list -2 times, thus leaving two guests
for i in range(0, len(guests)-2):
    guests.pop()

for person in guests:
    print(f"Hello, {person}. My name is Kyle, I'd like to invite you to my fabulous dinner party.")

# Iteratively remove each item in the list. 
for i in range(0, len(guests)):
    if len(guests)==0:
        del guests[0]
    else:
        del guests[i-1]

print(guests)