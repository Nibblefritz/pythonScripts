# Tuples are defined with parenthesis instead of brackets
dimensions = (200, 50)
print("Original Dimensions")
print(dimensions[0])
print(dimensions[1])

#you can change items in a tuple
#dimensions[0] = 250
#   File "/Users/kyle/Library/Mobile Documents/com~apple~CloudDocs/Code/pythonScripts/PythonCrashCourse/Chapter_04/tuples.py", line 7, in <module>
#    dimensions[0] = 250
#    ~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment

# you can't modify a tuple but you can reassign the tuple
dimensions = (400, 100)
print("\nModified Dimensions")
for dimension in dimensions:
    print(dimension)