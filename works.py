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
while True:
    indicator = ""
    var = input("Which direction do you want to go: n, s, e, or w?: ")
    if var == ("n"):
        dirs[0] += 1
        new_location = dirs
        if new_location in locations:
            indicator = str(locations.index(dirs))
            print("You are at " + place_description_dictionary.get(indicator)[0] + ".")
            print(place_description_dictionary.get(indicator)[1])
        else:
            dirs[0] -= 1
            new_location = dirs
            print("Not today. Choose a different direction: ")
    elif var == "s":
        dirs[0] -= 1
        new_location = dirs
        if new_location in locations:
            indicator = str(locations.index(dirs))
            print("You are at " + place_description_dictionary.get(indicator)[0] + ".")
            print(place_description_dictionary.get(indicator)[1])
        else:
            dirs[0] += 1
            new_location = dirs
            print("Not today. Choose a different direction: ")
    elif var == "e":
        dirs[1] += 1
        new_location = dirs
        if new_location in locations:
            indicator = str(locations.index(dirs))
            print("You are at " + place_description_dictionary.get(indicator)[0] + ".")
            print(place_description_dictionary.get(indicator)[1])
            if (new_location == locations[6]):
                break
        else:
            dirs[1] -= 1
            new_location = dirs
            print("Not today. Choose a different direction: ")
    elif var == "w":
        dirs[1] -= 1
        new_location = dirs
        if new_location in locations:
            indicator = str(locations.index(dirs))
            print("You are at " + place_description_dictionary.get(indicator)[0] + ".")
            print(place_description_dictionary.get(indicator)[1])
        else:
            dirs[1] += 1
            new_location = dirs
            print("Not today. Choose a different direction: ")
    else:
      print("Invalid entry.")
      continue