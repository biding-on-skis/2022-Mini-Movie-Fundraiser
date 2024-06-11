# **** get current date for heading and filename ****

# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = "---Mini Movie Fundraiser Ticket Data ({}/{}/{}) ---\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, year)

# change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)


# heading
print(heading)
print("The filename will be {}.txt.".format(filename))
