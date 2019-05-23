#167---
# 可能无解？
# 可能多解？ -》返回随意一个解/返回最大解 -》返回所有解

# 思路一：暴力解决-》双层遍历(可能超时) n^2

# 思路二：有序-》二分搜索  nlogn
def twoSum(numbers, target):
    for i in range(len(numbers)):
        x=target-numbers[i]
        newNumbers = numbers[:i]
        result=binarySearch(newNumbers,len(newNumbers),x)
        if(result!=-1):
            return [result+1,i+1]



def binarySearch(arr, n, target):
    l=0
    r=n-1
    while l<=r:
        mid = l + (r-l)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            l=mid+1
        else:
            r= mid-1
    return -1

# 优化-》一左一右相加与target相比（对撞指针）n
def twoSum2(numbers, target):
    l=0
    r=len(numbers)-1
    while l<r : #要找两个不同的元素
        if (numbers[l] + numbers[r] > target):
            r -= 1
        elif (numbers[l] + numbers[r] < target):
            l += 1
        else:
            return [l + 1, r + 1]
    return []

numbers = [2, 7, 11, 15]
target = 9
print(twoSum2(numbers,target),numbers)