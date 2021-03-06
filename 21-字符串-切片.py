"""
切片是指操作对象截取其中一部分的操作。
字符串、列表、元祖都支持切片操作
"""

'''========语法========
序列[开始位置下标:结束前位置下标:步长]
                             ^
                         选取位置间隔
'''

str1 = 'abcdefg'
#       0123456

print(str1[0:7:1])  # abcdefg
# [从下标0开始:到下标7前结束:步长为1]
# 注意：         是  ^   前，不是输出下标7而是下标7之前

str2 = "0123456789"
#       0123456789
print(str2[0:9:2])  # 步长为2 02468
print(str2[1::2])  # 13579 每个参数都可以省略
print(str2[:])  # 0123456789
