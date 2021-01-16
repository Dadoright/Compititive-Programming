count = int(input())
sum1 = 0 
prob = 0
for i in range(count):
    x = str(input())
    for i in x:
        if i == " ":
            continue
        else:
            x2 = int(i)
            sum1 = sum1 + x2
    if sum1 >1:
        prob = prob+1
    sum1 = 0
print(prob)
