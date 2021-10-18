print('1: Describe what is happening below by adding comments before each line')
#box_1 is a variable set to the value of str("books")
box_1 = 'books'
#box_2 is a variable set to the value of str("clothes")
box_2 = 'clothes'
#box_3 is a variable set to the value of str("plants")
box_3 = 'plants'
#box_4 is a variable set to the value of str("kitchen stuff")
box_4 = 'kitchen stuff'

print('2: Print the variables box_1, box_2, box_3, box_4')
print([box_1, box_2, box_3, box_4])

print('3.1: Declare a variable with the name "address", assign it any street name you like')
address = str("793 Sugar Hill Road")

print('3.2: Print the address variable')
print(address)

print('4: Reassign variables box_2 and box_4 with some other text and print box_1, box_2, box_3, box_4 again')
box_2 = "Moooo"
box_4 = "Moooo"
print([box_1, box_2, box_3, box_4])

print('5.1: The line of code below is commented out because it produces many SyntaxErrors. Fix the problem and turn the comment back into regular Python code')
completion_message = 'Completed the first Python challenge'

print('5.2: Turn the comment below back into regular Python code')
print(completion_message)