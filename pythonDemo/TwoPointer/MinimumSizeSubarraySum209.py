#209
# 明确子数组含义
# 解的情况
# 滑动窗口

# 暴力解法 n^2 遍历所有的子数组

# 优化-》避免重复计算
def minSubArrayLen(s, nums):
    l,r=0,-1 # [l,r]为滑动窗口
    sum = 0
    res = len(nums)+1 # 最小长度
    while l<len(nums):
        if((r+1<len(nums)) & (sum<s)): # 防止数组越界
            r += 1
            sum+=nums[r]
        else:
            sum-=nums[l]
            l += 1
        if(sum>=s):
            res = min(res,r-l+1) # 取当前子数组和res相比较小的的长度值（由于子数组是[],所以计算长度要加1）
    if(res == len(nums)+1):
        return 0
    else:
        return res  # 无解情况


s = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(s,nums))