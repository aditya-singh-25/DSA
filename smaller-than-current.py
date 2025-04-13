# to return all the numbers smaller than current  number in array
# TC = O(n^2)

n=int(input("enter the length of array : "))
arr=[]

for i in range(n):
    a=int(input(f"enter the {i+1} th element : "))
    arr.append(a)

res=[]
for i in range(n):
    count = 0
    for j in range(n):
        if arr[i]>arr[j]:
            count+=1
    res.append(count)

print(res)            


# optimal solution
# TC = O(nlogn)

n=int(input("enter the length of array : "))
arr=[]

for i in range(n):
    a=int(input(f"enter the {i+1} th element : "))
    arr.append(a)

temp=sorted(arr)
hm={}
res=[]

for i , num in enumerate(temp):
    if num not in hm:
        hm[num]=i

for i in arr:
    res.append(hm[i])

print(res)