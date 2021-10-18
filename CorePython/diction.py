name_and_pages = [('Alice', 32),('Bob', 48),('Charlie', 14)]
d = dict(name_and_pages)
print(d)
phonetic = dict(a='alfa', b='bravo', c='charlie')
print(phonetic)

#copy dict
e = d.copy() 
print(e)
f = dict(e)
print(f)

#update dict
g = dict(d='danie',e='echo')
f.update(g)
print(f)

#dictionary iteration

phonetics = dict(f)

for key in phonetics:
    print(f"{key} => {f[key]}")

#printing the values
for value in phonetics.values():
    print(value)

for key in phonetics.keys():
    print(key)

for key,value in phonetics.items():
     print(f"{key} => {value}")

m = {'A':[1],'B':[2,4]}
m['A'] += [5,7]
print(m)