#!/usr/bin/env python
from Fruit import Fruit

if __name__ == '__main__':
	x = Fruit.get_fruit()()
	print(type(x))