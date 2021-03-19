class GameCharacter:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
        self.slash = lambda: print("slash")


x = GameCharacter(health=532.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)


def t():
    print("armor")


x.armor = t
print(type(x.armor))
x.slash()
