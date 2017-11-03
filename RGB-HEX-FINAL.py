"""
Author: Ryan Nevares
Date: 30 October 2017
Title: RGB/HEX Converter
Version 2.0
This is a program to interconvert RGB and HEX values.  This program will run until the user intentionally stops it and will work using bitwise operators.
"""

from time import sleep
from sys import stdout
from textwrap import fill

def print_slow(string):
    for letter in string:
        stdout.write(letter)
        stdout.flush()
        sleep(.05)

# print start message to user
print ""
print_slow ("Converter started successfully!")
print "\n"

# create a method to validate RGB input
# RGB values range from 0 to 255
def get_rgb_values():
    # get the values for
    red = raw_input("Enter the RED value: ")
    green = raw_input("Enter the GREEN value: ")
    blue = raw_input("Enter the BLUE value: ")
    sleep(0.5)
    # Ensure that the values are compatible
    if "." in red or "." in green or "." in blue:
        print "Invalid input, RGB Values must be integers \n\n"
    else:
        if red.isdigit() and green.isdigit() and blue.isdigit():
            # Make sure the values are within the acceptable range
            if int(red) > 255 or int(green) > 255 or int(blue) > 255:
                print "\nInvalid input: Values out of acceptable range"
                sleep(.5)
                print_slow ("RGB values must be between 0 and 255")
                print "\n\n"
                sleep (.5)
                # Restart the function
                # "return" so that the first get_rgb isn't calling itself
                return get_rgb_values()
            else:
                return int(red), int(green), int(blue)
        else:
            print "Invalid input: You need to enter numbers \n\n"
            sleep(0.5)
            return get_rgb_values()

# Create a method to get and validate a HEX values
def get_hex_value():
    hex_value = raw_input("Enter a Hex value: ")
    # Ensure that the value entered is actually hex
    # THen convert it
    if len(hex_value) != 6:
        print "Invalid input: Hex input must be six characters long \n\n"
        sleep(0.5)
        return get_hex_value()
    else:
        for i in hex_value:
            if not i.isdigit() and not i in ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]:
                print "Invalid Input, value not acceptable HEX syntax \n\n"
                sleep(.5)
                return get_hex_value()
            else:
                hex_value = int(hex_value, 16)
                return hex_value

# Create the RGB to HEX function
def rgb_hex():
    # Get the user's red, green, and blue values
    values = get_rgb_values()
    # get individual values from the outputted tuple by index
    red = values[0]
    green = values[1]
    blue = values[2]
    # convert the RGB values into a single binary number
    value = (red << 16) + (green << 8) + blue
    # Now, convert the binary value to a hex with the hex() method
    value = hex(value).upper()[2:]
    print ""
    sleep (1)
    print "The hex value is", value
    print "\n\n"

# Create another method to convert HEX into RGB
def hex_rgb():
    value = get_hex_value()
    two_hex_digits = 2 ** 8
    # Begin conversion of HEX into RGB
    blue = value % two_hex_digits
    value = value >> 8 # Shift hex value by 8 bits
    green = value % two_hex_digits
    value = value >> 8
    red = value % two_hex_digits
    print ""
    sleep(1)
    # Print out all the values
    print "RGB values:"
    print "Red:", red
    print "Green:", green
    print "Blue", blue

# Create the main function
def convert():
    while True:
        # Ask the user what they would like to do
        print "Enter 1 to convert RGB to HEX \nEnter 2 to convert HEX to RGB \nEnter X to exit"
        option = raw_input(":")
        # Make sure the input is valid
        if option == "1":
            print ""
            print_slow ("RGB to HEX...")
            sleep (1)
            print ""
            rgb_hex()
            sleep(0.5)
            print "\n\n"
        elif option == "2":
            print ""
            print_slow ("HEX to RGB...")
            sleep(1)
            print ""
            hex_rgb()
            sleep(0.5)
            print "\n\n"
        elif option == "X" or option == "x": # Allow upper or lower case x
            # Exit the while loop with BREAK
            print_slow ("Sorry to see you go")
            sleep(0.5)
            print "\n\n"
            print_slow ("Exiting now...")
            print "\n\n\n"
            break
        else:
            print_slow ("Invalid input: You need to choose one of the options")
            print "\n\n"
            # Go back to the beginning of the function
            return convert()

# Don't forget to call the main function
convert()
