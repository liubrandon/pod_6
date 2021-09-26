print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

tsla = 500
gm = 750
dowjones = 300

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
Question_One = input('What is your name? ')

# TODO: Write code to ask the client his savings and save it to another variable.
Savings = int(input(f'What is is your amount of savings, {Question_One}, without commas? '))
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
# stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
# print()
Stock_two = str(input('Which stock are your interested in? Type "tsla" for Tesla, "gm" for General Motors, "dowjones" for Dow Jones Industrial. '))
print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''
convert = int(float(Savings / tsla))
convert_two = int(float(Savings / gm))
convert_three = int(float(Savings / dowjones))

if Stock_two == "tsla":
    print(f"{Question_One} has {Savings} and is able to purchase {convert} of Tesla stock shares at the price of {tsla}. ")
elif Stock_two == "gm":
    print(f"{Question_One} has {Savings} and is able to purchase {convert_two} of General Motors stock shares at the price of {gm}.")
elif Stock_two == "dowjones":
    print(f"{Question_One} and is able to purchase {convert_three} of Dow Jones Industrial stock shares at the price of {dowjones}.")
else:
    print("Incorrect syntax, please try again")

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
# print(f"{Question_One} has {Savings} and he/she can buy 50 shares of {Stock_two} at the price of {Savings / tsla}. ")
# print(f"{Question_One} has {Savings} and he/she can buy 50 shares of {Stock_two} at the price of {Savings / gm}. ")
# print(f"{Question_One} has {Savings} and he/she can buy 50 shares of {Stock_two} at the price of {Savings / dowjones}. ")
# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.


print()
