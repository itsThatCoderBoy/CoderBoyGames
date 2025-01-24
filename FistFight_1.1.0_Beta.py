##MADE BY CODERBOY.

import os
import random
import shelve
import time

##while True:
##    rand = random.randint(1,3)
##    if rand == 1:
##        print('No')
##    if rand == 2:
##        print('Nope')
##    if rand == 3:
##        print('Nuh-Uh')

hp = 100
maxhp = 100
attk = 15
crit = 0.15
defense = 0.0
xp = 0
level = 1
pclass = 'placeholder'
gold = 0
xpgoal = 5
name = ''
critchance = 20
weapon = 'Fist'
wins = 0
armor = "None"
totalwins = 0
totallosses = 0
highestlevel = 0
pets = 0
concious = True
econcious = True
poisoned = False
epoisoned = False
unconciouscounter = 0
eunconciouscounter = 0
epoisoncounter = 0
poisoncounter = 0
devTools = False
petname = ""
versionsProgrammed = "3.11.4 - 3.12.2, Replit Online"
loadedgame = []
buffs = [0, 0, 0, 0, 0, 0]
played = False
bossFightTime = False
version = '1.1.0 Beta'
tag = ''
atkUpgradeBar = "[|----|]"
hpUpgradeBar = "[|----|]"
defeUpgradeBar = "[|----|]"
critUpgradeBar = "[|----|]"
inventory = [
    'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'None', 'None'
]
experiments = 1


class Enemy:

  def __init__(self, name, atk, hp, critdam, maxhp, defe, critchance):
    self.name = name
    self.atk = atk
    self.hp = hp
    self.critdam = critdam
    self.maxhp = maxhp
    self.defe = defe
    self.critchance = critchance
    #self.petchance = petchance


sline = Enemy('Sline', 17, 100, 0.15, 100, 0.0, 0)
smake = Enemy('Smake', 20, 89, 0.13, 89, 0.0, 0)
skeletom = Enemy('Skeletom', 15, 105, 0.1, 105, 0.0, 0)
LEAF = Enemy('LEAF', 17, 115, 0.17, 105, 0.0, 0)
nagic = Enemy('Nagic', 17, 100, 0.15, 100, 0.0, 0)
platypus = Enemy('Platypus', 18, 90, 0.12, 90, 0.0, 0)
penguilian = Enemy('Penguilian', 19, 110, 0.1, 110, 0.01, 0)
bossWizard = Enemy('Strange Magic Man', 30, 200, 0.25, 200, 0.05, 5)


class Weapon:

  def __init__(self, name, dmg, cost, critchanceup):
    self.name = name
    self.dmg = dmg
    self.cost = cost
    self.critchanceup = critchanceup

sword = Weapon('Sword', 10, 40, 1)
mace = Weapon('Mace', 8, 30, 1)
dagger = Weapon('Dagger', 5, 25, 1)
staff = Weapon('Staff', 12, 50, 1)
bow = Weapon('Oddly Rusty Bow', 7, 35, 1)
leaf = Weapon('LEAF', 100, 200, 3)

print('[|-----|]')
time.sleep(0.5)
print('[|=----|]')
time.sleep(0.5)
print('[|==---|]')
time.sleep(0.5)
print('[|===--|]')
time.sleep(0.5)
print('[|====-|]')
time.sleep(0.5)
print('[|=====|]')
print('Load Complete!')
print()
time.sleep(0.5)
print('CoderBoy presents...')
time.sleep(1)
print(f'Fist Fight {version}!')
print()
time.sleep(1)
print('New game (new) or load game (load)?')
choice = input()

if choice == 'load':
  print()
  print("What is you tag? Include @ symbol. Remember, case does matter!")
  tag = input()
  saveFileShelf = shelve.open(f'saveFileFistFight_{tag}')
  hp = saveFileShelf['hp']
  maxhp = saveFileShelf['maxhp']
  attk = saveFileShelf['attk']
  crit = saveFileShelf['crit']
  defense = saveFileShelf['defense']
  pclass = saveFileShelf['pclass']
  gold = saveFileShelf['gold']
  name = saveFileShelf['name']
  totalwins = saveFileShelf['totalwins']
  totallosses = saveFileShelf['totallosses']
  highestlevel = saveFileShelf['highestlevel']
  pets = saveFileShelf['pets']
  petname = saveFileShelf['petname']
  experiments = saveFileShelf['experiments']
  inventory[0] = saveFileShelf['inventory[0]']
  inventory[1] = saveFileShelf['inventory[1]']
  inventory[2] = saveFileShelf['inventory[2]']
  inventory[3] = saveFileShelf['inventory[3]']
  inventory[4] = saveFileShelf['inventory[4]']
  inventory[5] = saveFileShelf['inventory[5]']
  inventory[6] = saveFileShelf['inventory[6]']
  inventory[7] = saveFileShelf['inventory[7]']
  sline.name = saveFileShelf['sline.name']
  sline.atk = saveFileShelf['sline.atk']
  sline.hp = saveFileShelf['sline.hp']
  sline.critdam = saveFileShelf['sline.critdam']
  sline.maxhp = saveFileShelf['sline.maxhp']
  sline.defe = saveFileShelf['sline.defe']
  sline.critchance = saveFileShelf['sline.critchance']
  smake.name = saveFileShelf['smake.name']
  smake.atk = saveFileShelf['smake.atk']
  smake.hp = saveFileShelf['smake.hp']
  smake.critdam = saveFileShelf['smake.critdam']
  smake.maxhp = saveFileShelf['smake.maxhp']
  smake.defe = saveFileShelf['smake.defe']
  smake.critchance = saveFileShelf['smake.critchance']
  skeletom.name = saveFileShelf['skeletom.name']
  skeletom.atk = saveFileShelf['skeletom.atk']
  skeletom.hp = saveFileShelf['skeletom.hp']
  skeletom.critdam = saveFileShelf['skeletom.critdam']
  skeletom.maxhp = saveFileShelf['skeletom.maxhp']
  skeletom.defe = saveFileShelf['skeletom.defe']
  skeletom.critchance = saveFileShelf['skeletom.critchance']
  LEAF.name = saveFileShelf['LEAF.name']
  LEAF.atk = saveFileShelf['LEAF.atk']
  LEAF.hp = saveFileShelf['LEAF.hp']
  LEAF.critdam = saveFileShelf['LEAF.critdam']
  LEAF.maxhp = saveFileShelf['LEAF.maxhp']
  LEAF.defe = saveFileShelf['LEAF.defe']
  LEAF.critchance = saveFileShelf['LEAF.critchance']
  nagic.name = saveFileShelf['nagic.name']
  nagic.atk = saveFileShelf['nagic.atk']
  nagic.hp = saveFileShelf['nagic.hp']
  nagic.critdam = saveFileShelf['nagic.critdam']
  nagic.maxhp = saveFileShelf['nagic.maxhp']
  nagic.defe = saveFileShelf['nagic.defe']
  nagic.critchance = saveFileShelf['nagic.critchance']
  platypus.name = saveFileShelf['platypus.name']
  platypus.atk = saveFileShelf['platypus.atk']
  platypus.hp = saveFileShelf['platypus.hp']
  platypus.critdam = saveFileShelf['platypus.critdam']
  platypus.maxhp = saveFileShelf['platypus.maxhp']
  platypus.defe = saveFileShelf['platypus.defe']
  platypus.critchance = saveFileShelf['platypus.critchance']
  penguilian.name = saveFileShelf['penguilian.name']
  penguilian.atk = saveFileShelf['penguilian.atk']
  penguilian.hp = saveFileShelf['penguilian.hp']
  penguilian.critdam = saveFileShelf['penguilian.critdam']
  penguilian.maxhp = saveFileShelf['penguilian.maxhp']
  penguilian.defe = saveFileShelf['penguilian.defe']
  penguilian.critchance = saveFileShelf['penguilian.critchance']
  atkUpgradeBar = saveFileShelf['atkUpgradeBar']
  hpUpgradeBar = saveFileShelf['hpUpgradeBar']
  defeUpgradeBar = saveFileShelf['defeUpgradeBar']
  critUpgradeBar = saveFileShelf['critUpgradeBar']
  weapon = saveFileShelf['weapon']  
  armor = saveFileShelf['armor']
  devTools = saveFileShelf['devTools']
  saveFileShelf.close()
  time.sleep(2)
  os.remove(f"saveFileFistFight_{tag}")
  ##os.remove(f"saveFileFistFight_{tag}.bak")
  ##os.remove(f"saveFileFistFight_{tag}.dir")
  print("The save file has been loaded and deleted.")

