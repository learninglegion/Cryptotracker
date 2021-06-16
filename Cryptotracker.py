# Program to record purchases of crypto. X dollars @ Y price results in
# Z coin ownership. E.g. $3500 when BTC is at 35000 = .1 BTC
# Date of purchase optional.

# Options in program will be to enter new purchases and review/modify/
# delete previously entered purchases

# Secondary function will pull current crypto value and calculate
# percentage increase and absolute value increase for each 
# entry

# Stretch goals include multiple choice crypto selection in
# order to use proper API to pull crypto value.

# example currency formats - requires float to convert to string
# print("{:.2f}".format(ledger_entry.get('Fiat amount purchased')))
# print("{:.2f}".format(buy_dollar))

# Initialize dictionary to record info
# Maybe change this process
ledger_entry= {}

#Next step, make entry a class?

#Initial test questions below

def intro():
    print("Let's track your crypto purchases!")
    print("Enter 'q' at any time to quit.")

intro()

#Questions for variable generation - conjure better variables
p_dollars = input("First, how much money did you spend on this crypto purchase? ")
formatted_dollars = float(p_dollars)
c_name = input("What was the name of the crypto you bought? ")
o_c_price = input(f"How much was -ONE- {c_name} when bought? ")
c_obtained = input(f"How much {c_name} did you own after fees? ")

# Ask for dollars spent in purchase (force money format,
# only numbers and 1 required decimal, limit to 14 characters (billions
# plus cents)

#print("First, how much money did you spend on this crypto purchase?")
#buy_dollar = Decimal(input("Dollar amount, including cents: "))

#testing
# buy_dollar = 3500.00
def money_spent(buy_dollar):
    # print("First, how much money did you spend on this crypto purchase?")
    # buy_dollar = 3500.00
    print("${:.2f}".format(buy_dollar)) # string output
    ledger_entry['buy_dollar'] = buy_dollar

money_spent(formatted_dollars)

# Ask what crypto was bought (push string format for now, change to
# multiple choice eventually to minimize errors when matching log
# entries to live crypto feeds, max 20 characters for now)

#buy_crypto_name = input("What was the name of the crypto you\
#bought? ")

#testing
# buy_crypto_name = "BTC"
def crypto_name_bought(buy_crypto_name):
    print("What was the name of the crypto you bought?")
    # buy_crypto_name = "BTC"
    print(buy_crypto_name)
    ledger_entry['buy_crypto_name'] = buy_crypto_name

crypto_name_bought(c_name)

# Ask for price of crypto at time of purchase (numbers only, 1 decimal
# required (pre-populate in web interface?), max 20 characters)

#buy_crypto_price = input(f"How much was one\
# {buy_crypto_name} worth when you bought it? ")

#testing
def crypto_purchase_price(buy_crypto_price, cnb = c_name):
    print(f"How much was -ONE- {cnb} when bought?")
    # buy_crypto_price = 35000
    print(buy_crypto_price)
    ledger_entry['buy_crypto_price'] = buy_crypto_price

crypto_purchase_price(o_c_price)

# Record/format price of crypto at time of purchase

# Ask for amount of crypto obtained (after fees, numbers only,
# 1 decimal required, max 20 characters

#purchase_crypto_obtained = input(f"How much {buy_crypto_name} did\
# you own after fees? ")

#testing
def crypto_obtained(purchase_crypto_obtained, cnb = c_name):
    print(f"How much {cnb} did you own after fees?")
    # purchase_crypto_obtained = .1
    print(purchase_crypto_obtained)
    ledger_entry['purchase_crypto_obtained'] = purchase_crypto_obtained

crypto_obtained(c_obtained)

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

print(f"Let's make sure this is all correct. You spent \
{'${:.2f}'.format(formatted_dollars)} dollars on {c_name} when one \
{c_name} was worth ${o_c_price} and \
own {c_obtained} {c_name} as a \
result of this transaction?")

    
# p_dollars = input("First, how much money did you spend on this crypto purchase?")
# c_name = input("What was the name of the crypto you bought?")
# o_c_price = input(f"How much was -ONE- {c_name} when bought?")
# c_obtained = input(f"How much {c_name} did you own after fees?"

#After confirmation, record/format values
# Use dictionary of dictionaries with entry number as key?
# Use database and store records?
print(ledger_entry)