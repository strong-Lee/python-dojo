# Python 3 集合（set）的增删改查操作示例

# 1. 创建和初始化集合 (Initialization)
# 可以创建一个空集合 (注意不能直接使用 {}，因为这会创建一个空字典)
my_set = set()
print(f"初始空集合: {my_set}")

# 也可以创建包含元素的集合
my_set = {1, 2, 3, 4, 5}
print(f"初始集合: {my_set}")

# 如果初始化的数据包含重复元素，集合会自动去重
my_set_with_duplicates = {1, 2, 2, 3, 4, 4, 5}
print(f"包含重复元素初始化后的集合 (已去重): {my_set_with_duplicates}")

# 可以从列表或其他可迭代对象创建集合
list_to_set = [6, 7, 8, 8, 9]
my_set_from_list = set(list_to_set)
print(f"从列表创建的集合: {my_set_from_list}")

# 2. 增加元素 (Add)

# 2.1 add(): 向集合中添加一个单一元素
my_set.add(6)
print(f"使用 add(6) 添加元素: {my_set}")
my_set.add(1) # 添加一个已存在的元素，集合不会改变 (因为集合元素唯一)
print(f"再次添加 1 (无变化): {my_set}")

# 2.2 update(): 添加来自另一个可迭代对象的所有元素到集合中
# 可以是列表、元组、另一个集合等
my_set.update([7, 8])
print(f"使用 update([7, 8]) 添加多个元素: {my_set}")
my_set.update({9, 10, 1}) # 也可以用另一个集合更新，同样会去重
print(f"使用 update({9, 10, 1}) 添加更多元素: {my_set}")

# 3. 删除元素 (Delete)

# 3.1 remove(): 从集合中删除指定元素
# 如果元素不存在，会引发 KeyError
my_set.remove(10)
print(f"使用 remove(10) 删除元素: {my_set}")

# try:
#     my_set.remove(100)
# except KeyError as e:
#     print(f"删除不存在的元素时出错 (remove): {e}")

# 3.2 discard(): 从集合中删除指定元素
# 如果元素不存在，不会引发错误
my_set.discard(9)
print(f"使用 discard(9) 删除元素: {my_set}")
my_set.discard(100) # 删除不存在的元素，不会报错
print(f"使用 discard(100) 删除不存在的元素 (无变化): {my_set}")

# 3.3 pop(): 随机删除并返回集合中的一个元素
# 因为集合是无序的，所以无法预测哪个元素会被删除
popped_element = my_set.pop()
print(f"使用 pop() 删除一个随机元素: {my_set}, 被删除的元素: {popped_element}")

# 如果集合为空，pop() 会引发 KeyError
# empty_set = set()
# try:
#     empty_set.pop()
# except KeyError as e:
#     print(f"从空集合 pop 时出错: {e}")

# 3.4 clear(): 删除集合中的所有元素，使集合变为空集合
my_set_to_clear = {1, 2, 3}
my_set_to_clear.clear()
print(f"使用 clear() 清空集合: {my_set_to_clear}")

# 4. 修改元素 (Modify)
# 集合中的元素是不可变的（immutable），这意味着你不能直接修改集合中的某个元素。
# "修改"集合通常指通过添加或删除元素来改变集合的构成。
# 例如，如果要“修改”一个元素，你需要先删除旧的，再添加新的。
current_set = {'apple', 'banana', 'cherry'}
print(f"原始集合: {current_set}")
# 假设我们想把 'banana' 改成 'grape'
if 'banana' in current_set:
    current_set.remove('banana')
    current_set.add('grape')
print(f"将 'banana' 修改为 'grape' 后的集合: {current_set}")

# 5. 查询元素 (Query)

# 5.1 in 运算符: 检查元素是否存在于集合中
if 1 in my_set:
    print("1 在集合中")
else:
    print("1 不在集合中")

if 100 in my_set:
    print("100 在集合中")
else:
    print("100 不在集合中")

# 5.2 len(): 获取集合的元素数量
set_length = len(my_set)
print(f"集合的长度 (元素数量): {set_length}")

# 5.3 集合运算 (Set Operations)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# union(): 并集 (所有不重复的元素)
union_set = set_a.union(set_b)
print(f"集合 A 和 B 的并集 (union): {union_set}") # 也可以使用 | 运算符: set_a | set_b

# intersection(): 交集 (两个集合共有的元素)
intersection_set = set_a.intersection(set_b)
print(f"集合 A 和 B 的交集 (intersection): {intersection_set}") # 也可以使用 & 运算符: set_a & set_b

# difference(): 差集 (在 A 中但不在 B 中的元素)
difference_set_ab = set_a.difference(set_b)
print(f"集合 A 和 B 的差集 (A - B): {difference_set_ab}") # 也可以使用 - 运算符: set_a - set_b

difference_set_ba = set_b.difference(set_a)
print(f"集合 B 和 A 的差集 (B - A): {difference_set_ba}") # 也可以使用 - 运算符: set_b - set_a

# symmetric_difference(): 对称差集 (在 A 或 B 中，但不同时在两者中的元素)
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(f"集合 A 和 B 的对称差集 (symmetric_difference): {symmetric_difference_set}") # 也可以使用 ^ 运算符: set_a ^ set_b

# issubset(): 检查一个集合是否是另一个集合的子集
is_subset = {1, 2}.issubset(set_a)
print(f"{{1, 2}} 是不是 {set_a} 的子集: {is_subset}") # 也可以使用 <= 运算符

# issuperset(): 检查一个集合是否是另一个集合的超集
is_superset = set_a.issuperset({1, 2})
print(f"{set_a} 是不是 {{1, 2}} 的超集: {is_superset}") # 也可以使用 >= 运算符

# isdisjoint(): 检查两个集合是否没有共同元素 (不相交)
set_c = {7, 8}
is_disjoint = set_a.isdisjoint(set_c)
print(f"{set_a} 和 {set_c} 是否不相交: {is_disjoint}")
is_disjoint_false = set_a.isdisjoint(set_b)
print(f"{set_a} 和 {set_b} 是否不相交: {is_disjoint_false}")

print("\n--- 集合操作示例结束 ---")
