# ask user for amount
# ask user for Unit
# check that unit is in dictionary

# if unit in dictionary, convert to mL

# if no unit given / unit is unknown, leave as is.


# Functions go here
def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(unit)
        how_much = how_much * mult_by * conversion_factor

        return how_much


def unit_checker():

    unit_tocheck = input("Unit? ")

    # Abbreviation listssnip
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
        print("you chose {}".format(unit_tocheck))
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






# Main Routine Goes here
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

keep_going = ""
while keep_going =="":
    amount = eval(input("How much? "))
    amount = float(amount)


    # Get unit and change it to match dictionary
    unit = unit_checker()

    amount = general_converter(amount, unit, unit_central, 1)
    print(amount)


   # keep_going = input("<enter> or q ")