else:

  ##   print("Would you like to activate Experiments? They can be glitchy and usually have bugs! [It is recommended that PlayTesters activate this setting] y/n")
  ##    niput = input()
  ##
  ##    if niput == 'Y' or niput == 'y':
  ##        print()
  ##        print(f"You decided to turn on Experiments.")
  ##        experiments = 1
  ##
  ##    else:
  ##        print()
  ##        print(f"You decided not to activate Experiments.")
  ##        experiments = 0

  print(
      """What would you like your name to be? Name cannot include ' or " symbols."""
  )
  name = input()
  tag = f"@{name}"

  print(
      f"Your tag is {tag}. Remember this or write it down somewhere, because you need this to access a save!"
  )
  print()
  print(f"Welcome to Fist Fight, {name}!!")
  print()
  
  print(
      'What class would you like to be? different classes apply different traits. You can choose from Nage (nage), Kmight (kmight), Barbariam (barbariam), Wizard (wizard), or Fish (fish).'
  )
  loop = True

  while loop is True:
    niput = input()

    if niput == 'nage':
      print()
      print(
          'You chose to become a nage! Good choice. Being a nage buffs your attack, critical hit bonus, and defense.'
      )
      pclass = 'Nage'
      xpgoal = 7
      defense = 0.06
      attk = 17
      crit = 0.18
      loop = False

    elif niput == 'kmight':
      print()
      print(
          'You chose to become a kmight! Good choice. Being a kmight buffs your defense, attack, and health.'
      )
      pclass = 'Kmight'
      crit = 0.13
      maxhp = 105
      hp = 105
      defense = 0.05
      attk += 3
      loop = False

    elif niput == 'wizard':
      print()
      print(
          'You chose to become a wizard! Good choice. Being a wizard buffs your defense, crit chance, and crit damage.'
      )
      pclass = 'Wizard'
      crit = 0.13
      defe = 0.075
      critchance = 15
      loop = False

    elif niput == 'fish':
      print()
      print(
          'You chose to become a fish! Good choice. Being a fish buffs your attack, health, and critical hit damage.'
      )
      pclass = 'Fish'
      crit = 0.15
      maxhp = 110
      hp = 110
      loop = False

    elif niput == 'barbariam':
      print()
      print(
          'You chose to become a barbariam! Good choice. Being a barbariam buffs your critical hit chance, attack, and critical hit damage.'
      )
      pclass = 'Barbariam'
      maxhp = 95
      crit = 0.20
      critchance -= 2
      attk += 5
      loop = False

    elif niput == 'leaf':
      print('Please input the password. ________')
      pas = input()

      if pas == 'password':
        print('Please enter password #2. _________')
        passw = 'i am LEAF'
        pas = input()

        if pas == passw:
          print()
          print(
              'You chose to become a leaf! Good choice. Being a leaf makes you god!'
          )
          maxhp = 1000
          pclass = 'LEAF'
          hp = 1000
          defense = 0.60
          attk += 100
          loop = False

        else:
          print('HAHAHAHAHAHAHAHA >:)')

      else:
        print('Leaf me alone :(')
        print()

    else:
      print(
          'Please choose a valid class. You must choose nage, kmight barbariam, or fish.'
      )

print("This is you:")
print()

if name == 'human eater':
  print("""               *
._{}_. * </>
 |[]|/       *
  ||""")

elif name == 'capybara_eater':
  print("""     _{$$}_
    /|[]|
   /~~||""")

elif pclass == 'Nage':
  print(""" /\\
_{}_
|[]|
 ||""")

elif pclass == 'Kmight':
  print(""" __
/__\\
|[]|/
 ||""")

elif pclass == 'Wizard':
  print("""_/\\_
_{}_
|[]|
 ||""")

elif pclass == 'Fish':
  print("""  
  /\\
 |. |
<|  |
 /  \\
 \\/\\/""")

elif pclass == 'Barbariam':
  print(""" ._{}_.
 .|[]|.
   ||""")

elif pclass == 'LEAF':
  print("""  /\\
 / |
/..|
|__/
 !""")

print()

if name == 'human eater' or name == 'capybara_eater':
  print("Hello, developer! Since you are a developer, you have access to dev tools!")
  devTools = True

buffs = [xpgoal, defense, attk, crit, hp, maxhp, critchance]

print()
print('Welcome to the dungeon.')
print()
gameloop = True

while gameloop is True:
  hp = maxhp
  print()
  print('FIST FIGHT')
  print('Main Menu')
  print()
  print('Options:')
  print('Fight! (fight)')
  print('Blacksmith! (blacksmith) [IN PROGRESS]')

  if experiments == 1:
    print('Manage Inventory! (minventory)')

  else:
    print('This action is locked behind the Experiment setting.')

  if experiments == 1:
    print('Shop! (shop)')

  else:
    print('This action is locked behind the Experiment setting.')

  print('Stats! (stats)')
  print('Quit Game! (qgame)')
  print('Credits! (credits)')
  niput = input()
  print()

  if niput == 'fight' or niput == 'Fight' or niput == 'fight!' or niput == 'Fight!':
    loop = True

    while loop is True and level != 10:
      enemy = random.randint(1, 7)

      if enemy == 1:
        currentenemy = sline

      elif enemy == 2:
        currentenemy = smake

      elif enemy == 3:
        currentenemy = skeletom

      elif enemy == 4:
        currentenemy = LEAF

      elif enemy == 5:
        currentenemy = nagic

      elif enemy == 6:
        currentenemy = platypus

      elif enemy == 7:
        currentenemy = penguilian

      print(f'A wild {currentenemy.name} has appeared!')
      hp = maxhp
      currentenemy.hp = currentenemy.maxhp

      if wins == 10: currentenemy.hp += 10
      print()
      loop1 = True

      while loop1 is True:

        if loop1 is True:
          hp = int(hp)
          maxhp = int(maxhp)
          attk = int(attk)
          crit = float(crit)
          defense = float(defense)
          gold = int(gold)
          totalwins = int(totalwins)
          totallosses = int(totallosses)
          highestlevel = int(highestlevel)
          pets = int(pets)

          if currentenemy.hp <= 0:
            thing = random.randint(2, 5)
            xp += thing
            wins += 1
            totalwins += 1

            if level > highestlevel: highestlevel = level

            goldget = random.randint(1, 5)
            gold += goldget
            print(
                f'You won the battle! Congratulations! You got {thing} xp and {goldget} gold!'
            )

            if pclass == 'LEAF':
              print()
              print("I see that your class is LEAF...")
              time.sleep(2)
              print("Did you obtain this class legally? y/n")
              niput = input()

              if niput == 'y' or niput == 'Y':
                print("...")
                time.sleep(2)
                print("You LIE! HOW DARE YOU!")

              else:
                print()
                print("Thank you for telling the truth.")

              print()
              print("*^&!%##*&@^")
              print("pclass = 'Dirt-Poor Farmer'")
              pclass = "Dirt-Poor Farmer"
              print("attk = 2")
              attk = 2
              print("hp = 50")
              hp = 50
              maxhp = 50
              print('defense = 0.0')
              defense = 0.0
              print("weapon = 'The stub that used to be your hand before you lost it in 'a tractor accident''")
              weapon = "The stub that used to be your hand before you lost it in a 'tractor accident'"
              print("crit = 0.0")
              crit = 0.0
              print("name = Cheat")
              name = 'Cheat'
              tag = '@Cheat'
              print("dysentaryChance = True")
              dysentaryChance = True
              print("&^%#&**^&$^%#")

            if xp >= xpgoal:
              xp -= xpgoal
              xpgoal += 5
              level += 1
              sline.hp += 1
              sline.maxhp += 1
              smake.hp += 1
              smake.maxhp += 1
              skeletom.hp += 1
              skeletom.maxhp += 1
              LEAF.hp += 1
              LEAF.maxhp += 1
              platypus.hp += 1
              platypus.maxhp += 1
              nagic.hp += 1
              nagic.maxhp += 1
              penguilian.hp += 1
              penguilian.maxhp += 1
              sline.atk += 1
              smake.atk += 1
              skeletom.atk += 1
              LEAF.atk += 1
              platypus.atk += 1
              nagic.atk += 1
              penguilian.atk += 1
              sline.defe += 0.05
              smake.defe += 0.05
              skeletom.defe += 0.05
              LEAF.defe += 0.05
              platypus.defe += 0.05
              nagic.defe += 0.05
              penguilian.defe += 0.05
              sline.critchance -= 1
              smake.critchance -= 1
              skeletom.critchance -= 1
              LEAF.critchance -= 1
              platypus.critchance -= 1
              nagic.critchance -= 1
              penguilian.critchance -= 1

              print(f'You leveled up! Congrats! You are now level {level}!')
              print('You get a bonus upgrade!')
              print(f'Attack: {atkUpgradeBar} (attack)')
              print(f'Health: {hpUpgradeBar} (health')
              print(f'Defense: {defeUpgradeBar} (defense)')
              print(f'Critical hit chance: {critUpgradeBar} (crit)')

              niput = input()

              if niput == 'health' and hpUpgradeBar != "[|====|] (MAX)":
                maxhp += 3
                if hpUpgradeBar == "[|----|]":
                  hpUpgradeBar = "[|=---|]"
                elif hpUpgradeBar == "[|=---|]":
                  hpUpgradeBar = "[|==--|]"
                elif hpUpgradeBar == "[|==--|]":
                  hpUpgradeBar = "[|===-|]"
                elif hpUpgradeBar == "[|===-|]":
                  hpUpgradeBar = "[|====|] (MAX)"

              elif niput == 'attack' and atkUpgradeBar != "[|====|] (MAX)":
                attk += 3
                if atkUpgradeBar == "[|----|]":
                  atkUpgradeBar = "[|=---|]"
                elif atkUpgradeBar == "[|=---|]":
                  atkUpgradeBar = "[|==--|]"
                elif atkUpgradeBar == "[|==--|]":
                  atkUpgradeBar = "[|===-|]"
                elif atkUpgradeBar == "[|===-|]":
                  atkUpgradeBar = "[|====|] (MAX)"

              elif niput == 'defense' and defeUpgradeBar != "[|====|] (MAX)":
                defense += 0.01
                if defeUpgradeBar == "[|----|]":
                  defeUpgradeBar = "[|=---|]"
                elif defeUpgradeBar == "[|=---|]":
                  defeUpgradeBar = "[|==--|]"
                elif defeUpgradeBar == "[|==--|]":
                  defeUpgradeBar = "[|===-|]"
                elif defeUpgradeBar == "[|===-|]":
                  defeUpgradeBar = "[|====|] (MAX)"

              elif niput == 'crit' and critUpgradeBar != "[|====|] (MAX)":
                critchance -= 1
                if critUpgradeBar == "[|----|]":
                  critUpgradeBar = "[|=---|]"
                elif critUpgradeBar == "[|=---|]":
                  critUpgradeBar = "[|==--|]"
                elif critUpgradeBar == "[|==--|]":
                  critUpgradeBar = "[|===-|]"
                elif critUpgradeBar == "[|===-|]":
                  critUpgradeBar = "[|====|] (MAX)"

              elif atkUpgradeBar == "[|====|] (MAX)" or hpUpgradeBar == "[|====|] (MAX)" or critUpgradeBar == "[|====|] (MAX)" or defeUpgradeBar != "[|====|] (MAX)":
                print(
                    "This skill has already reached its maximum upgrade level."
                )

              else:
                print("That is not a valid action.")

            loop1 = False
            wins += 1

          elif hp <= 0:
            totallosses += 1
            print(f'You lost. :( You defeated {wins} enemies.')
            print(
                f'Would you like to play again? This cost 5 gold. You have {gold} gold.y/n'
            )
            loop2 = True

            while loop2 is True:
              niput = input()

              if niput == 'y' and gold >= 3 or niput == 'Y' and gold >= 3:
                gold -= 3
                loop2 = False

              else:
                print('Are you sure? y/n')
                niput = input()

                if niput == 'y' or niput == 'Y':
                  loop2 = False
                  loop1 = False
                  loop = False

                else:
                  print()
                  print('Would you like to play again? y/n')

          elif hp > 0 and currentenemy.hp > 0:
            ##hp = int(hp * 1000) / 1000
            ##currentenemy.hp = int(currentenemy.hp * 1000) / 1000

            if hp > maxhp: hp = maxhp

            if currentenemy.hp > currentenemy.maxhp:
              currentenemy.hp = currentenemy.maxhp
            currentenemy.hp = round(currentenemy.hp, 1)
            hp = round(hp, 1)
            print(
                f"Health: You: {hp}. {currentenemy.name}: {currentenemy.hp}.")
            print(
                'What will you do? You can heal, attack, or run away (h,a, or r)'
            )

            if currentenemy.hp <= 10 and level >= 2 and pets == 0 and experiments == 1:
              print('You can capture this enemy and make it your pet! (pet)')

            niput = input()
            print()

            if niput == 'attack' or niput == 'a':
              critc = random.randint(1, critchance)
              dmgvary = random.randint(1, 3)

              if critc == 1:
                critatk = attk * crit
                totalatk = critatk + attk
                edefe = totalatk * currentenemy.defe
                totalatk -= edefe
                totalatk = round(totalatk, 1)

                if dmgvary == 1:
                  totalatk += 1

                if dmgvary == 2:
                  totalatk -= 1

                if dmgvary == 3:
                  totalatk = totalatk

                currentenemy.hp -= totalatk
                print(
                    f'You got a critical hit! You did {totalatk} damage with your {weapon}.'
                )

              else:
                edefe = attk * currentenemy.defe
                totalatk = attk - edefe
                totalatk = round(totalatk)

                if dmgvary == 1:
                  totalatk += 1

                if dmgvary == 2:
                  totalatk -= 1

                if dmgvary == 3:
                  totalatk = totalatk

                currentenemy.hp -= totalatk
                print(
                    f'You attacked the {currentenemy.name} with your {weapon} and did {totalatk} damage.'
                )

            elif niput == 'heal' or niput == 'h':
              healamount = random.randint(40, 50)
              hp += healamount
              print(f'You healed yourself and healed {healamount} health.')

            elif niput == 'run away' or niput == 'r':
              print(
                  f'You decided to run away. You ended up at level {level} and you defeated {wins} enemies.'
              )
              print(
                  f'Would you like to play again? This cost 5 gold. You have {gold} gold.y/n'
              )
              loop2 = True

              while loop2 is True:
                niput = input()

                if niput == 'y' and gold >= 3 or niput == 'Y' and gold >= 3:
                  gold -= 3
                  loop2 = False

                else:
                  print('Are you sure? y/n')
                  niput = input()

                  if niput == 'y' or niput == 'Y':
                    loop2 = False
                    loop1 = False
                    loop = False

                  else:
                    print()
                    print('Would you like to play again? y/n')

            elif currentenemy.hp <= 10 and level >= 2 and niput == 'pet' and experiments == 1:
              getpet = random.randint(1, 3)

              if getpet == 1:
                print('You failed to tame the enemy.')

              else:
                print(
                    f'You successfully got a pet {currentenemy.name} that you can bring into future battles with you!'
                )
                currentenemy.hp = currentenemy.maxhp
                petname = currentenemy.name
                petstats = currentenemy
                pets = 1

            else:
              print('That is not a valid action.')

            if loop1 is True:
              print()
              rando = random.randint(1, 5)

              if currentenemy.hp < currentenemy.maxhp * 0.75 and rando == 1:
                healamount = random.randint(25, 35)
                print(f'The {currentenemy.name} healed {healamount} health!')
                currentenemy.hp += healamount

              else:
                ecritchance = 20
                ecritchance -= currentenemy.critchance
                cri = random.randint(1, ecritchance)
                dmgvary = random.randint(1, 3)

                if cri == 1:
                  critatk = currentenemy.atk * currentenemy.critdam
                  atk = critatk + currentenemy.atk
                  resist = atk * defense
                  atk -= resist
                  atk = round(atk, 1)

                  if dmgvary == 1:
                    atk += 1

                  if dmgvary == 2:
                    atk -= 1

                  if dmgvary == 3:
                    atk = atk

                  hp -= atk
                  print(
                      f'The {currentenemy.name} got a critical hit! They did {atk} damage.'
                  )

                else:
                  atk = currentenemy.atk
                  resist = atk * defense
                  atk -= resist
                  atk = round(atk)

                  if dmgvary == 1:
                    atk += 1

                  if dmgvary == 2:
                    atk -= 1

                  if dmgvary == 3:
                    atk = atk

                  hp -= atk
                  print(
                      f'The {currentenemy.name} attacked you and did {atk} damage!'
                  )
                print()

