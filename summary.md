# 毕业总结

本次总结分为五个部分：第一部分是**数据结构**，对学习到的数据结构进行分类，同时给出对应的应用场景或者经典的题目；第二部分是**算法**，对学习到的算法进行分类；第三部分是需要刻意培养的**思维方式**；第四部分则是**练习方法**上的要点；第五部分是**经典题目**的汇总

## 一、数据结构

### 一维
+  基础
    + 数组（array）
    + 链表（linked list）
+ 高级
    + 栈（stack）：先入后出；相关题目有**括号匹配**、**直方图**
    + 队列（queue）：先入先出；相关题目有**滑动窗口**、**优先队列**、**堆排序**
    + 双端队列（deque）：在头部或者尾部做元素的进出；相关题目队列
    + 集合（set）：判断元素是否重复，有 hash set 和 tree set 的实现
    + 映射（map or hash）：经典的 key-valued 存储结构，同样有 hash map 和 tree map

    
### 二维
+ 基础
    + 树（tree）分层遍历（BFS）或者深度优先遍历
    + 图（graph）

+ 高级
    + 二叉搜索树（进一步演变出红黑树和 AVL），树也可以用来组成二叉堆（大顶堆和小顶堆）
    + 并查集（disjoin set）
    + 字典树（Trie）

### 特殊
+ 位运算（bitwise）：因为位运算是计算机底层的操作，所以一般实现的代码会比较简单；位运算可用于判重（N 皇后问题中搜索状态判重）；
    + 布隆过滤器
    + LRU Cache

### 时间复杂度
上述数据结构的时间复杂度可以在[Big-O-Cheet](https://www.bigocheatsheet.com/)网站获得

---

## 二、算法

### 基础组件
所有的算法都基于下述三个基础算法组件来构建：
+ 分支（branch）：if-else，switch
+ 循环（loop）：for，while，用于解决问题中关键的重复子问题
+ 递归（recursion）：用于解决问题中关键的重复子问题

### 搜索
+ 深度优先搜索（DFS）：基于栈实现的
+ 广度优先搜索（BFS）：基于队列实现的
+ A*：不使用栈，也不用队列，而是使用优先队列，就是 A* 启发式搜索

### 动态规划

寻找重复子问题时，发现子问题有最优解，同时可以在求解过程中淘汰次优解，那么这个问题就可以称为具有**最佳子结构**，那么就可以使用动态规划来求解

动态规划有两种做法：
+ 递归的方法，结合备忘录存储重复的子状态
+ 循环的方法，用数组存储所有的初始状态，然后用循环

### 二分查找

### 贪心算法

### 数学、几何问题

### **总结代码模板**

---

## 三、刻意培养的思维方式

### 化繁为简
实质上就是数学归纳法的实现，保证初始条件是正确的，保证从第 N 步到第 N+1 步也是正确的即可，从而让计算机来高效的解决问题，具体来说有下面的三点：

+ 人手动递归很繁琐且容易出错
+ 找到最近最简方法，将其拆分为可以重复解决的问题，从而可以利用算法的三大基础组件来解决问题
+ 数学归纳法思想

---

## 四、练习要点

+ 打好基本功，即刻意练习，对自己不熟悉的地方多加练习，基本功是业余和职业的区别
+ 做题目至少五遍，**只做一遍没有用**
    + 第一遍不要死磕，不会就看题解，一定要看国际版的高票回答
    + 马上自己写第二遍
    + 一天之后练习
    + 一周之后练习
    + 面试或者其他复习的时候练习
+ 即使得到反馈，看题解，或者国际版的高票回答

---

## 五、经典题目串讲

### 爬楼梯与硬币兑换

涵盖了面试时最高频的题目，二者可以相互转换，下面的解法都要掌握：

+ 动态规划
+ 递归加备忘录
+ 深度优先搜索

### 括号匹配，括号生成，直方图最大面积，滑动窗口

+ 括号匹配使用到栈

+ 括号生成也用到栈，递归和深度优先遍历

+ 直方图最大面积也是用到栈

+ 滑动窗口相关问题（在窗口中找最大值，最小值等），使用双端队列

### 二叉树

+ 二叉树的三种遍历方式

+ 分层输出二叉树，DFS 或者 BFS

+ 判断一个树是否是二叉搜索树

### 动态规划

+ 股票买卖

+ 偷房子

+ 字符串编辑距离，使用二维数据结构

+ 最长上升子序列

+ 最长公共子序列

### 字符串

+ 异位词的判断和归类

+ 回文串（最大回文串）

+ regex 匹配

+ 通配符匹配

### 高级数据结构

**模板一定要滚瓜烂熟**

+ Trie

+ BloomFilter

+ LRU Cache


    
