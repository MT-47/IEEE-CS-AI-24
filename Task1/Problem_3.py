def factorial(num):
    if num == 0 or num == 1 : return 1
    else: return num * factorial(num-1)

while True:
    num = int(input())
    if num >= 0 : break

#I don't know is this line is required but here it is 
factorial_expression = ' * '.join(str(i) for i in range(1, num + 1))

"""""
before knowing join method 

factorial_expression = ''
for i in range(1, num + 1):
    if i != 1: #skip first digit
        factorial_expression += ' * '
    factorial_expression += str(i)

"""""

print(f"The factorial of {num} is {factorial(num)} ({factorial_expression}).")
