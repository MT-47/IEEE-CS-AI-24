if __name__ == '__main__':

    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sort based on scores in descending order "searched for key part" 
    students.sort(key=lambda x: x[1], reverse=True)

    second_lowest= None
    min_score = min(student[1] for student in students) #store the last elment value
    for student in students:
        if student[1] > min_score:
            second_lowest = student[1] #last elment stored is the second lowest value

    #students names
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest]
    # Sort the names alphabetically
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
