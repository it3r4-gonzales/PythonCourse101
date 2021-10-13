temperature = 95

if temperature > 80 :
    print("it's too hot!")
    print("Stay inside!")
elif temperature < 60 :
    print("it's too hot!")
    print("Stay inside!")

else:
    print("Enjoy the outdoors!")

#Logical Operator - or
temperature = 50

if temperature > 80 or temperature < 60 :
    print("Stay inside!")

else:
    print("Enjoy the outdoors!")

#Logical Operator - and
temperature = 50
forecast = "rain"

if temperature > 80 and forecast != "rain" :
    print("Go outside!")

else:
    print("Stay inside!")

#Logical Operator - not
forecast = "rain"

if not forecast == "rain" :
    print("Go outside!")
else:
    print("Stay inside!")

#Evaluating Boolean Variables
raining = True

if raining:
     print ("Stay inside!")

if not raining:
    print("Go outside!")
else:
    print ("Stay inside!")