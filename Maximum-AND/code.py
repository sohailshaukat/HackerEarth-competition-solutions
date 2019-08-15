'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
times = int(input())
for _ in range(times):
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    maximum_and = 0
    maximum = (2 ** len(bin(a).replace('0b','')))-1
    for i in range(b+1,a,-1):
        if i &(i-1) > maximum_and:
            maximum_and = i&(i-1)
        if maximum_and == maximum:
            break
    print(maximum_and)
