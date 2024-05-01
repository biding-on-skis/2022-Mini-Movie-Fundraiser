# functions go here
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("PLease enter yes or no")


# Main routines go

want_instructions = yes_no("do you want to read the instructions? ")

if want_instructions == "yes" or want_instructions == "Yes":
    print("instructions go here")
elif want_instructions == "no" or want_instructions == "No":
    print("no instructions ")
else:
    print("please answer yes or no")
