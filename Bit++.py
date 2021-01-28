iter = int(input())
count = 0

for i in range(iter):
    change = input().strip('X')
    
    if change == '++':
        count = count+1
    elif change == '--':
        count = count-1

print(count)
