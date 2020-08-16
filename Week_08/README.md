# Week 8 学习笔记

本周的主题是**位运算**、**布隆过滤器**以及**排序算法**

## 一、位运算

机器里的数字就是用二进制来存储的，这为位运算提供了基础

### 常见位运算符

```python
<< # 左移
>> # 右移
|  # 按位或
&  # 按位与
~  # 按位取反
^  # 按位异或
```

### 异或技巧

```python
x ^ 0 = x
x ^ 1 = ~x
x ^ (~x) = 1
x ^ x = 0

# 满足结合律
a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c

# 满足交换律
a ^ b = b ^ a

# 交换两个数
c = a^b
a ^ c = b  # 结合律可以解释
b ^ c = a  # 结合律加交换律可以解释
```

### 指定位置的位运算技巧

```python
x & (~0 << n)  # x 的最右边的 n 位清零
(x >> n) & 1   # 获取 x 的第 n 位值
x & (1 << n)   # 获取 x 的第 n 位的幂值
x | (1 << n)   # 仅将第 n 位置为 1
x & (~(1 << n)) # 仅将第 n 位置为 0
x & ((1 << n) - 1) # 将 x 最高位至第 n 位（包含）清零
x & (~((1 << (n+1))-1) # 将第 n 位至 第 0 位（含）清零
```

### 实战练习题目：

1. https://leetcode-cn.com/problems/number-of-1-bits/
2. https://leetcode-cn.com/problems/power-of-two/
3. https://leetcode-cn.com/problems/reverse-bits/
4. https://leetcode-cn.com/problems/n-queens/description/
5. https://leetcode-cn.com/problems/n-queens-ii/description/

------

## 二、布隆过滤器与 LRU Cache

### 布隆过滤器

对于一个很长的二进制向量和一系列随机映射函数，布隆过滤器可以用于检索一个元素是否存在一个集合里面

**优点**：空间效率和查询效率都远超一般算法

**缺点**：有一定的误识别率和删除起来比较困难

### 案例

1. 比特币网络
2. 分布式系统如 Map-Reduce
3. Redis 缓存
4. 垃圾邮件和评论的过滤

### 实现

```python
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
```



### LRU Cache

LRU Cache 关注两个要素：大小和替换策略，一般用 Hash Table + Double LinkedList 实现

查询复杂度为 $O(1)$，修改和更新复杂度为 $O(1)$

### 实现

```python
class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```

------

## 三、排序算法







