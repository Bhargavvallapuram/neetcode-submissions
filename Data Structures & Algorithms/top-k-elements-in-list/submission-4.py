import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_table={}
        for i in nums:
            if i not in count_table:
                count_table[i]=1
            else:
                count_table[i]+=1
        count_table=dict(sorted(count_table.items(), key=operator.itemgetter(1), reverse=True))
        ls=list(count_table.keys())
        return ls[:k]

        