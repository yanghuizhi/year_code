# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况
#          ，插入后此元素之后的数，依次后移一个位置


# 方案一
# L = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13]
# print(L)
# # 我将通过插入数字7来加入按照从小到大排列的列表中
# n = int(input("输入一个数："))
# L.append(n)
# # 通过for循环
# for i in range(1, len(L)):
#     if L[-i] < L[-(i + 1)]:
#         L[-i], L[-(i + 1)] = L[-(i + 1)], L[-i]
#     else:
#         break
# print(u"插入数字后的列表为：\n", L)

# 最便利方案
# x = [1, 3, 5, 6, 88, 99]
# y = int(input("输入数字: "))
# x.append(y)
# x.sort()
# print(x)

import os
fi=os.path.dirname(os.path.dirname(__file__))
print(fi)
# 标准方案
# if __name__ == '__main__':
#     # 方法一 ： 0 作为加入数字的占位符
#     a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]
#     print('原始列表:')
#     for i in range(len(a)):
#         print(a[i], end=' ')
#     # number = int(raw_input("\n插入一个数字:\n"))
#     number = 7
#     end = a[9]
#     if number > end:
#         a[10] = number
#     else:
#         for i in range(10):
#             if a[i] > number:
#                 temp1 = a[i]
#                 a[i] = number
#                 for j in range(i + 1, 11):
#                     # temp2 = a[j]
#                     # a[j] = temp1
#                     # temp1 = temp2
#                     a[j], temp1 = temp1,a[j]
#                 break
#     print('排序后列表:')
#     for i in range(11):
#         print(a[i], end=' ')
