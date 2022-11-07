# %%
class Solution:
    def permute(self,nums):
        result = []

        #base case
        if (len(nums) == 1):
            return [nums[:]]

        #we want to go through all items in nums i.e [1,2,3]
        for i in range(len(nums)):
            #pop the value at the 0 index
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result

if __name__ == "__main__":
    t = Solution()
    print(t.permute([1,2,3]))


