# Python 3 元组（tuple）的增删改查操作示例

# 1. 创建和初始化元组 (Initialization)
# 可以创建一个空元组
my_tuple = ()
print(f"初始空元组: {my_tuple}")

# 创建包含一个元素的元组 (注意：必须在元素后加逗号)
single_element_tuple = (1,)
print(f"包含一个元素的元组: {single_element_tuple}")

# 创建包含多个元素的元组
my_tuple = (10, 20, 30, 40, 50)
print(f"初始元组: {my_tuple}")

# 也可以不使用括号创建元组 (称为元组打包 tuple packing)
another_tuple = 60, 70, 80
print(f"不使用括号创建的元组: {another_tuple}")

# 2. "增加"元素 (Simulating Add)
# 元组是不可变的，不能直接添加元素。但可以通过拼接创建新元组。

# 2.1 通过拼接添加单一元素 (创建一个新元组)
new_tuple_add_one = my_tuple + (60,) # 注意 60 后面需要逗号
print(f"通过拼接添加 60: {new_tuple_add_one}")

# 2.2 通过拼接添加多个元素 (创建一个新元组)
elements_to_add = (70, 80)
new_tuple_add_multiple = new_tuple_add_one + elements_to_add
print(f"通过拼接添加 (70, 80): {new_tuple_add_multiple}")

# 3. "删除"元素 (Simulating Delete)
# 元组是不可变的，不能直接删除元素。但可以通过切片创建新元组来“删除”元素。

# 3.1 "删除"指定索引的元素 (创建一个新元组，排除该元素)
# 假设我们要删除索引为 2 的元素 (即 30)
# 方法是取该元素之前和之后的切片，然后拼接
tuple_before_delete = (10, 20, 30, 40, 50)
index_to_delete = 2
new_tuple_after_delete = tuple_before_delete[:index_to_delete] + tuple_before_delete[index_to_delete + 1:]
print(f"原始元组: {tuple_before_delete}")
print(f"删除索引 {index_to_delete} 后的新元组: {new_tuple_after_delete}")

# 3.2 删除整个元组变量
# del 语句可以删除元组变量本身，而不是元组中的元素
my_tuple_to_delete = (1, 2, 3)
print(f"删除前的元组变量: {my_tuple_to_delete}")
del my_tuple_to_delete
# print(f"删除后的元组变量: {my_tuple_to_delete}") # 这行会引发 NameError，因为变量已被删除

# 4. "修改"元素 (Simulating Modify)
# 元组是不可变的，不能直接修改元素。但可以通过创建新元组来模拟修改。

# 4.1 "修改"指定索引的元素 (通过转换为列表，修改，再转回元组)
original_tuple = ('apple', 'banana', 'cherry')
print(f"原始元组: {original_tuple}")

# 假设我们想把 'banana' 改成 'grape'
list_from_tuple = list(original_tuple)
list_from_tuple[1] = 'grape'
modified_tuple = tuple(list_from_tuple)
print(f"将 'banana' 修改为 'grape' 后的新元组: {modified_tuple}")

# 5. 查询元素 (Query)

# 5.1 通过索引访问元素
print(f"元组的第一个元素 (索引 0): {my_tuple[0]}")
print(f"元组的最后一个元素 (索引 -1): {my_tuple[-1]}")

# 5.2 切片访问 (获取子元组)
# 获取从索引 1 到索引 3 (不包含) 的元素
sub_tuple = my_tuple[1:3]
print(f"切片 my_tuple[1:3]: {sub_tuple}")

# 获取从开头到索引 2 (不包含) 的元素
sub_tuple = my_tuple[:2]
print(f"切片 my_tuple[:2]: {sub_tuple}")

# 获取从索引 2 到末尾的元素
sub_tuple = my_tuple[2:]
print(f"切片 my_tuple[2:]: {sub_tuple}")

# 5.3 len(): 获取元组的长度（元素数量）
tuple_length = len(my_tuple)
print(f"元组的长度: {tuple_length}")

# 5.4 in 运算符: 检查元素是否存在于元组中
if 20 in my_tuple:
    print("20 在元组中")
else:
    print("20 不在元组中")

if 100 in my_tuple:
    print("100 在元组中")
else:
    print("100 不在元组中")

# 5.5 index(): 返回指定元素的第一个匹配项的索引
# 如果元素不存在，会引发 ValueError
try:
    index_of_40 = my_tuple.index(40)
    print(f"40 的索引是: {index_of_40}")
except ValueError as e:
    print(f"查找不存在的元素时出错: {e}")

# 5.6 count(): 返回指定元素在元组中出现的次数
my_repeated_tuple = (1, 2, 2, 3, 1, 4, 2)
count_of_2 = my_repeated_tuple.count(2)
print(f"元素 2 在 {my_repeated_tuple} 中出现的次数: {count_of_2}")
count_of_5 = my_repeated_tuple.count(5)
print(f"元素 5 在 {my_repeated_tuple} 中出现的次数: {count_of_5}")

print("\n--- 元组操作示例结束 ---")

