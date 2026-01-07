# Python 3 列表（list）的增删改查操作示例

# 1. 创建和初始化列表 (Initialization)
# 可以创建一个空列表
my_list = []
print(f"初始空列表: {my_list}")

# 也可以创建包含元素的列表
my_list = [10, 20, 30, 40, 50]
print(f"初始列表: {my_list}")

# 2. 增加元素 (Add)

# 2.1 append(): 在列表末尾添加一个元素
my_list.append(60)
print(f"使用 append() 添加 60: {my_list}")

# 2.2 insert(): 在指定索引位置插入一个元素
# 在索引为 1 的位置插入 15
my_list.insert(1, 15)
print(f"使用 insert(1, 15) 插入: {my_list}")

# 2.3 extend(): 将另一个列表（或任何可迭代对象）中的所有元素添加到当前列表的末尾
another_list = [70, 80]
my_list.extend(another_list)
print(f"使用 extend() 添加另一个列表: {my_list}")

# 3. 删除元素 (Delete)

# 3.1 del 语句: 根据索引删除元素
# 删除索引为 0 的元素 (即 10)
del my_list[0]
print(f"使用 del my_list[0] 删除: {my_list}")

# 删除一个范围的元素 (切片)
del my_list[4:6] # 删除索引 4 和 5 的元素
print(f"使用 del my_list[4:6] 删除切片: {my_list}")

# 3.2 remove(): 根据值删除第一个匹配的元素
# 删除值为 15 的元素
my_list.remove(15)
print(f"使用 remove(15) 删除: {my_list}")

# 如果要删除的值不存在，会引发 ValueError
# try:
#     my_list.remove(99)
# except ValueError as e:
#     print(f"删除不存在的元素时出错: {e}")

# 3.3 pop(): 根据索引删除元素并返回被删除的元素
# 删除最后一个元素并返回它
popped_element = my_list.pop()
print(f"使用 pop() 删除最后一个元素: {my_list}, 被删除的元素: {popped_element}")

# 删除指定索引的元素并返回它
popped_element = my_list.pop(2) # 删除索引为 2 的元素 (即 40)
print(f"使用 pop(2) 删除指定索引元素: {my_list}, 被删除的元素: {popped_element}")

# 3.4 clear(): 删除列表中的所有元素，使列表变为空列表
my_list_to_clear = [1, 2, 3]
my_list_to_clear.clear()
print(f"使用 clear() 清空列表: {my_list_to_clear}")

# 4. 修改元素 (Modify)

# 通过索引直接赋值来修改元素
# 将索引为 0 的元素 (即 20) 修改为 25
my_list[0] = 25
print(f"修改索引 0 的元素为 25: {my_list}")

# 修改一个范围的元素 (切片赋值)
my_list[1:3] = [35, 45] # 将索引 1 和 2 的元素替换为 35, 45
print(f"修改切片 my_list[1:3] 为 [35, 45]: {my_list}")

# 5. 查询元素 (Query)

# 5.1 通过索引访问元素
print(f"列表的第一个元素 (索引 0): {my_list[0]}")
print(f"列表的最后一个元素 (索引 -1): {my_list[-1]}")

# 5.2 切片访问 (获取子列表)
# 获取从索引 1 到索引 3 (不包含) 的元素
sub_list = my_list[1:3]
print(f"切片 my_list[1:3]: {sub_list}")

# 获取从开头到索引 2 (不包含) 的元素
sub_list = my_list[:2]
print(f"切片 my_list[:2]: {sub_list}")

# 获取从索引 2 到末尾的元素
sub_list = my_list[2:]
print(f"切片 my_list[2:]: {sub_list}")

# 5.3 len(): 获取列表的长度（元素数量）
list_length = len(my_list)
print(f"列表的长度: {list_length}")

# 5.4 in 运算符: 检查元素是否存在于列表中
if 25 in my_list:
    print("25 在列表中")
else:
    print("25 不在列表中")

if 100 in my_list:
    print("100 在列表中")
else:
    print("100 不在列表中")

# 5.5 index(): 返回指定元素的第一个匹配项的索引
# 如果元素不存在，会引发 ValueError
try:
    index_of_35 = my_list.index(35)
    print(f"35 的索引是: {index_of_35}")
except ValueError as e:
    print(f"查找不存在的元素时出错: {e}")

# 5.6 count(): 返回指定元素在列表中出现的次数
my_repeated_list = [1, 2, 2, 3, 1, 4, 2]
count_of_2 = my_repeated_list.count(2)
print(f"元素 2 在 {my_repeated_list} 中出现的次数: {count_of_2}")
count_of_5 = my_repeated_list.count(5)
print(f"元素 5 在 {my_repeated_list} 中出现的次数: {count_of_5}")

print("\n--- 列表操作示例结束 ---")
