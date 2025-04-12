#does an array contains duplicates value



#Brute Force approach
#O(n^2)

n=int(input("enter number of elements in array : "))
nums=[]
for i in range(n):
    element=int(input("enter the element:"))
    nums.append(element)

a=False
for i in range(n):
    for j in range(i+1,n):
        if(nums[i]==nums[j]):
            a=True
            break
        
if(a==True):
    print("array contains duplicate element = True")
else:
    print("array contains duplicate element = False")
    



#Optimized
#O(n)


n=int(input("size of arrray:"))
nums=[]

for i in range(n):
    x=int(input(f"enter the {i} th element: "))
    nums.append(x)

if len(set(nums))==len(nums):
    print("array contains duplicate element = False")
else:
    print("array contains duplicate element = True")