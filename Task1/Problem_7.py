num = int(input())
while num < 0:
    num = int(input())

factors = []
x = num
divisor = 2
while x > 1:
    while x % divisor == 0:
        factors.append(divisor)
        x = x / divisor
    divisor += 1

factors = list(set(factors)) #remove duplicates 

print(f"Prime Factors:", ', '.join(map(str, factors)))
