# Python 3 字典（dict）的增删改查操作示例

# 1. 创建和初始化字典 ()
# 可以创建一个空字典
my_dict = {}
print(f"初始空字典: {my_dict}")

# 也可以创建包含键值对的字典
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"初始字典: {my_dict}")

# 也可以使用 dict() 构造函数创建字典
another_dict = dict(brand="Ford", model="Mustang", year=1964)
print(f"使用 dict() 构造函数创建的字典: {another_dict}")

# 2. 增加/修改元素 (Add/Modify)
# 如果键不存在，则添加新的键值对
my_dict["email"] = "alice@example.com"
print(f"添加新键 'email': {my_dict}")

# 如果键已经存在，则修改对应的值
my_dict["age"] = 31
print(f"修改键 'age' 的值: {my_dict}")

# 使用 update() 方法添加多个键值对或更新现有键值对
my_dict.update({"zip": "10001", "city": "NYC"})
print(f"使用 update() 添加/修改多个键值对: {my_dict}")

# 3. 删除元素 (Delete)

# 3.1 del 语句: 根据键删除键值对
# 删除键为 'email' 的键值对
del my_dict["email"]
print(f"使用 del 删除键 'email': {my_dict}")

# 如果要删除的键不存在，会引发 KeyError
# try:
#     del my_dict["country"]
# except KeyError as e:
#     print(f"删除不存在的键时出错: {e}")

# 3.2 pop(): 根据键删除键值对并返回被删除的值
# 删除键为 'zip' 的键值对并获取其值
popped_value = my_dict.pop("zip")
print(f"使用 pop('zip') 删除: {my_dict}, 被删除的值: {popped_value}")

# pop() 也可以接受一个默认值，如果键不存在则返回默认值而不引发错误
popped_value_default = my_dict.pop("country", "N/A")
print(f"使用 pop('country', 'N/A') 删除不存在的键: {my_dict}, 返回默认值: {popped_value_default}")

# 3.3 popitem(): 删除并返回字典中的一个任意键值对 (Python 3.7+ 通常是最后一个插入的键值对)
key, value = my_dict.popitem()
print(f"使用 popitem() 删除一个键值对: {my_dict}, 被删除的键值对: ({key}, {value})")

# 3.4 clear(): 删除字典中的所有元素，使字典变为空字典
my_dict_to_clear = {"a": 1, "b": 2}
my_dict_to_clear.clear()
print(f"使用 clear() 清空字典: {my_dict_to_clear}")

# 4. 查询元素 (Query)

# 4.1 通过键访问值
print(f"访问键 'name' 的值: {my_dict['name']}")
print(f"访问键 'age' 的值: {my_dict['age']}")

# 如果键不存在，直接访问会引发 KeyError
# try:
#     print(my_dict['country'])
# except KeyError as e:
#     print(f"访问不存在的键时出错: {e}")

# 4.2 get(): 通过键访问值，如果键不存在则返回 None 或指定的默认值
value_name = my_dict.get("name")
print(f"使用 get('name') 获取值: {value_name}")

value_country = my_dict.get("country")
print(f"使用 get('country') 获取不存在的键 (返回 None): {value_country}")

value_country_default = my_dict.get("country", "Unknown")
print(f"使用 get('country', 'Unknown') 获取不存在的键 (返回默认值): {value_country_default}")

# 4.3 in 运算符: 检查键是否存在于字典中
if "name" in my_dict:
    print("'name' 键存在于字典中")
else:
    print("'name' 键不存在于字典中")

if "address" in my_dict:
    print("'address' 键存在于字典中")
else:
    print("'address' 键不存在于字典中")

# 4.4 len(): 获取字典中键值对的数量
dict_length = len(my_dict)
print(f"字典的长度 (键值对数量): {dict_length}")

# 4.5 keys(): 返回字典中所有键的视图
keys_view = my_dict.keys()
print(f"字典的所有键: {list(keys_view)}") # 转换为列表以便查看

# 4.6 values(): 返回字典中所有值的视图
values_view = my_dict.values()
print(f"字典的所有值: {list(values_view)}") # 转换为列表以便查看

# 4.7 items(): 返回字典中所有键值对的视图 (元组列表)
items_view = my_dict.items()
print(f"字典的所有键值对: {list(items_view)}") # 转换为列表以便查看

print("\n--- 字典操作示例结束 ---")

