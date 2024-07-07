first_name = "Kyle"
print(f"Hello {first_name}, would you like to learn some Python today?")

print(first_name.lower())
print(first_name.upper())
print(first_name.title())

famous_person = "Mark Twain"
quote = "Always obey your parents when they are present."
print(f"{famous_person} once wrote, \"{quote}\"")

name = "     Kyle Fifield     "
print(name.rstrip())
print(name.lstrip())
stripped_name = name.strip()

print(f"{stripped_name}\n\t{stripped_name}\n\t\t{stripped_name}")

filename = "test_file_name.txt"
print(filename.removesuffix(".txt"))

url = "https://www.example.com"
print(url.removeprefix("https://"))