#####################################################################################################################################################

    if level % 10 == 0 and level != 0:
      time.sleep(2)
      print("You hear a strange noise coming from the cave in front of you...")
      print()
      time.sleep(5)
      print("It is...")
      print()
      time.sleep(2)

      if level == 10:
        print("THE STRANGE MAGIC MAN!!")

      else:
        print("THE STRANGE MAGIC MAN, YET AGAIN!! (Don't ask how he came back, he's magic)")

      print()
      print("[insert epic boss music here]")
      print()
      time.sleep(2)
      loop5 = True

      while loop5 is True:

        if concious is True and econcious is True:
          print(f'Your current health: {hp} Strange Magic Man: {bossWizard.hp}')

        elif concious is True and econcious is False:
          print(f'Your current health: {hp} Strange Magic Man: {bossWizard.hp} [UNCONCIOUS]')

        elif concious is False and econcious is True:
          print(f'Your current health: {hp} [UNCONCIOUS] Strange Magic Man: {bossWizard.hp}')

        elif concious is False and econcious is False:
          print(f'Your current health: {hp} [UNCONCIOUS] Strange Magic Man: {bossWizard.hp} [UNCONCIOUS]')

        print()
        print()

        if concious is True:
          print("You have 3 actions: Attack (a), Heal (h), or Cast a spell (c)")
          niput = input()
          print()

          if niput == 'attack' or niput == 'a':
            critc = random.randint(1, critchance)
            dmgvary = random.randint(1, 3)

            if critc == 1:
              critatk = attk * crit
              totalatk = critatk + attk
              edefe = totalatk * bossWizard.defe
              totalatk -= edefe
              totalatk = round(totalatk, 1)

              if dmgvary == 1:
                totalatk += 1
              elif dmgvary == 2:
                totalatk -= 1
              else:
                totalatk = totalatk

              bossWizard.hp -= totalatk
              print(
                  f'You got a critical hit! You did {totalatk} damage with your {weapon}.'
              )

            else:
              edefe = attk * bossWizard.defe
              totalatk = attk - edefe
              totalatk = round(totalatk)

              if dmgvary == 1:
                totalatk += 1

              if dmgvary == 2:
                totalatk -= 1

              if dmgvary == 3:
                totalatk = totalatk

              bossWizard.hp -= totalatk
              print(
                  f'You attacked the {bossWizard.name} with your {weapon} and did {totalatk} damage.'
              )
              print()

          elif niput == 'heal' or niput == 'h':
            healamount = random.randint(40, 50)
            hp += healamount
            print(f'You healed yourself and healed {healamount} health.')
            print()

          elif niput == 'cast a spell' or niput == 'c':

            if pclass == 'Wizard':
              randspell = random.randint(1,6)

            else:
              randspell = random.randint(1,5)

            if randspell == 1:
              spellcast = "Fireball"
              castdmg = 15 + level*1.5

            elif randspell == 2:
              spellcast = "Lightning Bolt"
              castdmg = 20 + level*1.5

            elif randspell == 3:
              spellcast = "Backfire"

            elif randspell == 4:
              spellcast = "Heal"
              casthpgain = random.randint(40,50)

            elif randspell == 5:
              spellcast = "Ice Shard"
              econcious = False

            elif randspell == 6:
              spellcast = "Poison Stake"
              epoisoned = True
              epoisoncounter = 4

          print()

          if spellcast == "Backfire":
            print('Your spell backfired and knocked you unconcious!')
            unconciouscounter = 1
            concious = False

          elif spellcast == "Heal":
            print(f"You cast a healing spell and gained {casthpgain} health!")
            hp += casthpgain

          elif spellcast == "Ice Shard":
            print("You cast an ice shard and the enemy is now unconcious!")
            econciouscounter = 1
            econcious = False

          elif spellcast == "Poison Stake":
            print("You cast poison stake! The Strange Magic Man is now poisoned!")

          else:
            print("You cast {spellcast and dealt {castdmg} damage!")
            bossWizard.hp -= castdmg

        else:
          print("You are unconcious!")
          print()
          unconciouscounter -=1

          if unconciouscounter == 0:
            concious = True

        if epoisoncounter > 0:
          print("The Magic Wizard Man is poisoned! He took 15 poison damage!")
          bossWizard.hp -=15
          epoisoncounter -= 1

          if epoisoncounter == 0:
            epoisoned = False


        if econcious is True:
          niput = random.randint(1,3)
          if niput == 1:
            critc = random.randint(1, bossWizard.critchance)
            dmgvary = random.randint(1, 3)

            if critc == 1:
              critatk = bossWizard.atk * bossWizard.crit
              totalatk = critatk + bossWizard.atk
              edefe = totalatk * defense
              totalatk -= edefe
              totalatk = round(totalatk, 1)

              if dmgvary == 1:
                totalatk += 1
              elif dmgvary == 2:
                totalatk -= 1
              else:
                totalatk = totalatk

              hp -= totalatk
              print(
                  f'The Magic Wizard Man got a critical hit! They did {totalatk} damage.'
              )

            else:
              edefe = bossWizard.atk * defense
              totalatk = bossWizard.atk - edefe
              totalatk = round(totalatk)

              if dmgvary == 1:
                totalatk += 1

              if dmgvary == 2:
                totalatk -= 1

              if dmgvary == 3:
                totalatk = totalatk

              hp -= totalatk
              print(
                  f'The Strange magic Man attacked you and did {totalatk} damage.'
              )
              print()

          elif niput == 2:
            healamount = random.randint(40, 50)
            bossWizard.hp += healamount
            print(f'The Strange Magic Man healed {healamount} health.')
            print()

          elif niput == 3:
            randspell = random.randint(1,6)

            if randspell == 1:
              spellcast = "Fireball"
              castdmg = 15 + level*1.5

            elif randspell == 2:
              spellcast = "Lightning Bolt"
              castdmg = 20 + level*1.5

            elif randspell == 3:
              spellcast = "Backfire"

            elif randspell == 4:
              spellcast = "Heal"
              casthpgain = random.randint(40,50)

            elif randspell == 5:
              spellcast = "Ice Shard"
              concious = False

            elif randspell == 6:
              spellcast = "Poison Stake"
              poisoned = True
              poisoncounter = 4

          print()

          if spellcast == "Backfire":
            print("The Strange Magic Man's spell backfired and knocked him unconcious!")
            eunconciouscounter = 1
            econcious = False

          elif spellcast == "Heal":
            print(f"The Strange Magic Man cast a healing spell and gained {casthpgain} health!")
            bossWizard.hp += casthpgain

          elif spellcast == "Ice Shard":
            print("The Strange Magic Man cast an ice shard and the enemy is now unconcious!")
            conciouscounter = 1
            concious = False

          elif spellcast == "Poison Stake":
            print("The Strange Magic Man cast poison stake! You are now poisoned!")

          else:
            print(f"The Strange Magic Man cast {spellcast} and dealt {castdmg} damage!")
            hp -= castdmg

          print()

        else:
          print("The Magic Wizard Man is unconcious!")
          print()
          econciouscounter -= 1

          if econciouscounter == 0:
            econcious = True

        if poisoncounter > 0:
          print("You are poisoned! You took 15 poison damage!")
          hp -=15
          poisoncounter -= 1

          if poisoncounter == 0:
            poisoned = False

        if hp <= 0:
          print()
          print(f"The Strange Magic Man has defeated you. You have been sent back to level {level-5}, with your stats degraded.")
          atkUpgradeBar = "[|==--|]"
          hpUpgradeBar = "[|=---|]"
          defeUpgradeBar = "[|==--|]"
          critUpgradeBar = "[|=---|]"
          level -= 5
          atk -= 6
          hp -= 3
          maxhp -= 3
          defe -= 0.02
          critchance -= 1
          weapon = "Fist"
          loop5 = False   

        elif bossWizard.hp <= 0:
          print(f"You have defeated the Strange Magic Man! You are now level {level+1}! You have gained 50 gold!")
          level += 1
          gold += 50
          bossWizard.maxhp += 50
          bossWizard.hp = bossWizard.maxhp
          bossWizard.atk += 15
          bossWizard.defe += 0.05

  elif niput == 'blacksmith':
    blacksmithslot1 = random.randint(1,6)
    blacksmithslot2 = random.randint(1,6)
    blacksmithslot3 = random.randint(1,6)

    if blacksmithslot1 == 1:
      blacksmithslot1 = "Sword - 40 Gold (sword)"

    elif blacksmithslot1 == 2:
      blacksmithslot1 = "Mace - 30 Gold (mace)"

    elif blacksmithslot1 == 3:
      blacksmithslot1 = "Dagger - 25 Gold (dagger)"

    elif blacksmithslot1 == 4:
      blacksmithslot1 = "Staff - 50 Gold (staff)"

    elif blacksmithslot1 == 5:
      blacksmithslot1 = "Bow - 35 Gold (bow)"

    elif blacksmithslot1 == 6:
      blacksmithslot1 = "[OUT OF STOCK]"

    if blacksmithslot2 == 1:
      blacksmithslot2 = "Sword - 40 Gold (sword)"

    elif blacksmithslot2 == 2:
      blacksmithslot2 = "Mace - 30 Gold (mace)"

    elif blacksmithslot2 == 3:
      blacksmithslot2 = "Dagger - 25 Gold (dagger)"

    elif blacksmithslot2 == 4:
      blacksmithslot2 = "Staff - 50 Gold (staff)"

    elif blacksmithslot2 == 5:
      blacksmithslot2 = "Bow - 35 Gold (bow)"

    elif blacksmithslot2 == 6:
      blacksmithslot2 = "[OUT OF STOCK]"

    if blacksmithslot3 == 1:
      blacksmithslot3 = "Sword - 40 Gold (sword)"

    elif blacksmithslot3 == 2:
      blacksmithslot3 = "Mace - 30 Gold (mace)"

    elif blacksmithslot3 == 3:
      blacksmithslot3 = "Dagger - 25 Gold (dagger)"

    elif blacksmithslot3 == 4:
      blacksmithslot3 = "Staff - 50 Gold (staff)"

    elif blacksmithslot3 == 5:
      blacksmithslot3 = "Bow - 35 Gold (bow)"

    elif blacksmithslot3 == 6:
      blacksmithslot3 = "[OUT OF STOCK]"

    print("Welcome to the blacksmith's shop!")
    time.sleep(2)
    print("As you walk in, the sweet smell of wood combined with is sharp tang of hot metal reaches your nose, and you can't help but feel a sense of calm and relaxation flood over you like a wave on the beach on a sunny day.")
    time.sleep(1)
    print("A large man, who looks to be very heavily built, stands in front of you, his face bright, and his eyes sparkle with a warm excitement at seeing a new face in the shop.")
    time.sleep(1)
    print("""He smiles at you, and you can see that he is very happy to see you. "Welcome to the blacksmith's shop, my friend," he says, "I'm sure you're here to see my exquisite wares, which are quite nice, in my opinion," he chuckles softly.""")
    time.sleep(1)
    print("""He then shows you to a fine selection of tools and equipment. You are amazed by the variety of items he has to offer, and you can't help but feel a sense of excitement at the prospect of buying something. These are the items that you can buy:""")
    time.sleep(1)
    print()
    print(f"Option 1: {blacksmithslot1}")
    print(f"Option 2: {blacksmithslot2}")
    print(f"Option 3: {blacksmithslot3}")
    print()
    print("Please choose an item: (or type no to leave)")
    niput = input()

    if niput == 'sword' and blacksmithslot3 == "Sword - 40 Gold (sword)" or niput == 'sword' and blacksmithslot2 == "Sword - 40 Gold (sword)" or niput == 'sword' and blacksmithslot1 == "Sword - 40 Gold (sword)":

      if inventory[0] != "Empty" and inventory[1] != "Empty" and inventory[2] != "Empty" and inventory[3] != "Empty" and inventory[4] != "Empty" and inventory[5] != "Empty":
        print("You don't have enough space in your inventory to buy this item!")

      elif gold < 40:
        print("You don't have enough gold to buy this item!")

      elif inventory[0] == "Empty":
        inventory[0] = "Sword"
        gold -= 40
        print("You bought the sword!")

      elif inventory[1] == "Empty":
        inventory[1] = "Sword"
        gold -= 40
        print("You bought the sword!")

      elif inventory[2] == "Empty":
        inventory[2] = "Sword"
        gold -= 40
        print("You bought the sword!")

      elif inventory[3] == "Empty":
        inventory[3] = "Sword"
        gold -= 40
        print("You bought the sword!")

      elif inventory[4] == "Empty":
        inventory[4] = "Sword"
        gold -= 40
        print("You bought the sword!")

      elif inventory[5] == "Empty":
        inventory[5] = "Sword"
        gold -= 40
        print("You bought the sword!")
    
    elif niput == 'mace' and blacksmithslot3 == "Mace - 30 Gold (mace)" or niput == 'mace' and blacksmithslot2 == "Mace - 30 Gold (mace)" or niput == 'mace' and blacksmithslot1 == "Mace - 30 Gold (mace)":

      if inventory[0] != "Empty" and inventory[1] != "Empty" and inventory[2] != "Empty" and inventory[3] != "Empty" and inventory[4] != "Empty" and inventory[5] != "Empty":
        print("You don't have enough space in your inventory to buy this item!")

      elif gold < 30:
        print("You don't have enough gold to buy this item!")

      elif inventory[0] == "Empty":
        inventory[0] = "Mace"
        gold -= 30
        print("You bought the mace!")

      elif inventory[1] == "Empty":
        inventory[1] = "Mace"
        gold -= 30
        print("You bought the mace!")

      elif inventory[2] == "Empty":
        inventory[2] = "Mace"
        gold -= 30
        print("You bought the mace!")

      elif inventory[3] == "Empty":
        inventory[3] = "Mace"
        gold -= 30
        print("You bought the mace!")

      elif inventory[4] == "Empty":
        inventory[4] = "Mace"
        gold -= 30
        print("You bought the mace!")

      elif inventory[5] == "Empty":
        inventory[5] = "Mace"
        gold -= 30
        print("You bought the mace!")

    elif niput == 'dagger' and blacksmithslot3 == "Dagger - 25 Gold (dagger)" or niput == 'dagger' and blacksmithslot2 == "Dagger - 25 Gold (dagger)" or niput == 'dagger' and blacksmithslot1 == "Dagger - 25 Gold (dagger)":

      if inventory[0] != "Empty" and inventory[1] != "Empty" and inventory[2] != "Empty" and inventory[3] != "Empty" and inventory[4] != "Empty" and inventory[5] != "Empty":
        print("You don't have enough space in your inventory to buy this item!")

      elif gold < 25:
        print("You don't have enough gold to buy this item!")

      elif inventory[0] == "Empty":
        inventory[0] = "Dagger"
        gold -= 25
        print("You bought the dagger!")

      elif inventory[1] == "Empty":
        inventory[1] = "Dagger"
        gold -= 25
        print("You bought the dagger!")

      elif inventory[2] == "Empty":
        inventory[2] = "Dagger"
        gold -= 25
        print("You bought the dagger!")

      elif inventory[3] == "Empty":
        inventory[3] = "Dagger"
        gold -= 25
        print("You bought the dagger!")

      elif inventory[4] == "Empty":
        inventory[4] = "Dagger"
        gold -= 25
        print("You bought the dagger!")

      elif inventory[5] == "Empty":
        inventory[5] = "Dagger"
        gold -= 25
        print("You bought the dagger!")

    elif niput == 'staff' and blacksmithslot3 == "Staff - 50 Gold (staff)" or niput == 'staff' and blacksmithslot2 == "Staff - 50 Gold (staff)" or niput == 'staff' and blacksmithslot1 == "Staff - 50 Gold (staff)":
      
      if inventory[0] != "Empty" and inventory[1] != "Empty" and inventory[2] != "Empty" and inventory[3] != "Empty" and inventory[4] != "Empty" and inventory[5] != "Empty":
        print("You don't have enough space in your inventory to buy this item!")

      elif gold < 50:
        print("You don't have enough gold to buy this item!")

      elif inventory[0] == "Empty":
        inventory[0] = "Staff"
        gold -= 50
        print("You bought the staff!")

      elif inventory[1] == "Empty":
        inventory[1] = "Staff"
        gold -= 50
        print("You bought the staff!")

      elif inventory[2] == "Empty":
        inventory[2] = "Staff"
        gold -= 50
        print("You bought the staff!")

      elif inventory[3] == "Empty":
        inventory[3] = "Staff"
        gold -= 50
        print("You bought the staff!")

      elif inventory[4] == "Empty":
        inventory[4] = "Staff"
        gold -= 50
        print("You bought the staff!")

      elif inventory[5] == "Empty":
        inventory[5] = "Staff"
        gold -= 50
        print("You bought the staff!")

    elif niput == 'bow' and blacksmithslot3 == "Bow - 35 Gold (bow)" or niput == 'bow' and blacksmithslot2 == "Bow - 35 Gold (bow)" or niput == 'bow' and blacksmithslot1 == "Bow - 35 Gold (bow)":

      if inventory[0] != "Empty" and inventory[1] != "Empty" and inventory[2] != "Empty" and inventory[3] != "Empty" and inventory[4] != "Empty" and inventory[5] != "Empty":
        print("You don't have enough space in your inventory to buy this item!")

      elif gold < 35:
        print("You don't have enough gold to buy this item!")

      elif inventory[0] == "Empty":
        inventory[0] = "Bow"
        gold -= 35
        print("You bought the bow!")

      elif inventory[1] == "Empty":
        inventory[1] = "Bow"
        gold -= 35
        print("You bought the bow!")

      elif inventory[2] == "Empty":
        inventory[2] = "Bow"
        gold -= 35
        print("You bought the bow!")

      elif inventory[3] == "Empty":
        inventory[3] = "Bow"
        gold -= 35
        print("You bought the bow!")

      elif inventory[4] == "Empty":
        inventory[4] = "Bow"
        gold -= 35
        print("You bought the bow!")

      elif inventory[5] == "Empty":
        inventory[5] = "Bow"
        gold -= 35
        print("You bought the bow!")
      
  elif niput == 'credits' or niput == 'Credits' or niput == 'credits!' or niput == 'Credits!':
    i = 50
    while i >= 0:
      print()
      i -= 1
    print()
    print('Credits:')
    time.sleep(0.5)
    print()
    time.sleep(2)
    print(
        'Creator & Programmer: Joey Bacon, a random guy who likes computers and coding'
    )
    time.sleep(2)
    print(f'Engine: IDLE Python Shell {versionsProgrammed}.')
    time.sleep(2)
    print(f'Game version: {version}.')
    time.sleep(3)
    print("And finally...")
    time.sleep(4)
    print('Playtesters:  Noah Magone, Mateo Donado, Eli Cardoso, Soar Mutl, and Molly Bacon.')
    time.sleep(3)
    ##print("Players:", playerList["players"])
    ##time.sleep(3)
    print('Return to Main Menu?')
    niput = input()

  elif niput == 'shop' or niput == 'Shop' or niput == 'shop!' or niput == 'Shop!' and experiments == 1:
    print('Welcome to the shop! There are a few things for sale.')
    item1 = random.randint(1, 5)
    item2 = random.randint(1, 5)
    item3 = random.randint(1, 5)
    print()
    print('You have', gold, 'gold.')

    if item1 == 1:
      item1 = 'Tooth Relic (trelic) - 25 Gold'

    if item1 == 2:
      item1 = 'Heart Relic (hrelic) - 40 Gold'

    if item1 == 3:
      item1 = '[OUT OF STOCK]'

    if item1 == 4:
      item1 = 'Dagger (dagger) - 60 Gold'

    if item1 == 5:
      item1 = 'Shield Relic (srelic) - 50 Gold'

    if item2 == 1:
      item2 = 'Tooth Relic (trelic) - 25 Gold'

    if item2 == 2:
      item2 = 'Heart Relic (hrelic) - 40 Gold'

    if item2 == 3:
      item2 = '[OUT OF STOCK]'

    if item2 == 4:
      item2 = 'Dagger (dagger) - 60 Gold'

    if item2 == 5:
      item2 = 'Shield Relic (srelic) - 50 Gold'

    if item3 == 1:
      item3 = 'Tooth Relic (trelic) - 25 Gold'

    if item3 == 2:
      item3 = 'Heart Relic (hrelic) - 40 Gold'

    if item3 == 3:
      item3 = '[OUT OF STOCK]'

    if item3 == 4:
      item3 = 'Dagger (dagger) - 60 Gold'

    if item3 == 5:
      item3 = 'Shield Relic (srelic) - 50 Gold'

    print()
    print('Items for sale:')
    print(f'Item 1: {item1}!')
    print(f'Item 2: {item2}!')
    print(f'Item 3: {item3}!')
    print()
    print(
        'Please choose which item you want. If you do not want any items, type no.'
    )
    niput = input()

    if niput == 'trelic' and item1 == 'Tooth Relic (trelic) - 25 Gold' or niput == 'trelic' and item2 == 'Tooth Relic (trelic) - 25 Gold' or niput == 'trelic' and item3 == 'Tooth Relic (trelic) - 25 Gold':

      if gold >= 25:

        if inventory[0] == 'Empty' or inventory[1] == 'Empty' or inventory[
            2] == 'Empty' or inventory[3] == 'Empty' or inventory[
                4] == 'Empty' or inventory[5] == 'Empty':
          print()
          print('You bought the Tooth Relic.')
          gold -= 25

          if inventory[0] == 'Empty':
            inventory[0] = 'Tooth Relic - Increases Critical hit damage'

          elif inventory[1] == 'Empty':
            inventory[1] = 'Tooth Relic - Increases Critical hit damage'

          elif inventory[2] == 'Empty':
            inventory[2] = 'Tooth Relic - Increases Critical hit damage'

          elif inventory[3] == 'Empty':
            inventory[3] = 'Tooth Relic - Increases Critical hit damage'

          elif inventory[4] == 'Empty':
            inventory[4] = 'Tooth Relic - Increases Critical hit damage'

          elif inventory[5] == 'Empty':
            inventory[5] = 'Tooth Relic - Increases Critical hit damage'

        else:
          print("You don't have enough iventory space.")

      elif gold < 25:
        print()
        print('You do not have enough gold for this item.')

    elif niput == 'srelic' and item1 == 'Shield Relic (srelic) - 50 Gold' or niput == 'srelic' and item2 == 'Shield Relic (srelic) - 50 Gold' or niput == 'srelic' and item3 == 'Shield Relic (srelic) - 50 Gold':

      if gold >= 50:

        if inventory[0] == 'Empty' or inventory[1] == 'Empty' or inventory[
            2] == 'Empty' or inventory[3] == 'Empty' or inventory[
                4] == 'Empty' or inventory[5] == 'Empty':
          print()
          print('You bought the Shield Relic.')
          gold -= 50

          if inventory[0] == 'Empty':
            inventory[0] = 'Shield Relic - Increases defense'

          elif inventory[1] == 'Empty':
            inventory[1] = 'Shield Relic - Increases defense'

          elif inventory[2] == 'Empty':
            inventory[2] = 'Shield Relic - Increases defense'

          elif inventory[3] == 'Empty':
            inventory[3] = 'Shield Relic - Increases defense'

          elif inventory[4] == 'Empty':
            inventory[4] = 'Shield Relic - Increases defense'

          elif inventory[5] == 'Empty':
            inventory[5] = 'Shield Relic - Increases defense'

        else:
          print("You don't have enough iventory space.")

      elif gold < 50:
        print()
        print('You do not have enough gold for this item.')

    elif niput == 'dagger' and item1 == 'Dagger (dagger) - 60 Gold' or niput == 'dagger' and item2 == 'Dagger (dagger) - 60 Gold' or niput == 'dagger' and item3 == 'Dagger (dagger) - 60 Gold':

      if gold >= 60:

        if inventory[0] == 'Empty' or inventory[1] == 'Empty' or inventory[
            2] == 'Empty' or inventory[3] == 'Empty' or inventory[
                4] == 'Empty' or inventory[5] == 'Empty':
          print()
          print('You bought the Dagger.')
          gold -= 60

          if inventory[0] == 'Empty':
            inventory[0] = 'Dagger - Increases damage'

          elif inventory[1] == 'Empty':
            inventory[1] = 'Dagger - Increases damage'

          elif inventory[2] == 'Empty':
            inventory[2] = 'Dagger - Increases damage'

          elif inventory[3] == 'Empty':
            inventory[3] = 'Dagger - Increases damage'

          elif inventory[4] == 'Empty':
            inventory[4] = 'Dagger - Increases damage'

          elif inventory[5] == 'Empty':
            inventory[5] = 'Dagger - Increases damage'

        else:
          print("You don't have enough iventory space.")

      elif gold < 60:
        print()
        print('You do not have enough gold for this item.')

    elif niput == 'hrelic' and item1 == 'Heart Relic (hrelic) - 40 Gold' or niput == 'hrelic' and item2 == 'Heart Relic (hrelic) - 40 Gold' or niput == 'hrelic' and item3 == 'Heart Relic (hrelic) - 40 Gold':

      if gold >= 40:

        if inventory[0] == 'Empty' or inventory[1] == 'Empty' or inventory[
            2] == 'Empty' or inventory[3] == 'Empty' or inventory[
                4] == 'Empty' or inventory[5] == 'Empty':
          print()
          print('You bought the Heart Relic.')
          gold -= 40

          if inventory[0] == 'Empty':
            inventory[0] = 'Heart Relic - Increases health'

          elif inventory[1] == 'Empty':
            inventory[1] = 'Heart Relic - Increases health'

          elif inventory[2] == 'Empty':
            inventory[2] = 'Heart Relic - Increases health'

          elif inventory[3] == 'Empty':
            inventory[3] = 'Heart Relic - Increases health'

          elif inventory[4] == 'Empty':
            inventory[4] = 'Heart Relic - Increases health'

          elif inventory[5] == 'Empty':
            inventory[5] = 'Heart Relic - Increases health'

        else:
          print("You don't have enough iventory space.")

      elif gold <= 39:
        print()
        print('You do not have enough gold for this item.')

    elif niput == 'no':
      print(
          'You came to your senses and decided that the prices were too high.')

    else:
      print('That is not a valid item')

  elif niput == 'stats' or niput == 'Stats' or niput == 'stats!' or niput == 'Stats!':
    print('Statistics:')
    print()
    print(f'Name: {name}.')
    print(f'Class: {pclass}.')
    print(f'Max Health: {maxhp}.')
    print(f'Attack: {attk}.')
    print(f'Defense: {defense}.')
    print(f'Total enemies defeated: {totalwins}.')
    print(f'Total losses: {totallosses}.')
    print(f'Highest level reached: {highestlevel}.')
    print()
    print('Return to menu?')
    niput = input()

