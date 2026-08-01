class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
            
            f={}
            n= len(nums)
            win_s= 0
            max_s= 0
            for i in range(k):
                f[nums[i]]=f.get(nums[i],0)+ 1
                win_s += nums[i]

            if len(f) == k:
                max_s= max(max_s,win_s)

            for i in  range(k,n):

                f[nums[i]]= f.get(nums[i], 0)+1
                win_s += nums[i]

                f[nums[i-k]]= f.get(nums[i-k])-1
                if f[nums[i-k]] == 0:
                    del f[nums[i-k]]
                win_s -=    nums[i-k]

                if len(f)== k:
                    max_s = max(max_s, win_s)
                
            return max_s 