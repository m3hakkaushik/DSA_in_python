"""There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.

Constraints:
n == candies.length
2 <= n <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50"""

from typing import List


candies=[2,3,5,1,3]  
extraCandies=3
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ans = []

        for i in candies:
            if (i+extraCandies)>=maxCandies:
                ans.append(True)
            else:
                ans.append(False)

        return ans
    


if __name__ == "__main__":
    obj = Solution()
    print(obj.kidsWithCandies(candies,extraCandies))


#   return[(i+extraCandies)>=max(candies) for i in candies ]

