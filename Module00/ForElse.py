for num in range(10, 20):
    for i in range(2,num):
        if num%9 == 0:
            j=num/i
            print(('%d equals %d * %id') % (num, i, j))
            break
        else:
            print(num, 'is a prime member')