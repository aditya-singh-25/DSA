# to find those elements whose sum = target


#brute force approach 
# TC = O(n^2)

n=int(input("enter the length of array : "))
arr=[]

for i in range(n):
    a=int(input(f"enter the {i+1} th element : "))
    arr.append(a)

tar=int(input("enter target sum : "))
found = False

for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] == tar:
            print(arr[i]," + ",arr[j]," = ",tar)
            found = True
            break
            

if found==False:
    print("no such elements foun to have sum = target")



# Optimal solution 
# TC  = O(n)


n=int(input("enter the length of array : "))
arr=[]

for i in range(n):
    a=int(input(f"enter the {i+1} th element : "))
    arr.append(a)

tar=int(input("enter target sum : "))

h_m = {}
found = False

for i , v in enumerate(arr):
    if tar-v in h_m:
        print("indices:", h_m[tar - v], "and", i,"& ",  "values:", arr[h_m[tar - v]], "and", v)

        found = True
    else:
        h_m[v] = i
    
if not found:
    print("no such pair present")