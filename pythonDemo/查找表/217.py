# 217

def containsDuplicate(nums):
    dict={}
    for i in range(len(nums)):
        if nums[i] in dict:
            return True
        dict[nums[i]]=i
    return False

# 2
def containsDuplicate2(nums):
    return len(set(nums))!=len(nums)

print(containsDuplicate2([1,2,3,4]))