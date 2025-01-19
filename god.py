import csv
from decimal import Decimal

BUY_PERCENT = -0.20  # Example: Buy when price decreases by 20%
SELL_PERCENT = 0.20  # Example: Sell when price increases by 20%

money = 1000 # Example: Starting with 1000 money
bitcoin = 0 # Example: Initially owning no Bitcoin

for i in open_values_normalized:
    

#Read from CSV. Date, Open, Change%
#Formatted in vec.[open]

#Determine Whether to Buy, Sell, or Neutral from the Past x Number of Days
def basic_algo(today_change):
    #Returns 0 if Neutral, 1 if Buy, 2 if Sell
    if(abs(today_change)):
        return 1
    else:
        return 2


def convert_to_floats(string_array):
    """
    Convert an array of numbered strings to an array of floats.
    
    Args:
        string_array (list): A list of strings representing numbers.
    
    Returns:
        list: A list of floats converted from the input strings.
    """
    try:
        return [float(item) for item in string_array]
    except ValueError as e:
        print(f"Error: One of the items is not a valid number. {e}")
        return []


def open_values_normalized():
    # Initialize the list for storing Open values
    open_values = []

    # Read the CSV file
    with open("infinite money machine/IMM/Binance_1INCHBTC_1h.csv", mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            # Assuming the 'Open' column contains the Open values
            open_values.append(float(row['Open']))

    # Convert the Open values from scientific notation to regular format using Decimal
    open_values_normalized = [str(Decimal(value)) for value in open_values]

    # Now you have `open_values_normalized_float` with the converted Open values
    return open_values_normalized

#Determine Final Bitcoin and Money
def processTrans(decision, open):
    if(decision == 1 and money != 0):
        bitcoin = open/money
        money = 0
    if(decision == 2 and bitcoin > 0):
        money = bitcoin * open
        bitcoin = 0
    print("Bitcoin: " + bitcoin + "Money: " + money)
        

# main algorithm that runs every hour, assesses whether or not to buy, hold, or sell, based
# on last price recorded

# Function to perform the action based on the percent change
def switch(percent_change, curr_price):
    global money, bitcoin  # To modify global variables money and bitcoin

    if(percent_change < BUY_PERCENT):
        # If no money available
        if(money < curr_price):
            pass  # Do nothing if we can't afford to buy
        else:
            # Full buy
            bitcoin = money / curr_price
            money = 0  # All money is used to buy Bitcoin
            print(f"Buying Stock at {curr_price}, Total Stock: {bitcoin}")

    elif(percent_change > SELL_PERCENT):
        # If no Bitcoin held
        if(bitcoin == 0):
            pass  # Do nothing if no Bitcoin to sell
        else:
            # Full sell
            money = money + (bitcoin * curr_price)  # Sell all Bitcoin
            bitcoin = 0  # Reset Bitcoin ownership
            print(f"Selling Stock at {curr_price}, Total money: {money}")

# Main loop
full_open = open_values_normalized() #added this to save time
float_open = convert_to_floats(full_open)
for x, curr_price in enumerate(float_open):  # Assuming open_values_normalized is an iterable
    if x - 1 < 0:
        last_price = curr_price  # No previous price if at the start
    else:
        last_price = float_open[x - 1]  # Previous price

    # Calculate percent change
    percent_change = ((curr_price - last_price) / last_price) * 100
    
    # Call switch to handle the decision-making process
    switch(percent_change, curr_price)

    print(f"Money: [{money}]\n")
    print(f"Stock: [{bitcoin}]\n")\
    
    userinput = input("1HourLater:")



