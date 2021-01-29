string1 = input().lower()
string2 = input().lower()

for i in range(len(string1)):
    if string1[i] == string2[i]:
        count = 0
    elif string1[i] != string2[i]:
        if ord(string1[i]) < ord(string2[i]):
            count = -1
            break
        else:
            count = 1
            break

print(count)