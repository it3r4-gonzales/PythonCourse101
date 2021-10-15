#A Dictionary Maps Keys to Values

acronyms = {'LOL' : 'laugh out loud',
            'IDK' : "I don't know",
            'TBH' : 'To be honest'}

print(acronyms['LOL'])

#Dictionary of strings to strings
acronyms = {'LOL' : 'laugh out loud','IDK' : "I don't know"}

#Dictionary of strings to numbers
menu = {'Soup': 5, 'Salad': 6}

#Dictionary of anything
my_dict = {10:'hello',2:6.5}

#Adding new dictionary items:
acronyms['NP'] = 'no problem'

#View Current Dictionary
print(acronyms)

#Update Value in Dictionary
acronyms['TBH'] = 'honestly'

#View value
print(acronyms['TBH'])

#Delete Key 
del acronyms['LOL']

#use get so program won't crash
definition = acronyms.get('BTW')
print(definition)

#to check wether it have value or not
if definition:
    print(definition)
else:
    print("Key doesn't exist")

#Using a Dictionary to Translate a Sentence

sentence = 'IDK' + 'what happened' + 'TBH'
translation = acronyms.get('IDK')  + ' what happened ' + acronyms.get('TBH')
print('sentence:' ,sentence)
print('translation:', translation)