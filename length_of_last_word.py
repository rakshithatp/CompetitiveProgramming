def lengthOfLastWord(s):
    s = s.split()
    last_word = s[-1]
    count = 0
    for i in last_word:
        count += 1
    return count

s = "Hello World"
a = lengthOfLastWord(s)
print(a)