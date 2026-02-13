import math
list= [3, 4, 5, 6, 7, 12, 0, 15, 8]

class Solution :
    def secondMiniAndMax(self,list):
        mini= math.inf
        secondmin= math.inf
        a=secondmin 
        maxi = -math.inf
        secondmax = - math.inf
        b=secondmax
        for i in list:
            if i<mini:
                mini=i 
            if i < a and i > mini:
                a = i
            if i >maxi:
                maxi=i
            if i > b and i < maxi:
                b = i
        return f"-----MINIMUM----\nminumum:{mini}\n2nd minumum:{a}\n----MAXIMUM----\nmaximum:{maxi}\n2nd maximum:{b}"
if __name__ == "__main__":
    obj=Solution()
    print(obj.secondMiniAndMax(list))


    



