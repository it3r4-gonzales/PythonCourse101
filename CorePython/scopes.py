count = 0
def show_count(): #this default because no value set into global
    print(count)

def set_count(c):
    count = c
    
show_count()

set_count(5) #global count set to default = 0
show_count() #global count set to default = 0

def set_count(c):
    global count #set the global
    count = c

show_count()

set_count(5)
show_count()