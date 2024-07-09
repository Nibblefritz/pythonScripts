places = ["New Orleans", "France", "Alaska", "Chicago", "Germany"]

print(f"unsorted:{places}")
print(f"sorted:{sorted(places)}")
print(f"unsorted:{places}")
print(f"sorted in reverse alphabetical, but not altered original:{sorted(places, reverse=True)}")
print(f"unsorted:{places}")
places.reverse()
print(f"sorted in reverse original order, altered original:{places}")
places.sort()
print(f"sorted alphabetical and altered original:{places}")
places.reverse()
print(f"sorted in reverse alphabetical order, altered original:{places}")



