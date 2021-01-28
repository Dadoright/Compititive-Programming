size = list(map(int,input().strip().split()))[:2]

if size[0]%2 == 0 or size[1]%2 == 0:
    print(int(size[0]*size[1]/2))
else:
    print(int((size[0]*size[1]-1)/2))