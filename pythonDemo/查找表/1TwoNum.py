# 1 查找表问题
# 前面为查找表，下一个为要找的值，若没有加入查找表后继续找下一个
def twoSum(nums, target):
    d1={}
    for i in range(len(nums)):
        another = target - nums[i]
        if d1.get(another,-1)!=-1:
            return [i,d1[another]]
        d1[nums[i]]=i

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums,target))