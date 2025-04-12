#to find the all missing elements in an array


#optimal solution [ O(n)]

n=int(input("enter the length of array : "))
arr=[]

for i in range(n):
    a=int(input(f"enter the {i+1} th element : "))
    arr.append(a)

res=[]
set_arr = set(arr)

for i in range(1,len(arr)+1):
    if i not in set_arr:
        res.append(i)

print(res," are not present in array ")
        

