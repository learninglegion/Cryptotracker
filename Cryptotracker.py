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



print("Let's track your crypto purchases!")
print("Enter 'q' at any time to quit.")

# Ask for dollars spent in purchase (push decimal format)
print("First, how much money did you spend on this crypto purchase?")
p_dollar = Decimal(input("Dollar amount, including cents: "))
print(p_dollar)

# Record dollars spent in purchase

#Ask what crypto was bought (push string format)
p_crypto_name = input("What was the name of the crypto you bought? ")

#Record what crypto was bought

# Ask for price of crypto at time of purchase (cover millions/ths)
p_crypto_price = input(f"How much was one {p_crypto_name} worth when\
 you bought it? ")

# Record price of crypto at time of purchase

# Ask for amount of crypto obtained (after fees) (millions/ths)
p_crypto_obtained = input(f"How much {p_crypto_name} did you own after\
 fees? ")

# Record amount of crypto obtained (after fees)

# Ask for date purchased (determine adn push date format)
p_crypto_date = input(f"What date did you purchase {p_crypto_name}? ")

# Record date purchased

#Verify entry, push proper formats
print(f"Let's make sure this is all correct. You spent {p_dollar}\
 dollars on {p_crypto_name} when one {p_crypto_name} was worth\
 {p_crypto_price} and own {p_crypto_obtained} {p_crypto_name}\
 as a result of this transcation?")

 #After confirmation, record values