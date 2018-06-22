# Program to find the 10001st prime number
#Its takes very much time to iterate

count = 0
a = 1
while count != 10001:
    l = 2
    while a > l:
        pass
        if a % l == 0:
            break
        else:
            l += 1

    if l == a:
        count += 1
        print(a)
    a += 1
