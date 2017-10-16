from random import randint

def calculate_median(data):
    n = len(data)
    data.sort()
    if 0 < n <= 10000:
        if n%2 == 1:
            m = float(data[n//2])
        else:
            i = n//2
            m = (data[i - 1] + data[i])/2
        print(m)

n = 10
a = []
a_i = 0
for a_i in range(n):
    # a_t = randint(0, 9000)
    a_t = a_i + 1
    a.append(a_t)
    calculate_median(a)
