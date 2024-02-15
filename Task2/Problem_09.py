
set1 = input("Enter the first set: ")
set1 = set(map(int, set1.split()))

set2 = input("Enter the second set: ")
set2 = set(map(int, set2.split()))

common = set1.intersection(set2)

print("Common elements:", common)
