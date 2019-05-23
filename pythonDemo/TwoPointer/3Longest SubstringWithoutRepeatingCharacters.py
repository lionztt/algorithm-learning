# 3最长子串
# 字符集定义
# 大小写是否敏感

# 滑动窗口-》增大j使没有重复字符
# 记录重复字符-》freq[256]->ascII码出现频次  O（1）

def lengthOfLongestSubstring(s):
    if not s: return 0
    freq = [0 for i in range(256)]
    l = 0
    r = -1  # [l....r]为滑动窗口
    res = 0
    while l < len(s):
        if (r + 1 < len(s) and freq[ord(s[r + 1])] == 0):
            r += 1
            freq[ord(s[r])] += 1
        else:
            freq[ord(s[l])] -= 1
            l += 1
        res = max(r - l + 1, res)
    return res

# 存储字符串
def lengthOfLongestSubstring2(s):
    if not s:
        return 0
    ss = '' #字符串
    m=0
    for i in range(len(s)):
        while s[i] in ss:
            ss=ss[ss.index(s[i])+1:]
        ss=ss+s[i]
        if len(ss)>m:
            m=len(ss)
        print(i,m,ss)
    return m

print(lengthOfLongestSubstring2("abcabcbb"))