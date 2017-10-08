# -*- coding:utf-8-*_
from collections import Iterable, Iterator
"""
迭代器和可迭代对象 生成
"""


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    @staticmethod
    def get_weather(city):
        import requests
        response = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
        data = response.json()['data']['forecast'][0]
        return '%s: %s: %s:' % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


if __name__ == '__main__':
    for x in WeatherIterable(['武汉', '上海']):
        print(x)