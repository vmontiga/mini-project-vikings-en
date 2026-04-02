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

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns you All!"
        

    def receiveDamage(self, damage):
        self.damage -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

        
        
       

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        

    def receiveDamage(self, damage):
    
    pass
     

# Davicente

class War():
    def __init__(self):
       
        
    def addViking(self, viking):
        
    
    def addSaxon(self, saxon):
        
    
    def vikingAttack(self):
        

    def saxonAttack(self):
       

    def showStatus(self):
        
    pass
pass

