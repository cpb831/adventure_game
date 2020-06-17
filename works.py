dirs = [0,0]
locations = [[0,0], [0,1], [1,1], [-1,1], [0,2], [-1,2], [0,3]]
place_description_dictionary = {
    "0": ["the Arch", "Where it all begins..."],
    "1": ["University Hall", "So beautiful, n'est-ce pas?"],
    "2": ["the Library", "Study, study, study!"],
    "3": ["Kresge", "What can you say?  It's Kresge"],
    "4": ["Norris", "BONUS BUCKS!"],
    "5": ["the Music Building", "Time to practice!",],
    "6": ["the Lakefill", "Stick your toes in Lake Michigan.  You made it!"]}

print("Welcome to a Northwestern adventure game.\nGo Cats!\nYou're at the Arch.\nYour destination:"
      " the Lakefill.")
position = ""


def update_position(index):
    position = str(index)
    print("You are at " + place_description_dictionary.get(position)[0] + ".")
    print(place_description_dictionary.get(position)[1])
    if position == "6":
        exit()

def move(direction, amount):
    dirs[direction] += amount
    new_location = dirs
    if new_location in locations:
        update_position(locations.index(dirs))
    else:
        moveWasInvalid(direction, -amount)

def moveWasInvalid(direction, amount):
    dirs[direction] += amount
    new_location = dirs
    print("Not today. Choose a different direction: ")
            
while True:
    
    var = input("Which direction do you want to go: n, s, e, or w?: ")
    if var == ("n"):
        move(0, 1)

    elif var == "s":
        move(0, -1)
            
    elif var == "e":
        move(1, 1)
            
    elif var == "w":
        move(1, -1)
        
    else:
      print("Invalid entry.")
      continue
