class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Logic 1
        # result = []
        # total = 0

        # for num in nums:
            # total += num
            # print("current number:", num)
            # print("Total so far:", total)
            # result.append(total)

        # return result
        
        # Logic 2
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums
