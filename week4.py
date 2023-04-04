def process_string(s):
    L = s.split()
    for i, word in enumerate(L):
        L[i] = word.lower()
    return L

def process_string(s):
    L = s.split()
    for i, word in enumerate(L):
        if i % 2 == 0:
            L[i] = word.lower()
        else:
            L[i] = word.upper()
    return L

def fizz_buzz_sumz(i):
    sum = 0
    for x in range (1, i+1):
        if x % 3 ==0 and x % 5 == 0:
            continue
        elif x % 3 == 0:
            sum += 3*x
        elif x % 5 == 0:
            sum += 5*x
        else:
            sum += x
    return sum
