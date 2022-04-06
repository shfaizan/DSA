class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
            else:
                pass
        return False

rock = Solution()
sol = rock.containsDuplicate([1,2,3,4,4])
print(sol)

