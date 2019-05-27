# 220 219进阶版
# 查找表+滑动窗口


# （v-t，v+t）
def ceil(myset,num):
    for item in myset:
        if item>=num:
            return item
    return -10000



def containsNearbyAlmostDuplicate(nums, k, t):
    record = set()
    for i in range(len(nums)):
        if ceil(record, nums[i] - t)!=-10000 and ceil(record, nums[i] - t)<= nums[i] + t:
            return True
        record.add(nums[i])
        if len(record) == k + 1:
            record.remove(nums[i - k])
    return  False

def containsNearbyAlmostDuplicate2(nums, k, t):
    if k == 10000:
        return False
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, min(i + k + 1, n)):
            if abs(nums[i] - nums[j]) < t + 1:
                return True
    return False
nums = [1,2,3,1]
k = 3
t = 0
print(containsNearbyAlmostDuplicate2(nums,k,t))