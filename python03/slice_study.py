# -*- coding:utf-8 -*-
from itertools import islice

"""
迭代器切片操作
"""


def slice():
    file = open('www.66super.com_index.html', 'r', encoding='utf-8')
    it = islice(file, 10, 20)
    for i in it:
        print(i)


if __name__ == '__main__':
    slice()
