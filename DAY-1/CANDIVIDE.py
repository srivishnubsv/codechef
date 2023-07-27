# cook your dish here
n=int(input())
list=[]
for i in range(n):
    a=int(input())
    list.append(a)
for i in range(n):
    if(list[i]%3==0):
        print("YES")
    else:
        print("NO")
