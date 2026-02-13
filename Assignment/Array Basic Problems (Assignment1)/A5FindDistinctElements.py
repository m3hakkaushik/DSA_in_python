"""Given an integer array arr[], 
return the count of all the distinct elements in an array
Constraints:
1  ≤  arr.size()  ≤  105
-1000  ≤  arr[i]  ≤  1000
"""

num=[2,4,3,2,2,5,6]

class Solution:
    def findDistinctElements(self,arr):
        distinct=[]
        count=0
        
        for n in arr:
            if n not in distinct:
                distinct.append(n)
                count+=1
            result=f"distinct elements:{distinct}\ncount:{count}"
        return result
    
if __name__ == "__main__":
    obj=Solution()
    print(obj.findDistinctElements(num))
    
