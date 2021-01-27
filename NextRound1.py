list1 = list(map(int,input().strip().split()))[:2]
marks = list(map(int,input().strip().split()))[:list1[0]]

if marks[list1[1]-1]>0:
    count = list1[1]
else:
    count = 0
    for i in marks:
        if i>0:
            count = count + 1 

for i in range(list1[0]-list1[1]):
    if marks[list1[1]-1] == marks[list1[1]+i]:
        if marks[list1[1]+i] > 0:
            count = count+1
    else:
        break
    
print(count)