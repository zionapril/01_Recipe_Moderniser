# Conversion Function...

import csv

# ***** Functions go here *****
def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(lookup)
        how_much = how_much * float(mult_by) / conversion_factor
        converted = "yes"

    else:
        converted = "no"



    return [how_much, converted]

def unit_checker():

    unit_tocheck = input("Unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    ounce = ["oz", "fluid", "ounce", "fl"]
    cup = ["c", "cup"]
    pint = ["p", "pt"]
    quart = ["q", "qt"]
    millilitre = ["ml", "mL"]
    litre = ["L", "l"]
    decilitre = ["dl", "dL"]
    pound = ["lb", "#"]

    if unit_tocheck == "":
       # print("you chose {}".format(unit_tocheck))
            return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in millilitre:
        return "millilitre"
    elif unit_tocheck.lower() in litre:
        return "litre"
    elif unit_tocheck.lower() in decilitre:
        return "decilitre"
    elif unit_tocheck.lower() in pound:
        return "pound"
    else:
        return unit_tocheck

# **** Main Routine Goes here ****

# dictionaries go here
unit_central = {
    "tsp" : 5,
    "tbs" : 15,
    "cup" : 237,
    "ounce" : 30,
    "pint" : 473,
    "quart" : 946,
    "pound" : 454,
    "litre" : 1000
}

# *** Generate food dictionary ***
# open file
groceries = open('01_ingredients_ml_to_g.csv')

# Read data into a list
csv_groceries = csv.reader(groceries)

# Create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (first item in row is key, next is definition)

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

print(food_dictionary)

