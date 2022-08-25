#The given code declares a Player class, with its attributes and an intro() method.
#Then creates a Player object with the corresponding values and calls the intro() method of that object.
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")
name=str(input())
level=input()
player=Player(name,level)
player.intro()
