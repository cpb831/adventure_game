from variables_1 import *
def overall(str_1):
    start_game = True
    while start_game == True:
        if str_1 == "l":
            str_1 = input(place_description[2] + "\n\n\nThat's enough studying for now.\n"
                                               "Type \"u\" to go back to University Hall: ")
        if str_1 == "k":
            str_1 = input(place_description[3] + "\n" + "Type \"u\" to go to University Hall or \"m\" to go to the Music Building: ")
        if str_1 == "u":
            str_1 = input(place_description[1] + "\n" + "Type \"l\" to go to the Library, or"
                                                " \"k\" to go to Kresge, or"
                                                " \"n\" to hang at Norris: ")
        if str_1 == "m":
            str_1 = input(place_description[5] + "\n" + "Type \"k\" to go to Kresge or \"n\" to hang at Norris: ")
        if str_1 == "n":
            str_1 = input(place_description[4] + "\n" + "Type \"u\" to go to University Hall, or"
                                            " \"m\" to go to the Music Building, or"
                                            " \"lf\" to go the Lakefill: ")
        if str_1 == "lf":
            print(place_description[6])
            break

def begin():
    print("Welcome to Northwestern.\nGo Cats!\nYou're at the Arch.")
    input("Type any key to walk to University Hall: ")
begin()
overall("u")