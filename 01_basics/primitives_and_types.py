"""
基础数据类型与类型转换
重点：
1. Python 是强类型动态语言（不会像 JS 那样自动隐式转换 '1'+1）。
2. 理解可变(Mutable)与不可变(Immutable) —— 面试必问。
"""

# 1. 基础类型
a_int: int = 100
a_float: float = 3.14
a_bool: bool = True  # 注意首字母大写，PHP是 true
a_str: str = "Hello"
a_none: None = None  # 对应 PHP 的 null

# 2. 字符串格式化 (f-string) —— 以后每天都会用
# PHP: "Price: " . $price
print(f"整数: {a_int}, 浮点: {a_float}")

# 3. 类型转换 (Casting)
s_num = "50"
i_num = int(s_num)  # 字符串转整型
f_num = float(s_num) # 字符串转浮点
s_list = list("Hello") # 字符串转列表 -> ['H', 'e', 'l', 'l', 'o']
print(f"转换后的类型: {type(i_num)}")

# 4. ★★★ 重点：可变 vs 不可变 (这是 Python 的核心概念) ★★★
# 不可变 (Immutable): int, float, str, tuple, bool
# 意味着：你不能修改它本身，只能创建新的覆盖它。
s = "hello"
# s[0] = "H"  # ❌ 报错！字符串不支持修改
s = "H" + s[1:] # ✅ 正确：这是创建了一个新字符串赋值回去

# 可变 (Mutable): list, dict, set
# 意味着：可以在原地修改，内存地址不变。
l = [1, 2, 3]
print(f"修改前ID: {id(l)}")
l[0] = 100
print(f"修改后ID: {id(l)}") # ID 是一样的
