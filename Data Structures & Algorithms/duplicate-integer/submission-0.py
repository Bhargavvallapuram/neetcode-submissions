class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unq=[]
        for i in nums:
            if i not in unq:
                unq.append(i)
            else:
                return True
        return False

        