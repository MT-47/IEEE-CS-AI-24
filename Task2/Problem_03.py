if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    #in descending order
    arr.sort(reverse=True)

    runner_up_score = None
    for score in arr:
        if score < max(arr): #skipping the max values 
            runner_up_score = score
            break

    print(runner_up_score)
