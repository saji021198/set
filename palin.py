d=str(input())
k=len(d)
c=round(k/2)
string1=""
rev=d[k-1:c-1:-1]
for i in range (1,c):
    string1=string1+d[i]
if(string1==rev):
    print("yes")
else:
    print("no")
