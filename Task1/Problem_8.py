while True:
    num = int(input())
    if num >= 0:
        break

proper_divs = []
for divisor in range(1,num):
    if num % divisor == 0:
        proper_divs.append(divisor)
    divisor += 1

"""""
before knowing sum method is built in
sum = 0
for i in range(len(proper_divs)):
    sum += proper_divs[i]
"""""

if sum(proper_divs) == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

