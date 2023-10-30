def process_string(s):
    stack = []
    for char in s:
        if char != "#":
            stack.append(char)
        elif stack:
            stack.pop()
    return "".join(stack)

def check_equality_strings(a, t):
    return process_string(a) == process_string(t)

a = "ab#c"
t = "ad#c"
res = check_equality_strings(a, t)
print(res)

