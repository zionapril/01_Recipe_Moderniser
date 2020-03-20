# Get's recipe name and checks it is not blank


# Not Blank Function goes here
def not_blank(question):

    error = "Sorry - this can't be blank or contain numbers"

    valid = False
    while not valid:
        has_errors = ""
        response = input(question)

        # look at each character in string and if its a number, complain
        for letter in response:
            if letter.isdigit():
                has_errors = "yes"
                break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue

        else:
            return response

# Main Routine goes here

recipe_name = not_blank("What is the recipe name? ")
your_name = not_blank("Who are you? ")

print("Hello {}, You are making {}".format(your_name, recipe_name))