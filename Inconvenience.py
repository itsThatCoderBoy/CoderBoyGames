from pynput import keyboard


def onKeyPress(key):
    print(key)

listener = keyboard.Listener(on_press=onKeyPress)
listener.start()



## IMPORTS

import numpy as np
import time
from colorama import Fore
import shelve
import getkey
from pynput import keyboard


def onKeyPress(key):
    print(key)

listener = keyboard.Listener(on_press=onKeyPress)
listener.start()

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
    int(15), 
    int(15), 
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
    mostRecentPlayerInput = 10
        
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
