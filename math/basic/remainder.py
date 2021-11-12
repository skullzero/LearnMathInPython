from math import floor

# floor函数
# 正数向零取整；负数向无穷小取整
print("floor(8/3)=", floor(8/3))
print("floor(8/-3)=", floor(8/-3))
print("floor(-8/3)=", floor(-8/3))
print("floor(-8/-3)=", floor(-8/-3))


# 1.当两个数的符号相同，即同为负或者同为正时，取余和取模结果相同。
# 2.符号不同时，取模结果的符号和除数一致，取余结果的符号和被除数一致。
# 公式 r = a - (n * trunc(a/n))
# r is the remainder(余数).
# a is the dividend(被除数).
# n is the divisor(除数).
# r = 8 - (3 * floor(8 / 3)) = 8 - (3 * floor(2.66666667)) = 8 - 3*2 = 2
print("8mod3=", 8 % 3)
# r = 8 - (3 * floor(-8/-3)) = -8 - (-3 * floor(2.66666667)) = -8 - (-3*2) = -2
print("-8mod-3=", -8 % -3)
# r = -8 - (3 * floor(-8/3)) = -8 - (3 * floor(-2.66666667)) = -8 - (3*(-3)) = 1
print("-8mod3=", -8 % 3)
# r = 8 - (-3 * floor(8/-3)) = 8 - (-3 * floor(-2.66666667)) = 8 - (-3*(-3)) = -1
print("8mod-3=", 8 % -3)
