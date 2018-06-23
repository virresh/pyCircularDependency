#!/usr/bin/env python
from random import randint
from SummerFruit import SummerFruit
from WinterFruit import WinterFruit

class Fruit(object):
	@staticmethod
	def get_fruit():
		y = randint(0,99)
		if y%2==1:
			return SummerFruit
		else:
			return WinterFruit
