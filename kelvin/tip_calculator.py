'''               WELCOME YOUR STEAKHOUSE                         ''' 



num_of_people = float(input("Welcome, to Your Steakhouse How many in your party ?"))
bill = float(input(" Your Bill was!"))
tax = .10 
tip = int(input("Please, Remember your tip is 15% of your bill."))

tax_amount = bill * tax
tip_amunt = tip + bill
your_total = tax_amount + tip_amunt  
splitting_your_bill = your_total / num_of_people

print(f'Your Bill was ${your_total}')
print(f'If you split your bill each person needs to pay ${splitting_your_bill}:')