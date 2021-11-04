print("Challenge 3.2: Playing with the stock market")

print()

#Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

# print("Challenge 3.2.1: Taking user input")
# # TODO: Write code to ask the client his name and save it to a variable.
name = input ("what's your name?")
print(name)
# # TODO: Write code to ask the client his savings and save it to another variable.
savings =("How much saving do you have?")
print(name)
stock = input ("Which stock are you interested in? \nType {'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.}")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# # TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
num_of_stocks = 0
# '''
# Your code should look like this:

if stock == "amzn":
    price = amazon
    num_of_stocks = savings/price
elif stock == "aapl":
    price = apple
    num_of_stocks = savings/price
elif stock == "fb":
    price = fb
    num_of_stocks = savings/price
    
elif stock == "google":
     price = google
     num_of_stocks = savings/price
    
elif stock == "msft":
    price = msft
    num_of_stocks = savings/price
else:
    price = "NA" 
   

print()

print("Challenge 3.2.3: Output for the user the result")
# # TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
if price == "n/a":
    print("Incorrect stock name entered")
else:
    print(f"{name} has ${savings} in savings and he could purchase {num_of_stocks}, shares of {stock} at the price ${price}")
# # Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

clients_name = "Alex"
clients_savings = "5000"


    print(f"{clients_name} has ${clients_savings} in savings and he could purchase ({num_of_stocks}/{clients_savings}), shares of {stock} at the price ${price}"))
