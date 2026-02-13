"""Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Constraints:
1 <= n <= 10^5
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum_ = 0
        product = 1

        while temp>0:
            r = temp%10
            temp//=10
            sum_+=r
            product*=r

        return product-sum_
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.subtractProductAndSum(346))   
        