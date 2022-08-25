#The program takes a string as input and outputs a dictionary, which represents the letter count.
text = input()
dict = {}
for a in text:
    z=text.count(a)
    dict[a]=z
print(dict)
