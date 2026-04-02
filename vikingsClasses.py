import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking

# class Viking(Soldier):
#     def __init__(self, name, health, strength):
#         # your code here

#     def battleCry(self):
#         # your code here

#     def receiveDamage(self, damage):
#         # your code here

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"    

# Davicente

class War():
    def __init__(self):
        # your code here
        pass
    def addViking(self, viking):
        # your code here
        pass
    
    def addSaxon(self, saxon):
        # your code here
        pass

    def vikingAttack(self):
        # your code here
        pass

    def saxonAttack(self):
        # your code here
        pass

    def showStatus(self):
        # your code here
        pass
    

