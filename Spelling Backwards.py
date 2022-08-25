#Given a string as input, the program uses recursion to output each letter of the strings in reverse order, on a new line.
def spell(txt):
    if txt == "":
        return txt
    else:
        return spell(txt[1:]) +'\n'+txt[0]
txt = input()
print(spell(txt))
