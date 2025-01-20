import csv
from decimal import Decimal

BUY_PERCENT = -0.20  # Example: Buy when price decreases by 20%
SELL_PERCENT = 0.20  # Example: Sell when price increases by 20%

money = 1000 # Example: Starting with 1000 money
bitcoin = 0 # Example: Initially owning no Bitcoin

amtTrades = 0
#Fee is 1 - % taken
fee = 1

file_path = "IMM/Binance_1INCHBTC_1hrecent.csv"

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


def open_values_normalized_and_mirrored(file_path):
    """
    Reads a CSV file, extracts the 'Open' column, converts its values 
    from scientific notation to a regular float format using Decimal, 
    and mirrors (reverses) the order of the values.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        list: A list of mirrored 'Open' values in regular float format.
    """
    # Initialize the list for storing Open values
    open_values = []

    # Read the CSV file
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            # Assuming the 'Open' column contains the Open values
            open_values.append(float(row['Open']))

    # Convert the Open values to regular float format using Decimal
    open_values_normalized = [float(Decimal(value)) for value in open_values]

    # Mirror the list (reverse the order)
    open_values_normalized.reverse()

    return open_values_normalized

# main algorithm that runs every hour, assesses whether or not to buy, hold, or sell, based
# on last price recorded

# Function to perform the action based on the percent change
def switch(percent_change, curr_price):
    global money, bitcoin, amtTrades  # To modify global variables money and bitcoin

    if(percent_change < BUY_PERCENT):
        # If no money available
        if(money < curr_price):
            pass  # Do nothing if we can't afford to buy
        else:
            # Full buy
            bitcoin = money / curr_price
            #Add Coinbase Fees
            bitcoin *= fee
            amtTrades += 1
            money = 0  # All money is used to buy Bitcoin
            print(f"Buying Stock at {curr_price}, Total Stock: {bitcoin}")

    elif(percent_change > SELL_PERCENT):
        # If no Bitcoin held
        if(bitcoin == 0):
            pass  # Do nothing if no Bitcoin to sell
        else:
            # Full sell
            money = money + (bitcoin * curr_price)  # Sell all Bitcoin
            #Add Coinbase Fees
            money *= fee
            amtTrades += 1
            bitcoin = 0  # Reset Bitcoin ownership
            print(f"Selling Stock at {curr_price}, Total money: {money}")

# Main loop
full_open = open_values_normalized_and_mirrored(file_path) #added this to save time
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
    print(f"Stock: [{bitcoin}]\n")

#Sells All At the End so We Can See the Profit. Then Prints the Bitcoin and Money
switch(SELL_PERCENT + 0.01, float_open[len(float_open) - 1])

print(f"Money: [{money}]\n")
print(f"Stock: [{bitcoin}]\n")
print(f"NumTrades:{amtTrades}\n")



