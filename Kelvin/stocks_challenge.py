print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input("What's your name?")
print("3.2.1"  "name")


# TODO: Write code to ask the client his savings and save it to another variable.
savings =input("How much savings do you have?")
print(savings)
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input ("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print(stock)

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables.\
#  Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company\
#  that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''
num_of_stucks = 0 

print(num_of_stucks)

if stock == "amzn":
    price = amazon
    num_of_stocks = savings
elif stock == "aapl":
    price = "aapl"
    num_of_stocks = savings

elif stock == "fb":
    price = fb
    num_of_stocks = savings
elif stock == "goog":
    price = google
    num_of_stocks = savings

elif stock == "msft":
    price = msft
    num_of_stocks = savings
else:
    price = "NA"

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased,\
#  print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
if price == "NA":
    print("Incorrect stock name entered.")
else:
    print(f"{name} has ${savings} in savings and he can buy {num_of_stocks} shares of {stock} at the current price of ${price}.")

print()

