import math
list= [3, 4, 5, 6, 7, 12, 0, 15, 8]

class Solution :
    def secondMiniAndMax(self,list):
        mini= math.inf
        maxi = -math.inf
        for i in list:
            if i<mini:
                mini=i 
            if i >maxi:
                maxi=i
            sum=mini+maxi
        return f"{mini}+{maxi}={sum}"
if __name__ == "__main__":
    obj=Solution()
    print(obj.secondMiniAndMax(list))