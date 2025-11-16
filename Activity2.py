actual_cost=float(input("plz enter the actual product price: "))
sell_cost=float(input("plz enter the sell amount: "))
if sell_cost>actual_cost:
    amount=sell_cost-actual_cost
    print("total profit={0}".format(amount))
else:
    print("no profit")