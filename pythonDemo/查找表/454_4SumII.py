# 454
# 数据规模-》500，可以用n^2
# 时间：O(n^2)
# 空间：O(n^2)
# 查找表思想
def fourSumCount(A, B, C, D):
    cd_dict={}
    for i in range(len(C)):
        for j in range(len(D)):
            if cd_dict.get(C[i]+D[j],-1)!=-1:
                cd_dict[C[i]+D[j]]+=1
            else:
                cd_dict[C[i] + D[j]] = 1
    res=0
    for i in range(len(A)):
        for j in range(len(B)):
            if cd_dict.get(0-A[i]-B[j],-1)!=-1:
                res+=cd_dict[0-A[i]-B[j]]
    return res

# 优化
def fourSumCount2(A, B, C, D):
    map_ab = {}
    for v_a in A:
        for v_b in B:
            sum_value = v_a + v_b
            if sum_value in map_ab:
                map_ab[sum_value] += 1
            else:
                map_ab[sum_value] = 1

    ret = 0
    for v_c in C:
        for v_d in D:
            sum_value = -v_c - v_d
            if sum_value in map_ab:
                ret += map_ab[sum_value]
    return ret

A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]

print(fourSumCount2(A,B,C,D))