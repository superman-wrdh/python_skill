# -*- coding:utf-8 -*-
import re


def my_split(s):
    return re.split(r'[,;\t|]+', s)


if __name__ == '__main__':
    st = 'ab;cd|fasdfd|,,esf\tfd,saf;'
    print(my_split(st))



