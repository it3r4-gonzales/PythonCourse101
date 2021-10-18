r = [1, -4, 10 ,15, -2]
print(r[-1])
print(r[-2])
print(r[len(r)-1])

print(r[0])
print(r[-1])#same as r[0]

#slicing

print(r[1:3])
print(r[1:-1])
print(r[2:])
print(r[:])

a = [[1,2],[3,4]]
b= a[:]
print(a is b)
a==b
print(a[0],b[0])
print(a[0] is b[0])

a[0] = [8,9]
print(a[0],b[0])
a[1].append(5)
print(a[1],b[1])

c= [21,37]
d= c*4
print(d)

print([0]*9)
s = [[-1,+1]] *5
print(s)

s[2].append(7)

w = "the quick brow fox jumps over ther lazy dog".split()
print(w)
i = w.index('fox') #find index of fox
print(i)

print(w.count("the")) #count the word occurence
print(1 in [1, -4, 10 ,15, -2]) #check 1 is in the list

#delete in list
u = "jackdaws love my big sphinx of quartz".split()
print(u)
del u[3]
print(u)
u.remove('jackdaws')
print(u)
del u[u.index('quartz')]

#insert
a = 'I accidentally the whole universe'.split()
print(a)
a.insert(2, "destroyed")
print(a)
print(''.join(a))

#concatenate
m = [1,2,3]
n = [4,5,6]
k = m + n
print(k)

k += [7,8,9] #input in k list
k.extend([10,11,12])
print(k)
#reverse the list order
g = [1,2,3]
print(g.reverse())
#sort the list order
d = [3,1,2]

d.sort()
print(d)

#reverse in sort
d.sort(reverse=True)
print(d)

h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
print(h)
h.sort(key=len)
print(' '.join(h))

