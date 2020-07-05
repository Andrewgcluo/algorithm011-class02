# Week 2 学习笔记

本周的内容相对比较多，也是自己过往掌握的比较薄弱的一些地方，尤其是关于堆的相关讲解。下面主要围绕树和堆记录下一自己的的一些心得和体会。

## 树

课程主要讲解了一般的树，二叉树以及二叉搜索树。

主要掌握二叉树的遍历，以及二叉搜索树在插入和删除后的维护操作。

## 堆

堆要么是大根堆，要么是小根堆，二者不能兼容。

堆的定义可以看做是一个接口，具体实现形式比较多，其关键的一点就是在堆中寻找最大/最小值时，时间复杂度必须是 $$O(1)$$，这是堆最基本的要求。

课程主要讲解的是基于二叉堆进行的,主要是实现比较简单,也容易理解。二叉堆相比工程上实现的严格斐波拉契堆，其在插入删除时性能要相对差一些。主流的语言都实现了二叉堆，以 `Java` 为例，用优先队列实现了二叉堆。

二叉堆可以用一维数组来实现，其父节点和子节点的下标关系通过数学公式可以严格给出。

二叉堆（大顶堆为例）的各个操作时间复杂度如下：
1. find-max: $O(1)$
2. delete-max: $O(logn)$
3. insert: $O(logn)$

其中插入删除操作，每次都是按层执行，一次一层，每一层的操作都是常数次，所以其时间复杂度可以看做是$O(logn)$
