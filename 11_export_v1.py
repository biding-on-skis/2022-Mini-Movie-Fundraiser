import pandas
import random
from datetime import date

# dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 750, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge

}
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# print(mini_movie_frame)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# choose a winner from our name list
winner_name = random.choice(all_names)

# get position of winner name in list
win_index = all_names.index(winner_name)

# look up total amount won (ie: ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, 'Total']

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')
print(mini_movie_frame)

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

# create strings for printing...
ticket_costs_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Profit : ${}".format(total)
total_profit = "Total Profit : ${}".format(profit)




print()
print('<----Raffle Winner---->')
print('Congratulations {}. You have won ${} ie: your' ' ticket is free!'.format(winner_name, total_won))
