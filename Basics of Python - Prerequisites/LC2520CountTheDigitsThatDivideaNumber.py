"""
Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.

Constraints:
1 <= num <= 109
num does not contain 0 as one of its digits.
"""


# while num>0:
#     r=num%10
#     print(r,end=" ")
#     num//=10
num=7

class Solution:
    def countDigits(self, num: int) -> int:
        temp=num
        ans=0 
        while temp>0:
            r=temp%10
            if num%r==0:
                ans+=1
            temp//=10

        return ans

        

if __name__ == "__main__":
    obj = Solution()
    print(obj.countDigits(num))  
