"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Constraints:
-231 <= x <= 231 - 1
"""

num=71317
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev=0
        
        while temp>0:
            r = temp%10
            temp//=10
            rev=(rev*10+r)
        
        if rev==x:
            return True
        else:
            return False     #instead od if-else : "return rev==x"
        



if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome(num))  

"""
-------------------------------------------------------------
-------------------------------------------------------------
arr=[3,7,6,7,3]
new=[]
for i in range(len(arr)-1,-1,-1):
    new.append(arr[i])

if new==arr:
    return True
else:
    return False
-------------------------------------------------------------
-------------------------------------------------------------
"""