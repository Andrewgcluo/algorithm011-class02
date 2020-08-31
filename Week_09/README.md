# Week 9 学习笔记

本周的主题为**高级动态规划**和**字符串算法**

## 一、高级动态规划

### 1.1 复习

**递归**

所谓的递归，就是函数自己调用自己，递归有自己处理的模板

---

**分治**

加问题划分为若干子问题，然后对子问题分别求解，最后合并起来最终的答案。

分治也有代码模板

---

**动态规划**

动态规划和递归（或分治）没有本质上的不同，关键在于动态规划需要考虑所谓的最优子结构，且中间可以淘汰次优解。

三者都需要寻找重复子问题。



### 1.2 常见的动态规划问题

+ **爬楼梯**，递归公式为 $f(n) = f(n-1) + f(n-2), f(1)=1, f(0) = 0$
+ **不同路径**，递归公式为 $f(x, y) = f(x-1, y) + f(x, y-1)$
+ **打家劫舍**，递归公式为 $dp[i]=\max{(dp[i-2] + nums[i], dp[i-1])}$
+ **最小路径和**，递归公式为 $dp[i][j] = \min{(dp[i-1][j], dp[i][j-1] + A[i][j])}$



### 1.3 高阶动态规划问题

复杂度的来源包括：更多维度的状态；更复杂的状态转移方程

练习题有：

+ https://leetcode-cn.com/problems/longest-increasing-subsequence/
+ https://leetcode-cn.com/problems/decode-ways/
+ https://leetcode-cn.com/problems/longest-valid-parentheses/
+ https://leetcode-cn.com/problems/maximal-rectangle/
+ https://leetcode-cn.com/problems/distinct-subsequences/
+ https://leetcode-cn.com/problems/race-car/



---



## 二、字符串算法

### 1.1 字符串基本知识

**字符串**

```python
x = 'abc'
x = "abc"
```

**遍历字符串**

```python
for ch in "abc":
    print(ch)
```

### 1.2 字符串基础

**基础问题**

+ https://leetcode-cn.com/problems/to-lower-case/
+ https://leetcode-cn.com/problems/length-of-last-word/
+ https://leetcode-cn.com/problems/jewels-and-stones/
+ https://leetcode-cn.com/problems/first-unique-character-ina-string/
+ https://leetcode-cn.com/problems/string-to-integer-atoi/

**字符串操作问题**

+ https://leetcode-cn.com/problems/longest-common-prefix/description/
+ https://leetcode-cn.com/problems/reverse-string
+ https://leetcode-cn.com/problems/reverse-string-ii/
+ https://leetcode-cn.com/problems/reverse-words-in-a-string/
+ https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
+ https://leetcode-cn.com/problems/reverse-only-letters/

**异位词问题**

+ https://leetcode-cn.com/problems/valid-anagram/
+ https://leetcode-cn.com/problems/group-anagrams/
+ https://leetcode-cn.com/problems/find-all-anagrams-in-astring/

**回文串问题**

+ https://leetcode-cn.com/problems/valid-palindrome/
+ https://leetcode-cn.com/problems/valid-palindrome-ii/
+ https://leetcode-cn.com/problems/longest-palindromicsubstring/



### 1.3 高级字符串算法

**最长字串，子序列**

+ 最长子序列：https://leetcode-cn.com/problems/longest-common-subsequence/
+ 最长字串：
+ 编辑距离：https://leetcode-cn.com/problems/edit-distance/；https://leetcode-cn.com/problems/longest-palindromic-substring/

**字符串 + 递归 or 动态规划**

+ https://leetcode-cn.com/problems/regular-expressionmatching/
+ https://leetcode-cn.com/problems/regular-expressionmatching/solution/ji-yu-guan-fang-ti-jie-gen-xiang-xi-de-jiangjie-b/
+ https://leetcode-cn.com/problems/wildcard-matching/
+ https://leetcode-cn.com/problems/distinct-subsequences/



### 1.4 字符串匹配算法

**暴力法**

**Rabin-Karp 算法**

+ 设字串的长度为$M(pat)$，目标字符串的长度为$N(txt)$
+ 计算字串的 hash 值 `hash_pat`
+ 计算目标字符串`txt`每个长度为 $M$ 的子串的 hash 值
+ 比较 hash 值，如果 hash 值不同，字符串就不匹配；如何 hash 值相同，再用朴素算法再次判断

**KMP 算法**

+ KMP = Knuth-Morris-Pratt
+ 当子串与目标字符串不匹配时，前面匹配成功的那一部分字符是已知的，利用这个已知信息，继续把它后移，而不是移回已经比较过的位置，从而提高了效率
+ 参考链接：https://www.bilibili.com/video/av11866460?from=search&seid=17425875345653862171；http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html

