# Week 4 学习笔记

## 深度优先搜索和广度优先搜索

首先，明确这里的搜索指的是暴力搜索，即在搜索中不会智能化的操作，实际执行的是遍历操作

这样，深度优先和广度优先就变成了遍历树和图的两种特定方式，其中深度优先可以理解成每次遍历时沿着一条路径走到底；而广度优先可以理解成每次访问同一个层级的结点，层层发散出去

遍历的基本要求如下：

1. 每个节点都要访问一次
2. 每个结点都能访问一次
3. 访问节点的顺序不做要求

### 广度优先搜索的实现

广度优先搜索可以依靠队列的先入先出特性比较直观地实现按广度的顺序遍历节点，代码如下：

```python
# Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

### 深度优先搜索的实现

深度优先搜索可以直接依赖系统自己的函数调用栈来递归实现，代码如下：

注意递归代码的四个步骤

```python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

---

## 贪心算法

贪心算法的初衷：通过在每一步选择中都选择当下最优的选择，希望最后可以得到全局最优的结果

贪心法和动态规划的区别：

1. 贪心法在每一步所做出的的选择都是当下最优的，且一旦做出选择就没有办法回退
2. 动态规划这是保存了前面的步骤，可以按照需要进行回退操作

### 贪心算法的特性

贪心算法常见于优化问题中，如图中的最小生成树，哈夫曼编码等

在实际工程应用中，一般比较难以使用贪心算法来解决优化问题，如果一个问题可以拆分为子问题，且**子问题的最优解可以递推到最终问题的最优解**，那么这种问题可以用贪心算法来解决

因为贪心算法在每一次都是最优结果，如果一个问题可以用贪心算法来求解，那么贪心算法就是这个问题的最优解

另外，因为贪心算法一般比较高效，且求得的结果一般叫接近最优解，所以可以用来做辅助算法，或者求解一些要求结果不是特别精确的问题

---

## 二分查找

要使用二分查找，需要满足三个前提条件：

1. 目标函数必须是单调的，如数组必须是有序的
2. 必须存在上下界，比如数组个数是有限的
3. 元素必须可以通过下标来访问

在使用时必须严格审视问题是否满足上述的条件，注意不要将自己的思路局限在经典的二分查找，还有其他的问题也可以使用二分查找，比如：

1. [搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)
2. [X的平方根](https://leetcode-cn.com/problems/sqrtx/)

上面的题目可以提供更宽广的使用二分查找的视角

### 二分查找的实现

下面是二分查找的代码模板：

```pyhon
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```
