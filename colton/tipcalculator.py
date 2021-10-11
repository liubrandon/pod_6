# Tip calculator

# Colton McPhail Project #1 J.T.C.

while True:
    try:
        user_input = input("What is the total of your check? > $")
        total_check = float(user_input)
        break 
    except ValueError:
        print("I'm sorry, looks like you typed something incorrectly. Try typing in a number! :)")


while True:
    tip_choice = input("Would you like to leave a 10 percent tip? Type yes or no ")
    if tip_choice not in ('yes'):
        print("Type yes to see 10 percent tip ")
    else:
        if tip_choice == "yes":
            result = .10 * total_check  
    
        
        print("You should leave a $%.2f tip," % (result))
        print("The Total Amount is, ")
        print(total_check+result)
        break