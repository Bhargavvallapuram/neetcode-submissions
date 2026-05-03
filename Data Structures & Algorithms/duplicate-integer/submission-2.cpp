class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> sig;
        for(auto num : nums){
            if(sig.contains(num)){
                return true;
            }else{
                sig.insert(num);
            }
        }
        return false;
    }
};