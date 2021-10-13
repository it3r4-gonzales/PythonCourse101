#empty list
empty = []
#list of strings
acronyms = ['LOL','IDK','TBH']
#list of numbers
numbers = [5,10,15,20]
#list of mixed items
anything = [5,'SDK',10.5]
#list of lists
lists = [['A','B','C'],['D','E','F']]


#Create a List and Adding Items
acronyms.append('BFN')
acronyms.append('IMHO')
print(acronyms)

#Remove items
acronyms.remove('BFN')
print(acronyms)

#Check if Exists in List
if 1 in [1,2,3,4,5]:
    print('True')

#Check if Exists in List
word = 'BFN'

if word in acronyms:
    print(word + ' is in the list')
else:
    print(word + ' is NOT in the list')

# For loop: Looping Over Each Item in a List

for acronym in acronyms:
    print(acronym)