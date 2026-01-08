"""
逻辑控制流
重点：
1. 缩进决定作用域（没有 {}）。
2. Truthy/Falsy 值（PHP 程序员容易混淆的地方）。
3. match-case (Python 的 switch)。
"""

# 1. 真值测试 (Truth Value Testing)
# 在 Python 中，以下都被视为 False：
# None, False, 0, 0.0, "", [], {}, set()
data = []
if not data:
    print("列表是空的 (相当于 PHP if (empty($data)))")

# 2. 三元运算符
score = 85
# PHP: $res = $score > 60 ? "Pass" : "Fail";
result = "Pass" if score > 60 else "Fail" 
print(f"考试结果: {result}")

# 3. while 循环与 break/continue
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue # 跳过本次
    print(f"While Loop: {count}")

# 4. ★★★ match-case (Python 3.10+ 新特性) ★★★
# 非常适合处理爬虫的状态码或 API 响应
http_status = 404

match http_status:
    case 200:
        print("请求成功")
    case 404:
        print("页面未找到")
    case 500 | 502:  # 支持多个条件
        print("服务器错误")
    case _:          # 相当于 PHP 的 default
        print("未知状态")

# 5. 异常处理 (Try-Except)
# Python 哲学：EAFP (Easier to ask for forgiveness than permission)
# 先做，报错了再捕获，而不是先检查。
user_input = "abc"
try:
    number = int(user_input)
except ValueError as e:
    print("这不是一个数字！")
except Exception as e:
    print(f"发生了其他错误: {e}")
finally:
    print("无论如何都会执行 (通常用于关闭文件/数据库连接)")
