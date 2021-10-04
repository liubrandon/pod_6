print ("Challenge 3.2: Playing with the stock market")

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
facebook = 250
google = 1400
microsoft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
Name= input("what is your name? ")
# TODO: Write code to ask the client his savings and save it to another variable.
Savings= input("What is your savings?")
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

amzn=amazon
aapl=apple
fb=facebook
goog=google
msft=microsoft

number_of_stocks= 0

if stock == amzn:
    number_of_stocks=(Savings/amazon)
elif number_of_stocks>0:
    print(f"Congratulations {Name} you have {Savings} of savings and you can buy {number_of_stocks} Amazon stocks ")
elif number_of_stocks<0:
    print("Sorry, you can not buy Amazon stocks with the {savings}")
elif stock== aapl:
     number_of_stocks=(Savings/apple)
elif number_of_stocks>0:
    print(f"Congratulations {Name} you have {Savings} of savings and you can buy {number_of_stocks} Apple stocks ")
elif number_of_stocks<0:
    print("Sorry, you can not buy Apple stocks with the {savings}")
elif stock== fb:
   number_of_stocks=(Savings/facebook)
elif number_of_stocks>0:
    print(f"Congratulations {Name} you have {Savings} of savings and you can buy {number_of_stocks} Facebook stocks ")
elif number_of_stocks<0:
    print("Sorry, you can not buy Facebook stocks with the {savings}")
elif stock==goog:
    number_of_stocks=(Savings/google)
elif number_of_stocks>0:
    print(f"Congratulations {Name} you have {Savings} of savings and you can buy {number_of_stocks} Google stocks ")
elif number_of_stocks<0:
    print("Sorry, you can not buy Google stocks with the {savings}")
elif stock==msft:
    number_of_stocks=(Savings/microsoft)
elif number_of_stocks>0:
    print(f"Congratulations {Name} you have {Savings} of savings and you can buy {number_of_stocks} Google stocks ")
elif number_of_stocks<0:
    print("Sorry, you can not buy Google stocks with the {savings}")
else:
     print("No stocks can be purchased with amount of savings at this time")


print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.



print(f"{Name} has {Savings} and he can buy {number_of_stocks} shares of {stock} at the current price of $100")