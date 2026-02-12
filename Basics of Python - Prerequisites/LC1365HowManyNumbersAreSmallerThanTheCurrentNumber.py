"""Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.

Constraints:
2 <= nums.length <= 500
0 <= nums[i] <= 100
"""

from typing import List

nums=[8,1,4,3,2]
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            c=0
            for j in nums:
                if j<i :
                    c+=1
            ans.append(c)
        return ans
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.smallerNumbersThanCurrent(nums))

 