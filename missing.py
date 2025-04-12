#to find the missing element in the array



#brute force approach

n = int(input("Enter the size of the array (including the missing element if any): "))
arr = []


for i in range(n - 1):  
    x = int(input(f"Enter the {i + 1}th element: "))  
    arr.append(x)


valid = True

for x in arr:
    if x < 1 or x > n:
        valid = False
        break

if not valid:
    print("Invalid input. The array must contain numbers between 1 and", n)

else:
    a = None
    for i in range(n - 1):  
        if arr[i] != i + 1:
            a = i + 1
            break

    if a:
        print(a, "is the missing element")
    else:
        print("No element is missing!")





#optimized code

n = int(input("Enter the size of the array (including the missing element if any): "))
arr = []


for i in range(n - 1):  
    x = int(input(f"Enter the {i + 1}th element: "))  
    arr.append(x)

total=n*(n+1)//2
arr_sum = 0

for x in arr:
    arr_sum = arr_sum+x

missing = total-arr_sum

print(missing," is the missing element")

