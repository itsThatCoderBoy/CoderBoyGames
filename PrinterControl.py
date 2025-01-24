##MADE BY CODERBOY. DO NOT DISTRIBUTE.

# STEPPER MOTOR AND SERVO CONTROL ======================================================================================================





moveamountx = 10
moveamounty = 10

# Imports
    # Connect to the Arduino
from pyfirmata2 import Arduino, util
    # Allow delays
import time

# Initialize connection to the Arduino
board = Arduino('COM2')
iterator = util.Iterator(board)
iterator.start()

# Define pins for buttons
pin10 = board.get_pin('d:10:i')  # Button on pin 10 (input)
pin10.enable_reporting()           # Enable reporting on button pin
pin12 = board.get_pin('d:12:i')  # Button on pin 12 (input)
pin12.enable_reporting()           # Enable reporting on button pin

# Store the current state of the buttons
button1_state = None
button2_state = None


# Callback function for button state changes
def button_callback(value, pin_num):
    global button1_state, button2_state
    if pin_num == 10:
        button1_state = value

    elif pin_num == 12:
        button2_state = value


# Register callback functions for both buttons
pin10.register_callback(lambda value: button_callback(value, 10))
pin12.register_callback(lambda value: button_callback(value, 12))


# Function to check if both buttons are pressed
def check_buttons_pressed():
    while True:
        # Ensure both buttons are pressed (active LOW)
        if button1_state is not None and button2_state is not None:
            if button1_state == 0 and button2_state == 0:  # Both pressed
                print("Both buttons pressed. Continuing...")
                break

        time.sleep(0.1)  # Small delay to avoid busy waiting


# Setup servo and motor pins
servo_pin = board.get_pin('d:10:p')
motor1_pins = [6, 7, 8, 9]
motor1_pins_objects = [board.get_pin(f'd:{pin}:o') for pin in motor1_pins]
motor2_pins = [2, 3, 4, 5]
motor2_pins_objects = [board.get_pin(f'd:{pin}:o') for pin in motor2_pins]

# Define the step sequence for the 28BYJ-48
sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]


# Controls Stepper motors
def step_motor(steps: object, steps2: object, direction1: object = 'forward', direction2: object = 'forward', motor1: object = None, motor2: object = None) -> object:
    delay = 0.001
    steps = steps * moveamountx
    steps2 = steps2 * moveamounty
    if direction1 == 'reverse':
        step_sequence1 = list(reversed(sequence))

    else:
        step_sequence1 = sequence

    if direction2 == 'reverse':
        step_sequence2 = list(reversed(sequence))

    else:
        step_sequence2 = sequence

    if steps2 <= steps:
        for _ in range(steps):
            if motor1:
                for step in step_sequence1:
                    for pin, value in zip(motor1, step):
                        pin.write(value)

                    time.sleep(delay)
                    steps -= 1

            if motor2:
                for step in step_sequence2:
                    for pin, value in zip(motor2, step):
                        pin.write(value)

                    time.sleep(delay)
                    steps2 -= 1

        if steps2 > 0:
            for i in range(steps2):
                if motor2:
                    for step in step_sequence2:
                        for pin, value in zip(motor2, step):
                            pin.write(value)

                        time.sleep(delay)
                        steps2 -= 1

    else:
        for _ in range(steps2):
            if motor1:
                for step in step_sequence1:
                    for pin, value in zip(motor1, step):
                        pin.write(value)

                    time.sleep(delay)
                    steps -= 1

            if motor2:
                for step in step_sequence2:
                    for pin, value in zip(motor2, step):
                        pin.write(value)

                    time.sleep(delay)
                    steps2 -= 1

        if steps > 0:
            for i in range(steps):
                for step in step_sequence1:
                    for pin, value in zip(motor1, step):
                        pin.write(value)

                    time.sleep(delay)
                    steps -= 1


# Moves servo
def move_servo(angle):
    # Convert angle to a PWM value
    pwm_value = (angle / 180.0) * 1.5 + 0.5
    servo_pin.write(pwm_value)


# Gets object motor1
def getmotor1():
    return motor1_pins_objects


# Gets object motor2
def getmotor2():
    return motor2_pins_objects





# MAIN PROGRAM FOR CONTROLLING PRINTER AND DRAWING ======================================================================================





# Imports
    # Arrays
import numpy as np
    # Images
from PIL import Image
    # For detecting Q key for pausing
import keyboard
    # For saving the previous prints
import shelve

# Basic Variables
headx = 0
heady = 0
xmotor = getmotor1()
ymotor = getmotor2()


