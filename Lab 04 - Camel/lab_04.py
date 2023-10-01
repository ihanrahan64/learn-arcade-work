import random

def main():
    print ('Welcome to Camel!')
    print('You have stolen a camel to make your way across the great Mobi desert.')
    print('The natives want their camel back and are chasing you down! Survive your')
    print('desert trek and out run the natives.\n')

    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    distance_the_natives_have_traveled = -20
    water_left = 3
    oasis = 0

    while (done == False):
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        answer = input("What is your choice? ")
        print("")
        if answer == ("q") or answer == ("Q"):
            done = True

        elif answer == ("e") or answer == ("E"):
            print("Miles traveled:  " + str(miles_traveled))
            print("Drinks in canteen:  " + str(water_left))
            print("The natives are " + str(miles_traveled - distance_the_natives_have_traveled) + " miles behind you.")

        elif answer == ("d") or answer == ("D"):
            camel_tiredness = 0
            print("the camel is happy and no longer tired")
            theyre_closing_in = random.randrange(7, 14)
            distance_the_natives_have_traveled += theyre_closing_in

        elif answer == ("c") or answer == ("C"):
            traveled = random.randrange(10, 20)
            miles_traveled += traveled
            theyre_closing_in = random.randrange(7, 14)
            distance_the_natives_have_traveled += theyre_closing_in
            print("you\'ve gone " + str(traveled) + " miles.")
            thirst += 1
            camel_tiredness += random.randrange(1, 3)
            oasis = random.randrange(0, 21)
            if oasis == 20:
                print("you have found an oasis,")
                print("your canteen has been refilled, camel rested, and you are no longer thirsty")
                thirst = 0
                camel_tiredness = 0
                water_left = 3

        elif answer == ("b") or answer == ("B"):
            traveled = random.randrange(5, 12)
            miles_traveled += traveled
            theyre_closing_in = random.randrange(7, 14)
            distance_the_natives_have_traveled += theyre_closing_in
            print("you\'ve gone " + str(traveled) + " miles.")
            thirst += 1
            camel_tiredness += 1
            oasis = random.randrange(0, 21)
            if oasis == 20:
                print("you have found an oasis,")
                print("your canteen has been refilled, camel rested, and you are no longer thirsty")
                thirst = 0
                camel_tiredness = 0
                water_left = 3

        elif answer == ("a") or answer == ("A"):
            if water_left == 0:
                print("there is no water left")
            else:
                thirst = 0
                water_left -= 1

        if thirst >= 6:
            print("You died of thirst!")
            done = True
        elif camel_tiredness >= 8:
            print("Your camel is dead.")
            done = True
        elif miles_traveled <= distance_the_natives_have_traveled:
            print("you were caught")
            done = True
        elif miles_traveled >= 200:
            print("you have escaped!")
            done = True

        elif thirst >= 4 or camel_tiredness == 5 or camel_tiredness == 6 or camel_tiredness == 7 or (miles_traveled - distance_the_natives_have_traveled) <= 15:
            if thirst >= 4:
                print("you are thirsty")
            if camel_tiredness == 5 or camel_tiredness == 6 or camel_tiredness == 7:
                print("Your camel is getting tired.")
            if (miles_traveled - distance_the_natives_have_traveled) <= 15:
                print("The natives are getting close!")

    print("thanks for playing")

main()