

num = [1,2,3,4,5,6,7,8,9,10]

class Solution:
    def calculateSumandProduct(self, arr: list) -> list:
        sum_ = 0
        product = 1

        for n in arr:
            sum_ += n
            product *= n

        return [sum_, product]


if __name__ == "__main__":
    obj = Solution()
    print(obj.calculateSumandProduct(num))

