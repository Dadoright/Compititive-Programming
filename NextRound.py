a1 = input()
list1 = []
list1 = a1.strip().split()
list1 = [int(i) for i in list1]
a2 = input()
marks = []
marks = a2.strip().split()
marks = [int(i) for i in marks]

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