#219
# 时间复杂度：O(n)
# 空间复杂度：O(k)
# 滑动窗口(固定长度为k)+查找表
def containsNearbyDuplicate(nums, k):
    record = set()
    for i in range(len(nums)):
        if nums[i] in record:
            return True
        record.add(nums[i])
        if(len(record)>k):
            record.remove(nums[i-k])
    return False

# dict实现
def containsNearbyDuplicate2(nums, k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            if i - dic[nums[i]] <= k:
                return True
        dic[nums[i]] = i
    return False

nums = [1,2,3,1]
k = 3

# 没有符合条件的情况，返回False
nums2=[1,2,3,1,2,3]
k2=2
print(containsNearbyDuplicate2(nums2,k2))