##    elif niput == 'pets' and pets > 0 and experiments == 1 or niput == 'Pets' and pets > 0 and experiments == 1 or niput == 'pets!' and pets > 0 and experiments == 1 or niput == 'Pets!' and pets > 0 and experiments == 1:
##        print(f'[This feature is in progress]')
##        print(f"Slot 1: You have a pet {petname}! It's stats are: Health: {petstats.hp}, Attack: {petstats.atk}, {petstats.critdam * 100} Percent bonus for critical hits, {petstats.defe * 100} percent defense, and a 1 in {20 - critchance} chance to land a critical blow.")
##        print(f'Pet equipped: Yes')
##        print(f'Return to menu?')
##        niput = input()

  elif niput == 'minventory' and experiments == 1:
    print('Inventory:')
    print(f'Slot 1: {inventory[0]}')
    print(f'Slot 2: {inventory[1]}')
    print(f'Slot 3: {inventory[2]}')
    print(f'Slot 4: {inventory[3]}')
    print(f'Slot 5: {inventory[4]}')
    print(f'Slot 6: {inventory[5]}')
    print(f'Equipped Artifact 1: {inventory[6]}')
    print(f'Equipped Artifact 2: {inventory[7]}')
    print(f'Equipped Weapon: {weapon}')
    print(f'Armor: {armor}')
    print()
    print(
        'What would you like to do? You can either equip an artifact (equip), unequip and artifact (unequip), equip or unequip a weapon (wequip), or manage your inventory (manage).'
    )
    niput = input()

    if niput == 'manage':
      print()
      print(
          'You can do things. You can delete an item (delete) or move an item (move).'
      )
      niput = input()
      print()

      if niput == 'delete':
        print(
            "To delete an item, just type 'slot ', then the slot number. To not delete anything, type no."
        )
        niput = input()

        if niput == 'slot 1':
          print('Are you sure? y/n')
          niput = input()

          if niput == 'Y' or niput == 'y':
            inventory[0] = 'Empty'

          else:
            print("You didn't delete the item.")

        if niput == 'slot 2':
          print('Are you sure? y/n')
          niput = input()

          if niput == 'Y' or niput == 'y':
            inventory[1] = 'Empty'

          else:
            print("You didn't delete the item.")

        if niput == 'slot 3':
          print('Are you sure? y/n')
          niput = input()

          if niput == 'Y' or niput == 'y':
            inventory[2] = 'Empty'

          else:
            print("You didn't delete the item.")

        if niput == 'slot 4':
          print('Are you sure? y/n')
          niput = input()

          if niput == 'Y' or niput == 'y':
            inventory[3] = 'Empty'

          else:
            print("You didn't delete the item.")

        if niput == 'slot 5':
          print('Are you sure? y/n')
          niput = input()

          if niput == 'Y' or niput == 'y':
            inventory[4] = 'Empty'

          else:
            print("You didn't delete the item.")

        if niput == 'slot 6':
          print('Are you sure? y/n')
          niput = input()

          if niput == 'Y' or niput == 'y':
            inventory[5] = 'Empty'

          else:
            print("You didn't delete the item.")

        else:
          print("That is not a viable slot")

      elif niput == 'move':
        print(
            "Which item would you like to move? Format: 'slot ' numberOfSlot")
        niput = input()

        if niput == 'slot 1':
          moveslot1 = inventory[0]
          moveslotnum = 1
          print('You chose slot 1.')

        elif niput == 'slot 2':
          moveslot1 = inventory[1]
          moveslotnum = 2
          print('You chose slot 2.')

        elif niput == 'slot 3':
          moveslot1 = inventory[2]
          moveslotnum = 3
          print('You chose slot 3.')

        elif niput == 'slot 4':
          moveslot1 = inventory[3]
          moveslotnum = 4
          print('You chose slot 4.')

        elif niput == 'slot 5':
          moveslot1 = inventory[4]
          moveslotnum = 5
          print('You chose slot 5.')

        elif niput == 'slot 6':
          moveslot1 = inventory[5]
          moveslotnum = 6
          print('You chose slot 6.')

        else:
          print('That is not a valid slot.')
          moveslot1 = 'none'

        if moveslot != 'none':
          print(
              "Now choose which slot you want to swap it with. Format: 'slot ' numberOfSlot."
          )
          niput = input()

          if niput == 'slot 1':

            if moveslotnum == 1:
              inventory[0] = inventory[0]
              inventory[0] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 2:
              inventory[1] = inventory[0]
              inventory[0] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 3:
              inventory[2] = inventory[0]
              inventory[0] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 4:
              inventory[3] = inventory[0]
              inventory[0] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 5:
              inventory[4] = inventory[0]
              inventory[0] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 6:
              inventory[5] = inventory[0]
              inventory[0] = moveslot1
              print('Slots successfully swapped!')

          elif niput == 'slot 2':

            if moveslotnum == 1:
              inventory[0] = inventory[1]
              inventory[1] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 2:
              inventory[1] = inventory[1]
              inventory[1] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 3:
              inventory[2] = inventory[1]
              inventory[1] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 4:
              inventory[3] = inventory[1]
              inventory[1] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 5:
              inventory[4] = inventory[1]
              inventory[1] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 6:
              inventory[5] = inventory[1]
              inventory[1] = moveslot1
              print('Slots successfully swapped!')

          elif niput == 'slot 3':

            if moveslotnum == 1:
              inventory[0] = inventory[2]
              inventory[2] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 2:
              inventory[1] = inventory[2]
              inventory[2] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 3:
              inventory[2] = inventory[2]
              inventory[2] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 4:
              inventory[3] = inventory[2]
              inventory[2] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 5:
              inventory[4] = inventory[2]
              inventory[2] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 6:
              inventory[5] = inventory[2]
              inventory[2] = moveslot1
              print('Slots successfully swapped!')

          elif niput == 'slot 4':

            if moveslotnum == 1:
              inventory[0] = inventory[3]
              inventory[3] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 2:
              inventory[1] = inventory[3]
              inventory[3] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 3:
              inventory[2] = inventory[3]
              inventory[3] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 4:
              inventory[3] = inventory[3]
              inventory[3] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 5:
              inventory[4] = inventory[3]
              inventory[3] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 6:
              inventory[5] = inventory[3]
              inventory[3] = moveslot1
              print('Slots successfully swapped!')

          elif niput == 'slot 5':

            if moveslotnum == 1:
              inventory[0] = inventory[4]
              inventory[4] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 2:
              inventory[1] = inventory[4]
              inventory[4] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 3:
              inventory[2] = inventory[4]
              inventory[4] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 4:
              inventory[3] = inventory[4]
              inventory[4] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 5:
              inventory[4] = inventory[4]
              inventory[4] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 6:
              inventory[5] = inventory[4]
              inventory[4] = moveslot1
              print('Slots successfully swapped!')

          elif niput == 'slot 6':

            if moveslotnum == 1:
              inventory[0] = inventory[5]
              inventory[5] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 2:
              inventory[1] = inventory[5]
              inventory[5] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 3:
              inventory[2] = inventory[5]
              inventory[5] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 4:
              inventory[3] = inventory[5]
              inventory[5] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 5:
              inventory[4] = inventory[5]
              inventory[5] = moveslot1
              print('Slots successfully swapped!')

            if moveslotnum == 6:
              inventory[5] = inventory[5]
              inventory[5] = moveslot1
              print('Slots successfully swapped!')

          else:
            print('That is not a valid slot.')

    elif niput == 'equip':
      print(
          "Please choose which item you want to equip, using the format: 'slot ' NumberOfSlot"
      )
      niput = input()

      if niput == 'slot 1' and inventory[0] == 'Empty':
        print('That slot is empty.')

      elif niput == 'slot 2' and inventory[1] == 'Empty':
        print('That slot is empty.')

      elif niput == 'slot 3' and inventory[2] == 'Empty':
        print('That slot is empty.')

      elif niput == 'slot 4' and inventory[3] == 'Empty':
        print('That slot is empty.')

      elif niput == 'slot 5' and inventory[4] == 'Empty':
        print('That slot is empty.')

      elif niput == 'slot 6' and inventory[5] == 'Empty':
        print('That slot is empty.')

      elif niput == 'slot 1' and inventory[0] != 'Empty':

        if inventory[6] == 'None':
          print(f'You have activated your {inventory[0]}!')
          inventory[6] = inventory[0]
          inventory[0] = 'Empty'

          if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[6] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[6] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[6] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        elif inventory[7] == 'None':
          print(f'You have activated your {inventory[0]}!')
          inventory[6] = inventory[0]
          inventory[0] = 'Empty'

          if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[7] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[7] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[7] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        else:
          print('You have already equipped the max amount of items.')

      elif niput == 'slot 2' and inventory[1] != 'Empty':

        if inventory[6] == 'None':
          print(f'You have activated your {inventory[1]}!')
          inventory[6] = inventory[1]
          inventory[1] = 'Empty'

          if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[6] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[6] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[6] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        elif inventory[7] == 'None':
          print(f'You have activated your {inventory[1]}!')
          inventory[6] = inventory[1]
          inventory[1] = 'Empty'

          if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[7] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[7] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[7] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        else:
          print('You have already equipped the max amount of items.')

      elif niput == 'slot 3' and inventory[2] != 'Empty':

        if inventory[6] == 'None':
          print(f'You have activated your {inventory[2]}!')
          inventory[6] = inventory[2]
          inventory[2] = 'Empty'

          if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[6] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[6] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[6] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        elif inventory[7] == 'None':
          print(f'You have activated your {inventory[2]}!')
          inventory[6] = inventory[2]
          inventory[2] = 'Empty'

          if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[7] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[7] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[7] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        else:
          print('You have already equipped the max amount of items.')

      elif niput == 'slot 4' and inventory[3] != 'Empty':

        if inventory[6] == 'None':
          print(f'You have activated your {inventory[3]}!')
          inventory[6] = inventory[3]
          inventory[3] = 'Empty'

          if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[6] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[6] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[6] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        elif inventory[7] == 'None':
          print(f'You have activated your {inventory[3]}!')
          inventory[6] = inventory[3]
          inventory[3] = 'Empty'

          if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[7] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[7] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[7] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        else:
          print('You have already equipped the max amount of items.')

      elif niput == 'slot 5' and inventory[4] != 'Empty':

        if inventory[6] == 'None':
          print(f'You have activated your {inventory[4]}!')
          inventory[6] = inventory[4]
          inventory[4] = 'Empty'

          if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[6] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[6] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[6] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        elif inventory[7] == 'None':
          print(f'You have activated your {inventory[4]}!')
          inventory[6] = inventory[4]
          inventory[4] = 'Empty'

          if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[7] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[7] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[7] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        else:
          print('You have already equipped the max amount of items.')

      elif niput == 'slot 6' and inventory[5] != 'Empty':

        if inventory[6] == 'None':
          print(f'You have activated your {inventory[5]}!')
          inventory[6] = inventory[5]
          inventory[5] = 'Empty'

          if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[6] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[6] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[6] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        elif inventory[7] == 'None':
          print(f'You have activated your {inventory[5]}!')
          inventory[6] = inventory[5]
          inventory[5] = 'Empty'

          if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
            crit += 0.1
            buffs[3] += 0.1

          elif inventory[7] == 'Shield Relic - Increases defense':
            defense += 0.07
            buffs[1] += 0.07

          elif inventory[7] == 'Dagger - Increases damage':
            attk += 3
            buffs[2] += 3

          elif inventory[7] == 'Heart Relic - Increases health':
            maxhp += 3
            buffs[5] += 3

        else:
          print('You have already equipped the max amount of items.')

      else:
        print('That is not a valid slot.')

    elif niput == 'unequip':
      print(
          "Please choose which slot you want to unequip. Choose slot 1 or slot 2."
      )
      niput = input()

      if niput == 'slot 1' and inventory[6] == 'None':
        print('That slot is empty.')

      elif niput == 'slot 2' and inventory[7] == 'None':
        print('That slot is empty.')

      elif niput == 'slot 1' and inventory[0] == 'None':

        print(f"You unequipped your {inventory[6]}.")

        if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
          inventory[0] = 'Tooth Relic - Increases Critical hit damage'
          inventory[6] = 'None'
          crit -= 0.1

        elif inventory[6] == 'Shield Relic - Increases defense':
          inventory[0] = 'Shield Relic - Increases defense'
          inventory[6] = 'None'
          defe -= 0.7

        elif inventory[6] == 'Dagger - Increases damage':
          inventory[0] = 'Dagger - Increases damage'
          inventory[6] = 'None'
          atk -= 3

        elif inventory[6] == 'Heart Relic - Increases health':
          inventory[0] = 'Heart Relic - Increases health'
          inventory[6] = 'None'
          maxhp -= 3

      elif niput == 'slot 2' and inventory[0] == 'None':

        print(f"You unequipped your {inventory[7]}.")

        if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
          inventory[0] = 'Tooth Relic - Increases Critical hit damage'
          inventory[7] = 'None'
          crit -= 0.1

        elif inventory[7] == 'Shield Relic - Increases defense':
          inventory[0] = 'Shield Relic - Increases defense'
          inventory[7] = 'None'
          defe -= 0.7

        elif inventory[7] == 'Dagger - Increases damage':
          inventory[0] = 'Dagger - Increases damage'
          inventory[7] = 'None'
          atk -= 3

        elif inventory[7] == 'Heart Relic - Increases health':
          inventory[0] = 'Heart Relic - Increases health'
          inventory[7] = 'None'
          maxhp -= 3

      elif niput == 'slot 1' and inventory[1] == 'None':

        print(f"You unequipped your {inventory[6]}.")

        if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
          inventory[1] = 'Tooth Relic - Increases Critical hit damage'
          inventory[6] = 'None'
          crit -= 0.1

        elif inventory[6] == 'Shield Relic - Increases defense':
          inventory[1] = 'Shield Relic - Increases defense'
          inventory[6] = 'None'
          defe -= 0.7

        elif inventory[6] == 'Dagger - Increases damage':
          inventory[1] = 'Dagger - Increases damage'
          inventory[6] = 'None'
          atk -= 3

        elif inventory[6] == 'Heart Relic - Increases health':
          inventory[1] = 'Heart Relic - Increases health'
          inventory[6] = 'None'
          maxhp -= 3

      elif niput == 'slot 2' and inventory[1] == 'None':

        print(f"You unequipped your {inventory[7]}.")

        if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
          inventory[1] = 'Tooth Relic - Increases Critical hit damage'
          inventory[7] = 'None'
          crit -= 0.1

        elif inventory[7] == 'Shield Relic - Increases defense':
          inventory[1] = 'Shield Relic - Increases defense'
          inventory[7] = 'None'
          defe -= 0.7

        elif inventory[7] == 'Dagger - Increases damage':
          inventory[1] = 'Dagger - Increases damage'
          inventory[7] = 'None'
          atk -= 3

        elif inventory[7] == 'Heart Relic - Increases health':
          inventory[1] = 'Heart Relic - Increases health'
          inventory[7] = 'None'
          maxhp -= 3

      elif niput == 'slot 1' and inventory[2] == 'None':

        print(f"You unequipped your {inventory[6]}.")

        if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
          inventory[2] = 'Tooth Relic - Increases Critical hit damage'
          inventory[6] = 'None'
          crit -= 0.1

        elif inventory[6] == 'Shield Relic - Increases defense':
          inventory[2] = 'Shield Relic - Increases defense'
          inventory[6] = 'None'
          defe -= 0.7

        elif inventory[6] == 'Dagger - Increases damage':
          inventory[2] = 'Dagger - Increases damage'
          inventory[6] = 'None'
          atk -= 3

        elif inventory[6] == 'Heart Relic - Increases health':
          inventory[2] = 'Heart Relic - Increases health'
          inventory[6] = 'None'
          maxhp -= 3

      elif niput == 'slot 2' and inventory[2] == 'None':

        print(f"You unequipped your {inventory[7]}.")

        if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
          inventory[2] = 'Tooth Relic - Increases Critical hit damage'
          inventory[7] = 'None'
          crit -= 0.1

        elif inventory[7] == 'Shield Relic - Increases defense':
          inventory[2] = 'Shield Relic - Increases defense'
          inventory[7] = 'None'
          defe -= 0.7

        elif inventory[7] == 'Dagger - Increases damage':
          inventory[2] = 'Dagger - Increases damage'
          inventory[7] = 'None'
          atk -= 3

        elif inventory[7] == 'Heart Relic - Increases health':
          inventory[2] = 'Heart Relic - Increases health'
          inventory[7] = 'None'
          maxhp -= 3

      elif niput == 'slot 1' and inventory[3] == 'None':

        print(f"You unequipped your {inventory[6]}.")

        if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
          inventory[3] = 'Tooth Relic - Increases Critical hit damage'
          inventory[6] = 'None'
          crit -= 0.1

        elif inventory[6] == 'Shield Relic - Increases defense':
          inventory[3] = 'Shield Relic - Increases defense'
          inventory[6] = 'None'
          defe -= 0.7

        elif inventory[6] == 'Dagger - Increases damage':
          inventory[3] = 'Dagger - Increases damage'
          inventory[6] = 'None'
          atk -= 3

        elif inventory[6] == 'Heart Relic - Increases health':
          inventory[3] = 'Heart Relic - Increases health'
          inventory[6] = 'None'
          maxhp -= 3

      elif niput == 'slot 2' and inventory[3] == 'None':

        print(f"You unequipped your {inventory[7]}.")

        if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
          inventory[3] = 'Tooth Relic - Increases Critical hit damage'
          inventory[7] = 'None'
          crit -= 0.1

        elif inventory[7] == 'Shield Relic - Increases defense':
          inventory[3] = 'Shield Relic - Increases defense'
          inventory[7] = 'None'
          defe -= 0.7

        elif inventory[7] == 'Dagger - Increases damage':
          inventory[3] = 'Dagger - Increases damage'
          inventory[7] = 'None'
          atk -= 3

        elif inventory[7] == 'Heart Relic - Increases health':
          inventory[3] = 'Heart Relic - Increases health'
          inventory[7] = 'None'
          maxhp -= 3

      elif niput == 'slot 1' and inventory[4] == 'None':

        print(f"You unequipped your {inventory[6]}.")

        if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
          inventory[4] = 'Tooth Relic - Increases Critical hit damage'
          inventory[6] = 'None'
          crit -= 0.1

        elif inventory[6] == 'Shield Relic - Increases defense':
          inventory[4] = 'Shield Relic - Increases defense'
          inventory[6] = 'None'
          defe -= 0.7

        elif inventory[6] == 'Dagger - Increases damage':
          inventory[4] = 'Dagger - Increases damage'
          inventory[6] = 'None'
          atk -= 3

        elif inventory[6] == 'Heart Relic - Increases health':
          inventory[4] = 'Heart Relic - Increases health'
          inventory[6] = 'None'
          maxhp -= 3

      elif niput == 'slot 2' and inventory[4] == 'None':

        print(f"You unequipped your {inventory[7]}.")

        if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
          inventory[4] = 'Tooth Relic - Increases Critical hit damage'
          inventory[7] = 'None'
          crit -= 0.1

        elif inventory[7] == 'Shield Relic - Increases defense':
          inventory[4] = 'Shield Relic - Increases defense'
          inventory[7] = 'None'
          defe -= 0.7

        elif inventory[7] == 'Dagger - Increases damage':
          inventory[4] = 'Dagger - Increases damage'
          inventory[7] = 'None'
          atk -= 3

        elif inventory[7] == 'Heart Relic - Increases health':
          inventory[4] = 'Heart Relic - Increases health'
          inventory[7] = 'None'
          maxhp -= 3

      elif niput == 'slot 1' and inventory[5] == 'None':

        print(f"You unequipped your {inventory[6]}.")

        if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
          inventory[5] = 'Tooth Relic - Increases Critical hit damage'
          inventory[6] = 'None'
          crit -= 0.1

        elif inventory[6] == 'Shield Relic - Increases defense':
          inventory[5] = 'Shield Relic - Increases defense'
          inventory[6] = 'None'
          defe -= 0.7

        elif inventory[6] == 'Dagger - Increases damage':
          inventory[5] = 'Dagger - Increases damage'
          inventory[6] = 'None'
          atk -= 3

        elif inventory[6] == 'Heart Relic - Increases health':
          inventory[5] = 'Heart Relic - Increases health'
          inventory[6] = 'None'
          maxhp -= 3

      elif niput == 'slot 2' and inventory[5] == 'None':

        print(f"You unequipped your {inventory[7]}.")

        if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
          inventory[5] = 'Tooth Relic - Increases Critical hit damage'
          inventory[7] = 'None'
          crit -= 0.1

        elif inventory[7] == 'Shield Relic - Increases defense':
          inventory[5] = 'Shield Relic - Increases defense'
          inventory[7] = 'None'
          defe -= 0.7

        elif inventory[7] == 'Dagger - Increases damage':
          inventory[5] = 'Dagger - Increases damage'
          inventory[7] = 'None'
          atk -= 3

        elif inventory[7] == 'Heart Relic - Increases health':
          inventory[5] = 'Heart Relic - Increases health'
          inventory[7] = 'None'
          maxhp -= 3

      else:
        print("All slots are full.")

  elif niput == 'qgame':
    print()
    print("You quit the game. A backup has been made.")
    saveFileShelf = shelve.open(f'saveFileFistFight_{tag}')
    saveFileShelf['hp'] = hp
    saveFileShelf['maxhp'] = maxhp
    saveFileShelf['attk'] = attk
    saveFileShelf['crit'] = crit
    saveFileShelf['defense'] = defense
    saveFileShelf['pclass'] = pclass
    saveFileShelf['gold'] = gold
    saveFileShelf['name'] = name
    saveFileShelf['totalwins'] = totalwins
    saveFileShelf['totallosses'] = totallosses
    saveFileShelf['highestlevel'] = highestlevel
    saveFileShelf['pets'] = pets
    saveFileShelf['petname'] = petname
    saveFileShelf['experiments'] = experiments
    saveFileShelf['inventory[0]'] = inventory[0]
    saveFileShelf['inventory[1]'] = inventory[1]
    saveFileShelf['inventory[2]'] = inventory[2]
    saveFileShelf['inventory[3]'] = inventory[3]
    saveFileShelf['inventory[4]'] = inventory[4]
    saveFileShelf['inventory[5]'] = inventory[5]
    saveFileShelf['inventory[6]'] = inventory[6]
    saveFileShelf['inventory[7]'] = inventory[7]
    saveFileShelf['sline.name'] = sline.name
    saveFileShelf['sline.atk'] = sline.atk
    saveFileShelf['sline.hp'] = sline.hp
    saveFileShelf['sline.critdam'] = sline.critdam
    saveFileShelf['sline.maxhp'] = sline.maxhp
    saveFileShelf['sline.defe'] = sline.defe
    saveFileShelf['sline.critchance'] = sline.critchance
    saveFileShelf['smake.name'] = smake.name
    saveFileShelf['smake.atk'] = smake.atk
    saveFileShelf['smake.hp'] = smake.hp
    saveFileShelf['smake.critdam'] = smake.critdam
    saveFileShelf['smake.maxhp'] = smake.maxhp
    saveFileShelf['smake.defe'] = smake.defe
    saveFileShelf['smake.critchance'] = smake.critchance
    saveFileShelf['skeletom.name'] = skeletom.name
    saveFileShelf['skeletom.atk'] = skeletom.atk
    saveFileShelf['skeletom.hp'] = skeletom.hp
    saveFileShelf['skeletom.critdam'] = skeletom.critdam
    saveFileShelf['skeletom.maxhp'] = skeletom.maxhp
    saveFileShelf['skeletom.defe'] = skeletom.defe
    saveFileShelf['skeletom.critchance'] = skeletom.critchance
    saveFileShelf['LEAF.name'] = LEAF.name
    saveFileShelf['LEAF.atk'] = LEAF.atk
    saveFileShelf['LEAF.hp'] = LEAF.hp
    saveFileShelf['LEAF.critdam'] = LEAF.critdam
    saveFileShelf['LEAF.maxhp'] = LEAF.maxhp
    saveFileShelf['LEAF.defe'] = LEAF.defe
    saveFileShelf['LEAF.critchance'] = LEAF.critchance
    saveFileShelf['nagic.name'] = nagic.name
    saveFileShelf['nagic.atk'] = nagic.atk
    saveFileShelf['nagic.hp'] = nagic.hp
    saveFileShelf['nagic.critdam'] = nagic.critdam
    saveFileShelf['nagic.maxhp'] = nagic.maxhp
    saveFileShelf['nagic.defe'] = nagic.defe
    saveFileShelf['nagic.critchance'] = nagic.critchance
    saveFileShelf['platypus.name'] = platypus.name
    saveFileShelf['platypus.atk'] = platypus.atk
    saveFileShelf['platypus.hp'] = platypus.hp
    saveFileShelf['platypus.critdam'] = platypus.critdam
    saveFileShelf['platypus.maxhp'] = platypus.maxhp
    saveFileShelf['platypus.defe'] = platypus.defe
    saveFileShelf['platypus.critchance'] = platypus.critchance
    saveFileShelf['penguilian.name'] = penguilian.name
    saveFileShelf['penguilian.atk'] = penguilian.atk
    saveFileShelf['penguilian.hp'] = penguilian.hp
    saveFileShelf['penguilian.critdam'] = penguilian.critdam
    saveFileShelf['penguilian.maxhp'] = penguilian.maxhp
    saveFileShelf['penguilian.defe'] = penguilian.defe
    saveFileShelf['penguilian.critchance'] = penguilian.critchance
    saveFileShelf['atkUpgradeBar'] = atkUpgradeBar
    saveFileShelf['hpUpgradeBar'] = hpUpgradeBar
    saveFileShelf['defeUpgradeBar'] = defeUpgradeBar
    saveFileShelf['critUpgradeBar'] = critUpgradeBar
    saveFileShelf['weapon'] = weapon
    saveFileShelf['armor'] = armor
    saveFileShelf['devTools'] = devTools
    saveFileShelf.close()
    ##        print(f"Your game has been saved in a folder as 'SaveFileFistFight.txt'. Please do not move, edit, or delete this file without also moving the source code file.")

    loop = False
    loop1 = False
    loop2 = False
    gameloop = False
    time.sleep(2)
    time.sleep(1)
    i = 50
    while i >= 0:
      print()
      i -= 1
    print()
    print('Credits:')
    time.sleep(0.5)
    print()
    time.sleep(2)
    print('Creator & Programmer: Joey Bacon, a random guy who likes computers and coding.')
    time.sleep(2)
    print(f'Engine: IDLE Python Shell {versionsProgrammed}')
    time.sleep(2)
    print(f'Game version: {version}.')
    time.sleep(3)
    print("And finally...")
    time.sleep(4)
    print('Playtesters: Noah Magone, Mateo Donado, Eli Cardoso, Soar Mutl, and Molly Bacon.')
    time.sleep(3)
    ##print("Players:", playerList["players"])
    ##time.sleep(3)
    print("Thank you for playing...")
    time.sleep(1)
    print("See you again soon!")

  else:
    print('That is not a valid action.')

print()
print()
print()
print("Game closed. You may now stop the program.")
