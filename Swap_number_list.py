def swap_first_and_last(l):
    #o(1)
    first = l[0]
    m = len(l)
    last = l[m-1]
    l[0] = last
    l[m-1] = first
    return  l

def swap_first_and_last1(l):
    #o(1)
    l[0],l[-1] = l[-1],l[0]
    return  l

def swap_first_and_last2(l):
    #o(n)
    get = l[-1],l[0]
    l[0], l[-1] = get
    return  l

def swap_first_and_last3(l):
    a,*b,c = l
    m = [c,*b,a]
    return  m

def swap_first_and_last4(l):
    first = l.pop(0)
    last = l.pop(-1)
    l.insert(0,last)
    l.append(first)
    return  l

def swap_first_and_last5(l):
    if len(l) > 2 :
        l  = l[-1 : ] + l[1:-1] + l[ : 1]

    return  l
l = [12, 35, 9, 56, 24]
l1 = [1,2,3]
out = swap_first_and_last5(l)
print(out)