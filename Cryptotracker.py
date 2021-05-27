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

from decimal import Decimal

# Use entry_number as dictionary key for each entry - increment by one
# after each entry confirmed.
entry_number = 1

print("Let's track your crypto purchases!")
print("Enter 'q' at any time to quit.")

# Ask for dollars spent in purchase (force money format,
# only numbers and 1 required decimal, limit to 14 characters (billions
# plus cents)
print("First, how much money did you spend on this crypto purchase?")
purchase_dollar = Decimal(input("Dollar amount, including cents: "))

# Record dollars spent in purchase

# Ask what crypto was bought (push string format for now, change to
# multiple choice eventually to minimize errors when matching log
# entries to live crypto feeds, max 20 characters for now)
purchase_crypto_name = input("What was the name of the crypto you\
 bought? ")

#Record what crypto was bought

# Ask for price of crypto at time of purchase (numbers only, 1 decimal
# required (pre-populate in web interface?), max 20 characters)
purchase_crypto_price = input(f"How much was one\
 {purchase_crypto_name} worth when you bought it? ")

# Record price of crypto at time of purchase

# Ask for amount of crypto obtained (after fees, numbers only,
# 1 decimal required, max 20 characters
purchase_crypto_obtained = input(f"How much {purchase_crypto_name} did\
 you own after fees? ")

# Record amount of crypto obtained (after fees)

# Ask for date purchased (determine adn push date format)
purchase_crypto_date = input(f"What date did you purchase\
 {purchase_crypto_name}? ")

# Record date purchased

# Verify entry, push proper format - if confirmation response is 'no'
# then go back to beginning of loop or ask for element to correct.
print(f"Let's make sure this is all correct. You spent\
 {purchase_dollar} dollars on {purchase_crypto_name} when one\
 {purchase_crypto_name} was worth {purchase_crypto_price} and\
 own {purchase_crypto_obtained} {purchase_crypto_name} as a\
 result of this transaction?")

 #After confirmation, record values