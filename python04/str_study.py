# -*- coding:utf-8 -*-
import re
"""
正则替换日志文件中的日期格式
"""

def read_log():
    log = open('service.log', 'r', encoding='utf-8').read()
    print(re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log))


def read_log2():
    """
    ?P<year>给组命名
    """
    log = open('service.log', 'r', encoding='utf-8').read()
    print(re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', log))


if __name__ == '__main__':
    read_log2()