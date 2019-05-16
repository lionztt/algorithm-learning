#75 数组排序问题
# 遇到排序问题-1。暴力解决法-》常规排序算法--快排啥的（甚至编程语言自身的排序函数）
# 2。观察题目特殊条件改进排序算法

# 计数排序适合于元素个数非常有限的排序算法
import unittest

def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    count0=0
    count1=0
    count2=0
    for i in range(len(nums)):
        if(nums[i]>=0&nums[i]<=2): # 保证输入数据合法性
            if(nums[i]==0):
                count0+=1
            elif(nums[i]==1):
                count1+=1
            else:
                count2+=1
    for j in range(count0):
        nums[j]=0
    for j in range(count0,count0+count1):
        nums[j]=1
    for j in range(count0 + count1, count0 + count1+count2):
        nums[j] = 2

def sortColors2(nums):
    count=[0,0,0]
    for i in range(len(nums)):
        if(nums[i]>=0&nums[i]<=2): # 保证输入数据合法性
            count[nums[i]]+=1
    index = 0
    for k in range(len(count)):
        for j in range(count[k]):
            nums[index]=k
            index+=1

# 优化-》三路快排（分成小于val/等于val/大于val  三个部分，小于val和大于val的分治递归）
def sortColors3(nums):
    zero = -1 # nums[0....zero] == 0
    two = len(nums) # nums[two....n-1] == 2
    i=0
    while(i<two):
        if(nums[i]==1):
            i+=1
        elif(nums[i]==2):
            two -= 1
            nums[i],nums[two]=nums[two],nums[i]
        elif(nums[i]==0):
            zero+=1
            nums[i], nums[zero] = nums[zero], nums[i]
            i+=1


mynums=[2,0,2,1,1,0]
sortColors3(mynums)
print(mynums)