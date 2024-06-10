# Code adapted from


from datetime import date

# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = "---Mini Movie Fundraiser Ticket Data ({}/{}/{}) ---\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, year)

#heading
print(heading)
print("The filename will be {}.txt.".format(filename))
