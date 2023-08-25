def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f'{i}. {dwarf}')
        i+= 1

def summon_captain_planet(planeteers):
    newList = []
    for planteer in planeteers:
        newList.append(planteer.capitalize() + '!')
    return newList


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods):
    cheeses = ["camembert", "gouda", "cheddar"]
    for food in foods:
        if food in cheeses:
            return food
    return None
