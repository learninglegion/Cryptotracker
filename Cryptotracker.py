# Program to record purchases of crypto. X dollars @ Y price results in
# Z coin ownership. E.g. $3500 of BTC at 35000 = .1 BTC
# Date of purchase optional. Variables given not calculated currently.

# Options in program will be to enter new purchases and review/modify/
# delete previously entered purchases

# Secondary function will pull current crypto value and calculate
# percentage increase and absolute value increase for each 
# entry

# Stretch goals include multiple choice crypto selection in
# order to use proper API to pull crypto value as well as an
# api (coinbase?) to allow people to purchase crypto in app.
# Different currencies also possible.


#######################################################################

# Initialize dictionary to record info
# Maybe change this process
ledger_entry= {}

# Next refactoring, make purchase a class - instantiate for each entry

#Initial test questions below

def intro():
    print("Let's track your crypto purchases!")
    print("Enter 'q' at any time to quit.")

intro()

#Questions for variable generation - conjure better variables
# order_dollars = input("First, dollar amount spent on this crypto purchase? ")
# f_order_dollars = float(order_dollars)
# order_crypto = input("What was the name of the crypto you bought? ")
# order_price = input(f"How much was -ONE- {order_crypto} when bought? ")
# order_bought = input(f"How much {order_crypto} did you own after fees? ")

# Ask for dollars spent in purchase (force money format,
# only numbers and 1 required decimal, limit to 14 characters (billions
# plus cents)

# example currency formats - requires float to convert to string
# print("{:.2f}".format(ledger_entry.get('Fiat amount purchased')))
# print("{:.2f}".format(buy_dollar))
#testing
# order_dollars = 3500.00
def record_money_spent():
    order_dollars = input("First, dollar amount spent on this crypto purchase?\n")
    # dollars = 3500.00
    # print("${:.2f}".format(order_dollars)) # string output
    f_order_dollars = float(order_dollars)
    ledger_entry['dollars'] = f_order_dollars

record_money_spent()

# Ask what crypto was bought (push string format for now, change to
# multiple choice eventually to minimize errors when matching log
# entries to live crypto feeds, max 20 characters for now)

#buy_crypto_name = input("What was the name of the crypto you\
#bought? ")

#testing
# crypto_name = "BTC"
def record_crypto_name():
    order_crypto = input("What was the name of the crypto you bought?\n")
    # order_crypto = "BTC"
    print(order_crypto)
    ledger_entry['order_crypto'] = order_crypto

record_crypto_name()

# Ask for price of crypto at time of purchase (numbers only, 1 decimal
# required (pre-populate in web interface?), max 20 characters)

#buy_crypto_price = input(f"How much was one\
# {buy_crypto_name} worth when you bought it? ")

#testing
def record_crypto_price(name = ledger_entry['order_crypto']):
    order_price = input(f"How much was -ONE- {name} when bought? ")
    # buy_crypto_price = 35000
    print(order_price)
    ledger_entry['order_price'] = order_price

record_crypto_price()

# Record/format price of crypto at time of purchase

# Ask for amount of crypto obtained (after fees, numbers only,
# 1 decimal required, max 20 characters

#purchase_crypto_obtained = input(f"How much {buy_crypto_name} did\
# you own after fees? ")

#testing
def record_crypto_obtained(name = ledger_entry['order_crypto']):
    order_bought = input(f"How much {name} did you own after fees? ")
    # purchase_crypto_obtained = .1
    print(order_bought)
    ledger_entry['order_bought'] = order_bought

record_crypto_obtained()

# Record/format amount of crypto obtained (after fees)

# Ask for date purchased (determine adn push date format)

#purchase_crypto_date = input(f"What date did you purchase\
# {buy_crypto_name}? ")

#testing
# print(f"What date did you buy {buy_crypto_name}?")
# purchase_crypto_date = "5-31-21"
# print(purchase_crypto_date)

# Record/format date purchased

# Verify entry, push proper format - if confirmation response is 'no'
# then go back to beginning of loop or ask for element to correct.

print(f"Let's make sure this is all correct. You spent\
 {'${:.2f}'.format(ledger_entry['dollars'])} dollars on\
 {ledger_entry['order_crypto']} when one {ledger_entry['order_crypto']}\
 was worth ${ledger_entry['order_price']} and own\
 {ledger_entry['order_bought']} {ledger_entry['order_crypto']} as a\
 result of this transaction?")

    
# p_dollars = input("First, how much money did you spend on this crypto purchase?")
# c_name = input("What was the name of the crypto you bought?")
# o_c_price = input(f"How much was -ONE- {c_name} when bought?")
# c_obtained = input(f"How much {c_name} did you own after fees?"

#After confirmation, record/format values
# Use dictionary of dictionaries with entry number as key?
# Use database and store records?
# print(ledger_entry)