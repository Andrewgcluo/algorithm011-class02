# Week 7 学习笔记

本周的主题是关于**字典树和并查集**、**高级搜索**和**红黑树和AVL树**



## 字典树和并查集

### 字典树

字典树即**Trie 树**，又称**单词树**或者**键树**，多用于统计和排序大量的字符串，常见于搜索引擎中用于统计文本的词频。因为它可以最大限度减小无谓的字符串比较，查询效率比哈希表还要高。

**基本性质**：

1. 结点本身不存储完整单词
2. 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串
3. 每个结点的所有子结点路径代表的字符都不相同。

Trie 树的核心思想就是空间换时间，利用字符串的公共前缀来降低查询时间的开销以达到提速的目的。

**经典题目**：

1. https://leetcode-cn.com/problems/implement-trie-prefix-tree/#/description
2. https://leetcode-cn.com/problems/word-search-ii/



### 并查集

并查集，即 **Disjoint Set**，多用于**组团**和**配对**问题中。

**基本操作**：

1. `makeSet(s)`：建立一个并查集，包含 s 个单元素集合

2. `unionSet(x,y)`：把元素 x 和元素 y 所在的集合合并，要求 x 和 y 所在的集合不相交，如何相交则不合并。

3. `find(x)`：找到元素 x 所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合。

   

**经典题目**：

1. https://leetcode-cn.com/problems/friend-circles
2. https://leetcode-cn.com/problems/number-of-islands/
3. https://leetcode-cn.com/problems/surrounded-regions/



## 高级搜索

高级搜索包含**剪枝**，**双向BFS**和**启发式搜索 (A*)**

### 剪枝

剪枝多用于对初级搜索的优化，对于状态空间特别多的，如棋类游戏很有效

**经典题目**：

1. https://leetcode-cn.com/problems/n-queens/

2. https://leetcode-cn.com/problems/valid-sudoku/description/
3. https://leetcode-cn.com/problems/sudoku-solver/#/description



### 双向 BFS

双向 BFS 可以看作是在搜索方向上加以优化

**经典题目**：

1. https://leetcode-cn.com/problems/word-ladder/
2. https://leetcode-cn.com/problems/minimum-geneticmutation/



### 启发式搜索 A*

**示例代码**：

```python
def AstarSearch(graph, start, end):
	pq = collections.priority_queue() # 优先级 —> 估价函数
	pq.append([start]) 
	visited.add(start)
	while pq: 
		node = pq.pop() # can we add more intelligence here ?
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
   unvisited = [node for node in nodes if node not in visited]
		pq.push(unvisited)
```

**估价函数**：用来评价哪些结点最有希望是一个想要找的结点，其返回一个非负实数，即估价成本。

**经典题目**：

1. https://leetcode-cn.com/problems/shortest-path-in-binarymatrix/
2. https://leetcode-cn.com/problems/sliding-puzzle/
3. https://leetcode-cn.com/problems/sudoku-solver/



## 高级树、AVL 树和红黑树

### 高级树

这里可以看作是二叉搜索树，即 Binary Search Tree，具有下述的性质：

1. 左子树的所有结点均小于它的根结点的值
2. 右子树的所有节点均大于它的根结点的值
3. 左右子树也都是二叉搜索树
4. 中序遍历即升序排列

### AVL 树

[AVL 树](https://en.wikipedia.org/wiki/Self balancing_binary_search_tree)的设计目的是为了保证二叉搜索树的平衡，即通过**四种**旋转操作来进行平衡。

**旋转操作**：

1. 左旋 右右子树
2. 右旋 左左子树
3. 左右旋 左右子树
4. 右左旋 右左子树

AVL 树可以看作是**平衡**二叉搜索树，每个结点均有平衡因子，通过四种旋转操作来实现平衡。但是结点要存储额外信息，且调整次数频繁



### 红黑树

红黑树是一种**近似**平衡的二叉搜索树，能够确保任意一个结点的左右子树的高度差小于两倍。

**特性**：

1. 每个结点要么是红色，要么是黑色
2. 根结点是黑色
3. 每个叶结点是黑色，包含空结点
4. 不能有相邻接的两个红色结点
5. 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点
6. **从根到叶子的最长可能路径不多于最短的可能路径的两倍长**



