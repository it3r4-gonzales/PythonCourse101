menus = [['Egg Sandwich','Bagel','Coffee'],
        ['BLT','PB&J','Turkey Sandwich'],
        ['Soup','Salad','Spaghetti','Taco']]


print('Breakfast Menu:\t',menus[0]) 
print('Lunch Menu:\t',menus[1])
print('Dinner Menu:\t',menus[2])

#printing specific item inside list
print(menus[0][1])

#list become key and values
menus = {'Breakfast':['Egg Sandwich','Bagel','Coffee'],
        'Lunch':['BLT','PB&J','Turkey Sandwich'],
        'Dinner':['Soup','Salad','Spaghetti','Taco']}

print('Breakfast Menu:\t',menus['Breakfast']) 
print('Lunch Menu:\t',menus['Lunch'])
print('Dinner Menu:\t',menus['Dinner'])

#returning keys in a dictionary

for item in menus:
    print(item)

# using a Dictionary key and value in a for loop

for name, menu in menus.items():
    print(name, ':' ,menu)


