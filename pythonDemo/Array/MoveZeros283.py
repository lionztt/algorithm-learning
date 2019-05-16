# LeetCode-283-Move Zeros
# facebook/Bloomberg面试题
# https://leetcode-cn.com/problems/move-zeroes/solution/


# 时间复杂度：O(n)
# 空间复杂度：O(n)
def moveZeroes(nums):
    noneZeroElements = []
    for i in range(len(nums)):
        if(nums[i]!=0):
            noneZeroElements.append(nums[i])
    for i in range(len(noneZeroElements)):
        nums[i] = noneZeroElements[i]
    for i in range(len(nums)-len(noneZeroElements)):
        nums[len(noneZeroElements)+i]=0

# 优化-》不用任何辅助空间
def moveZeroes2(nums):
    k = 0 # 零元素索引
    for i in range(len(nums)):
        if(nums[i]!=0):
            nums[k]=nums[i]
            k+=1
    for i in range(len(nums)-k):
        nums[k+i]=0

# 优化-》 只进行一次循环
def moveZeroes3(nums):
    k = 0 # 非零元素索引
    for i in range(len(nums)):
        if(nums[i]):
            nums[k], nums[i] = nums[i], nums[k]
            k+=1

# 优化-》自己与自己不进行交换
def moveZeroes4(nums):
    k = 0 # 非零元素索引
    for i in range(len(nums)):
        if(nums[i]!=0):
            if(i!=k): # 防止所有元素都是非零元素（特殊用例）-》自己与自己交换
                nums[k], nums[i] = nums[i], nums[k]
            k+=1

mynums=[0,1,0,3,12]
moveZeroes4(mynums)
print(mynums)

