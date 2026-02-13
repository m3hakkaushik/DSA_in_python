class Solution:
    def checkSorted(self, arr):
        ascending = True
        descending = True

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                ascending = False
            if arr[i] < arr[i + 1]:
                descending = False

        if ascending:
            return "Forward Sorted"
        elif descending:
            return "Backward Sorted"
        else:
            return "Not Sorted"


if __name__ == "__main__":
    obj = Solution()
    print(obj.checkSorted([1,2,3,4]))   # Forward
    print(obj.checkSorted([4,3,2,1]))   # Backward
    print(obj.checkSorted([1,3,2,4]))   # Not sorted
