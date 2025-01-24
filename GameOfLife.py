##MADE BY CODERBOY. DO NOT DISTRIBUTE.

import random
import time
#Game of life
#Variables


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
        
elif indoorstat >= 50 and creativitystat >= 65:
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
