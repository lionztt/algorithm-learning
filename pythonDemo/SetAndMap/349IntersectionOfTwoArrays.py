# 两类查找问题
# 1。查找有无-》'a'是否存在？-》set集合
# 2。 查找对应关系-》'a'出现几次？-》map字典

# Set Map 常见操作
# 插入/删除/查找/更新


# 349 Set问题
# 思路1-》直接使用set
def intersection(nums1, nums2):
    s1=set(nums1)
    s2=set(nums2)
    # O(min(len(s1), len(s2))
    s3=s1 & s2
    result = []
    for item in s3:
        result.append(item)
    return result

# 思路2 -》不创造
# python时间复杂度：https://blog.csdn.net/u010366748/article/details/51469937
# 时间复杂度 O(n)
# 空间复杂度 O(n)
def intersection2(nums1, nums2):
    # O(n)
    s1=set(nums1)
    # O(n)
    s2=set(nums2)
    s3=set()
    # O(n)
    for item in s1:
        if item in s2:
            s3.add(item)
    result=[]
    # O(n)
    for item in s3:
        result.append(item)
    return result

# 问题：可以只使用一个set来完成题目吗？
def intersection3(nums1, nums2):
    # O(n)
    s1=set(nums1)
    result = {}
    for i in range(len(nums2)):
        if nums2[i] in s1:
            result[nums2[i]]=1
    return list(result.keys())

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection3(nums1,nums2))