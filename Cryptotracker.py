# Program to record purchases of crypto. X dollars @ Y price results in
# Z coin ownership. E.g. $200 when BTC is at 4371.08 = .00164 BTC
# Date of purchase optional.

# Options in program will be to enter new purchases and review/modify/
# delete previously entered purchases

# Secondary function will pull current crypto value and calculate
# percentage increase and absolute value increase for each 
# entry

#Stretch goals include multiple choice crypto selection in
#order to use proper API to pull crypto value.

#example currency formats
# print("{:.2f}".format(ledger_entry.get('Fiat amount purchased')))
# print("{:.2f}".format(purchase_dollar))

#Initialize dictionary to record info
ledger_entry= {}


#Initial test questions below

print("Let's track your crypto purchases!")
print("Enter 'q' at any time to quit.")

# Ask for dollars spent in purchase (force money format,
# only numbers and 1 required decimal, limit to 14 characters (billions
# plus cents)

#print("First, how much money did you spend on this crypto purchase?")
#purchase_dollar = Decimal(input("Dollar amount, including cents: "))

#testing
print("First, how much money did you spend on this crypto purchase?")
purchase_dollar = 3500.00
print("${:.2f}".format(purchase_dollar)) # string output
ledger_entry['purchase_dollar'] = purchase_dollar

# Ask what crypto was bought (push string format for now, change to
# multiple choice eventually to minimize errors when matching log
# entries to live crypto feeds, max 20 characters for now)

#purchase_crypto_name = input("What was the name of the crypto you\
#bought? ")

#testing
print("What was the name of the crypto you bought?")
purchase_crypto_name = "BTC"
print(purchase_crypto_name)
ledger_entry['purchase_crypto_name'] = purchase_crypto_name

# Ask for price of crypto at time of purchase (numbers only, 1 decimal
# required (pre-populate in web interface?), max 20 characters)

#purchase_crypto_price = input(f"How much was one\
# {purchase_crypto_name} worth when you bought it? ")

#testing
print(f"How much was -ONE- {purchase_crypto_name} when bought?")
purchase_crypto_price = 35000
print(purchase_crypto_price)
ledger_entry['purchase_crypto_price'] = purchase_crypto_price


# Record/format price of crypto at time of purchase

# Ask for amount of crypto obtained (after fees, numbers only,
# 1 decimal required, max 20 characters

#purchase_crypto_obtained = input(f"How much {purchase_crypto_name} did\
# you own after fees? ")

#testing
print(f"How much {purchase_crypto_name} did you own after fees?")
purchase_crypto_obtained = .1
print(purchase_crypto_obtained)
ledger_entry['purchase_crypto_obtained'] = purchase_crypto_obtained

# Record/format amount of crypto obtained (after fees)

# Ask for date purchased (determine adn push date format)

#purchase_crypto_date = input(f"What date did you purchase\
# {purchase_crypto_name}? ")

#testing
# print(f"What date did you buy {purchase_crypto_name}?")
# purchase_crypto_date = "5-31-21"
# print(purchase_crypto_date)

# Record/format date purchased

# Verify entry, push proper format - if confirmation response is 'no'
# then go back to beginning of loop or ask for element to correct.

print(f"Let's make sure this is all correct. You spent\
 {purchase_dollar} dollars on {purchase_crypto_name} when one\
 {purchase_crypto_name} was worth {purchase_crypto_price} and\
 own {purchase_crypto_obtained} {purchase_crypto_name} as a\
 result of this transaction?")

#After confirmation, record/format values
# Use dictionary of dictionaries with entry number as key?
# Use database and store records?
print(ledger_entry)