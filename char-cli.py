import math
import random

def main():
    print("Welcome to the Char CLI")
    print("This app remains a work in progress, and only covers core PHB rules for character creation")
    
    # book info
    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    # todo: subraces and subclasses through arrays nested in a named pair

    # initialize character info
    charName = input("What's your character's name? \n")
    charRace = input("Their race? \n")
    charClass = input("Their class? \n")
    charLevel = input("What level are they in that class? \n")
    # todo: multiclassing
    
    autoStatsQ = ""
    while (autoStatsQ != "Y" and autoStatsQ != "N"):
        autoStatsQ = input("Y or N, would you like Char to roll your stats for you? \n")
        autoStats = 0   # initialize to false
        match autoStatsQ:
            case "Y":
                autoStats = True
            case "N":
                autoStats = False
            case _:
                print("Now that's not a Y or an N, bucko")
        stats = rollStats(autoStats)
    print("Sweet! Here's a little character sheet for you:")

    print(%s%s%s%s%s%s%s % (charName, ", ", charRace, " ", charClass, " ", charLevel)
    print("STR DEX CON INT WIS CHA")
    print(" " + stats[0] + "  " + stats[1] + "  " + stats[2] + "  " + stats[3] + "  " + stats[4] + "  " + stats[5])
    
def rollStats(autoStats):
    # rollStats is only called from an input-checked environment
    stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    match autoStats:
        case True:
            print("Blowing on the dice...")
            for x in range(6): 
                stats[x] = roll(3, 6)
                return stats
        case False:
            print("Use whatever point generation method you'd like, and enter the results here:")
            for x in range(6):
                stats[x] = input(stats[x] + ": ")
                return stats

def roll(n, d):
    roll = 0
    for i in range(n):
        roll += math.floor(random.randint(0, d))
    return roll

main()
