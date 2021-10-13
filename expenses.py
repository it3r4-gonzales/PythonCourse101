##sum of expenses
# expenses = [10.5,8,5,15,20,5,3]
# sum = 0

# for value in expenses:
#     sum = sum + value

# print("You spent $", sum, " on lunch this week.", sep='')

#sum function

expenses = [10.5,8,5,15,20,5,3]
total = sum(expenses)

print("You spent $", total, " on lunch this week.", sep='')

#Adding Input To Expenses Calculator
total2=0
expenses2 = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses2.append(float(input("Enter an expense:")))
total2 = sum(expenses2)

print("You spent $", total2, sep=' ')

