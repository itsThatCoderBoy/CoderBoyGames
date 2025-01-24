##MADE BY CODERBOY. DO NOT DISTRIBUTE.

import random
import time
import os
import shelve
import numpy as np
from colorama import Fore
import shelve
import getkey
from pyfirmata2 import Arduino, util
import secrets

niput = " "

print("Welcome to CoderBoy's Library of games! Please select a game to play.")
print()
print("""
1) Tic-Tac-Toe
2) Scuffed Bank Robbing Simulator
3) Game of Life
4) Axolotl Clicker
5) Inconvenience
6) Fist Fight
""")
niput = input()
if not niput.isnumeric():
    niput = ":("
else:
    niput = int(niput)

if niput == 1:
  print("Welcome to Tic-Tac-Toe!")
  c11 = '?'
  c12 = '?'
  c13 = '?'
  c21 = '?'
  c22 = '?'
  c23 = '?'
  c31 = '?'
  c32 = '?'
  c33 = '?'
  p1name = ''
  p2name = ''
  print('Welcome to Tic-Tac-Toe!')
  print()
  print("Player 1, choose your name.")
  p1name = input()
  print("Nice! PLayer 2, choose your name.")
  p2name = input()
  print('Noice!')
  print()
  loop = True
  while loop:
      loop1 = True
      while loop1:
          print('1  2  3')
          print(c11,'',c12,'',c13, '1')
          print(c21,'',c22,'',c23, '2')
          print(c31,'',c32,'',c33, '3')
          print()
          print("It is", p1name, "'s turn. Input the coordinates as the format xy.")
          coords = input()
          if coords == '11' and c11 == '?':
              c11 = 'O'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '12' and c12 == '?':
              c12 = 'O'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '13' and c13 == '?':
              c13 = 'O'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '21' and c21 == '?':
              c21 = 'O'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '22' and c22 == '?':
              c22 = 'O'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '23' and c23 == '?':
              c23 = 'O'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '31' and c31 == '?':
              c31 = 'O'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '32' and c32 == '?':
              c32 = 'O'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '33' and c33 == '?':
              c33 = 'O'
              print('Good job!')
              print()
              loop1 = False
          else:
              print('That is not a valid coordinate.')

      if c11 == 'O' and c12 == 'O' and c13 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c21 == 'O' and c22 == 'O' and c23 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c31 == 'O' and c32 == 'O' and c33 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c12 == 'O' and c21 == 'O' and c31 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c12 == 'O' and c22 == 'O' and c32 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c13 == 'O' and c23 == 'O' and c33 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c11 == 'O' and c22 == 'O' and c33 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c13 == 'O' and c22 == 'O' and c31 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False

      if c11 == 'X' and c12 == 'X' and c13 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c21 == 'X' and c22 == 'X' and c23 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c31 == 'X' and c32 == 'X' and c33 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c12 == 'X' and c21 == 'X' and c31 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c12 == 'X' and c22 == 'X' and c32 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c13 == 'X' and c23 == 'X' and c33 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c11 == 'X' and c22 == 'X' and c33 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c13 == 'X' and c22 == 'X' and c31 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      loop1 = True
      while loop1:
          print('1  2  3')
          print(c11,'',c12,'',c13, '1')
          print(c21,'',c22,'',c23, '2')
          print(c31,'',c32,'',c33, '3')
          print()
          print("It is", p2name, "'s turn. Input the coordinates as the format xy.")
          coords = input()
          if coords == '11' and c11 == '?':
              c11 = 'X'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '12' and c12 == '?':
              c12 = 'X'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '13' and c13 == '?':
              c13 = 'X'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '21' and c21 == '?':
              c21 = 'X'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '22' and c22 == '?':
              c22 = 'X'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '23' and c23 == '?':
              c23 = 'X'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '31' and c31 == '?':
              c31 = 'X'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '32' and c32 == '?':
              c32 = 'X'
              print('Good job!')
              print()
              loop1 = False
          elif coords == '33' and c33 == '?':
              c33 = 'X'
              print('Good job!')
              print()
              loop1 = False
          else:
              print('That is not a valid coordinate.')
      if c11 == 'O' and c12 == 'O' and c13 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c21 == 'O' and c22 == 'O' and c23 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c31 == 'O' and c32 == 'O' and c33 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c12 == 'O' and c21 == 'O' and c31 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c12 == 'O' and c22 == 'O' and c32 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c13 == 'O' and c23 == 'O' and c33 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c11 == 'O' and c22 == 'O' and c33 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False
      if c13 == 'O' and c22 == 'O' and c31 == 'O':
          print("Congratulations!", p1name, "won the game!")
          loop = False

      if c11 == 'X' and c12 == 'X' and c13 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c21 == 'X' and c22 == 'X' and c23 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c31 == 'X' and c32 == 'X' and c33 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c12 == 'X' and c21 == 'X' and c31 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c12 == 'X' and c22 == 'X' and c32 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c13 == 'X' and c23 == 'X' and c33 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c11 == 'X' and c22 == 'X' and c33 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
      if c13 == 'X' and c22 == 'X' and c31 == 'X':
          print("Congratulations!", p2name, "won the game!")
          loop = False
  
elif niput == 2:
  print("Welcome to Scuffed Bank Robbing Simulator!")
  money = 0
  totalmoney = 0
  timesevadedtaxes = 0
  jobchance = 0
  bananacount = 0
  petaxolotls = 0
  bankteir = 'trash'
  bankmoney = 100
  town = 'placeholder'
  choice = 'placeholder'
  password = 'test86'
  jailchance = 250
  upgradecost = 150
  bankmoney2 = 0
  passlengthmax = 6
  passlengthmin = 2

  print('CoderBoy presents:')
  time.sleep(2.5)
  print('Bank Robbing Simulator Beta!!!!')
  print('Please choose your town name.')
  town = input()
  if town == 'test':
      print('type the password')
      password = input()
      if password == 'test86':
          money = 1000000
          totalmoney = 1000000
      else:
          print('Grrrrrr')
  else:
      town = town
  playing = True
  while playing == True:
      print('You have', money, 'dollars and ', bananacount, 'banananananas.')
      ##print('Your chance to get a job is', jobchance,'.')
      print('The bank tier in', town, 'is', bankteir,'.')
      time.sleep(1)
      print('Would you like to rob a bank? The chance that you will be thrown in jail is 1 in', jailchance,'. Type rob.')
      print('Would you like to upgrade to a better bank teir for $', upgradecost, '. Type upgrade.')
      choice = input()
      if choice == 'rob':
          thingy = random.randint(1,6)
          if thingy == 1:
              print('Okay')
              print("Here's how you do it.")
              time.sleep(2)
              passwod = secrets.token_hex(random.randint(passlengthmin,passlengthmax))
              print('You have to type in the password,', passwod,'.')
              time.sleep(2)
              print('You are now entering the bananananana bank. Do not type the password yet.')
              time.sleep(6)
              print('You are in the bank.')
              print('Please type in the password')
              passs = input()
              if passs == passwod:
                  caught = random.randint(1,100)
                  if caught == 0:
                      print('You got caught!!!!! Game over.')
                      playing = False
                  else:
                      moneygot = random.randint(1,50)
                      print('You got', moneygot, 'banananananas from robbing the bank')
                      print('')
                      bananacount += moneygot

          else:
              print('Okay')
              print("Here's how you do it.")
              time.sleep(2)
              passwod = secrets.token_hex(random.randint(passlengthmin,passlengthmax))
              print('You have to type in the password,', passwod,'.')
              time.sleep(2)
              print('You are now entering the bank. Do not type the password yet.')
              time.sleep(6)
              print('You are in the bank.')
              print('Please type in the password')
              passs = input()
              if passs == passwod:
                  caught = random.randint(0,jailchance)
                  if caught == 0:
                      print('You got caught!!!!! Game over.')
                      playing = False
                  else:
                      moneygot = random.randint(bankmoney2,bankmoney)
                      print('You got', moneygot, 'money from robbing the bank')
                      print('')
                      money += moneygot
                      totalmoney += moneygot

              else:
                  print('You got caught!!! Game over.')
                  playing = False
      elif choice == 'upgrade' and money >= upgradecost:
          print('Please choose a name for your new city.')
          town = input()
          print('Your city is now', town, '.')
          if bankteir == 'trash':
              bankteir = 'slightly below average'
          elif bankteir == 'slightly below average':
              bankteir = 'average'
          elif bankteir == 'average':
              bankteir = 'slightly above average'
          elif bankteir == 'slightly above average':
              bankteir = 'above average'
          elif bankteir == 'above average':
              bankteir = 'great'
          elif bankteir == 'great':
              bankteir = 'Fort Knox'
              bankmoney = 1000
              bankmoney2 = 1000
          else:
              print('Hmmmmm...')
          if jailchance < 100:
              jailchance = 100
          else:
              jailchance -= 40
          bankmoney += 50
          money -= upgradecost
          passlengthmax += 2
          passlengthmin += 2
          bankmoney2 += 50
          upgradecost += upgradecost * 0.25


      else:
          print('That is not a real action')

  
