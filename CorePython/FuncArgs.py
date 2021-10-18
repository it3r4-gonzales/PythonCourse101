# Default Argument Values
import time
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("Norwegian Blue")

# Default Value Evaluation
time.ctime()
def show_default(arg=time.ctime()):
    print(arg)

show_default()

#Mutable Default Values

def add_spam(menu=[]):
    menu.append("spam")
    return menu

breakfast = ['beacon', 'eggs']
add_spam(breakfast)
print(breakfast)
lunch = ['baked beans']
add_spam(lunch)
print(lunch)
add_spam()#default argument is "spam" ["spam"]
add_spam()#["spam","spam"]
add_spam()#["spam","spam","spam"]

#Immutable Default Values
