from itertools import product
print("Plz enter the elements for A seperated by spaces",)
A = list(map(int,input().split()))
print("Plz enter the elements for B seperated by spaces",)
B = list(map(int, input().split()))

output = list(product(A,B))

for item in output:
    print(item,"",end="")