elif niput == 3:
  print("Welcome to Game of Life!")
  money = random.randint(1,50)
  bankaccountpass = 'placeholder'
  name = 'placeholder'
  smartness = 50
  age = 0



  jobtype = 'placeholder'
  jobmoney = 0
  extrajob = 'placeholder'
  ejobmoney = 0
  joblevel = 0

  extrajobs = 1
  joblevelprogress = 0
  joblevelprogresslimit = 20

  haspass = 0
  hasmarker = 0
  hasbook = 0
  haspaper = 0
  hascomputer = 0
  hasdesk = 0

  global personality
  personality = 0
  jobs = 1

  recentdeposit = 0
  bankmoney = 10
  shopspace1 = 'placeholder'
  shopspace2 = 'placeholder'
  shopspace3 = 'placeholder'
  sickness = 'none'


  peoplestat = 0
  techstat = 0
  indoorstat = 0
  outdoorstat = 0
  creativestat = 0


  day = 1
  year = 1
  incollege = 0
  bpres = 'placeholder'
  #intro
  time.sleep(3)
  print('Hello. Welcome to The game of life 1.13.9, where you can distract yourself by playing with a digital person!')
  print('What would you like to be called?')
  name = input()
  print('Hello,', name, 'welcome to the')
  time.sleep(1)
  print('Game!')
  time.sleep(1)
  print('Of!')
  time.sleep(1)
  print('Life!!')
  time.sleep(2)
  print("Okay. Now it's time to set your personality traits. These can raise or lower over time, but these traits will control what jobs you are able to get in the future.")
  print("You must answer with the numbers 0-100, 0 being absolutely not and 100 being absolutely yes.")
  time.sleep(1)

  #personality traits
  loop1 = True
  while loop1 == True:
   print('')
   print('How much of a people person are you?')
   statpeople = input('Must be a number!  ')
   numeric = statpeople.isnumeric()
   if numeric == False:
       print('You have to enter a number.')
   elif numeric == True:
       peoplestat = int(statpeople)
       if peoplestat >= 0 and peoplestat <= 100:
           print('Good job!')
           loop1 = False
       else:
           print('That is not a valid number.')
           loop1 = True


  loop1 = True
  while loop1 == True:
   print('')
   print('How much do you like technology?')
   stattech = input('Must be a number!  ')
   numeric = stattech.isnumeric()
   if numeric == False:
       print('You have to enter a number.')
   elif numeric == True:
      techstat = int(stattech)
      if techstat >= 0 and techstat <= 100:
           print('Good job!')
           loop1 = False
      else:
           print('That is not a valid number.')
           loop1 = True

  loop1 = True
  while loop1 == True:
   print('')
   print('How creative are you?')
   statcreate = input('Must be a number!  ')
   numeric = statcreate.isnumeric()
   if numeric == False:
       print('You have to enter a number.')
   elif numeric == True:
      creativestat = int(statcreate)
      if creativestat >= 0 and creativestat <= 100:
          print('Good job!')
          loop1 = False
      else:
           print('That is not a valid number.')
           loop1 = True


  loop1 = True
  while loop1 == True:
   print('')
   print('How much do you like the outdoors?')
   statout = input('Must be a number!  ')
   numeric = statout.isnumeric()
   if numeric == False:
       print('You have to enter a number.')
   elif numeric == True:
      outdoorstat = int(statout)
      if outdoorstat >= 0 and outdoorstat <= 100:
          print('Good job!')
          #outdoorstat -= 10
          loop1 = False
      else:
          print('That is not a valid number.')
          loop1 = True

  print()
  loop1 = True
  while loop1 == True:
   print('')
   print('How much do you like the indoors?')
   statin = input('Must be a number!  ')
   numeric = statin.isnumeric()
   if numeric == False:
      print('You have to enter a number.')
   elif numeric == True:
      indoorstat = int(statin)
      if indoorstat >= 0 and indoorstat <= 100:
          print('Good job!')
          loop1 = False
      else:
          print('That is not a valid number.')
          loop1 = True


  print('')
  print('Now, you have to create a bank account. This account is where you can store coins and are able to get interest every year.')
  print(name, ', please choose your password for your bank account. ')
  bankaccountpass = input()
  print("Ok, now remember that. You'll need it to access your bank account later.")
  print('')

  loop = True
  while loop == True:
      job = random.randint(1,7)
      if job == 1 and outdoorstat >= 40:
          jobtype = 'ice cream worker'
          jobmoney = 5
          loop = False
      elif job == 2 and peoplestat >= 50:
          jobtype = 'fast food worker'
          jobmoney = 6
          loop = False
      elif job == 3 and peoplestat >= 45:
          jobtype = 'cashier'
          jobmoney = 6
          loop = False
      elif job == 4:
          jobtype = 'nothing'
          jobmoney = 2
          loop = False
      elif job == 5 and creativestat >= 60:
          jobtype = 'meme maker'
          jobmoney = 7
          loop = False
      elif job == 6 and outdoorstat >= 35:
          jobtype = 'salesman'
          jobmoney = 6
          loop = False
      elif job == 7 and techstat >= 60:
          jobtype = 'youtuber'
          jobmoney = 6
          loop = False
      else:
          jobtype = 'laborer'
          jobmoney = 5
          loop = False
  #personality1 = techy personality2 = peopley personality3 = doodler personality4 = general


  #def personalityt(personality): 

  if techstat >= 60 and indoorstat >= 30 and outdoorstat <= 80 and peoplestat <= 70:
      personality = 1
      #return [personality]

  elif peoplestat >= 60 and outdoorstat >= 40 and creativestat >= 60:
      personality = 2
      #return [personality]

  elif indoorstat >= 50 and creativestat >= 65:
      personality = 3
      #return [personality]

  else:
      personality = 4
      #return [personality]


  #personalityt(personality)
  print('Would you like a quick tutorial? y/n')
  tutorial = input()
  if tutorial == 'y':
   print('')
   print("In this game, you will go to college, get a job and much more! Here's a quick tutorial.")
   print('In this game, time is measured in days and years. There are 15 days in a year. You can do different things each day, and you unlock more things to do from the store')
   print('If you see an action you would like to take, look at what is in the parenthesis (), and that is what you type to do that action.')
   print("Here's an example:")
   print('')
   loop1 = True
   while loop1 == True:
       print('Would you like to go to the shop (buy)?')
       print('Type what is in the parentheses.')
       thing = input()
       if thing == 'buy':
           print('Good job! Now you are in the shop, where you can buy things!')
           print('')
           print('What would you like to buy? You have 15 coins.')
           print('Book (book): 15 coins. Desk (desk): 50 coins. Computer (puter): 150 coins.')
           print('')
           print('Looks like you can only buy a book. Type book. ')
           thing = input()
           if thing == 'book':
               print('Good job! You have unlocked a new pastime: Reading!')
               print('')
               print('That is the end of this tutorial, but there are still things to learn, but you will learn along the way.')
               loop1 = False
           else:
               print('That is not right. You must type book, because you have no money for anything else.')
               print("Let's start over.")
               print('')
               loop1 = True
       else:
           print('That is not right. The only action you can take here is buy.')
           print('')
           loop1 = True
  #Main game


  print('')
  loop1 = True
  while loop1 == True:
   if peoplestat < 0:
       peoplestat = 0
   elif peoplestat >= 101:
       peoplestat = 100
   elif techstat < 0:
       techstat = 0
   elif techstat > 100:
       techstat = 100
   elif creativestat < 0:
       creativestat = 0
   elif creativestat > 100:
       creativestat = 100
   elif outdoorstat < 0:
       outdoorstat = 0
   elif outdoorstat > 100:
       outdoorstat = 100
   elif indoorstat < 0:
       indoorstat  = 0
   elif indoorstat > 100:
       indoorstat = 100

   money = money
   print('')
   money += jobmoney
   print('Today is day', day, ', year', year, 'and you are', age, 'years old.')
   if jobs == 1:
      print('You are a', jobtype, 'and you make', jobmoney, 'coins per day.')
   elif jobs == 2:
      print('You are a', jobtype, 'and you make', jobmoney, 'coins per day. Your extra job is a level', joblevel, extrajob, 'and you make', ejobmoney, 'coins per work.')
   print('You have', money, 'coins and', smartness, 'smartness.')
   if day == 1 and year != 1:
       intrestmoney = bankmoney * 0.15
       print('Today you got interest on your bank account! You got', intrestmoney, 'coins in interest!')
       bankmoney += intrestmoney

   print('What would you like to do today,', name,'? You can wait(wait), end the game(end), go to the store(buy), ')
   print('check your bank account (check),  check your stats (stats), or look at jobs (job).')
   if jobs == 2 and extrajobs == 1:
       print('You can work your second job(work)')
   if hasbook == 1:
       print('You can read (read)!')
   if incollege == 1:
       print('You can also study (study).')
   if day == 1 and year != 1:
       bmoney = random.randint(50,100)
       print("It's your birthday!")
       print('You got', bmoney, 'dollars from your grandma!')
       money += bmoney


  #        bpres = random.randint(1,15)
  #        #generates random number :)
  #        if bprez == 1:
  #            print
       #find the item classified with that number
       #also get money

   if day == 5 and year == 1 and incollege == 0:
      print('You can now go to college! Would you like to? this will take until day 1 year 3. This costs 30 coins.  y/n')
      college = input()

      if college == 'y' and money >= 30:
          incollege = 1
          print('You have successfully been enrolled into college.')
          print('To complete college, you must have 150 or more smartness.')
          money -= 30
      elif college == 'y' and money < 30:
          print('You do not have enough money to go to college.')
          incollege = 3
      else:
          print('You chose not to go to college')
          incollege = 2

   if day == 1 and year ==3 and incollege == 1 and smartness >= 150:
       print('You have successfully completed college! You have now unlocked better jobs!')
       extrajobs = 1

   elif day == 1 and year ==2 and incollege == 1 and smartness <= 149:
       print('Sadly, you have not passed college because you were not smart enough. :0')
   day += 1
   if day == 16:
       year += 1
       day = 1
   else:
       day = day
   choose = input()
   if choose == 'wait':
       print('Today you waited.')
   elif choose == 'work' and jobs == 2 and extrajobs == 1:
       print('You worked today and got', ejobmoney, 'more dollars.')
       money += ejobmoney
       joblevelprogress += 1
       if joblevelprogress < joblevelprogresslimit:
           print('You are now 1 xp closer to leveling up. You have', joblevelprogress, 'out of', joblevelprogresslimit, 'xp needed to level up.')
       elif joblevelprogress == joblevelprogresslimit:
           joblevelprogresslimit += 30
           joblevelprogress = 0
           joblevel += 1
           ejobmoney += 5
           print('You leveled up your job! You are now level', joblevel, 'and you job money has gone up by 5.')




   elif choose == 'stats':
       print('Your stats are:')
       print('People stat:', peoplestat)
       print('Technology stat:', techstat)
       print('Creativity stat:', creativestat)
       print('Indoor stat:', indoorstat)
       print('and outdoor stat:', outdoorstat)

   elif choose == 'end':
       print('You ended the game. You made it to day', day, 'year', year, '')

   elif choose == 'study' and incollege == 1:
       smart = random.randint(2,15)
       print('You studied for a test and got plus', smart, 'more smart.')
       smartness += smart
   elif choose == 'w':
       print(personality)

   elif choose == 'read':
       smartgain = random.randint(5,10)
       peoplegain = random.randint(1,10)
       print('You have read and gained +', smartgain, 'more startness and -', peoplegain, 'people stat.')
       peoplestat -= peoplegain
       smartness += smartgain
   elif choose == 'job':
       if extrajobs != 1:
           print('This setting is locked and will continue to be locked until you pass college.')
       elif extrajobs == 1:

           print('Welcome to the job menu!')
           print('You have unlocked better jobs!!')
           print('There are a few jobs available for you:')
           chance = random.randint(1,100)
           if chance == 1:
               print('You have the EXTREMELY rare chance of becoming a blacksmith (blacksmith). This job pays 20 coins per work but is very hard to level up.')
           #techy personality
           if personality == 1:

               print('Coder (coder): 10 coins per work, is a bit hard to level up')
               print('Engineer (engi): 12 coins per work, is moderately hard to level up')
               print('Youtuber (youtube): 15 coins per work, is very hard to level up')
               ting = input()
               if ting == 'coder':
                   jobs = 2
                   extrajob = 'coder'
                   ejobmoney = 10
                   joblevel = 1
                   print("You chose to be a coder. You have this job on top of your old job, and you use the function 'work' to work andd make this money. The more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 20
               elif ting == 'engi':
                   jobs = 2
                   extrajob = 'engineer'
                   ejobmoney = 12
                   joblevel = 1
                   print("You chose to be an engineer. You have this job on top of your old job, and you use the function 'work' to work andd make this money. The more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 30
               elif ting == 'youtube':
                   jobs = 2
                   joblevel = 1
                   extrajob = 'youtuber'
                   ejobmoney = 15
                   print("You chose to be a youtuber. You have this job on top of your old job, and you use the function 'work' to work andd make this money. The more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 40
               elif ting == 'blacksmith' and chance == 1:
                   jobs = 2
                   extrajob = 'blacksmith'
                   ejobmoney = 20
                   joblevel = 1
                   print("You chose to be an blacksmith. Good choice. You have this job on top of your old job, and you use the function 'work' to work andd make this money. The more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 50
               else:
                  print('That is not a valid job.')

           #peopley personality
           elif personality == 2:

               print('Teacher (teach): 8 coins per work, is a bit hard to level up')
               print('Reporter (report): 11 coins per work, is moderately hard to level up')
               print('Customer service representative (csr): 16 coins per work, is very hard to level up')
               ting = input()
               if ting == 'teach':
                   jobs = 2
                   extrajob = 'teach'
                   ejobmoney = 8
                   joblevel = 1
                   print("You chose to be a teacher. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 20
               elif ting == 'report':
                   jobs = 2
                   extrajob = 'reporter'
                   ejobmoney = 11
                   joblevel = 1
                   print("You chose to be a reporter. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 30
               elif ting == 'csr':
                   jobs = 2
                   joblevel = 1
                   extrajob = 'customer service representative'
                   ejobmoney = 16
                   print("You chose to be a customer service representative. You have this job on top of your old job, and you use the function 'work' to work and make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 40
               elif ting == 'blacksmith' and chance == 1:
                   jobs = 2
                   extrajob = 'blacksmith'
                   ejobmoney = 20
                   joblevel = 1
                   print("You chose to be an blacksmith. Good choice. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 50
               else:
                  print('That is not a valid job.')

           #creative personality
           elif personality == 3:

               print('Writer (writer): 9 coins per work, is a bit hard to level up')
               print('Artist (artist): 10 coins per work, is moderately hard to level up')
               print('Graphic designer (gd): 14 coins per work, is very hard to kevel up')
               ting = input()
               if ting == 'writer':
                   jobs = 2
                   extrajob = 'writer'
                   ejobmoney = 9
                   joblevel = 1
                   print("You chose to be a writer. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 20
               elif ting == 'artist':
                   jobs = 2
                   extrajob = 'artist'
                   ejobmoney = 10
                   joblevel = 1
                   print("You chose to be a artist. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 30
               elif ting == 'gd':
                   jobs = 2
                   joblevel = 1
                   extrajob = 'graphic designer'
                   ejobmoney = 16
                   print("You chose to be a graphic designer. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 40
               elif ting == 'blacksmith' and chance == 1:
                   jobs = 2
                   extrajob = 'blacksmith'
                   ejobmoney = 20
                   joblevel = 1
                   print("You chose to be an blacksmith. Good choice. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 50

               else:
                  print('That is not a valid job.')

           #other personality
           elif personality == 4:

               print('Architect (arch): 9 coins per work, is a bit hard to level up')
               print('Radiologist (radio): 10 coins per work, is moderately hard to level up')
               print('Biologist (bio): 14 coins per work, is very hard to kevel up')
               ting = input()
               if ting == 'arch':
                   jobs = 2
                   extrajob = 'architect'
                   ejobmoney = 9
                   joblevel = 1
                   print("You chose to be an architect. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 20
               elif ting == 'radio':
                   jobs = 2
                   extrajob = 'radiologist'
                   ejobmoney = 10
                   joblevel = 1
                   print("You chose to be a raiologist. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 30
               elif ting == 'bio':
                   jobs = 2
                   joblevel = 1
                   extrajob = 'biologist'
                   ejobmoney = 14
                   print("You chose to be a biologist. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 40
               elif ting == 'blacksmith' and chance == 1:
                   jobs = 2
                   extrajob = 'blacksmith'
                   ejobmoney = 20
                   joblevel = 1
                   print("You chose to be an blacksmith. Good choice. You have this job on top of your old job, and you use the function 'work' to work andd make this money. the more times you work, the faster it is to level up!")
                   joblevelprogresslimit = 50
               else:
                  print('That is not a valid job.')


           else:
               print("ErRoR...")



   elif choose == 'check':
       print('Please type in your bank account password.')
       pas = input()
       if pas == bankaccountpass:
           time.sleep(1)
           print('...')
           time.sleep(1)
           print('....')
           time.sleep(1)
           print('.....')
           time.sleep(2)
           print('You have accessed your bank account.')
           print('Your bank account has', bankmoney, 'coins in it')
           print('Your last deposit in your bank account was for', recentdeposit, 'coins.')
           print('What would you like to do in your bank account? You can deposit money (deposit) or take out money (take).')

           bankquest = input()

           if bankquest == 'deposit':
               print('')
               print('How much money would you like to deposit?')
               deposit = input()
               depositint = int(deposit)#not adding money to bank account, everything else is fine.
               if depositint > money:
                   print('You cannot deposit this much money.')
               elif depositint <= money:
                   print('You have deposited', depositint, 'coins.')
                   recentdeposit = depositint
                   bankmoney += depositint
                   money -= depositint
           elif bankquest == 'take':
               print('How much money do you want to take out of your bank account.')
               withdraw = input()
               withdrawint = int(withdraw)
               if withdrawint > bankmoney:
                   print('You cannot withdraw that much money.')
               elif withdrawint <= bankmoney:
                   print('You have wthdrawn', withdraw, 'coins.')
                   money += withdrawint
                   bankmoney -= withdrawint
           else:
               print('ErRoR...')
       else:
           print('Error: Incorrect password detected.')

   elif choose == 'buy':
       if hasbook == 0:
           print('Welcome to the shop! There is 1 thing for sale!.')
           print('You can buy a book (book) for 35 coins.')
           shop = input()
           if shop =='book' and money >= 35:
               print('You have bought a book! You have unlocked a new pastime: Reading!')
               hasbook = 1
               money -= 30
       elif hascomputer == 0:
           print('Welcome to the shop! There is 1 thing for sale.')
           print('You can buy a computer (puter) for 1,000 coins!')
           shop = input()
           if shop == 'puter' and money >= 1000:
               hascomputer = 1
               money -= 1000
               print('You have won the game,', name, '!!!')
               print('You ended the game with', smartness, 'smartness and', money, 'money!!!!!!')
               print('CONGRATULATIONS!!!!!!! You made it to day', day, 'year', year, 'and you had the job of a', jobtype, '!!!!!!!!!!!')
               loop1 = False
   else:
       print('That is not a real action.')
       day -= 1

  
elif niput == 4:
  print("Welcome to Axolotl Clicker!")
  totalaxolotls = 0
  goldenaxolotls = 0
  omegaaxolotls = 0
  diamondaxolotls = 0
  ultimateaxolotls = 0
  ascendcount = 0

  axolotlsinbank = 0
  axolotlspersecond = 0
  axolotlsperclick = 1
  heavenlyaxolotls = 0
  gaxolotlchance = 100
  upgradelevel = 0
  upgradecost = 1000
  extra = 0
  item1cost = 15
  item2cost = 100
  item3cost = 150
  item4cost = 500
  item5cost = 750
  item6cost = 1000
  item7cost = 1500
  item8cost = 2000
  item9cost = 7500

  goldentier = 0
  extracount = 0
  farmercount = 0
  aquarcount = 0
  spondcount = 0
  bfoodcount = 0
  mpondcount = 0
  lpondcount = 0
  lakecount = 0
  towncount = 0
  timesascended = 0

  difficulty = 1
  floodcount = 10
  hungerlost = 0
  extrathing = 0
  hasgod = 0
  counter = 0
  hasdetect = 0
  foodup = 20

  goal1 = 10000
  goal2 = 100000
  goal3 = 150000
  goal = 1000000000

  goal9 = 'unreached'
  goldenaxolotlchance = 0
  detectorcost = 500
  axolotlhunger = 101
  foodcost = 25
  playing = True
  loop = True

  print('CoderBoy presents')
  time.sleep(3)
  print('Axolotl Clicker 1.73!')

  print('This project was inspired by the game Cookie Clicker')
  print("Free Weekend!!! (we know it isn't the weekend, just roll with it.)")
  print('Newest update: Achievements!!!!! Also added: Bug fixes and more golden axolotl tiers. Also added secret building.')
  print('')

  print('Please choose the difficulty. Harder difficulty means that floods will happen more often and your axolotl will lose more hunger faster. Choose from easy, normal, or hard.')

  #this line is cursed, don't use it
  while loop == True:
      diffinput = input()
      if diffinput == 'easy':
          floodcount = 250
          print('You chose easy mode. your chances of getting a flood are 250 to 1 and your axolotl loses .5 hunger per turn.')
          hungerlost = 0.5
          axolotlhunger = 100.5
          loop = False
      elif diffinput == 'normal':
          floodcount = 100
          print('You chose normal mode. your chances of getting a flood are 100 to 1 and your axolotl loses 1 hunger per turn.')
          hungerlost = 1
          loop = False
      elif diffinput == 'hard':
          floodcount = 50
          print('You chose hard mode. your chances of getting a flood are 50 to 1 and your axolotl loses 2 hunger per turn.')
          hungerlost = 2
          axolotlhunger = 102
          loop = False
      elif diffinput == 'test':
          floodcount = 1000000000000000
          print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 0 hunger per turn.')
          hungerlost = 0
          axolotlsinbank = 1000000000
          totalaxolotls = 1000000000
          loop = False
      elif diffinput == 'test2':
          floodcount = 1000000000000000
          print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 100 hunger per turn.')
          hungerlost = 100
          axolotlsinbank = 1000000000
          totalaxolotls = 1000000000
          loop = False

      else:
          print('That is not a true difficulty. Please choose a real difficulty.')
          loop = True


  playing = True
  #the game
  while playing:
      if axolotlhunger <= 0:
          print("The game is over! You let your axolotl's hunger drop to 0!")
          print('Your final score was', totalaxolotls, 'axolotls.')
          print('Would you like to play again? y/n')
          playagain = input()
          if playagain == 'y':
              print('NoodlePole Games presents')
              print('Axolotl Clicker 1.0')
              print('This project was inspired by the game Cookie Clicker')
              print('')
              loop = True
              print('Please Choose a difficulty. Easy, normal, or hard')
              while loop == True:
                  diffinput = input()
                  if diffinput == 'easy':
                      floodcount = 250
                      print('You chose easy mode. your chances of getting a flood are 250 to 1 and you axolotl loses .5 hunger per turn.')
                      hungerlost = 0.5
                      axolotlhunger = 100.5
                      loop = False
                  elif diffinput == 'normal':
                      floodcount = 100
                      print('You chose normal mode. your chances of getting a flood are 100 to 1 and you axolotl loses 1 hunger per turn.')
                      hungerlost = 1
                      loop = False
                  elif diffinput == 'hard':
                      floodcount = 50
                      print('You chose hard mode. your chances of getting a flood are 50 to 1 and you axolotl loses 2 hunger per turn.')
                      hungerlost = 2
                      axolotlhunger = 102
                      loop = False
                  elif diffinput == 'test':
                      floodcount = 1000000000000000
                      print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 0 hunger per turn.')
                      hungerlost = 0
                      axolotlsinbank = 1000000000
                      totalaxolotls = 1000000000
                      loop = False
                  elif diffinput == 'test2':
                      floodcount = 1000000000000000
                      print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 100 hunger per turn.')
                      hungerlost = 100
                      axolotlsinbank = 1000000000
                      totalaxolotls = 1000000000
                      loop = False

                  else:
                      print('That is not a true difficulty. Please choose a real difficulty.')
                      loop = True

              totalaxolotls = 0
              axolotlsinbank = 0
              axolotlspersecond = 0
              axolotlsperclick = 1
              item1cost = 15
              item2cost = 100
              item3cost = 150
              item4cost = 500
              item5cost = 750
              item6cost = 1000
              item7cost = 1500
              item8cost = 2000
              item9cost = 7500
              extracount = 0
              goldentier = 0
              farmercount = 0
              aquarcount = 0
              spondcount = 0
              bfoodcount = 0
              mpondcount = 0
              lpondcount = 0
              lakecount = 0
              towncount = 0
              hasgod = 0
              hasdetect = 0
              foodup = 20
              goal1 = 10000
              goal2 = 100000
              goal3 = 150000
              goal = 1000000000
              goldenaxolotlchance = 0
              axolotlhunger = 101
              foodcost = 25
          else:
              playing = False


      if axolotlsinbank <= -1:
          print("The game is over! You have less than 0 axolotls left!")
          print('Your final score was', totalaxolotls, 'axolotls.')
          print('Would you like to play again? y/n')
          playagain = input()
          if playagain == 'y':
              print('NoodlePole Games presents')
              print('Axolotl Clicker 1.0')
              print('This project was inspired by the game Cookie Clicker')
              print('')
              loop = True
              print('Please Choose a difficulty. Easy, normal, or hard')
              while loop == True:
                  diffinput = input()
                  if diffinput == 'easy':
                      floodcount = 250
                      print('You chose easy mode. your chances of getting a flood are 250 to 1 and you axolotl loses .5 hunger per turn.')
                      hungerlost = 0.5
                      axolotlhunger = 100.5
                      loop = False
                  elif diffinput == 'normal':
                      floodcount = 100
                      print('You chose normal mode. your chances of getting a flood are 100 to 1 and you axolotl loses 1 hunger per turn.')
                      hungerlost = 1
                      loop = False
                  elif diffinput == 'hard':
                      floodcount = 50
                      print('You chose hard mode. your chances of getting a flood are 50 to 1 and you axolotl loses 2 hunger per turn.')
                      hungerlost = 2
                      axolotlhunger = 102
                      loop = False
                  elif diffinput == 'test':
                      floodcount = 1000000000000000
                      print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 0 hunger per turn.')
                      hungerlost = 0
                      axolotlsinbank = 1000000000
                      totalaxolotls = 1000000000
                      loop = False
                  elif diffinput == 'test2':
                      floodcount = 1000000000000000
                      print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 100 hunger per turn.')
                      hungerlost = 100
                      axolotlsinbank = 1000000000
                      totalaxolotls = 1000000000
                      loop = False

                  else:
                      print('That is not a true difficulty. Please choose a real difficulty.')
                      loop = True

              totalaxolotls = 0
              axolotlsinbank = 0
              axolotlsperclick = 1
              item1cost = 15
              item2cost = 100
              item3cost = 150
              item4cost = 500
              item5cost = 750
              item6cost = 1000
              item7cost = 1500
              item8cost = 2000
              item9cost = 7500
              extracount = 0
              goldentier = 0
              farmercount = 0
              aquarcount = 0
              spondcount = 0
              bfoodcount = 0
              mpondcount = 0
              lpondcount = 0
              lakecount = 0
              towncount = 0
              hasgod = 0
              hasdetect = 0
              foodup = 20
              goal1 = 10000
              goal2 = 100000
              goal3 = 150000
              goal = 1000000000
              goldenaxolotlchance = 0
              axolotlhunger = 101
              foodcost = 25
          else:
              playing = False


      axolotlsinbank += axolotlspersecond
      print('')


      if totalaxolotls == goal:
          goal += 500000000
          print('You have officially won axolotl clicker. No one has yet to make it this far. Your goal has been increased to', goal, '. As your reward, another thing has been opended in the shop for you. find out what it does. Congragutations. Contact me at jbacon1105@icloud.com to claim your prize. ;)')
          goal9 = 'reached'
          extrathing = 1
      elif goal9 == 'reached' and hasgod == 1:
          print('You have bought the axolotl god.')
          goal9 == 'finished'
      else:
          extrathing = 0
      round(axolotlsinbank, 0)
      round(item1cost, 0)
      round(item2cost, 0)
      round(item3cost, 0)
      round(item4cost, 0)
      round(item5cost, 0)
      round(item6cost, 0)
      round(item7cost, 0)
      round(item8cost, 0)
      round(item9cost, 0)

      print('You currently have ', axolotlsinbank, 'axolotls. You also have', goldenaxolotls, 'golden axolotls,', omegaaxolotls, 'omega axolotls,', diamondaxolotls, 'diamond aolotls, and', ultimateaxolotls, 'ultimate axolotls.')
      print('Your options are to click (c) or upgrade (upgrade).You can also type upgrade10 or upgrade100 to upgrade things more than once at a time.')
      print('If you would like to feed you axolotl, type feed.')
      print('You earned', axolotlspersecond, 'axolotls this turn.')


      happinessmeter = random.randint(1,100)
      if happinessmeter == 69:
          happymoney = random.randint(1,100)
          print('The axolotls are feeling happier than usual today! They are going to give you', happymoney, 'more axolotls!')
          axolotlsinbank += happymoney
          totalaxolotls += happymoney

      else:
          axolotlsinbank = axolotlsinbank

      tradermeter = random.randint(1,249)
      if tradermeter == 69:
          tradermoney = random.randint(100,500)
          print('An axolotl trader came through town and would like to invest in you. You got', tradermoney, ' axolotls.')
          axolotlsinbank += tradermoney
          totalaxolotls += tradermoney

      else:
          axolotlsinbank = axolotlsinbank

      floodmeter = random.randint(1,floodcount)
      if floodmeter == 1:
          axolotlslost = random.randint(1,100)
          if axolotlslost > axolotlsinbank:
              axolotlslost = axolotlsinbank
              print('Oh No! A flood came through town and you lost', axolotlslost, 'axolotls!')
              axolotlsinbank -= axolotlslost
          else:
              print('Oh No! A flood came through town and you lost', axolotlslost, 'axolotls!')
              axolotlsinbank -= axolotlslost
      else:
          axolotlsinbank = axolotlsinbank

      tmeter = random.randint(1,250)
      if tmeter == 1:
          taxolotlslost = random.randint(100,500)
          if taxolotlslost > axolotlsinbank:
              taxolotlslost = axolotlsinbank
              print('Oh No! A tsunami came through town and you lost', taxolotlslost, 'axolotls!')
              axolotlsinbank -= taxolotlslost
          else:
              print('Oh No! A tsunami came through town and you lost', taxolotlslost, 'axolotls!')
              axolotlsinbank -= taxolotlslost
      else:
          axolotlsinbank = axolotlsinbank

      axolotlhunger -= hungerlost
      print('Your axolotl has', axolotlhunger, 'percent hunger left.')
      if spondcount >= 1:
          pondchance = random.randint(1,250)
          if pondchance == 1:
              print('Oh no! The dam for one of your ponds has broken! If you would like to fix it for 200 axolotls, say y, if not, type n')
              pondanswer = input()
              if pondanswer == 'y' and axolotlsinbank >= 200:
                  print('You fixed the pond')
                  axolotlsinbank -= 200
              else:
                  print("Oops! You didn't have enough or you typed no.")
                  axolotlspersecond -= 5
                  spondcount -= 1

      #golden axolotls            
      if upgradelevel == 1:
          upgradecost = 5000
      elif upgradelevel == 2:
          upgradecost = 15000
      elif upgradelevel == 3:
          upgradecost = 45000
      elif upgradelevel == 3:
          upgradecost = 100000
      elif upgradelevel == 4:
          upgradecost = 150000
      elif upgradelevel == 5:
          upgradecost = 200000
      elif upgradelevel == 6:
          upgradecost = 250000
      elif upgradelevel == 7:
          upgradecost = 300000
      elif upgradelevel >= 8:
          upgradecost = upgradecost * 3

      else:
          upgradecost = upgradecost


      unluckychance = random.randint(1,250)
      if unluckychance == 69:
          if hasdetect == 1:
             print('Your unlucky Axolotl detector has detected an unlucky axolotl and helped you avoid a disaster!')

          elif hasdetect == 0:
              print('A golden axolotl has appeared! Would you like to click it? y/n')
              answerforaxolotl = input()
              if answerforaxolotl == 'y':
                  print('>:) You fell into my trap! Your axolotls have been divided by 1.5!')
                  axolotlsinbank / 1.5
                  randomamount = random.randint(1,100)
                  if randomamount >= axolotlsinbank: randomamount = axolotlsinbank
                  axolotlsinbank -= randomamount
                  print(randomamount, 'axolotls have been subtracted!')
              else:
                  print('Good job! That was an unlucky axollotl!')

      if upgradelevel == 0:
          goldenaxolotlchance = random.randint(0,gaxolotlchance)
          if goldenaxolotlchance == 1:
              goldenaxolotls += 1
              print('A golden Axolotl has appeared! Would you like to click it? y/n')
              goldenaxolotlanswer = input()
              if goldenaxolotlanswer == 'y':
                  print('Your axolotls have been multiplied by 2!')
                  totalaxolotls = totalaxolotls + axolotlsinbank
                  axolotlsinbank = axolotlsinbank * 2
                  moneygained = random.randint(0,1000)
                  print('You also earned', moneygained, 'axolotls!')
                  axolotlsinbank = axolotlsinbank + moneygained
                  totalaxolotls = totalaxolotls + moneygained
              elif goldenaxolotlanswer == 'n':
                  print('Next time, click it, seriously. You passed up so much money!')
              else:
                  print('That is not a valid action. please choose y/n')
                  goldenaxolotlanswer = input()
                  if goldenaxolotlanswer == 'y':
                      print('Your axolotls have been multiplied by 2!')
                      totalaxolotls = totalaxolotls + axolotlsinbank
                      axolotlsinbank = axolotlsinbank * 2
                      moneygained = random.randint(0,1000)
                      print('You also earned', moneygained, 'axolotls!')
                      axolotlsinbank = axolotlsinbank + moneygained
                      totalaxolotls = totalaxolotls + moneygained
                  elif goldenaxolotlanswer == 'n':
                      print('Next time click it, seriously? You passed up so much money!')


      elif upgradelevel == 1:
          goldenaxolotlchance = random.randint(0,gaxolotlchance)
          if goldenaxolotlchance == 69:
              goldenaxolotls += 1
              print('A golden Axolotl has appeared! Would you like to click it? y/n')
              goldenaxolotlanswer = input()
              if goldenaxolotlanswer == 'y':
                  print('Your axolotls have been multiplied by 2.5!')
                  totalaxolotls = totalaxolotls + axolotlsinbank * 1.5
                  axolotlsinbank = axolotlsinbank * 2.5
                  moneygained = random.randint(1000,10000)
                  print('You also earned', moneygained, 'axolotls!')
                  axolotlsinbank = axolotlsinbank + moneygained
                  totalaxolotls = totalaxolotls + moneygained
              elif goldenaxolotlanswer == 'n':
                  print('Next time click it, seriously? You passed up so much money!')
              else:
                  print('That is not a valid action. please choose y/n')
                  goldenaxolotlanswer = input()
                  if goldenaxolotlanswer == 'y':
                      print('Your axolotls have been multiplied by 2.5!')
                      totalaxolotls = totalaxolotls + axolotlsinbank * 1.5
                      axolotlsinbank = axolotlsinbank * 2.5
                      moneygained = random.randint(1000,10000)
                      print('You also earned', moneygained, 'axolotls!')
                      axolotlsinbank = axolotlsinbank + moneygained
                      totalaxolotls = totalaxolotls + moneygained
                  elif goldenaxolotlanswer == 'n':
                      print('Next time click it, seriously? You passed up so much money!')


      elif upgradelevel == 2:
          goldenaxolotlchance = random.randint(0,gaxolotlchance)
          if goldenaxolotlchance == 69:
              goldenaxolotls += 1
              print('A golden Axolotl has appeared! Would you like to click it? y/n')
              goldenaxolotlanswer = input()
              if goldenaxolotlanswer == 'y':
                  print('Your axolotls have been multiplied by 3!')
                  totalaxolotls = totalaxolotls + axolotlsinbank * 2
                  axolotlsinbank = axolotlsinbank * 3
                  moneygained = random.randint(10000,50000)
                  print('You also earned', moneygained, 'axolotls!')
                  axolotlsinbank = axolotlsinbank + moneygained
                  totalaxolotls = totalaxolotls + moneygained
              elif goldenaxolotlanswer == 'n':
                  print('Next time click it, seriously? You passed up so much money!')
              else:
                  print('That is not a valid action. please choose y/n')
                  goldenaxolotlanswer = input()
                  if goldenaxolotlanswer == 'y':
                      print('Your axolotls have been multiplied by 3!')
                      totalaxolotls = totalaxolotls + axolotlsinbank * 2
                      axolotlsinbank = axolotlsinbank * 3
                      moneygained = random.randint(10000,50000)
                      print('You also earned', moneygained, 'axolotls!')
                      axolotlsinbank = axolotlsinbank + moneygained
                      totalaxolotls = totalaxolotls + moneygained
                  elif goldenaxolotlanswer == 'n':
                      print('Next time click it, seriously? You passed up so much money!')


      elif upgradelevel == 3:
          goldenaxolotlchance = random.randint(0,gaxolotlchance)
          if goldenaxolotlchance == 69:
              goldenaxolotls += 1
              print('A golden Axolotl has appeared! Would you like to click it? y/n')
              goldenaxolotlanswer = input()
              if goldenaxolotlanswer == 'y':
                  print('Your axolotls have been multiplied by 3.5!')
                  totalaxolotls = totalaxolotls + axolotlsinbank * 2.5
                  axolotlsinbank = axolotlsinbank * 3.5
                  moneygained = random.randint(50000,100000)
                  print('You also earned', moneygained, 'axolotls!')
                  axolotlsinbank = axolotlsinbank + moneygained
                  totalaxolotls = totalaxolotls + moneygained
              elif goldenaxolotlanswer == 'n':
                  print('Next time click it, seriously? You passed up so much money!')
              else:
                  print('That is not a valid action. please choose y/n')
                  goldenaxolotlanswer = input()
                  if goldenaxolotlanswer == 'y':
                      print('Your axolotls have been multiplied by 3.5!')
                      totalaxolotls = totalaxolotls + axolotlsinbank * 2.5
                      axolotlsinbank = axolotlsinbank * 3.5
                      moneygained = random.randint(50000,100000)
                      print('You also earned', moneygained, 'axolotls!')
                      axolotlsinbank = axolotlsinbank + moneygained
                      totalaxolotls = totalaxolotls + moneygained
                  elif goldenaxolotlanswer == 'n':
                      print('Next time click it, seriously? You passed up so much money!')


      elif upgradelevel == 4:
          goldenaxolotlchance = random.randint(0,gaxolotlchance)
          if goldenaxolotlchance == 69:
              goldenaxolotls += 1
              print('A golden Axolotl has appeared! Would you like to click it? y/n')
              goldenaxolotlanswer = input()
              if goldenaxolotlanswer == 'y':
                  print('Your axolotls have been multiplied by 4!')
                  totalaxolotls = totalaxolotls + axolotlsinbank * 3
                  axolotlsinbank = axolotlsinbank * 4
                  moneygained = random.randint(150000,150000)
                  print('You also earned', moneygained, 'axolotls!')
                  axolotlsinbank = axolotlsinbank + moneygained
                  totalaxolotls = totalaxolotls + moneygained
              elif goldenaxolotlanswer == 'n':
                  print('Next time click it, seriously? You passed up so much money!')
              else:
                  print('That is not a valid action. please choose y/n')
                  goldenaxolotlanswer = input()
                  if goldenaxolotlanswer == 'y':
                      print('Your axolotls have been multiplied by 4!')
                      totalaxolotls = totalaxolotls + axolotlsinbank * 3
                      axolotlsinbank = axolotlsinbank * 4
                      moneygained = random.randint(150000,150000)
                      print('You also earned', moneygained, 'axolotls!')
                      axolotlsinbank = axolotlsinbank + moneygained
                      totalaxolotls = totalaxolotls + moneygained
                  elif goldenaxolotlanswer == 'n':
                      print('Next time click it, seriously? You passed up so much money!')

      elif upgradelevel == 5:
          goldenaxolotlchance = random.randint(0,gaxolotlchance)
          if goldenaxolotlchance == 69:
              goldenaxolotls += 1
              print('A golden Axolotl has appeared! Would you like to click it? y/n')
              goldenaxolotlanswer = input()
              if goldenaxolotlanswer == 'y':
                  print('Your axolotls have been multiplied by 4.5!')
                  totalaxolotls = totalaxolotls + axolotlsinbank * 3.5
                  axolotlsinbank = axolotlsinbank * 4.5
                  moneygained = random.randint(150000,150000)
                  print('You also earned', moneygained, 'axolotls!')
                  axolotlsinbank = axolotlsinbank + moneygained
                  totalaxolotls = totalaxolotls + moneygained
              elif goldenaxolotlanswer == 'n':
                  print('Next time click it, seriously? You passed up so much money!')
              else:
                  print('That is not a valid action. please choose y/n')
                  goldenaxolotlanswer = input()
                  if goldenaxolotlanswer == 'y':
                      print('Your axolotls have been multiplied by 4!')
                      totalaxolotls = totalaxolotls + axolotlsinbank * 3
                      axolotlsinbank = axolotlsinbank * 4
                      moneygained = random.randint(150000,150000)
                      print('You also earned', moneygained, 'axolotls!')
                      axolotlsinbank = axolotlsinbank + moneygained
                      totalaxolotls = totalaxolotls + moneygained
                  elif goldenaxolotlanswer == 'n':
                      print('Next time click it, seriously? You passed up so much money!')


      elif upgradelevel == 6:
          goldenaxolotlchance = random.randint(0,gaxolotlchance)
          if goldenaxolotlchance == 69:
              goldenaxolotls += 1
              print('A golden Axolotl has appeared! Would you like to click it? y/n')
              goldenaxolotlanswer = input()
              if goldenaxolotlanswer == 'y':
                  print('Your axolotls have been multiplied by 5!')
                  totalaxolotls = totalaxolotls + axolotlsinbank * 4
                  axolotlsinbank = axolotlsinbank * 5
                  moneygained = random.randint(150000,150000)
                  print('You also earned', moneygained, 'axolotls!')
                  axolotlsinbank = axolotlsinbank + moneygained
                  totalaxolotls = totalaxolotls + moneygained
                  #the scred line
              elif goldenaxolotlanswer == 'n':
                  print('Next time click it, seriously? You passed up so much money!')
              else:
                  print('That is not a valid action. please choose y/n')
                  goldenaxolotlanswer = input()
                  if goldenaxolotlanswer == 'y':
                      print('Your axolotls have been multiplied by 4!')
                      totalaxolotls = totalaxolotls + axolotlsinbank * 3
                      axolotlsinbank = axolotlsinbank * 4
                      moneygained = random.randint(150000,150000)
                      print('You also earned', moneygained, 'axolotls!')
                      axolotlsinbank = axolotlsinbank + moneygained
                      totalaxolotls = totalaxolotls + moneygained
                  elif goldenaxolotlanswer == 'n':
                      print('Next time click it, seriously? You passed up so much money!')            
  #buying                    

      if totalaxolotls >= goal1:
          foodcost = 75
          print('The food cost was raised!')
          goal1 = 999999999999999
      elif totalaxolotls >= goal2:
          foodcost = 100
          print('the food cost was raised!')
          goal2 = 999999999999999
      elif totalaxolotls >= goal3:
          foodcost = 1000
          print('The food cost was raised! It will no longer raise.')
          goal3 = 99999999999999999
      else:
          foodcost = foodcost

      action = input()
      if action == 'c':
          axolotlsinbank = axolotlsinbank + axolotlsperclick
          totalaxolotls = totalaxolotls + axolotlsperclick
          totalaxolotls = totalaxolotls + axolotlspersecond

      elif action == 'c100':
          axolotlsinbank = axolotlsinbank + axolotlsperclick * 100
          totalaxolotls = totalaxolotls + axolotlsperclick * 100
          totalaxolotls = totalaxolotls + axolotlspersecond * 100

      elif action == 'upgrade':
          print('There are some things for sale')
          loop3 = True
          while loop3 == True:
              print('')
              print('You can now choose which upgrade category to buy from: buildings, golden axolotls, special, and misc.')
              upgrade = input()
              if upgrade == 'golden axolotls':
                  loop3 = False
                  if upgradelevel == 6:
                      print('You have the max amount of golden axolotl upgrades.')
                      print('')
                  else:
                      print('You can upgrade your golden axolotl to level', goldentier + 1, '(upgrade) for', upgradecost, 'axolotls (Warning: this only takes effect levels 1 through 7')
                      print('')
                      print('You can merge your golden axolotls together, just type merge')

              elif upgrade == 'misc':
                  loop3 = False
                  if hasdetect == 1:
                      hasdetect = 1
                      print('You have already bought the unlucky axolotl detector.')
                  else:
                      print("You can buy the upgrade 'Unlucky Axolotl detector' (detector) for 500 axolotls")
                      print('')
                  print('If you would like to check how many of each building you currently have, type buildcheck')
                  print('You can also check your acheivements (achievs)!')
                  print('')
                  print("If you ever want to end the game, type 'end'.")
                  print('If you would like to check your total score, type score')
                  print('')

              elif upgrade == 'buildings':
                  loop3 = False
                  print('You can buy Extra axolotls per click(extra), for', item1cost, 'axolotls. An Axolotl Farmer(farmer) for', item2cost, 'axolotls. An aquarium(aquar) for', item3cost, "axolotls. A small pond of axolotls(pond) for", item4cost, 'axolotls.')
                  print('You can buy Better axolotl food(foodbetter), for', item5cost, 'axolotls. A medium pond(mpond) for', item6cost, 'axolotls. A large pond(lpond) for', item7cost, 'axolotls. An axolotl lake(lake) for', item8cost, 'axolotls. An axolotl town for (town) for', item9cost, 'axolotls.')
                  print('')

              elif upgrade == 'special':
                  loop3 = False
                  if goal9 == 'reached':
                      print('You have unlocked Axolotl god. He costs 1 Billion axolotls, and if you buy him, well, just find out. Type god')
                      print('')
                  elif hasgod == 1:
                      print('You are now able to ascend. Type ascend.')
                  else:
                      print('??????')
                      print('??????')
                      print('')


          print("If you don't have enough money for anything, type no")
          action2 = input()

  #extra       
          if action2 == 'extra' and axolotlsinbank >= item1cost:
              print('You made your axolotls per click go up by 1!')
              axolotlsperclick = axolotlsperclick + 1
              axolotlsinbank = axolotlsinbank - item1cost
              item1cost = item1cost *1.1
              extracount += 1
              print('')
  #farmer             
          elif action2 == 'farmer' and axolotlsinbank >= item2cost:
              print('You made your axolotls per turn go up by 1!')
              axolotlspersecond = axolotlspersecond + 1
              axolotlsinbank = axolotlsinbank - item2cost
              item2cost = item2cost *1.1
              farmercount += 1
              print('')
  #aquar            
          elif action2 == 'aquar' and axolotlsinbank >= item3cost:
              print('You made your axolotls per click go up by 5!')
              axolotlsperclick = axolotlsperclick + 5
              axolotlsinbank = axolotlsinbank - item3cost
              item3cost = item3cost *1.1
              aquarcount += 1
              print('')
  #pond
          elif action2 == 'pond' and axolotlsinbank >= item4cost:
              print('You made your axolotls per turn go up by 5!')
              axolotlspersecond = axolotlspersecond + 5
              axolotlsinbank = axolotlsinbank - item4cost
              item4cost = item4cost *1.1
              spondcount += 1
              print('')
  #foodbetter
          elif action2 == 'foodbetter' and axolotlsinbank >= item5cost:
              print('You made the amount of hunger that your axolotl gets when you feed it went up by 5%')
              foodup += 5
              axolotlsinbank -= item5cost
              item5cost *= 1.1
              print('')
  #mpond
          elif action2 == 'mpond' and axolotlsinbank >= item6cost:
              print('You made your axolotls per turn go up by 10!')
              axolotlspersecond = axolotlspersecond + 10
              axolotlsinbank = axolotlsinbank - item6cost
              item6cost = item6cost *1.1
              mpondcount += 1
              print('')
  #lpond  
          elif action2 == 'lpond' and axolotlsinbank >= item7cost:
              print('You made your axolotls per click go up by 25!')
              axolotlsperclick = axolotlsperclick + 25
              axolotlsinbank = axolotlsinbank - item7cost
              item7cost = item7cost *1.1
              lpondcount += 1
              print('')
  #god
          elif action2 == 'god' and axolotlsinbank >= 1000000000:
              if hasgod == 1:
                  print('You have already bought the axolotl god.')
              else:
                  print('You are now a true axolotl god. You have made every stat go up by 100000.')
                  axolotlsperclick += 100000
                  axolotlspersecond += 100000
                  axolotlsinbank -= 1000000000
                  hasgod = 1
                  goal9 = 'finished'

  #acsend
          elif action2 == 'ascend' and hasgod == 1 and totalaxolotls >= 1000000000:
              hasascended = 1
              ascendcount =+ 1

              heavenlyaxolotls += 10
              loop2 = True
              while loop2 == True:

                  print('You are ascending...')
                  time.sleep(5)
                  print('You have ascended. You currently have', heavenlyaxolotls, 'heavenly axolotls.')
                  print('What would you like to do with your heavenly axolotls?')
                  print('You can make your restarting axolotls perclick go up by 0.5 for 10 heavenly axolotls. Type upgrade. If youwould not like to buy anything, type no')
                  decide = input()
                  if decide == 'upgrade' and heavenlyaxolotls >= 10:
                      print('You upraded your axolotls per click by 0.5.')
                      heavenlyaxolotls -= 10
                      ascendcount =+ 1
                      extra += 0.5
                      print('Would you like to purchase another thing?')
                      choice4 = input()
                      if choice4 == 'y':
                          loop2 = True
                      else:
                          print('You have returned to the mortal world.')
                          axolotlsinbank = 0
                          axolotlspersecond = 0
                          axolotlsperclick = 1 + extra
                          foodcost = 25
                          item1cost = 15
                          item2cost = 100 
                          item3cost = 150
                          item4cost = 500
                          item5cost = 750
                          item6cost = 1000
                          item7cost = 1500
                          item8cost = 2000
                          item9cost = 7500
                          extracount = 0
                          goldentier = 0
                          farmercount = 0
                          aquarcount = 0
                          spondcount = 0
                          bfoodcount = 0
                          mpondcount = 0
                          lpondcount = 0
                          lakecount = 0
                          towncount = 0
                          hasgod = 0
                          hasdetect = 0
                          foodup = 20
                          goal1 = 10000 * timesascended
                          goal2 = 100000 * timesascended
                          goal3 = 150000 * timesascended

                          goal = 1000000
                          goldenaxolotlchance = 0
                          axolotlhunger = 101
                          foodcost = 25
                          goal9 = 'unreached'
                          loop2 = False

                  elif decide == 'no':
                      print('You have decided to return to the mortal world.')
                      axolotlsinbank = 0
                      axolotlspersecond = 0
                      axolotlsperclick = 1
                      foodcost = 25
                      item1cost = 15
                      item2cost = 100 
                      item3cost = 150
                      item4cost = 500
                      item5cost = 750
                      item6cost = 1000
                      item7cost = 1500
                      item8cost = 2000
                      item9cost = 7500
                      extracount = 0
                      goldentier = 0
                      farmercount = 0
                      aquarcount = 0
                      spondcount = 0
                      bfoodcount = 0
                      mpondcount = 0
                      lpondcount = 0
                      lakecount = 0
                      towncountcount = 0
                      hasgod = 0
                      hasdetect = 0
                      foodup = 20
                      goal1 = 10000 * timesascended
                      goal2 = 100000 * timesascended
                      goal3 = 150000 * timesascended
                      goal = 1000000
                      goldenaxolotlchance = 0
                      axolotlhunger = 101
                      foodcost = 25
                      goal9 = 'unreached'
                      loop2 = False

                  else:
                      loop2 = True

  #lake
          elif action2 == 'lake' and axolotlsinbank >= item8cost:
              print('You made your axolotls per turn go up by 25!')
              axolotlspersecond = axolotlspersecond + 25
              axolotlsinbank = axolotlsinbank - item8cost
              item8cost = item8cost *1.1
              lakecount += 1
              print('')
  #town
          elif action2 == 'town' and axolotlsinbank >= item9cost:
              print('You made everything go up by 50!')
              axolotlsperclick += 50
              axolotlspersecond += 50
              axolotlsinbank -= item9cost
              item9cost *= 1.1
              towncount+= 1
              print('')

  #score
          elif action2 == 'score':
              print('You currently have a total score of', totalaxolotls, 'axolotls')

  #buildcheck
          elif action2 == 'buildcheck':
              print('You currently have', extracount, 'extras, ', farmercount, 'farmers, ', aquarcount, 'aquariums, ', spondcount, 'ponds, ', bfoodcount, 'times better food, ', mpondcount, 'medium ponds, ', lpondcount, 'large ponds, ', lakecount, 'lakes, and ', towncount, 'towns')      
  #achievs
          elif action2 == 'achievs':
              if totalaxolotls >= 100:
                  print('Achievement: Get 100 axolotls!')   
              if totalaxolotls >= 1000:
                  print('Achievement: Get 1,000 axolotls!')
              if totalaxolotls >= 10000:
                  print('Achievement: Get 10,000 axolotls!')
              if totalaxolotls >= 100000:
                  print('Achievement: Get 100,000 axolotls!')
              if totalaxolotls >= 100000:
                  print('Achievement: Get 1,000,000 axolotls!')
              if totalaxolotls >= 10000000:
                  print('Achievement: Get 10,000,000 axolotls!')
              if totalaxolotls >= 100000000:
                  print('Achievement: Get 100,000,000 axolotls!')
              if totalaxolotls >= 1000000000:
                  print('Achievement: Get 1 BILLION axolotls!!!')
              if extracount >= 1:
                  print('Achievement: Get 1 Extra!')
              if farmercount >= 1:
                  print('Achiement: Get 1 farmer!')

              if totalaxolotls <= 100:
                  print('???')
              if totalaxolotls <= 1000:
                  print('???')
              if totalaxolotls <= 10000:
                  print('???')
              if extracount <= 1:
                  print('???')
              if farmercount <= 1:
                  print('???')


  #upgrade 
          elif action2 == 'upgrade' and axolotlsinbank >= upgradecost:
              if upgradelevel == 6:
                  print('You have the max amout of golden axolotl upgrades.')
              else:
                  upgradelevel = upgradelevel + 1
                  gaxolotlchance += 50
                  axolotlsinbank = axolotlsinbank - upgradecost
                  print('Your golden axolotl is now level', upgradelevel, ', and the golden axolotl has become rarer but also better.')
                  goldentier +=1
  #no
          elif action2 == 'no':
              print('You decided to leave the shop!')
              print('')
  #detect
          elif action2 == 'detector' and axolotlsinbank >= detectorcost:
              if hasdetect == 1:
                  print('You already have the unlucky axolotl detector.')
              else:
                  print('You purchased the Unlucky Axolotl Detector!')
                  hasdetect = 1
                  axolotlsinbank -= detectorcost
                  print('')
  #end
          elif action2 == 'end':
              print('Are you sure you want to end the game? y/n')
              areusure = input()
              if areusure == 'y':
                  print('You decided to end the game')
                  print('Your final score was', totalaxolotls, 'axolotls.')
                  print('Would you like to play again? y/n')
                  playagain = input()
                  if playagain == 'y':
                      print('NoodlePole Games presents')
                      print('Axolotl Clicker 1.0')
                      print('This project was inspired by the game Cookie Clicker')
                      print('')
                      loop = True
                      print('Please Choose a difficulty. Easy, normal, or hard')
                      while loop == True:
                          diffinput = input()
                          if diffinput == 'easy':
                              floodcount = 250
                              print('You chose easy mode. your chances of getting a flood are 250 to 1 and you axolotl loses .5 hunger per turn.')
                              hungerlost = 0.5
                              axolotlhunger = 100.5
                              loop = False
                          elif diffinput == 'normal':
                              floodcount = 100
                              print('You chose normal mode. your chances of getting a flood are 100 to 1 and you axolotl loses 1 hunger per turn.')
                              hungerlost = 1
                              loop = False
                          elif diffinput == 'hard':
                              floodcount = 50
                              print('You chose hard mode. your chances of getting a flood are 50 to 1 and you axolotl loses 2 hunger per turn.')
                              hungerlost = 2
                              axolotlhunger = 102
                              loop = False
                          elif diffinput == 'test':
                              floodcount = 1000000000000000
                              print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 0 hunger per turn.')
                              hungerlost = 0
                              axolotlsinbank = 1000000000
                              totalaxolotls = 1000000000
                              loop = False
                          elif diffinput == 'test2':
                              floodcount = 1000000000000000000
                              print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 100 hunger per turn.')
                              hungerlost = 100
                              axolotlsinbank = 1000000000
                              totalaxolotls = 1000000000
                              loop = False

                          else:
                              print('That is not a true difficulty. Please choose a real difficulty.')
                              loop = True

                      totalaxolotls = 0
                      axolotlsinbank = 0
                      axolotlspersecond = 0
                      axolotlsperclick = 1
                      foodcost = 25
                      item1cost = 15
                      item2cost = 100 
                      item3cost = 150
                      item4cost = 500
                      item5cost = 750
                      item6cost = 1000
                      item7cost = 1500
                      item8cost = 2000
                      item9cost = 7500
                      extracount = 0
                      goldentier = 0
                      farmercount = 0
                      aquarcount = 0
                      spondcount = 0
                      bfoodcount = 0
                      mpondcount = 0
                      lpondcount = 0
                      lakecount = 0
                      towncount = 0
                      hasgod = 0
                      hasdetect = 0
                      foodup = 20
                      goal1 = 10000
                      goal2 = 100000
                      goal3 = 150000
                      goal = 1000000
                      goldenaxolotlchance = 0
                      axolotlhunger = 101
                      foodcost = 25
                  else:
                      playing = False
              else:
                  print('You changed your mind.')

          elif action2 == 'merge':
              print('You decided to merge together your golden axolotls. The way this works is that for every 4 of each type of golden axolotl you have, you get 1 of the next type of golden axolotl.')
              loop0 = True
              while loop0 == True:
                  if goldenaxolotls >= 4:
                      goldenaxolotls -= 4
                      omegaaxolotls += 1

                  if omegaaxolotls >= 4:
                          omegaaxolotls -= 4
                          diamondaxolotls += 1

                  if diamondaxolotls >= 4:
                              diamondaxolotls -= 4
                              ultimateaxolotls += 1

                  if goldenaxolotls < 4 and omegaaxolotls < 4 and diamondaxolotls < 4:
                      loop0 = False


          else:
              print("You don't have enough money!") 
              print('')
  #upgrade10

      elif action == 'upgrade10':
          print('There are some things for sale')
          loop3 = True
          while loop3 == True:
              print('')
              print('You can now choose which upgrade category to buy from: buildings, golden axolotls, special, and misc.')
              upgrade = input()
              if upgrade == 'golden axolotls':
                  loop3 = False
                  if upgradelevel == 6:
                      print('You have the max amount of golden axolotl upgrades.')
                      print('')
                  else:
                      print('You can upgrade your golden axolotl to level', goldentier + 1, '(upgrade) for', upgradecost, 'axolotls (Warning: this only takes effect levels 1 through 7')
                      print('')
                      print('You can merge your golden axolotls together, just type merge')

              elif upgrade == 'misc':
                  loop3 = False
                  if hasdetect == 1:
                      hasdetect = 1
                      print('You have already bought the unlucky axolotl detector.')
                  else:
                      print("You can buy the upgrade 'Unlucky Axolotl detector' (detector) for 500 axolotls")
                      print('')
                  print('If you would like to check how many of each building you currently have, type buildcheck')
                  print('You can also check your acheivements (achievs)!')
                  print('')
                  print("If you ever want to end the game, type 'end'.")
                  print('If you would like to check your total score, type score')
                  print('')

              elif upgrade == 'buildings':
                  loop3 = False
                  print('You can buy Extra axolotls per click(extra), for', item1cost * 13, 'axolotls. An Axolotl Farmer(farmer) for', item2cost * 13, 'axolotls. An aquarium(aquar) for', item3cost * 13, "axolotls. A small pond of axolotls(pond) for", item4cost * 13, 'axolotls.')
                  print('You can buy Better axolotl food(foodbetter), for', item5cost * 13, 'axolotls. A medium pond(mpond) for', item6cost * 13, 'axolotls. A large pond(lpond) for', item7cost * 13, 'axolotls. An axolotl lake(lake) for', item8cost * 13, 'axolotls. An axolotl town for (town) for', item9cost * 13, 'axolotls.')
                  print('')

              elif upgrade == 'special':
                  loop3 = False
                  if goal9 == 'reached':
                      print('You have unlocked Axolotl god. He costs 1 Billion axolotls, and if you buy him, well, just find out. Type god')
                      print('')
                  elif hasgod == 1:
                      print('You are now able to ascend. Type ascend.')
                  else:
                      print('??????')
                      print('??????')
                      print('')


          print("If you don't have enough money for anything, type no")
          action2 = input()

  #extra       
          if action2 == 'extra' and axolotlsinbank >= item1cost * 13:
              print('You made your axolotls per click go up by 10!')
              axolotlsperclick = axolotlsperclick + 10
              axolotlsinbank = axolotlsinbank - item1cost * 13
              item1cost = item1cost * 2
              extracount += 10
              print('')
  #farmer             
          elif action2 == 'farmer' and axolotlsinbank >= item2cost * 13:
              print('You made your axolotls per turn go up by 10!')
              axolotlspersecond = axolotlspersecond + 10
              axolotlsinbank = axolotlsinbank - item2cost * 13
              item2cost = item2cost * 2
              farmercount += 10
              print('')
  #aquar            
          elif action2 == 'aquar' and axolotlsinbank >= item3cost * 13:
              print('You made your axolotls per click go up by 50!')
              axolotlsperclick = axolotlsperclick + 50
              axolotlsinbank = axolotlsinbank - item3cost * 13
              item3cost = item3cost * 2
              aquarcount += 10
              print('')
  #pond
          elif action2 == 'pond' and axolotlsinbank >= item4cost * 13:
              print('You made your axolotls per turn go up by 50!')
              axolotlspersecond = axolotlspersecond + 50
              axolotlsinbank = axolotlsinbank - item4cost * 13
              item4cost = item4cost * 2
              spondcount += 10
              print('')
  #foodbetter
          elif action2 == 'foodbetter' and axolotlsinbank >= item5cost * 13:
              print('You made the amount of hunger that your axolotl gets when you feed it went up by 50%')
              foodup += 50
              axolotlsinbank -= item5cost * 13
              item5cost *= 2
              bfoodcount += 10
              print('')
  #mpond
          elif action2 == 'mpond' and axolotlsinbank >= item6cost * 13:
              print('You made your axolotls per turn go up by 100!')
              axolotlspersecond = axolotlspersecond + 100
              axolotlsinbank = axolotlsinbank - item6cost * 13
              item6cost = item6cost * 2
              mpondcount += 10
              print('')
  #lpond  
          elif action2 == 'lpond' and axolotlsinbank >= item7cost * 13:
              print('You made your axolotls per click go up by 250!')
              axolotlsperclick = axolotlsperclick + 250
              axolotlsinbank = axolotlsinbank - item7cost * 13
              item7cost = item7cost * 2
              lpondcount += 10
              print('')

  #lake
          elif action2 == 'lake' and axolotlsinbank >= item8cost * 13:
              print('You made your axolotls per turn go up by 250!')
              axolotlspersecond = axolotlspersecond + 250
              axolotlsinbank = axolotlsinbank - item8cost * 13
              item8cost = item8cost * 2
              lakecount += 10
              print('')
  #town
          elif action2 == 'town' and axolotlsinbank >= item9cost * 13:
              print('You made everything go up by 500!')
              axolotlsperclick += 500
              axolotlspersecond += 500
              axolotlsinbank -= item9cost * 13
              item9cost *= 2
              towncount+= 10
              print('')

  #score
          elif action2 == 'score':
              print('You currently have a total score of', totalaxolotls, 'axolotls')


  #no
          elif action2 == 'no':
              print('You decided to leave the shop!')
              print('')

  #end
          elif action2 == 'end':
              print('Are you sure you want to end the game? y/n')
              areusure = input()
              if areusure == 'y':
                  print('You decided to end the game')
                  print('Your final score was', totalaxolotls, 'axolotls.')
                  print('Would you like to play again? y/n')
                  playagain = input()
                  if playagain == 'y':
                      print('NoodlePole Games presents')
                      print('Axolotl Clicker 1.0')
                      print('This project was inspired by the game Cookie Clicker')
                      print('')
                      loop = True
                      print('Please Choose a difficulty. Easy, normal, or hard')
                      while loop == True:
                          diffinput = input()
                          if diffinput == 'easy':
                              floodcount = 250
                              print('You chose easy mode. your chances of getting a flood are 250 to 1 and you axolotl loses .5 hunger per turn.')
                              hungerlost = 0.5
                              axolotlhunger = 100.5
                              loop = False
                          elif diffinput == 'normal':
                              floodcount = 100
                              print('You chose normal mode. your chances of getting a flood are 100 to 1 and you axolotl loses 1 hunger per turn.')
                              hungerlost = 1
                              loop = False
                          elif diffinput == 'hard':
                              floodcount = 50
                              print('You chose hard mode. your chances of getting a flood are 50 to 1 and you axolotl loses 2 hunger per turn.')
                              hungerlost = 2
                              axolotlhunger = 102
                              loop = False
                          elif diffinput == 'test':
                              floodcount = 1000000000000000
                              print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 0 hunger per turn.')
                              hungerlost = 0
                              axolotlsinbank = 1000000000
                              totalaxolotls = 1000000000
                              loop = False
                          elif diffinput == 'test2':
                              floodcount = 1000000000000000
                              print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 100 hunger per turn.')
                              hungerlost = 100
                              axolotlsinbank = 1000000000
                              totalaxolotls = 1000000000
                              loop = False

                          else:
                              print('That is not a true difficulty. Please choose a real difficulty.')
                              loop = True

                      totalaxolotls = 0
                      axolotlsinbank = 0
                      axolotlspersecond = 0
                      axolotlsperclick = 1
                      foodcost = 25
                      item1cost = 15
                      item2cost = 100 
                      item3cost = 150
                      item4cost = 500
                      item5cost = 750
                      item6cost = 1000
                      item7cost = 1500
                      item8cost = 2000
                      item9cost = 7500
                      extracount = 0
                      goldentier = 0
                      farmercount = 0
                      aquarcount = 0
                      spondcount = 0
                      bfoodcount = 0
                      mpondcount = 0
                      lpondcount = 0
                      lakecount = 0
                      towncount = 0
                      hasgod = 0
                      hasdetect = 0
                      foodup = 20
                      goal1 = 10000
                      goal2 = 100000
                      goal3 = 150000
                      goal = 1000000
                      goldenaxolotlchance = 0
                      axolotlhunger = 101
                      foodcost = 25
                  else:
                      playing = False
              else:
                  print('You changed your mind.')

          else:
              print("You don't have enough money!") 
              print('')
      #upgrade100

      elif action == 'upgrade100':
          print('There are some things for sale')
          loop3 = True
          while loop3 == True:
              print('')
              print('You can now choose which upgrade category to buy from: buildings, golden axolotls, special, and misc.')
              upgrade = input()
              if upgrade == 'golden axolotls':
                  loop3 = False
                  if upgradelevel == 6:
                      print('You have the max amount of golden axolotl upgrades.')
                      print('')
                  else:
                      print('You can upgrade your golden axolotl to level', goldentier + 1, '(upgrade) for', upgradecost, 'axolotls (Warning: this only takes effect levels 1 through 7')
                      print('')
                      print('You can merge your golden axolotls together, just type merge')

              elif upgrade == 'misc':
                  loop3 = False
                  if hasdetect == 1:
                      hasdetect = 1
                      print('You have already bought the unlucky axolotl detector.')
                  else:
                      print("You can buy the upgrade 'Unlucky Axolotl detector' (detector) for 500 axolotls")
                      print('')
                  print('If you would like to check how many of each building you currently have, type buildcheck')
                  print('You can also check your acheivements (achievs)!')
                  print('')
                  print("If you ever want to end the game, type 'end'.")
                  print('If you would like to check your total score, type score')
                  print('')

              elif upgrade == 'buildings':
                  loop3 = False
                  print('You can buy Extra axolotls per click(extra), for', item1cost * 113, 'axolotls. An Axolotl Farmer(farmer) for', item2cost * 113, 'axolotls. An aquarium(aquar) for', item3cost * 113, "axolotls. A small pond of axolotls(pond) for", item4cost * 113, 'axolotls.')
                  print('You can buy Better axolotl food(foodbetter), for', item5cost * 113, 'axolotls. A medium pond(mpond) for', item6cost * 113, 'axolotls. A large pond(lpond) for', item7cost * 113, 'axolotls. An axolotl lake(lake) for', item8cost * 113, 'axolotls. An axolotl town for (town) for', item9cost * 113, 'axolotls.')
                  print('')

              elif upgrade == 'special':
                  loop3 = False
                  if goal9 == 'reached':
                      print('You have unlocked Axolotl god. He costs 1 Billion axolotls, and if you buy him, well, just find out. Type god')
                      print('')
                  elif hasgod == 1:
                      print('You are now able to ascend. Type ascend.')
                  else:
                      print('??????')
                      print('??????')
                      print('')


          print("If you don't have enough money for anything, type no")
          action2 = input()

  #extra       
          if action2 == 'extra' and axolotlsinbank >= item1cost * 113:
              print('You made your axolotls per click go up by 100!')
              axolotlsperclick = axolotlsperclick + 100
              axolotlsinbank = axolotlsinbank - item1cost * 113
              item1cost = item1cost * 200
              extracount += 100
              print('')
  #farmer             
          elif action2 == 'farmer' and axolotlsinbank >= item2cost * 133:
              print('You made your axolotls per turn go up by 100!')
              axolotlspersecond = axolotlspersecond + 100
              axolotlsinbank = axolotlsinbank - item2cost * 133
              item2cost = item2cost * 200
              farmercount += 100
              print('')
  #aquar            
          elif action2 == 'aquar' and axolotlsinbank >= item3cost * 133:
              print('You made your axolotls per click go up by 500!')
              axolotlsperclick = axolotlsperclick + 500
              axolotlsinbank = axolotlsinbank - item3cost * 133
              item3cost = item3cost * 200
              aquarcount += 100
              print('')
  #pond
          elif action2 == 'pond' and axolotlsinbank >= item4cost * 133:
              print('You made your axolotls per turn go up by 500!')
              axolotlspersecond = axolotlspersecond + 500
              axolotlsinbank = axolotlsinbank - item4cost * 133
              item4cost = item4cost * 200
              spondcount += 100
              print('')
  #foodbetter
          elif action2 == 'foodbetter' and axolotlsinbank >= item5cost * 133:
              print('You made the amount of hunger that your axolotl gets when you feed it went up by 500%')
              foodup += 500
              axolotlsinbank -= item5cost * 133
              item5cost *= 200
              bfoodcount += 100
              print('')
  #mpond
          elif action2 == 'mpond' and axolotlsinbank >= item6cost * 133:
              print('You made your axolotls per turn go up by 1000!')
              axolotlspersecond = axolotlspersecond + 1000
              axolotlsinbank = axolotlsinbank - item6cost * 133
              item6cost = item6cost * 200
              mpondcount += 100
              print('')
  #lpond  
          elif action2 == 'lpond' and axolotlsinbank >= item7cost * 133:
              print('You made your axolotls per click go up by 2500!')
              axolotlsperclick = axolotlsperclick + 2500
              axolotlsinbank = axolotlsinbank - item7cost * 133
              item7cost = item7cost * 200
              lpondcount += 100
              print('')

  #lake
          elif action2 == 'lake' and axolotlsinbank >= item8cost * 133:
              print('You made your axolotls per turn go up by 2500!')
              axolotlspersecond = axolotlspersecond + 2500
              axolotlsinbank = axolotlsinbank - item8cost * 133
              item8cost = item8cost * 200
              lakecount += 100
              print('')
  #town
          elif action2 == 'town' and axolotlsinbank >= item9cost * 133:
              print('You made everything go up by 5000!')
              axolotlsperclick += 5000
              axolotlspersecond += 5000
              axolotlsinbank -= item9cost * 133
              item9cost *= 200
              towncount+= 100
              print('')

  #score
          elif action2 == 'score':
              print('You currently have a total score of', totalaxolotls, 'axolotls')


  #no
          elif action2 == 'no':
              print('You decided to leave the shop!')
              print('')

  #end
          elif action2 == 'end':
              print('Are you sure you want to end the game? y/n')
              areusure = input()
              if areusure == 'y':
                  print('You decided to end the game')
                  print('Your final score was', totalaxolotls, 'axolotls.')
                  print('Would you like to play again? y/n')
                  playagain = input()
                  if playagain == 'y':
                      print('NoodlePole Games presents')
                      print('Axolotl Clicker 1.0')
                      print('This project was inspired by the game Cookie Clicker')
                      print('')
                      loop = True
                      print('Please Choose a difficulty. Easy, normal, or hard')
                      while loop == True:
                          diffinput = input()
                          if diffinput == 'easy':
                              floodcount = 250
                              print('You chose easy mode. your chances of getting a flood are 250 to 1 and you axolotl loses .5 hunger per turn.')
                              hungerlost = 0.5
                              axolotlhunger = 100.5
                              loop = False
                          elif diffinput == 'normal':
                              floodcount = 100
                              print('You chose normal mode. your chances of getting a flood are 100 to 1 and you axolotl loses 1 hunger per turn.')
                              hungerlost = 1
                              loop = False
                          elif diffinput == 'hard':
                              floodcount = 50
                              print('You chose hard mode. your chances of getting a flood are 50 to 1 and you axolotl loses 2 hunger per turn.')
                              hungerlost = 2
                              axolotlhunger = 102
                              loop = False
                          elif diffinput == 'test':
                              floodcount = 1000000000000000
                              print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 0 hunger per turn.')
                              hungerlost = 0
                              axolotlsinbank = 1000000000
                              totalaxolotls = 1000000000
                              loop = False
                          elif diffinput == 'test2':
                              floodcount = 1000000000000000
                              print('You have activated test mode. your chances of getting a flood are 1000000 to 1 and you axolotl loses 100 hunger per turn.')
                              hungerlost = 100
                              axolotlsinbank = 1000000000
                              totalaxolotls = 1000000000
                              loop = False

                          else:
                              print('That is not a true difficulty. Please choose a real difficulty.')
                              loop = True

                      totalaxolotls = 0
                      axolotlsinbank = 0
                      axolotlspersecond = 0
                      axolotlsperclick = 1
                      foodcost = 25
                      item1cost = 15
                      item2cost = 100 
                      item3cost = 150
                      item4cost = 500
                      item5cost = 750
                      item6cost = 1000
                      item7cost = 1500
                      item8cost = 2000
                      item9cost = 7500
                      extracount = 0
                      goldentier = 0
                      farmercount = 0
                      aquarcount = 0
                      spondcount = 0
                      bfoodcount = 0
                      mpondcount = 0
                      lpondcount = 0
                      lakecount = 0
                      towncount = 0
                      hasgod = 0
                      hasdetect = 0
                      foodup = 20
                      goal1 = 10000
                      goal2 = 100000
                      goal3 = 150000
                      goal = 1000000
                      goldenaxolotlchance = 0
                      axolotlhunger = 101
                      foodcost = 25
                  else:
                      playing = False
              else:
                  print('You changed your mind.')

          else:
              print("You don't have enough money!") 
              print('')

      elif action == 'feed':
          print('This food costs', foodcost, 'axolotls. y/n')
          foodanswer = input()
          if foodanswer == 'y' and axolotlsinbank >= foodcost:
              print("You bought your axolotl food, and your axolotl's hunger went up by", foodup, "%")
              axolotlhunger = axolotlhunger + foodup
              axolotlsinbank = axolotlsinbank - foodcost
              print('')

          else:
              print('You decided not to buy the food.')
              print('')

      else:
          print('That is not a real action')
          axolotlhunger += hungerlost
  
elif niput == 5:
  print("Welcome to Inconvenience!")
      ##MADE BY CODERBOY

      ## IMPORTS
  if True:
      import platform 
      os = platform.system()
      if os == "Windows":
          import keyboard
      elif os == "Linux":
          import getkey

      ##IDEA: CHECK OS -> DEPENDING ON OS IT CHANGES HOW KEYS ARE GATHERED

      ##Print an array nicely.
      def print_arr(arr):
          for i in arr:
              for j in i:
                  print(j, end="")

              print()


      ##Perleanate an array.
      def perlin(noise, sizex, sizey):
          final = noise
          x = 0
          y = 0
          for i in range(sizex * sizey):
              #print(x)
              #print(y)
              if x == 0 and y == 0:
                  final[x, y] = (
                      noise[x, y] + 
                      noise[x, y + 1] +
                      noise[x + 1, y + 1] + 
                      noise[x + 1, y]
                  ) / 4

              elif x == 0 and y != 0 and y != sizey - 1:
                  final[x, y] = (
                      noise[x, y] + 
                      noise[x, y + 1] +
                      noise[x + 1, y + 1] + 
                      noise[x + 1, y] +
                      noise[x + 1, y - 1] + 
                      noise[x, y - 1]
                  ) / 6

              elif x == sizex - 1 and y == 0:
                  final[x, y] = (
                      noise[x, y] + 
                      noise[x, y + 1] + 
                      noise[x - 1, y] +
                      noise[x - 1, y + 1]
                  ) / 4

              elif x == sizex - 1 and y != 0 and y != sizey - 1:
                  final[x, y] = (
                      noise[x, y] + 
                      noise[x, y + 1] + 
                      noise[x, y - 1] +
                      noise[x - 1, y - 1] + 
                      noise[x - 1, y] +
                      noise[x - 1, y + 1]
                  ) / 6

              elif x == sizex - 1 and y == sizey - 1:
                  final[x, y] = (
                      noise[x, y] + 
                      noise[x, y - 1] +
                      noise[x - 1, y - 1] + 
                      noise[x - 1, y]
                  ) / 4

              elif x != 0 and x != sizex - 1 and y == sizey - 1:
                  final[x, y] = (
                      noise[x, y] + 
                      noise[x + 1, y] +
                      noise[x + 1, y - 1] + 
                      noise[x, y - 1] +
                      noise[x - 1, y - 1] + 
                      noise[x - 1, y]
                  ) / 6

              elif x == 0 and y == sizey - 1:
                  final[x, y] = (
                      noise[x, y] + 
                      noise[x + 1, y] +
                      noise[x + 1, y - 1] + 
                      noise[x, y - 1]
                  ) / 4

              elif x == 0 and y != 0 and y != sizey - 1:
                  final[x, y] = (
                      noise[x, y] + 
                      noise[x, y + 1] +
                      noise[x + 1, y + 1] + 
                      noise[x + 1, y] +
                      noise[x + 1, y - 1] + 
                      noise[x, y - 1]
                  ) / 6

              else:
                  final[x, y] = (
                      noise[x, y] + 
                      noise[x, y + 1] + 
                      noise[x + 1, y + 1] +
                      noise[x + 1, y] + 
                      noise[x + 1, y - 1] +
                      noise[x, y - 1] + 
                      noise[x - 1, y - 1] +
                      noise[x - 1, y] + 
                      noise[x - 1, y + 1]) / 9

              x += 1
              if x == sizex:
                  y += 1
                  x = 0

          return final


      ##Perleanate an array multiple times.
      def perlin_multiple(noise, sizex, sizey, rounds):
          intermediate = noise
          final = noise
          next = intermediate
          for i in range(rounds):
              intermediate = perlin(next, sizex, sizey)
              next = intermediate

          final = next
          return final


      ##Create a 7-layer Perlean-Floor black and white map.
      def make_map(size, Player):
          noise = np.zeros((size, size))
          x = 0
          y = 0
          for i in range(size**2):
              noise[x, y] = np.random.randint(0, 100)
              x += 1
              if x == size:
                  y += 1
                  x = 0

          perlin = perlin_multiple(noise, size, size, 7)
          perlin = perlin.astype(int)
          map2d = np.empty((size,size))
          map2d = map2d.astype(str)
          x = 0
          y = 0
          for i in range(size**2):
              if perlin[x, y] < 50:
                  map2d[x, y] = Fore.BLACK + '██'

              else:
                  map2d[x, y] = Fore.LIGHTBLACK_EX + '██'

              x += 1
              if x == size:
                  y += 1
                  x = 0

          map2d = map2d.astype(str)
          x = 0
          y = 0

          while map2d[Player.x, Player.y] == Fore.LIGHTBLACK_EX + '██':
              noise = np.zeros((size, size))
              x = 0
              y = 0
              for i in range(size**2):
                  noise[x, y] = np.random.randint(0, 100)
                  x += 1
                  if x == size:
                      y += 1
                      x = 0

              perlin = perlin_multiple(noise, size, size, 7)
              perlin = perlin.astype(int)
              map2d = np.empty((size,size))
              map2d = map2d.astype(str)
              x = 0
              y = 0
              for i in range(size**2):
                  if perlin[x, y] < 50:
                      map2d[x, y] = Fore.BLACK + '██'

                  else:
                      map2d[x, y] = Fore.LIGHTBLACK_EX + '██'

                  x += 1
                  if x == size:
                      y += 1
                      x = 0

              map2d = map2d.astype(str)
              x = 0
              y = 0

          #mpl.title("7x Perlin Noise Floored")
          #mpl.imshow(perlinrounded, cmap="gray")
          #mpl.savefig("perlin_noisex10_floored.png")
          return map2d


      ##Takes in a map, a player, and a UI and layers them together so that they can all be printed at once.
      def get_full_screen(sideLength, UICover, map, playerInfo):
          fullScreen = np.empty((sideLength, sideLength))
          fullScreen = fullScreen.astype(str)
          fullScreen[fullScreen == "0.0"] = "  "
          fullScreen = map
          fullScreen[playerInfo.y, playerInfo.x] = playerInfo.sprite
          if playerInfo.heldItem != "  ":
              fullScreen[playerInfo.y+1, playerInfo.x] = playerInfo.heldItem
          fullScreen[0,0] = UICover[0,0]
          fullScreen[1,0] = UICover[1,0]
          fullScreen[29,27] = UICover[29,27]
          fullScreen[29,28] = UICover[29,28]
          fullScreen[29,29] = UICover[29,29]
          return fullScreen


      def make_enemy(level, x, y):
          enemy = enemyClass(
              Fore.RED + "<> ",
              x,
              y,
              int(level*2-1)
          )
          enemylist.append(enemy)
          return enemy


      ##Be able to make multiple players and get info from them.
      class playerClass:

          def __init__(self, name, pclass, sprite, x, y, bigX, bigY, inventory, heldItem, health):
              self.name = name
              self.pclass = pclass
              self.sprite = sprite
              self.x = x
              self.y = y
              self.bigX = bigX
              self.bigY = bigY
              self.inventory  = inventory
              self.heldItem = heldItem
              self.health = health


      class enemyClass:

          def __init__(self, sprite, x, y, health):
              self.sprite = sprite
              self.x = x
              self.y = y
              self.health = health


      enemylist = []

      ##Define the map sizes.
      mapSideLength = 30
      worldGenSideLength = 20

      ##Make the plain player.
      global Player
      Player = playerClass(
          "Main", 
          "placeholder",
          Fore.LIGHTGREEN_EX + "[]", 
          int(10), 
          int(10), 
          10, 
          10,
          np.array(["", ""]),
          "  ",
          3
      )

      ##Create the UI map.

      UI = np.array([
          [f"{Fore.LIGHTWHITE_EX}[{Player.inventory[0]}]", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          [f"{Fore.LIGHTWHITE_EX}[{Player.inventory[0]}]", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", Fore.LIGHTRED_EX + "\u265E ", Fore.LIGHTRED_EX + "\u265E ", Fore.LIGHTRED_EX + "\u265E ", "\u265E"]
      ])

      ##Variables.
      title = """
                  inconvenience.
                  """
      worldMap = np.empty((worldGenSideLength, worldGenSideLength, mapSideLength, mapSideLength))

      ##Make the world map.
      worldMap = worldMap.astype(str)

      ##Start reading player input.

      ##Remind the player to connect the controller
      '''
      print("Hey! Just a reminder, do you have your controller connected and the CoolTerm program connected and recording? (y/n)")
      niput = input()
      if niput == "y":
          print("Good! Let's go!")

      elif niput == "n":
          print()
          print("Why? (I don't know how (idk)/It's not working (nw)")
          niput = input()
          if niput == "idk":
              print()
              print("That's ok! Here's how to do it.")
              print()
              print("""            1) Go to the folder that this application is in.
                  2) Open the file "Controller.CoolTernSettings".
                  3) Change the connected port to the port that your controller is connected to.
                  4) Press "Connect"
                  5) Go to "Connection" and start recording, just make sure that you're saving the text file as "playerControlInput.txt".
                  6) You should be all good!""")
              print()

          elif niput == "nw":
              print()
              print("Not gonna lie, just talk to Joey.")

      '''

      ##Title screen.
      for i in range(45):
          print()

      print(title)
      for i in range(1):
          print()

      print("                  a game by joey, with an idea from audrey.")
      for i in range(3):
          print()

      for i in range(26):
          print()

      gameLoaded = False
      print("Hello, traveler!")
      time.sleep(0.5)
      print("Have you been here before? (y/n)")
      niput = input()
      print()
      if niput == 'y':
          gameLoaded = True
          print("Why hello again! What is your username?")
          niput = input()
          file = shelve.open(f"{niput}data")
          Player = file["player"]
          worldMap = file["map"]
          file.close()

      else:
          print("Why hello! What might your name be, traveler?")
          Player.name = input()
          print()
          time.sleep(0.5)
          print(f"Hello, {Player.name}!")
          print()
          print()
          time.sleep(0.5)
          print("Welcome to the world of [insert name here]!")
          print()
          time.sleep(0.5)
          print()
          print()
          loop = True
          while loop:
              print("You must now choose a class; mage, knight, barbarian, or archer.")
              niput = input()
              print()
              if niput == "mage":
                  Player.pclass = "mage"
                  print("You're a mage!")
                  loop = False

              elif niput == "knight":
                  Player.pclass = "knight"
                  print("You're a knight!")
                  loop = False

              elif niput == "barbarian":
                  Player.pclass = "barbarian"
                  print("You're a barbarian!")
                  loop = False

              elif niput == "archer":
                  Player.pclass = "archer"
                  print("You're an archer!")
                  loop = False

      time.sleep(1)
      for i in range(20):
          print()
      print("                     [play (\u229A)]")
      print("                     [controls (\u2298)]")
      ##Wait for player input to choose the screen option.
      runningStart = True
      while runningStart:
          ##Get player input
          mostRecentPlayerInput = '10'

          if mostRecentPlayerInput[-2] == "1":
              for i in range(45):
                  print()

              print("P", end="")
              time.sleep(0.5)
              print("L", end="")
              time.sleep(0.5)
              print("A", end="")
              time.sleep(0.5)
              print("Y", end="")
              time.sleep(0.5)
              print("!")
              time.sleep(0.5)
              print()
              if not gameLoaded:
                  print("Generating map.", end="\r")
                  time.sleep(0.5)
                  print("Generating map..", end="\r")
                  time.sleep(0.5)
                  print("Generating map...", end="\r")
                  map = make_map(mapSideLength, Player)
                  time.sleep(0.5)
                  print("Generating map....", end="\r")
                  time.sleep(0.5)
                  print("Generating map.....", end="\r")
                  time.sleep(0.5)
                  worldMap[10,10] = map

              else:
                  print("Loading map.", end="\r")
                  time.sleep(0.5)
                  print("Loading map..", end="\r")
                  time.sleep(0.5)
                  print("Loading map...", end="\r")
                  time.sleep(0.5)
                  print("Loading map....", end="\r")
                  time.sleep(0.5)
                  print("Loading map.....", end="\r")
                  time.sleep(0.5)
                  map = worldMap[Player.bigX, Player.bigY]

              print()
              time.sleep(1)
              runningStart = False
              for i in range(20):
                  print()


      display = get_full_screen(mapSideLength, UI, map, Player)

      print_arr(display)
      ##For movement, just do (move then erase prev player)
      running = True
      while running:
          ##Get player input
          old = """
          playerInputFile = open("playerControlInput.txt")
          playerInput = playerInputFile.read()
          mostRecentPlayerInput = playerInput[-15:]
          playerInputFile.close()

          ##Make sure the input file isn't too large
          if len(playerInput) >= 14*50:
              playerInputFile.write(playerInput[-17:])

          mostRecentPlayerInput = mostRecentPlayerInput.split(".")
          xInput = int(mostRecentPlayerInput[0])
          yInput = int(mostRecentPlayerInput[1])
          sw2Input = int(mostRecentPlayerInput[2])
          swInput = int(mostRecentPlayerInput[3])
          if xInput >= 900:
              if map[Player.y, Player.x + 1] != Fore.LIGHTBLACK_EX + '███':
                  map[Player.y, Player.x] = Fore.BLACK + "███"
                  Player.x += 1

          elif xInput <= 100:
              if map[Player.y, Player.x - 1] != Fore.LIGHTBLACK_EX + '███':
                  map[Player.y, Player.x] = Fore.BLACK + "███"
                  Player.x -= 1

          elif yInput >= 900:
              if map[Player.y + 1, Player.x] != Fore.LIGHTBLACK_EX + '███':
                  map[Player.y, Player.x] = Fore.BLACK + "███"
                  Player.y += 1

          elif yInput <= 100:
              if map[Player.y - 1, Player.x] != Fore.LIGHTBLACK_EX + '███':
                  map[Player.y, Player.x] = Fore.BLACK + "███"
                  Player.y -= 1

          if swInput == 1:
              save = shelve.open(f"{Player.name}data")
              save["map"] = worldMap
              save["player"] = Player
              save["UI"] = UI
              save.close()
          if sw2Input == 1:
              running = False
          """

          ##FIND A WAY TO CHANGE GETKEY METHOD WITH OS

          if os == "Windows":
              key = keyboard.read_key()
          elif os == "Linux":
              key = getkey.getkey()


          if key == "w":
              if Player.y != 0:
                  if map[Player.y - 1, Player.x] != Fore.LIGHTBLACK_EX + '██':
                   map[Player.y, Player.x] = Fore.BLACK + "██"
                   Player.y -= 1

              else:
                  map[Player.y, Player.x] = Fore.BLACK + "██"
                  Player.y = 29
                  Player.bigY -= 1
                  if Player.bigY <= 0:
                      Player.bigY = 0

                  else:
                      if worldMap[Player.bigY, Player.bigX, Player.y, Player.x] == "0.0":
                          worldMap[Player.bigY, Player.bigX] = make_map(mapSideLength, Player)
                          map = worldMap[Player.bigY, Player.bigX]

                      else:
                          map = worldMap[Player.bigY, Player.bigX]

          elif key == "s":
              if Player.y != 29:
                  if map[Player.y + 1, Player.x] != Fore.LIGHTBLACK_EX + '██':
                      map[Player.y, Player.x] = Fore.BLACK + "██"
                      Player.y += 1

              else:
                  map[Player.y, Player.x] = Fore.BLACK + "██"
                  Player.y = 0
                  Player.bigY += 1
                  if Player.bigY >= 19:
                      Player.bigY = 0

                  else:
                          if worldMap[Player.bigY, Player.bigX, Player.y, Player.x] == "0.0":
                              worldMap[Player.bigY, Player.bigX] = make_map(mapSideLength, Player)
                              map = worldMap[Player.bigY, Player.bigX]

                          else:
                              map = worldMap[Player.bigY, Player.bigX]

          elif key == "a":
              if Player.x != 0:
                  if map[Player.y, Player.x - 1] != Fore.LIGHTBLACK_EX + '██':
                      map[Player.y, Player.x] = Fore.BLACK + "██"
                      Player.x -= 1

              else:
                  map[Player.y, Player.x] = Fore.BLACK + "██"
                  Player.x = 29
                  Player.bigX -= 1
                  if Player.bigX <= 0:
                      Player.bigX = 0

                  else:
                      if worldMap[Player.bigY, Player.bigX, Player.y, Player.x] == "0.0":
                          worldMap[Player.bigY, Player.bigX] = make_map(mapSideLength, Player)
                          map = worldMap[Player.bigY, Player.bigX]

                      else:
                          map = worldMap[Player.bigY, Player.bigX]

          elif key == "d":
              if Player.x != 29:
                  if map[Player.y, Player.x + 1] != Fore.LIGHTBLACK_EX + '██':
                      map[Player.y, Player.x] = Fore.BLACK + "██"
                      Player.x += 1

              else:
                  map[Player.y, Player.x] = Fore.BLACK + "██"
                  Player.x = 0
                  Player.bigX += 1
                  if Player.bigX >= 19:
                      Player.bigX = 0

                  else:
                      if worldMap[Player.bigY, Player.bigX, Player.y, Player.x] == "0.0":
                          worldMap[Player.bigY, Player.bigX] = make_map(mapSideLength, Player)
                          map = worldMap[Player.bigY, Player.bigX]

                      else:
                          map = worldMap[Player.bigY, Player.bigX]

          elif key == "e":
              save = shelve.open(f"{Player.name}data")
              save["map"] = worldMap
              save["player"] = Player
              save.close()

          display = get_full_screen(mapSideLength, UI, map, Player)
          print('\033[32A')
          time.sleep(0.05)
          print()
          print_arr(display)
          time.sleep(0.35)

  
elif niput == 6:
  print("Welcome to Fist Fight!")
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
  
else:
  print("That is not a game.")
  