# Basic Move Functions
    # Moves pen up
def moveup():
    move_servo(130)


    # Moves pen down
def movedown():
    move_servo(80)


    # Goes to a defined position
def goto(x, y):
    moveup()
    movex = x - headx
    movey = y - heady
    if movex >= 0:
        step_motor(movex, None, 'forward', None, xmotor, None)

    else:
        step_motor(-movex, None, 'reverse', None, xmotor, None)

    if movey >= 0:
        step_motor(None, movey * moveamounty, None, 'forward', None, ymotor)

    else:
        step_motor(None, -movey * moveamounty, None, 'reverse', None, ymotor)

    movedown()


moveup()


    # Main movements in all 8 directions
def move0():
    step_motor(1, 0, 'forward', None, xmotor, None)


def move1():
    step_motor(1, 1, 'forward', 'forward', xmotor, ymotor)


def move2():
    step_motor(0, 1, None, 'forward', None, ymotor)


def move3():
    step_motor(1, 1, 'reverse', 'forward', xmotor, ymotor)


def move4():
    step_motor(1, 0, 'reverse', None, xmotor, None)


def move5():
    step_motor(1, 1, 'reverse', 'reverse', xmotor, ymotor)


def move6():
    step_motor(0, 1, None, 'reverse', None, ymotor)


def move7():
    step_motor(1, 1, 'forward', 'reverse', xmotor, ymotor)


# Basic user interaction
    # Loading Sequence
print("LOADING...")
time.sleep(1)
print("[-----]")
time.sleep(0.5)
print("[=----]")
time.sleep(0.5)
print("[==---]")
time.sleep(0.5)
print("[===--]")
time.sleep(0.5)
print("[====-]")
time.sleep(0.5)
print("[=====]")
time.sleep(0.5)
print("Loading Complete!")
print()
print("2D Printer Software 1.0.0")
print()
time.sleep(0.5)

# User input start
print("0) Manage save files or 1) Print")
niput = input()
if niput == "0":
    print()
    print("Current Saves:")
    print()
    save_file = shelve.open("Previous_Prints")
    numSaves = save_file["numSaves"]
    Saves = np.array([numSaves, 3])
    num = 1
    numm = 0
    for i in range(numSaves):
        Saves[numm, 0] = f"#{num}: "
        strin = save_file[f"Save{num}"]
        break1 = strin.index("(")
        break2 = strin.index(")")
        strin2 = strin[break1:break2-1]
        Saves[numm, 1] = strin2
        break1 = strin.index("/")
        break2 = strin.index("]")
        strin2 = strin[break1:break2-1]
        Saves[numm, 2] = strin2
        num += 1
        numm += 1

    print()
    time.sleep(1)

