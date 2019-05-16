# 二分查找法
import time

#在有n个元素的arr数组中寻找target元素，并返回数组下标
def binarySearch(arr, n, target):
    # ！！！明确变量意义，保证循环不变量--》在[l.....r]范围中寻找target（可以保证算法正确性）
    l = 0
    r = n-1
    # 注意边界问题--》当l==r时，区间[l.....r]依然有效，所以要保留"="
    while l <= r:
        # mid = (l+r) // 2 # 注意！这里对于c++ int的加法来说可能会超出int值，万无一失的写法在下面
        mid = l + (r-l) // 2 # 用减法不会超出int（1962年才发现的bug）
        if(arr[mid] == target):
            return mid
        elif(target>arr[mid]):
            l = mid + 1
        else:
            r = mid - 1
    # 没有target，返回-1
    return -1

#更改一下边界
def binarySearch2(arr, n, target):
    # ！！！明确变量意义，保证循环不变量--》在[l.....r）范围中寻找target（可以保证算法正确性）
    l = 0
    r = n
    # 注意边界问题--》当l==r时，区间[l.....r）无效
    while l < r:
        mid = l + (r - l) // 2
        if(arr[mid] == target):
            return mid
        elif(target>arr[mid]):
            l = mid + 1 # target在[mid+1.....r)中
        else:
            r = mid # target在[l.....mid)中
    # 没有target，返回-1
    return -1

time_start = time.time()
print (binarySearch2((1,3,4,5,7,8,9,12,13,15),10,15))
time_end = time.time()
print('totally cost',time_end-time_start)
