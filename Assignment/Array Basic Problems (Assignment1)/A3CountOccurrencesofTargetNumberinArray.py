num=[3,4,5,3,5,7]
target=3
class Solution:
    def countoccurrencesoftarget(self, arr: list) -> list:
        count=0
        for i in arr:
            if i == target :
                count+=1
        return count
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.countoccurrencesoftarget(num))

                
