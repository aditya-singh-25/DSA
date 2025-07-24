n = int (input("enter number of prices you want to enter : "))
prices=[]
for i in range(n):
    a=int(input("enter the price of the stock : "))
    prices.append(a)

print(prices)

l,r=0,1
maxp = 0
while r!=len(prices):
    if prices[l]<prices[r]:
        prof=prices[r]-prices[l]
        maxp=max(maxp,prof)
    else:
        l=r
    r+=1
print(maxp)
