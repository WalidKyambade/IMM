

init_money = 300
init_bitcoin = 0

money = init_money
bitcoin = init_bitcoin

#Read from CSV. Date, Open, Change%
#Formatted in [date, open, change]


import csv
from decimal import Decimal

# Initialize the list for storing Open values
open_values = []

# Read the CSV file
with open('/home/jovyan/infinite money machine/IMM/Binance_1INCHBTC_1h.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Assuming the 'Open' column contains the Open values
        open_values.append(float(row['Open']))

# Convert the Open values from scientific notation to regular format using Decimal
open_values_normalized = [str(Decimal(value)) for value in open_values]

# Now you have `open_values_normalized_float` with the converted Open values
print(open_values_normalized)

for i in open_values_normalized:
    

#Determine Whether to Buy, Sell, or Neutral from the Past x Number of Days
def basic_algo(today_change):
    #Returns 0 if Neutral, 1 if Buy, 2 if Sell
    if(abs(today_change)):
        return 1
    else:
        return 2

#Determine Final Bitcoin and Money
def processTrans(decision, open):
    if(decision == 1 and money != 0):
        bitcoin = open/money
        money = 0
    if(decision == 2 and bitcoin > 0):
        money = bitcoin * open
        bitcoin = 0
    print("Bitcoin: " + bitcoin + "Money: " + money)
        