

init_money = 300
init_bitcoin = 0

money = init_money
bitcoin = init_bitcoin

#Read from CSV. Date, Open, Change%
#Formatted in [date, open, change]

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
        