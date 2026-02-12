"""Given two non-negative integers low and high.
Return the count of odd numbers between low and high (inclusive).

Constraints:
0 <= low <= high <= 10^9"""


class Solution:
    def countOdds(self,low:int,high:int)-> int:
        return (high+1)//2- (low//2)
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.countOdds(4,80))  