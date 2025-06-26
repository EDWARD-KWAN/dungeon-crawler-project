import  random, math, time 

class entity:
 def __init__(self,name, health, damage):
  self.name = name
  self.health = health
  self.damage = damage

 def alive(self):
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
 
 def attacks(self, other):
  total_damage = self.damage
  if self.equipment:
   total_damage *= self.equipment.damagemult # time the total damage
   print(f"{self.name} attacks with {self.equipment.name} for {total_damage} damage!")
   other.take_damage(total_damage)
   
  if not other.alive():
   self.score += 1 # score/0 + 1
   print(f"{other.name} is defeated! Score: {self.score}")
  
  
class equipment:
 def __init__(self, name, damagemult):
  self.name = name
  self.damagemult = damagemult
sword= equipment('sword', 2)
dagger= equipment('dagger',3)
beserk = equipment('fire', 1)



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
        return player("Knight", 1000, 10, sword)
    elif select == 'B':
        return player("Assassin", 7000, 20, dagger)
    elif select == 'C':
        return player("Tank", 20000, 5, beserk)
    else:
        return None # no variable or nothing


def combat():

 enemys_list = enemy + bosses
 random.shuffle(enemys_list) # shuffle to new list

 for opponent in enemys_list:
   time.sleep(1)
   print(f'a {opponent.name} caught you')
   while opponent.alive() and player_set.alive(): # connect form line nine
    player_set.attacks(opponent)
    time.sleep(0) 
    if opponent.alive():
     opponent.attack(player_set)
     time.sleep(0) 
    if not player_set.alive():
     print("You have Varnish")
     return
    
   if not opponent.alive() == True:
     print(f'You defeat {opponent.name} \n continue your journey')



  
  


 
 
 

def menu ():
 print('''DUNGEON ATTACKER
 (A) Play
 (B) Continue Play
 (C) High Score
 (D) Exit''')
 while True:
  choose = input('choose: ').upper()
  if choose == 'A':
   create_game()
  elif choose == 'B':
   continue_play ()
  elif choose == 'C':
   pass
  elif choose == 'D':
   break
  else:
   print('error try again')
   menu()
  
def create_game ():
 
 global player_set # relearn global since i forgot global can be vesatile in all function
 while True:
  print('''Choose A Character
 (A) Knight
 (B) Dagger
 (C) Tank
 (D) Back to menu''')
  choose = (input('choose a class for your adventure: ')).upper()
  if choose in ['A', 'B', 'C']: # since there 3 option of choosing character from character preset 
                                # using elif as exit.
                                #by using in/or used shared behavior
                                #e.g selecting a,b,c for all behaviour
                                #but using  playerpreset(choose) can be useful for having a preset
                                # then have differewnt behavior such like 
                                #if and elif 
   player_set = playerpreset(choose)
   print(f"You selected {player_set.name}!")
   continue_play()
   break # stop while loop
  elif choose == 'D':
   menu()
  else:
   print("Invalid input. Try again.")


def continue_play ():
 if not player_set:
  print ('you dont have a player selected')
  return # dosen't continue to start combat(). will start error

 print (f'hello {player_set.name} your journey have process')
 combat()

player_set =None # found that using none as null value is good so it won't give me error to define

menu()