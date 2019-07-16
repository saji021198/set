a=int(input(""))
lia=list(map(str,input().split()[:a]))
lia.sort()
lia.sort(key=len)
for i in lia:
    print(i,end=" ")
