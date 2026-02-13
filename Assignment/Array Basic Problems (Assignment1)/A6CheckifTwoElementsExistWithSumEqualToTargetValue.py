
nums = [2,7,11,15]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        s = {}
        i = 0

        for num in nums:
            n = target - num

            if n in s:
                return [s[n], i]

            s[num] = i
            i += 1

if __name__ == "__main__":
    obj = Solution()
    print(obj.twoSum(nums,target))
    