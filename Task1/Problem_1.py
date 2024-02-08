numbers = []

while True:
    num = int(input())
    if num == -1:
        break
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)

print(largest, smallest)
