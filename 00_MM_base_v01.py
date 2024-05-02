#functions go here

# Checks user has entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("PLease enter yes or no")

# checks that user response is not blank
def not_blank(question):


    while True:
        response = input(question)

        if response == "":
            print('sorry this cant be blank. Please try again')
        else:
            return response

# main routine starts here

# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# ask user if they want to see the instructions
want_instructions = yes_no("do you want to read the instructions? ")

if want_instructions == "yes" or want_instructions == "Yes":
    print("instructions go here")
elif want_instructions == "no" or want_instructions == "No":
    print("no instructions ")
else:
    print("please answer yes or no")

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all of your tickets")
else:
    print("you have sold {} ticket/s. There is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
