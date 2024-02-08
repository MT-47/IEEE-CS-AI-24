String = input()

Words_List = String.split()

Rev_Words_List = Words_List[::-1]

"""""
before knowing join method 

Rev_String = ''
for i in range(len(Rev_Words_List)):
    if i != 0: #skip first word
        Rev_String += ' '
    Rev_String += Rev_Words_List[i]

"""""

Rev_String = ' '.join(Rev_Words_List)

print(Rev_String)
