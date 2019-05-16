# 26

def removeDuplicates(nums):
    k = 0
    for i in range(len(nums)):
        if(nums[i]!= nums[k]):
            k+=1
            nums[k]=nums[i]
    del nums[k:len(nums)-1]
    return len(nums)

mynums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(mynums),mynums)
