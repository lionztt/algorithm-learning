# 447

# 构建 距离-个数 查找表
# 对应n 个数选择方式 n*(n-1)
# 时间复杂度 O(n^2)
# 空间复杂度 O(n)
def numberOfBoomerangs(points):
    res = 0
    for i in range(len(points)):
        dis_dict = {}
        for j in range(len(points)):
            if j!=i:
                if dis(points[i],points[j]) in dis_dict:
                    dis_dict[dis(points[i],points[j])]+=1
                else:
                    dis_dict[dis(points[i], points[j])] = 1
        for value in dis_dict.values():
            res+=value*(value-1)
    return res

# 距离平方公式
def dis(a,b):
    return (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])

points=[[0,0],[1,0],[2,0]]
print(numberOfBoomerangs(points))