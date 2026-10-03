# -*- coding: utf-8 -*-
"""
D001 · 2026-10-03 · 第一行 Python 代码

运行方式：
    1. VS Code 里按 Ctrl+F5
    2. 或者终端：
       conda activate rl
       cd /d D:/code/python-learning         # 用正斜杠！文档里想写 \\n 这种反斜杠要写两个
       python "01-Python基础/week1/D001_hello.py"

今天的任务：让这个文件跑起来，然后动手改几处，看输出怎么变。
"""

print("Hello, Python!")
print("我是大工的，104 天后我要手写 PPO")

print("-" * 40)

# ============ 1. 算术运算：和 C 语言最容易搞混的几个 ============
print("1 + 2      =", 1 + 2)
print("10 / 3     =", 10 / 3)      # 3.333...  注意！Python 的 / 结果是小数
print("10 // 3    =", 10 // 3)     # 3         整除要用 //
print("10 % 3     =", 10 % 3)      # 1         取余和 C 一样
print("2 ** 10    =", 2 ** 10)     # 1024      幂运算，不是 ^（^ 在 Python 里是异或）
print("divmod     =", divmod(10, 3))  # (3, 1)  同时拿到商和余数

print("-" * 40)

# ============ 2. 变量：不需要声明类型 ============
name = "谢泽铭"
age = 21
height = 1.76
weight=70
is_student = True                # 注意首字母大写，C 里没有这个类型

# f-string：最常用的字符串格式化，比 C 的 printf 好用
print(f"我是{name}，今年{age}岁，身高{height}米")
print(f"明年我就{age + 1}岁了")           # 大括号里可以直接写表达式
print(f"身高保留一位小数：{height:.1f}")    # 还能控制格式

print("-" * 40)

# ============ 3. 类型：type() 是你的好朋友 ============
print("name 的类型是：", type(name))
print("age  的类型是：", type(age))
print("注意：Python 的 int 不会溢出，多大都能存")
print("2 的 100 次方 =", 2 ** 100)

# ============ 动手改一改（今天的【敲】任务）============
# 1. 把 name / age / height 改成你自己的信息，重新运行
# 2. 加一行，用 f-string 打印你的 BMI（体重kg / 身高m的平方）
# 3. 试试 print(10 // 0) 会发生什么？把报错信息读一遍，再改回来
# 4. 试试 print("年龄" + 20) 会报什么错？为什么？怎么改才对？
print(f"我的BMI是{weight/height**2:.1f}")
#print(10//0)
print("年龄",20)
