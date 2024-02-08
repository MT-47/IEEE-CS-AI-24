while True:
    num = int(input())
    if num >= 0:
        break

sum = 0
for i in range(2, num + 1,2):
    sum += i

print(f"The sum of even numbers from 1 to {num} is {sum} ({'+'.join(str(i) for i in range(2, num + 1, 2))}).")
