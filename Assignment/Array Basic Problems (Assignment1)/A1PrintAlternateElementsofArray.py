# print alternate elements of an array using any loop


# method1
num = [1,2,3,4,5,6,7,8,9,10]
class Solution:
    def printAlternate(self,arr:list)-> list:
        result = []
        for i in range(0,len(arr),2):
            result.append(arr[i])
        return result   

if __name__ == "__main__":
    obj = Solution()
    print(obj.printAlternate(num))


# method2

# class Solution:
#     def printAlternate(self,arr:list)-> list:
#         return arr[::2]
    
# if __name__ == "__main__":
#     obj = Solution()
#     print(obj.printAlternate([1,2,3,4,5,6,7,8,9,10]))