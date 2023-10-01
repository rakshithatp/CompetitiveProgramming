from collections import Counter

shoe_num = int(input())
shoe_size = [int(i) for i in list((input().split()))]
cust_num = int(input())
orders = [
    [int(i) for i in input().split()]
    for i in range(cust_num)
    ]
stock = Counter(shoe_size)
profit = 0

for order in orders:
    shoe = order[0]
    price = order[1]
    if shoe in stock and stock[shoe] > 0:
        stock[shoe] -= 1
        profit += price

print(profit)