from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans=[]
        minimum_diff =float('inf')

        for i in range(len(arr)-1):
            minimum_diff=min(minimum_diff, arr[i+1]-arr[i])

        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==minimum_diff:
                ans.append([arr[i],arr[i+1]])

        return ans
        