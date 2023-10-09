def find_Subarray_sum(A):
    l = []
    for i in range(0, len(A), 2):
        current_sum = 0
        for j in range(i, min(i + 3, len(A))):
            current_sum += A[j]
        l.append(current_sum)
    m = f"my current sum stored in a list is {l}"
    return m


A = [1, 2, 3, 4, 5, 6]
b = find_Subarray_sum(A)
print(b)
