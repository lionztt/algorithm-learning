# 27 移除元素
# https://leetcode-cn.com/problems/remove-element/

def removeElement(nums, val):
    k = 0  # 不等元素索引
    for i in range(len(nums)):
        if (nums[i] != val):
            if (i != k):  # 防止所有元素都是非零元素（特殊用例）-》自己与自己交换
                nums[k], nums[i] = nums[i], nums[k]
            k += 1
    return k

# 优化-》

def removeElement2(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] == val:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    del nums[:i]
    return len(nums)

def removeElement3(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement3(nums,val),nums)