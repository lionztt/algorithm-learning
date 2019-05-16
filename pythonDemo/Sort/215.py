#215

def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]

nums=[3,2,1,5,6,4]
k = 2

print(findKthLargest(nums,k),nums)