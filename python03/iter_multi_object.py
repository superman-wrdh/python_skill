# -*- coding:utf-8 -*-
from random import randint
"""
迭代多个对象
"""


def sum_c_m_e():
    """
    求每一个同学三门课程总分
    :return:
    """
    chinese = [randint(60, 100) for _ in range(40)]
    math = [randint(60, 100) for _ in range(40)]
    english = [randint(60, 100) for _ in range(40)]
    total = []
    for c, m, e in zip(chinese, math, english):
        total.append(c+m+e)
    print(total)


def count_score():
    """
    有4个班级 统计每个班级大于90分人数
    """
    from itertools import chain
    c1 = [randint(60, 100) for _ in range(40)]
    c2 = [randint(60, 100) for _ in range(42)]
    c3 = [randint(60, 100) for _ in range(36)]
    c4 = [randint(60, 100) for _ in range(38)]
    count = 0
    for s in chain(c1, c2, c3, c4):
        if s > 90:
            count += 1
    print(count)


if __name__ == '__main__':
    #sum_c_m_e()
    count_score()

