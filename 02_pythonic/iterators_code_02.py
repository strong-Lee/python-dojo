
### 为什么把类改成生成器函数？

"""
将迭代器类 (`LazyIterator`) 改为生成器函数 (`lazy_generator`) 是一种更 **Pythonic** 的优化方式，主要原因有：

1.  **简洁性与可读性**：
    *   生成器函数使用 `yield` 关键字，它会自动处理迭代器的所有繁琐细节：保存内部状态（`self.current`）、暂停执行、以及在迭代结束时自动抛出 `StopIteration` 异常。
    *   相比之下，手动实现 `__iter__` 和 `__next__` 方法需要更多的样板代码，并且需要开发者自己管理状态和异常。
    *   对于简单的序列生成，生成器函数能用更少的代码表达相同的逻辑，代码更清晰易懂。

2.  **符合 Python 惯用法**：
    *   在 Python 中，当你需要一个简单的、按需生成值的序列时，生成器函数是首选的实现方式。它们是实现惰性计算（lazy evaluation）的强大工具。

3.  **性能（通常）**：
    *   虽然对于非常简单的迭代器，性能差异可能不明显，但生成器函数通常比同等的类实现有更低的内存开销和更快的执行速度，因为它们避免了创建完整的类实例以及方法调用的额外开销。
    *   更重要的是，它们的核心优势在于“惰性”，即不一次性生成所有数据，只在需要时生成，这对于处理大量数据或无限序列非常高效。

### 如果只是优化 `LazyIterator` 类（保持类的写法），应该怎么写？

如果你希望保持类 (`class`) 的写法，并且优化 `LazyIterator`，那么主要的优化点在于遵循迭代器协议的最佳实践：**将“可迭代对象（Iterable）”和“迭代器（Iterator）”分开**。

你最初的 `LazyIterator` 类同时充当了可迭代对象和迭代器。这意味着如果你创建了一个 `LazyIterator` 实例并对其进行迭代，它会消耗掉自己的状态。如果你想再次迭代它，它就无法从头开始，因为 `self.current` 已经到达了 `n`。

为了支持多次独立的迭代，一个可迭代对象（如列表、元组）在每次调用 `iter()` 时应该返回一个新的迭代器实例。

以下是优化后的类写法，它将原始的 `LazyIterator` 拆分为一个可迭代对象 `LazyRangeIterable` 和一个独立的迭代器 `LazyRangeIterator`：

1.  **`LazyRangeIterable` (可迭代对象)**：这个类负责创建一个迭代器实例。它的 `__iter__` 方法会返回一个新的 `LazyRangeIterator` 实例。
2.  **`LazyRangeIterator` (迭代器)**：这个类包含实际的迭代逻辑 (`__next__` 方法) 和迭代状态 (`self.current`)。它的 `__iter__` 方法会返回 `self`，因为迭代器本身也是可迭代的（它返回它自己）。

这样，每次你对 `LazyRangeIterable` 的实例调用 `iter()` 时，都会得到一个全新的、独立的 `LazyRangeIterator`，从而可以多次从头开始迭代。
"""
# 优化后的类写法
class LazyRangeIterable: # 这是可迭代对象
    def __init__(self, n: int) -> None:
        self.n = n

    def __iter__(self):
        return LazyRangeIterator(self.n) # 每次调用iter()都返回一个新的迭代器实例

class LazyRangeIterator: # 这是迭代器
    def __init__(self, n: int) -> None:
        self.n = n
        self.current = 0

    def __next__(self) -> int:
        if self.current < self.n:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self): # 迭代器本身可迭代，返回自身
        return self

# 演示：
my_range = LazyRangeIterable(3) # 这是可迭代对象

# 第一次迭代
iter1 = iter(my_range) # 获取一个新的迭代器
print(list(iter1)) # [0, 1, 2]

# 第二次迭代 (从头开始)
iter2 = iter(my_range) # 再次获取一个新的迭代器
print(list(iter2)) # [0, 1, 2]

# 注意：iter1 的状态已经被消耗，而 iter2 是全新的
print(list(iter1)) # []
