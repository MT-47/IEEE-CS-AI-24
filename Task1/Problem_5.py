Word = input()

Rev_Word = Word[::-1]

if Word == Rev_Word:
    print(f"The word '{Word}' is a palindrome")
else:
    print(f"The word '{Word}' is not a palindrome")
