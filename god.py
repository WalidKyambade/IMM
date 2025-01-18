
import pandas as pd

init_money = 300
init_bitcoin = 0

money = init_money
bitcoin = init_bitcoin

#Read from CSV. Date, Open, Change%
#Formatted in [date, open, change]


# Load the CSV file
file_path = '/mnt/data/Binance_1INCHBTC_1h.csv'

# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Extract the 'open' column (assuming it is named 'open')
open_values = data['open'].values

# Convert from scientific notation to standard float notation
open_values_float = [float(f"{value:.10f}") for value in open_values]

# Display results
print("Original 'open' values:")
print(open_values)
print("\nConverted 'open' values:")
print(open_values_float)

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
        