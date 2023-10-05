import random

def main():
    print('Welcome to Camel!')
    print('You have stolen a camel to make your way across the great Mobi desert.')
    print('The natives want their camel back and are chasing you down! Survive your')
    print('desert trek and out run the natives.\n')

    check = False
    while (check == False):
        hardmode = input("hardmode? y/n ")
        if hardmode.lower() == "y":
            difficulty = True
            check = True
        elif hardmode.lower() == "n":
            difficulty = False
            check = True

    if difficulty == False:
        done = False
        miles_traveled = 0
        thirst = 0
        camel_tiredness = 0
        distance_the_natives_have_traveled = -20
        water_left = 3
        event = 0
    elif difficulty == True:
        done = False
        miles_traveled = 0
        thirst = 0
        camel_tiredness = 2
        distance_the_natives_have_traveled = random.randrange(-30, -25)
        water_left = random.randrange(1, 4)
        event = 0

    while (done == False):
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        if difficulty == True:
            print("F. look for water")
        print("Q. Quit.")


        answer = input("What is your choice? ")
        print("")
        if answer == ("q") or answer == ("Q"):
            done = True


        elif answer == ("f") or answer == ("F"):
            find_water = random.randrange(1, 4)
            if difficulty == False:
                print("i don\'t really think you\'ll need this")
            if find_water == 1 or find_water == 2:
                water_left = 3
                print("you\'ve found water! your canteen has been refilled")
            else:
                print("you failed to find any water")
            theyre_closing_in = random.randrange(3, 9)
            distance_the_natives_have_traveled += theyre_closing_in


        elif answer == ("e") or answer == ("E"):
            print("Miles traveled:  " + str(miles_traveled))
            print("Drinks in canteen:  " + str(water_left))
            print("The natives are " + str(miles_traveled - distance_the_natives_have_traveled) + " miles behind you.")
            if difficulty == True:
                print("the camel seems to be " + str(camel_tiredness + random.randrange(-1, 2)) + " tired")


        elif answer == ("d") or answer == ("D"):
            camel_tiredness = 0
            theyre_closing_in = random.randrange(7, 14)
            distance_the_natives_have_traveled += theyre_closing_in
            event = random.randrange(1, 21)
            if difficulty == True and event == 1:
                    print("a sandstorm appeared and, you weren\'t able to rest fully")
                    camel_tiredness = 2
                    theyre_closing_in = random.randrange(-5, 7)
                    distance_the_natives_have_traveled += theyre_closing_in
            else:
                print("the camel is happy and no longer tired")
                if difficulty == True:
                    distance_the_natives_have_traveled += 1


        elif answer == ("c") or answer == ("C"):
            traveled = random.randrange(10, 20)
            miles_traveled += traveled
            theyre_closing_in = random.randrange(7, 14)
            distance_the_natives_have_traveled += theyre_closing_in
            thirst += 1
            camel_tiredness += random.randrange(1, 3)
            event = random.randrange(1, 21)
            if event == 20:
                print("you\'ve gone " + str(traveled) + " miles.")
                print("you have found an oasis,")
                print("your canteen has been refilled, camel rested, and you are no longer thirsty")
                thirst = 0
                camel_tiredness = 0
                water_left = 3
                print("you\'ve gone " + str(traveled) + " miles.")
                if difficulty == True:
                    distance_the_natives_have_traveled += 3
            elif difficulty == True and event == 1:
                print("a sandstorm appeared, you and the natives got lost")
                miles_traveled += (traveled - 13)
                print("you\'ve gone " + str(traveled - 13) + " miles.")
                theyre_closing_in = random.randrange(-9, 7)
                distance_the_natives_have_traveled += theyre_closing_in
            else:
                print("you\'ve gone " + str(traveled) + " miles.")
                if difficulty == True:
                    distance_the_natives_have_traveled += 3


        elif answer == ("b") or answer == ("B"):
            traveled = random.randrange(5, 12)
            miles_traveled += traveled
            theyre_closing_in = random.randrange(7, 14)
            distance_the_natives_have_traveled += theyre_closing_in
            thirst += 1
            camel_tiredness += 1
            event = random.randrange(1, 21)
            if event == 20:
                print("you\'ve gone " + str(traveled) + " miles.")
                print("you have found an oasis,")
                print("your canteen has been refilled, camel rested, and you are no longer thirsty")
                thirst = 0
                camel_tiredness = 0
                water_left = 3
                if difficulty == True:
                    distance_the_natives_have_traveled += 3
            elif difficulty == True and event == 1:
                print("a sandstorm appeared, you and the natives got lost")
                miles_traveled += (traveled - 7)
                print("you\'ve gone " + str(traveled - 7) + " miles.")
                theyre_closing_in = random.randrange(-9, 7)
                distance_the_natives_have_traveled += theyre_closing_in
            else:
                print("you\'ve gone " + str(traveled) + " miles.")
                if difficulty == True:
                    distance_the_natives_have_traveled += 3


        elif answer == ("a") or answer == ("A"):
            if water_left == 0:
                print("there is no water left")
            else:
                thirst = 0
                water_left -= 1
                print("you feel refreshed")


        if thirst >= 6:
            print("You died of thirst!")
            done = True
        elif camel_tiredness >= 8:
            print("Your camel is dead.")
            done = True
        elif miles_traveled <= distance_the_natives_have_traveled:
            print("you were caught")
            done = True
        elif miles_traveled >= 200 and difficulty == False:
            print("you have escaped!")
            done = True
        elif miles_traveled >= 350 and difficulty == True:
            print("you have escaped!")
            done = True
        elif done == True:
            print("you gave up")

        elif thirst >= 4 or camel_tiredness == 5 or camel_tiredness == 6 or camel_tiredness == 7 or (miles_traveled - distance_the_natives_have_traveled) <= 15:
            if thirst >= 4:
                print("you are thirsty")
            if camel_tiredness == 5 or camel_tiredness == 6 or camel_tiredness == 7:
                print("Your camel is getting tired.")
            if (miles_traveled - distance_the_natives_have_traveled) <= 15:
                print("The natives are getting close!")

    print("thanks for playing")

main()