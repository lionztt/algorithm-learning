# 350 Map问题(dict)

def intersect(nums1,nums2):
    d1={}
    for i in range(len(nums1)):
        if nums1[i] in d1:
            d1[nums1[i]]+=1
        else:
            d1[nums1[i]]=1

    result=[]
    for i in range(len(nums2)):
        if d1.__contains__(nums2[i]) and d1[nums2[i]]>0:
            result.append(nums2[i])
            d1.update({nums2[i]:d1[nums2[i]]-1})
    return result

# 语法2
def intersect2(nums1,nums2):
    d1={}
    for i in range(len(nums1)):
        if nums1[i] in d1:
            d1[nums1[i]]+=1
        else:
            d1[nums1[i]]=1

    result=[]
    for i in range(len(nums2)):
        if d1.get(nums2[i],-1)!=-1 and d1[nums2[i]]>0:
            result.append(nums2[i])
            d1[nums2[i]]-=1
    return result

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1,nums2))


# 测试 map

def testMap():
    d1={}
    if d1.get('22',-1)==-1 :
        print("dict没有22！")
    else:
        print("dict有22！")
    print(d1['22'])
    if d1.get('22',-1)==-1:
        print("dict没有22！")
    else:
        print("dict有22！")
    print(d1['22'])

print(testMap())

# 经实验可知： python 的 dict 没有默认值，也不会在访问后自动放入默认值