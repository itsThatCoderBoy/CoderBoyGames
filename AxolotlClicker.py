##MADE BY CODERBOY.

import random
import time

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
