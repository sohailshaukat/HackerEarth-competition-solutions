'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
times = int(input())
for _ in range(times):
    inp = input().split()
    branches, levels = int(inp[0]),int(inp[1])
    number_of_nodes = 0
    for i in range(levels + 1):
        number_of_nodes += branches ** i
    mod = []
    break_point = False
    while True:
        remainder = number_of_nodes%10
        mod.append(remainder)
        number_of_nodes = number_of_nodes//10
        if break_point:
            break
        if number_of_nodes < 10:
            break_point = True
    print(sum(mod))
