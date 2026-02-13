
nums=[0,1,2,3,4,5,6,7,9]
class Solution :
    def missingnumber(self,nums):
        n=len(nums)
        expected_sum=n*(n+1)//2
        actual_sum=sum(nums)

        return expected_sum - actual_sum
    
if __name__ == "__main__" :
    obj=Solution()
    print(obj.missingnumber(nums))

