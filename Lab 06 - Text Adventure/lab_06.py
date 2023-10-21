class Room:
    def __init__(self, description = "", north = 0, east = 0, south = 0, west = 0, up = 0, down = 0):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down


def main():
    room_list = []
    current_room = 0

# entrance room 0
    room = Room("""you are in an entrance room
there are a flight of stairs ledding up and a door to the north""", 1, None, None, None, 7, None)
    room_list.append(room)

# dinning hall room 1
    room = Room("""you appear to be in a dinning hall
there are doors leading north, south, east, and west""", 4, 3, 0, 2, None, None)
    room_list.append(room)

# kitchen room 2
    room = Room("""you appear to be in a kitchen
there is a door leading east""", None, 1, None, None, None, None)
    room_list.append(room)

# hallway1 room 3
    room = Room("""you appear to be in a hallway 
there are doors leading north, east, and west""", 6, 5, None, 1, None, None)
    room_list.append(room)

# garden room 4
    room = Room("""you appear to be in a garden with walls on each side
there is a door leading south""", None, None, 1, None, None, None)
    room_list.append(room)

# bedroom1 room 5
    room = Room("""you appear to be in a bedroom
there is a door leading west""", None, None, None, 3, None, None)
    room_list.append(room)

# bathroom1 room 6
    room = Room("""you appear to be in a bathroom
there is a door leading south""", None, None, 3, None, None, None)
    room_list.append(room)

# hallway2 room 7
    room = Room("""you appear to be in a hallway 
light is coming from the north 
there are stairs leaing down, and a door to the north""", 8, None, None, None, None, 0)
    room_list.append(room)

# balcony room 8
    room = Room("""you appear to be on a balcony above a garden  
there is a door to the south""", None, None, 7, None, None, 4)
    room_list.append(room)


    done = False

    while done == False:
        print(room_list[current_room].description)
        action = input("where would you like to go? ")
        print("")

        if action.lower() == "n" or action.lower() == "north":
            next_room = room_list[current_room].north
            if room_list[current_room].north == None:
                print("you bumped into the wall")
            else:
                current_room = room_list[current_room].north

        elif action.lower() == "e" or action.lower() == "east":
            next_room = room_list[current_room].east
            if room_list[current_room].east == None:
                print("you bumped into the wall")
            else:
                current_room = room_list[current_room].east

        elif action.lower() == "w" or action.lower() == "west":
            next_room = room_list[current_room].west
            if room_list[current_room].west == None:
                print("you bumped into the wall")
            else:
                current_room = room_list[current_room].west

        elif action.lower() == "s" or action.lower() == "south":
            next_room = room_list[current_room].south
            if room_list[current_room].south == None:
                print("you bumped into the wall")
            else:
                current_room = room_list[current_room].south

        elif action.lower() == "up":
            next_room = room_list[current_room].up
            if next_room == None:
                    print("you did a small jump but went nowhere")
            else:
                current_room = next_room

        elif action.lower() == "down":
            next_room = room_list[current_room].down
            if next_room == None:
                    print("you sat on the ground")
            else:
                current_room = next_room
                if next_room == 4:
                    print("you jump into a fountain that saves you as you fall")

        elif action.lower() == "q" or action.lower() == "quit":
            done = True

        else:
            print("Reply hazy, try again")


main()
