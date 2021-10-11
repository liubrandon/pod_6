# dictionary inside dictionary
# lists inside dictionary
# lists in lists
# dictionaries in lists
# dictionary inside a list inside a dictionary

# HOW TO GET ? UPDATE INFO WITHIN NESTED DATA STRUCTURES

cart = {
    'cleaning_products' : ['soap', 'broom']
}

#print(cart)
#print(cart['cleaning_products'])

#print(type(cart))
#print(cart['cleaning_products'][0])
#print(cart['cleaning_products'][1])

cart['cleaning_products'].append('mop')
cart['cleaning_products'].append('lysol')

#print(cart['cleaning_products'])
#print(cart)

# adding a new list as a value in the dictionary
cart['tooth_care'] = ['toothbrush', 'floss', 'mouthwash']

#print(cart)

cart['tooth_care'].remove('floss')

#print(cart)

# use pop to remove the entire key-value pair for cleaning products
cart.pop('cleaning_products')

#print(cart)
#print(type(cart['tooth_care']))

#print(cart)

cart['home_improvement'] = {'shovel': 27.99,
                            'duct_tape': 2.17,
                            'paint': 17.43
                            }

#print(cart['home_improvement'][0])

# Lists are ORDERED so we always use the INDEX to find data inside of them
# Dictionaries are not ORDERED so we always use the KEY to find the data inside of them

print(type(cart['tooth_care']))

# Dictionary : NOT ORDERED -- key
print(type(cart['home_improvement']))
print(cart['home_improvement']['paint'])

# you have to figure out if you are working with a list or a dictionary!

cart['total_price'] = 28.99

a = [] #list
b = {} #dictionary

# you can have any data type inside of a dictionary

print(cart)

# another level of nesting

cart['tooth_care'].append({'floss': 2.39})

print(cart)

# triple nested data structure ^^^

