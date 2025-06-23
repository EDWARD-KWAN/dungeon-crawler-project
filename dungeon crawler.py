import  random, math, time 

class entity:
 def __init__(self,name, health, damage):
  self.name = name
  self.health = health
  self.damage = damage

 def is_alive(self):
  return self.health > 0

 def take_damage(self, amount):
  self.health -= amount # damage amount
  print(f"{self.name} took {amount} damage. Remaining health: {self.health}")

 def attack(self, other): # other user /enemy
  print(f"{self.name} attacks {other.name} for {self.damage} damage!")
  other.take_damage(self.damage)

  
class player (entity):
 def __init__(self, name, health, damage,equipment):
  super().__init__(name, health, damage)
  self.equipment = equipment
  self.score = 0 # set the score, cannot be an attribute
 
 def attack(self, other):
  total_damage = self.damage
  if self.equipment:
   total_damage *= self.equipment.damagemult
   print(f"{self.name} attacks with {self.equipment.name if self.equipment else 'no weapon'} for {total_damage} damage!")
   other.take_damage(total_damage)
  if not other.is_alive():
   self.score += 1 # score/0 + 1
  print(f"{other.name} is defeated! Score: {self.score}")
  
class equipment:
 def __init__(self, name, damagemult):
  self.name = name
  self.damagemult = damagemult
sword= equipment('sword', 5)
dagger= equipment('sword',10)
beserk = equipment('fire', 3)


class enemies(entity):
 def __init__(self, name, health, damage):
  super().__init__(name, health, damage)

 
class boss(entity):
 def __init__(self, name, health, damage):
  super().__init__( name, health, damage)


enemy = [
    enemies("Goblin", 30, 5),
    enemies("Dark Knight", 50, 10),
    enemies("Warlord", 70, 15)
]
bosses = [
    boss("Dragon", 100, 20),
    boss("King", 150, 25),
    boss("Goliath", 200, 30),
    boss("God", 500, 50)
]
def playerpreset(select): # return to this  playerpreset(choice). this would be used in new game selection
                          # this to make it more easier
    if select == 'A':
        return player("Knight", 100, 10, sword)
    elif select == 'B':
        return player("Assassin", 70, 20, dagger)
    elif select == 'C':
        return player("Tank", 200, 5, beserk)
    else:
        return None
# this can be used 

def map()
 
 

def menu ():
 '''DUNGEON ATTACKER
 (A) Play
 (B) Continue Play
 (C) High Score
 (D) Exit'''
 while True:
  choose = input('choose').upper
  if choose == 'A':
   create_game()
  elif choose == 'B':
   continue_play ()
  elif choose == 'C':
   high_score()
  elif choose == 'D':
   break
  else:
   print('error try again')
   menu()
  
def create_game ():
 while True:
  
  '''Choose A Character
 (A) Knight
 (B) Dagger
 (C) Tank
 (D) Back to menu'''
  choose = (input('choose a class for your adventure')).upper
  if choose in ['A', 'B', 'C']: # since there 3 option of choosing character from character preset 
                                # using elif as exit.
                                #by using in/or used shared behavior
                                #e.g selecting a,b,c for all behaviour
                                #but using  playerpreset(choose) can be useful for having a preset
                                # then have differewnt behavior such like 
                                #if and elif 
   player = playerpreset(choose)
   print(f"You selected {player.name}!")
   continue_play()
   break # stop while loop
  elif choose == 'D':
   menu()
  else:
   print("Invalid input. Try again.")


def continue_play ():
 if 

def high_score ():