else:
    print()
    print("What is the path to your image?")
    path = input('Path:   ')
    print()
    time.sleep(0.5)
    print("What is the resolution of your image?")
    print("0) 108x137 \n 1) 216x279 \n 2) 432x558")
    resolution = input("Choice:   ")
    if resolution == "0":
        resolution = (108, 137)

    if resolution == "1":
        resolution = (216, 279)

    if resolution == "2":
        resolution = (432, 558)

    time.sleep(0.5)
    print()
    print("What infill pattern do you want to use; 0) vertical, 1) diagonal [NOT IMPLEMENTED], 2) horizontal [NOT IMPLEMENTED]")
    infill = input("Choice:   ")
    time.sleep(0.5)
    if infill == "0":
        infill = "vertical"

    if infill == "1":
        infill = "diagonal"

    if infill == "2":
        infill = "horizontal"

    print()
    print("Are these settings correct (y/n):")
    print()
    print(f"Image Path: {path}")
    print(f"Resolution: {resolution}")
    print(f"Infill Pattern: {infill}")
    niput = input()
    print()
    if niput == 'n':
        print("RESTARTING...")
        exit()

    else:
        print("Enter to print:")
        input()
        loop = False

    # No more user input

    # Converts image to NumPy array
    img = Image.open(path).convert("L")
    data = np.asarray(img).copy()
    data = data.astype(np.uint8)
    imgCopy = Image.open(path).convert("L")
    dataCopy = np.asarray(imgCopy).copy()
    dataCopy = dataCopy.astype(np.uint8)

    # Converts orange (221,44, 0) -> 2
    data[(data[:, :, 0] == 221) & (data[:, :, 1] == 44) & (data[:, :, 2] == 0)] = 2

    # Convert white (255, 255, 255) -> 0
    data[(data[:, :, 0] == 255) & (data[:, :, 1] == 255) & (data[:, :, 2] == 255)] = 0

    # Convert black (0, 0, 0) -> 1
    data[(data[:, :, 0] == 0) & (data[:, :, 1] == 0) & (data[:, :, 2] == 0)] = 1

    # Starting print
    print("Hold Q to pause print.")
    print()
    print("Printing...")

    # Moves down if underneath is 1 (black)
    if data[headx, heady] == 1:
        movedown()

    print()
    print()
    print()

    # Check if both buttons are pressed before continuing
    check_buttons_pressed()

    print("Beginning Outline...")

    #Outlining
    while np.any(data == 1) and printing:
        #Doing the line
        if headx == 0 and heady != 0 and heady != 278:
            if data[headx, heady + 1] == 1:
                heady += 1
                move0()

            elif data[headx + 1, heady + 1] == 1:
                headx += 1
                heady += 1
                move1()

            elif data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx + 1, heady - 1] == 1:
                headx += 1
                heady -= 1
                move3()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

        elif headx != 0 and headx != 215 and heady == 0:
            if data[headx, heady + 1] == 1:
                heady += 1
                move0()

            elif data[headx + 1, heady + 1] == 1:
                headx += 1
                heady += 1
                move1()

            elif data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

            elif data[headx - 1, heady + 1] == 1:
                headx -= 1
                heady += 1
                move7()

        elif headx == 215 and heady != 0 and heady != 278:
            if data[headx, heady + 1] == 1:
                heady += 1
                move0()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

            elif data[headx - 1, heady - 1] == 1:
                headx -= 1
                heady -= 1
                move5()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

            elif data[headx - 1, heady + 1] == 1:
                headx -= 1
                heady += 1
                move7()

        elif headx != 0 and headx != 215 and heady == 278:
            if data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx + 1, heady - 1] == 1:
                headx += 1
                heady -= 1
                move3()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

            elif data[headx - 1, heady - 1] == 1:
                headx -= 1
                heady -= 1
                move5()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

        elif headx == 0 and heady == 0:
            if data[headx, heady + 1] == 1:
                heady += 1
                move0()

            elif data[headx + 1, heady + 1] == 1:
                headx += 1
                heady += 1
                move1()

            elif data[headx + 1, heady] == 1:
                headx += 1
                move2()

        elif headx == 215 and heady == 0:
            if data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx + 1, heady - 1] == 1:
                headx += 1
                heady -= 1
                move3()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

        elif headx == 0 and heady == 278:
            if data[headx, heady - 1] == 1:
                heady -= 1
                move4()

            elif data[headx - 1, heady - 1] == 1:
                headx -= 1
                heady -= 1
                move5()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

            elif data[headx - 1, heady + 1] == 1:
                headx -= 1
                heady += 1
                move7()

        elif headx == 215 and heady == 278:
            if data[headx - 1, heady - 1] == 1:
                headx -= 1
                heady -= 1
                move5()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

            elif data[headx - 1, heady + 1] == 1:
                headx -= 1
                heady += 1
                move7()

        else:
            if data[headx, heady + 1] == 1:
                heady += 1
                move0()

            elif data[headx + 1, heady + 1] == 1:
                headx += 1
                heady += 1
                move1()

            elif data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx + 1, heady - 1] == 1:
                headx += 1
                heady -= 1
                move3()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

            elif data[headx - 1, heady - 1] == 1:
                headx -= 1
                heady -= 1
                move5()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

            elif data[headx - 1, heady + 1] == 1:
                headx -= 1
                heady += 1
                move7()

        #If there are no black pixels around the head, looks for black pixels and if it finds any, moves to it
        if np.any(data == 1) and data[headx, heady+1] != 1 and data[headx+1, heady+1] != 1 and data[headx+1, heady] != 1 and data[headx+1, heady-1] != 1 and data[headx, heady-1] != 1 and data[headx-1, heady-1] != 1 and data[headx-1, heady] != 1 and data[headx-1, heady+1] != 1:
            x = 0
            y = 0
            for i in range(216*279):
                if data[x,y] == 1:
                    goto(x,y)
                    break

                else:
                    x += 1
                    if x == 216:
                        y += 1
                        x = 0
        #Pause print
        if keyboard.key_down("Q"):
            print("Print paused. Continue? (y/n)")
            niput = input()
            if niput == 'n':
                printing = False
                print("Printing stopped early.")
                goto(0,0)
                moveup()

    #Changes all 2s to 1s (because I just copied the code above and fucked around with it until it worked and I'm too lazy to change all the 1s to 2s)
    data[data==2] = 1

    print()
    print()
    print()
    print("Completed Outline...")
    print()
    print()
    print()
    print("Beginning Infill...")

    #Infills
        #Basically the same thing but does a funky pattern lol
    while np.any(data == 2) and printing and infill == 'vertical':
        if headx == 0 and heady != 0 and heady != 278:
            if data[headx, heady + 1] == 1:
                heady += 1
                move0()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

            elif data[headx + 1, heady] == 1:
                headx += 1
                move2()

        elif headx != 0 and headx != 215 and heady == 0:
            if data[headx, heady + 1] == 1:
                heady += 1
                move0()

            elif data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

        elif headx == 215 and heady != 0 and heady != 278:
            if data[headx, heady + 1] == 1:
                heady += 1
                move0()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

        elif headx != 0 and headx != 215 and heady == 278:
            if data[headx, heady - 1] == 1:
                heady -= 1
                move4()

            elif data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

        elif headx == 0 and heady == 0:
            if data[headx, heady + 1] == 1:
                heady += 1
                move0()

            elif data[headx + 1, heady] == 1:
                headx += 1
                move2()

        elif headx == 215 and heady == 0:
            if data[headx, heady - 1] == 1:
                heady -= 1
                move4()

            elif data[headx + 1, heady] == 1:
                headx += 1
                move2()

        elif headx == 0 and heady == 278:
            if data[headx, heady - 1] == 1:
                heady -= 1
                move4()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

        elif headx == 215 and heady == 278:
            if data[headx - 1, heady] == 1:
                headx -= 1
                move6()

        else:
            if data[headx, heady + 1] == 1:
                heady += 1
                move0()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

            elif data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

        #Its exactly the same as the first one.
        if np.any(data == 1) and data[headx, heady+1] != 1 and data[headx+1, heady+1] != 1 and data[headx+1, heady] != 1 and data[headx+1, heady-1] != 1 and data[headx, heady-1] != 1 and data[headx-1, heady-1] != 1 and data[headx-1, heady] != 1 and data[headx-1, heady+1] != 1:
            x = 0
            y = 0
            for i in range(216*279):
                if data[x,y] == 1:
                    goto(x,y)
                    break

                else:
                    x += 1
                    if x == 216:
                        y += 1
                        x = 0

        #Pause print
        if keyboard.key_down("Q"):
            print("Print paused. Continue? (y/n)")
            niput = input()
            if niput == 'n':
                printing = False
                print("Printing stopped early.")
                goto(0,0)
                moveup()

    while np.any(data == 2) and printing and infill == 'horizontal':
        #Doing the line
        if headx == 0 and heady != 0 and heady != 278:
            if data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()
            
            elif data[headx, heady + 1] == 1:
                heady += 1
                move0()

        elif headx != 0 and headx != 215 and heady == 0:
            if data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()
            elif data[headx, heady + 1] == 1:
                heady += 1
                move0()

        elif headx == 215 and heady != 0 and heady != 278:
            if data[headx - 1, heady] == 1:
                headx -= 1
                move6()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()
            
            elif data[headx, heady + 1] == 1:
                heady += 1
                move0()

        elif headx != 0 and headx != 215 and heady == 278:
            if data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

        elif headx == 0 and heady == 0:
            if data[headx + 1, heady] == 1:
                headx += 1
                move2()
            
            elif data[headx, heady + 1] == 1:
                heady += 1
                move0()

        elif headx == 215 and heady == 0:
            if data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

        elif headx == 0 and heady == 278:
            if data[headx - 1, heady] == 1:
                headx -= 1
                move6()
            
            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()

        elif headx == 215 and heady == 278:
            if data[headx - 1, heady] == 1:
                headx -= 1
                move6()

        else:
            if data[headx + 1, heady] == 1:
                headx += 1
                move2()

            elif data[headx - 1, heady] == 1:
                headx -= 1
                move6()

            elif data[headx, heady - 1] == 1:
                heady -= 1
                move4()
                
            elif data[headx, heady + 1] == 1:
                heady += 1
                move0()

        #If there are no black pixels around the head, looks for black pixels and if it finds any, moves to it
        if np.any(data == 1) and data[headx, heady+1] != 1 and data[headx+1, heady+1] != 1 and data[headx+1, heady] != 1 and data[headx+1, heady-1] != 1 and data[headx, heady-1] != 1 and data[headx-1, heady-1] != 1 and data[headx-1, heady] != 1 and data[headx-1, heady+1] != 1:
            x = 0
            y = 0
            for i in range(216*279):
                if data[x,y] == 1:
                    goto(x,y)
                    break

                else:
                    x += 1
                    if x == 216:
                        y += 1
                        x = 0
        #Pause print
        if keyboard.key_down("Q"):
            print("Print paused. Continue? (y/n)")
            niput = input()
            if niput == 'n':
                printing = False
                print("Printing stopped early.")
                goto(0,0)
                moveup()

    while np.any(data == 1) and printing and infill == 'horizontal':
        #Doing the line
        if headx == 0 and heady != 0 and heady != 278:

            if data[headx + 1, heady + 1] == 1:
                headx += 1
                heady += 1
                move1()

            elif data[headx + 1, heady - 1] == 1:
                headx += 1
                heady -= 1
                move3()

        elif headx != 0 and headx != 215 and heady == 0:
            if data[headx + 1, heady + 1] == 1:
                headx += 1
                heady += 1
                move1()

            elif data[headx - 1, heady + 1] == 1:
                headx -= 1
                heady += 1
                move7()

        elif headx == 215 and heady != 0 and heady != 278:
            if data[headx - 1, heady - 1] == 1:
                headx -= 1
                heady -= 1
                move5()

            elif data[headx - 1, heady + 1] == 1:
                headx -= 1
                heady += 1
                move7()

        elif headx != 0 and headx != 215 and heady == 278:
            if data[headx + 1, heady - 1] == 1:
                headx += 1
                heady -= 1
                move3()

            elif data[headx - 1, heady - 1] == 1:
                headx -= 1
                heady -= 1
                move5()

        elif headx == 0 and heady == 0:
            if data[headx + 1, heady + 1] == 1:
                headx += 1
                heady += 1
                move1()

        elif headx == 215 and heady == 0:
            if data[headx + 1, heady - 1] == 1:
                headx += 1
                heady -= 1
                move3()

        elif headx == 0 and heady == 278:
            if data[headx - 1, heady - 1] == 1:
                headx -= 1
                heady -= 1
                move5()

            elif data[headx - 1, heady + 1] == 1:
                headx -= 1
                heady += 1
                move7()

        elif headx == 215 and heady == 278:
            if data[headx - 1, heady - 1] == 1:
                headx -= 1
                heady -= 1
                move5()

            elif data[headx - 1, heady + 1] == 1:
                headx -= 1
                heady += 1
                move7()

        else:
            if data[headx + 1, heady + 1] == 1:
                headx += 1
                heady += 1
                move1()

            elif data[headx + 1, heady - 1] == 1:
                headx += 1
                heady -= 1
                move3()

            elif data[headx - 1, heady - 1] == 1:
                headx -= 1
                heady -= 1
                move5()

            elif data[headx - 1, heady + 1] == 1:
                headx -= 1
                heady += 1
                move7()

        #If there are no black pixels around the head, looks for black pixels and if it finds any, moves to it
        if np.any(data == 1) and data[headx, heady+1] != 1 and data[headx+1, heady+1] != 1 and data[headx+1, heady] != 1 and data[headx+1, heady-1] != 1 and data[headx, heady-1] != 1 and data[headx-1, heady-1] != 1 and data[headx-1, heady] != 1 and data[headx-1, heady+1] != 1:
            x = 0
            y = 0
            for i in range(216*279):
                if data[x,y] == 1:
                    goto(x,y)
                    break

                else:
                    x += 1
                    if x == 216:
                        y += 1
                        x = 0
        #Pause print
        if keyboard.key_down("Q"):
            print("Print paused. Continue? (y/n)")
            niput = input()
            if niput == 'n':
                printing = False
                print("Printing stopped early.")
                goto(0,0)
                moveup()

    print()
    print()
    print()
    print("Completed Infill...")
    time.sleep(3)
    goto(0,0)
    time.sleep(3)
    print("Completed print!")
    time.sleep(1)
    print()
    print()
    print()
    print("Would you like to save this print to you save file? y/n")
    niput = input()
    if niput == 'y':
        save_file = shelve.open("Previous_Prints")
        numSaves = save_file['numSaves']
        print()
        print("Please name this print.")
        name = input()
        save_file[f"Save{numSaves + 1}"] = f"({name}).../{dataCopy}]"
        save_file.close()
        
    else:
        print("The print file has not been saved.")
        
    print()
    print()
    time.sleep(1)
    print("You may now close the program.")
