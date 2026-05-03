class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers=sorted(numbers)
        for i in range(len(numbers)):
            s=-1
            try:
                s=numbers.index(target-numbers[i])
            except ValueError:
                s=-1
            if (s!=-1):
                return [i+1,s+1]
        return []
        