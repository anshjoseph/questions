#n = 5
#if n == 2:
#    print(True)
#if n == 3:
#    print(True)
#if n & 1 == 0:
    #even number has zero at the end
    #and odd number has 1 at the end
#    print(False)
#d= 3
#while d * d <= n:
#    if n % d == 0:
#        print(False)
#    d= d + 2
#print(True)


def ch_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n & 1 == 0:
        return False
    d= 3
    while d * d <= n:
        if n % d == 0:
            return False
        d= d + 2
    return True


data = list()

count = 0
for i in range(2,1001):
    if i % 100 == 0:
        count += 10
        print(f'{count}%')
    if ch_prime(i):
        data.append(i)