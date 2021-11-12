# 1. 为什么使用二进制?
# 二进制具有抗干扰能力强、可靠性高的特点。
# Computers use voltages(电压) and since voltages changes often, no specific voltage is set for each number in the decimal
# system. For this reason, binary is measured as a two-state system i.e. on or off. Also, to keep calculations simple
# and convert into binary online, computers use the binary number system.
# 2. 为什么二进制抗干扰能力强
# 由于周围环境的影响，电压不总是稳定的。如果采用十进制等，就要把一定范围内电压分成若干范围来表示不同的数字，而不稳定的电压则可能造成对信号对错误
# 解读。而二进制只需要判断高低电压，范围更大，发生错误的几率相对小很多，也就是抗干扰能力更强。
# 3. 为什么无符号整数的最大值最后要减去1，2^(n-1)-1？
# 从0开始计数。2^8=256，即从0计数到255。因此，能存储或者表达的最大值就是255，即2^8-1。
from math import floor
from operator import mod

number = 53

# int -> binary
print("binary of 53 is " + bin(53))
# binary -> int
print("decimal of 0b110101 is " + int("0b110101", 2).__str__())

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 9
d = -9
print("-------------二进制的逻辑运算")
# 逻辑与，对应的两位中，两个都是1，结果为1，否则为0
print("a & b =", a & b, bin(a & b))
# 逻辑或，对应的两位中，其中一个为1，则结果为1
print("a | b =", a | b, bin(a | b))
# 异或，对应的两位，如果不同(一个1，一个0)，则结果为1
print("a ^ b =", a ^ b, bin(a ^ b))

print("-------------二进制的移位运算")
# 二进制左移，就是乘以2^n
print("60 << 1 =", a << 1)
# 二进制右移一位，对于正数来说，就是将数字除以2^n并向零取整
print("60 >> 1 =", a >> 1)
print("9 >> 1 =", c >> 1)

# 负数
print("9的二进制", bin(c))
print("-9的二进制", bin(d))

