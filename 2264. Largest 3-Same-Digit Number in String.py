class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr_max=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                if num[i:i+3] > curr_max:
                    curr_max = num[i:i+3]
        return curr_max