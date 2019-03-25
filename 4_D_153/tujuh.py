def binSe(list, target):
    low = 0
    high = len(list) -1
    data = []
    while(low != high):
        mid = (high + low) //2
        if(list[mid] == target):
            break
        elif(target < list[mid]):
            high = mid -1
        else:
            low = mid +1
    for i in range (low, high):
        if target == list[i]:
            data.append(i)
    return data

list = [2,3,4,5,8,8,9,12]
target = 8
print(binSe(list,target))


        
