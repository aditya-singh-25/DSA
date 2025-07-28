from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count=0
        num=[]
        for i in range(len(nums)):
            if i==0:
                num.append(nums[i])
            elif nums[i]==nums[i-1]:
                continue
            else:    
                num.append(nums[i])
        for i in range(len(num)):
            if i==0:
                continue
            elif i==len(num)-1:
                continue
            
            elif num[i]>num[i-1] and num[i]>num[i+1]:
                count=count+1
            elif num[i]<num[i-1] and num[i]<num[i+1]:
                count+=1
            
        return count
                