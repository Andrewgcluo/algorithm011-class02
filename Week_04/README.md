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


