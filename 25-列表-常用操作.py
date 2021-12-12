"""
列表
格式：
    list = [数据1, 数据2, 数据3, 数据4, 数据5......]
"""

# ======================查找=======================

# ----------------------下标-----------------------
name_list = ['Tom', 'Jack', 'Lily', 'Rose', 'Tom']
#    下标：     0      1       2       3
#                  和字符串差不多

print(name_list[0])  # Tom
print(name_list[1])  # Jack
print(name_list[3])  # Rose
# ------------------------函数---------------------
# ·············index 返回指定数据所在的下标···········
# 跟字符串的index(见22-字符串-查找的第22行)差不多
print(name_list.index('Lily', 0, 3))  # 2
# ···············count 返回出现次数··················
print(name_list.count('Tom'))  # 2
# ············len 访问列表数据个数，即长度·············
print(len(name_list))  # 5

