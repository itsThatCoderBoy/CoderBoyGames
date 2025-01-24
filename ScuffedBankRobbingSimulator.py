##MADE BY CODERBOY.

import random
import time
import secrets

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
