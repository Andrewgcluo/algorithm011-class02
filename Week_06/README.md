# Week 6 学习笔记

本周的主题是关于动态规划

## 动态规划

动态规划是一种求解问题的思路，来源于运筹学，其为了解决多阶段决策过程最优化问题提出的一种数学方法。通过将多阶段问题变换为一系列相互联系的的单阶段问题，然后分别加以解决。

一个问题可以用动态规划来求解，需要满足下面的条件：

1. **重叠子结构**：拆分后的子问题必须是同一类型的，不然没法使用提前子问题的计算结果来递推解决问题
2. **最优子结构**：即全局最优解一定可以拆分为子问题的最优解，从而才可以递归的解决

基于上述两个条件，动态规划的解题思路如下：

1. 找出最优子结构
2. 存储中间状态
3. 用递推公式（状态转移方程）解决问题

## 递归

递归的代码模板如下：

```pyton
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

## 分治

分治的代码模板如下：

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

## 动态规划与递归（分治）的联系

动态规划与递归（分治）最大的区别就在于前者需要存在最优子结构，二者的相同点就在于需要寻找**重复（重叠）子问题**

## 总结

动态规划是一个比较难以快速上手的工具，后续需要进一步的练习来掌握这种数学和解题工具。



