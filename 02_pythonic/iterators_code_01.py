import sys
import time

# 选手A 传统的列表
class EagerList:
    def __init__(self, n):
        self.data = [i for i in range(n)]

# 选手B 手写迭代器
class LazyIterator:
    def __init__(self, n) -> None:
        self.n = n
        self.current = 0 # 状态机：只记录当前游标

    def __iter__(self):
        return self     # 协议第一步：返回自己

    def __next__(self) -> int: # 协议第二步：生产逻辑
        if self.current < self.n:
            num = self.current
            self.current += 1 # 更新状态
            return num
        else:
            raise StopIteration # 信号：没货了，别拧了

