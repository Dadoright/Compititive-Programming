x = str(input())
total = int(x[0])
passmem = int(x[2])

y = str(input())
marks = []
count = 0
for i in y:
    if i == " ":
        continue
    else:
        marks.append(i)
    count = count +1

count = 0

passmark = marks[passmem-1]

passed = passmem
count2 = 1
for k in range(total-passmem):
    if marks[passmem-1] == marks[passmem+i]:
        passed = passed + 1
    count2 = count2+1

print(passed)
