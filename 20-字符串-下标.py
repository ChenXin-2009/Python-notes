"""
“下标”又叫“索引”，就是编号。
可以通过下标快速的找到对应的数据
"""

# 使用某个特定的数据
# 从0开始按顺序分配一个编号
str1 = "abcdefg"
#       0123456 ————编号对应着每一个数据

print(str1[0])  # 输出对应着编号0的 a
print(str1[2])  # 输出对应着编号2的 c
str2 = str1[1]  # 设置str2为对应str1的1编号的b
print(str2)  # 输出b
