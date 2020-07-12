# Week 3 学习笔记

## 递归

### 递归的原理

递归可以看做是一种循环，即函数体循环调用自己，而这种循环调用可以成立的前提就是我们解决的问题是具有自相似性的。

### 递归的特点

1. 递归调用是线性顺序的，不能跨层进行递归调用
2. 递归通过参数以及全局变量来跨层传递信息
3. 递归实际上是发现重复子问题并加以解决

### 递归的实现

1. 递归的终止条件
2. 当前层业务代码
3. 进入下一层
4. 清理当前层代码

具体的 Python 代码实现如下：

```python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```

---

## 分治与回溯

### 分治与回溯的原理

二者可以看做是递归的一种特殊形式，这里可以联想到程序的三种基本结构：分治，循环以及**递归**

分治和回溯依赖于找**最近子问题**

### 分治的实现

分治的 Python 代码模板如下：

```python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 
  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

通过代码模板可以看出，分治相比通用的递归代码，多了一步组合子问题的步骤，这也是体现出**分而治之**这一特点

### 回溯的特点

回溯是在递归过程中，通过在当前层尝试可能情况，尽可能早的去掉不可能的解。

回溯的思想可以看做是一个试错的方式，比较类似于机器学习训练模型中的“早停法“的思想——即如果发现在训练中模型的性能出现了下降，就终止模型的训练，避免劳而无功。

关于回溯的掌握还需要多多练习。

