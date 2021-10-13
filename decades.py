#Creating an Age Calculator
age = int(input("How old are you? \n"))

decade = age // 10
year = age % 10 # % is modulo gets the remainder value


print("You are " + str(decade) + "decades and " + str(year)  + " years old.")