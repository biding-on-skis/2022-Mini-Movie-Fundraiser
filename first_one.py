#functions go here


#Main routines go

want_instructions = input("do you want to read the instructions? ")

if want_instructions == "yes" or want_instructions == "Yes":
    print("instructions go here")
elif want_instructions == "no" or want_instructions == "No":
    print("no instructions ")
else:
    print("please answer yes or no")