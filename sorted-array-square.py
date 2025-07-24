n=int(input("enter numbers of elemenmts you want : "))
arr=[]
for i in range(n):
    inp=int(input("enter the element : "))
    arr.append(inp)
print(arr)
sorted_sq=[]
for i in range(n):
    sorted_sq.append(arr[i]*arr[i])

sorted_sq.sort()
print(sorted_sq)

#more optimized code below
# n = int(input("Enter number of elements: "))
# arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
# print("Original list:", arr)

# # Use list comprehension for squaring
# sorted_sq = [x * x for x in arr]
# print("Squared list:", sorted_sq)
