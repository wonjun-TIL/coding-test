def binary_search(data,target, low, high, loww, highh):
    # print(low, high)
    if low > high:
        aa = []
        if high >= loww:
            aa.append(high)
        if low < highh+1:
            aa.append(low)
        if high+1 < highh+1:
            aa.append(high+1)
        if low-1 >= loww:
            aa.append(low-1)
        MAX_score = 100000000000000001
        answer = -1
        for i in aa:
            if abs(data[i] - target) < MAX_score:
                answer = i
                # print("answer", answer)
                MAX_score = abs(data[i] - target)
        return answer
            
    
    mid = (low + high) // 2
    
    if data[mid] == target:
        return mid

    elif data[mid] > target:
        return binary_search(data, target, low, mid - 1,loww, highh)

    else:
        return binary_search(data, target, mid + 1, high,loww, highh)


N = int(input())

data = list(map(int, input().split()))

min_score = 100000000000000001
answer1 = 0
answer2 = N-1

index1 = 0
index2 = N-1

while index1 < index2:
    # print(min_score)
    index2 = binary_search(data,-data[index1],  index1+1, index2, index1+1, index2)
    if abs(data[index1] + data[index2]) < min_score:
        answer1 = index1
        answer2 = index2
        min_score = abs(data[index1] + data[index2])

    index1 += 1

print(data[answer1], data[answer2])
        
    
    
        
