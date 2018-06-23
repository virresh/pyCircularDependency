#!/usr/bin/env python
from random import randint

class Fruit(object):
	@staticmethod
	def get_fruit():
		y = randint(0,99)
		if y%2==1:
			SummerFruit = __import__('SummerFruit')
			return SummerFruit.SummerFruit
		else:
			WinterFruit = __import__('WinterFruit')
			return WinterFruit.WinterFruit
