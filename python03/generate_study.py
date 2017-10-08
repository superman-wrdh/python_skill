# -*- coding:utf-8 -*-
"""
使用生成器实现可迭代对象
"""


class PrimeNumber:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def is_prime_number(k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start ,self.end):
            if self.is_prime_number(k):
                yield k


if __name__ == '__main__':
    for x in PrimeNumber(1, 100):
        print(x)




