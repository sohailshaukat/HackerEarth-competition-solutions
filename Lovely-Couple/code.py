'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
import math
def factorization(n):
    i = 2
    num = n[0]
    factors = []
    limit = int(math.sqrt(num))+2
    while i <= limit:
        if num % i == 0:
            if i == math.sqrt(num):
                factors.append(i)
            else:
                factors.append(i)
                factors.append(int(num/i))
        i += 1
    return factors
if __name__ == '__main__':
    times = int(input())
    for _ in range(times):
        inp = input().split()
        a = int(inp[0])
        b = int(inp[1])
        lowest_common_multiple = factorization([a])+factorization([b])
        lowest_common_multiple = (list(set(lowest_common_multiple)))
        factors = lowest_common_multiple
        counter = 0
        for factor in factors:
            if len(factorization([factor]))==2:
                counter += 1
        if len(factorization([counter]))==2 and counter !=0 and counter != 1:
            print("Yes")
        else:
            print("No")
