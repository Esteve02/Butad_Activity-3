# promt the user to enter purchase amount and display the sales tax (6%) with two digits after the dicimal point.

amount = float(input('Enter Purchase Amount: '))

# assign variable for the sales tax
tax= 0.06

# compute amount with tax
comp = amount * tax
comp = "{:.2f}".format(comp)

print('purchase amount: ', amount)
print('sales tax', comp)