from typing import List
import random

SHAPE_CONST: List[str] = ['TRI', 'RECT', 'CIR', 'STAR']

class ShapeInfo:
	small: str = ''
	large: str = ''

	def __init__(self) -> None:
		self.large, self.small = random.choices(SHAPE_CONST, k = 2)

	def is_same(self, _shape) -> bool:
		if self.small == _shape.small and self.large == _shape.large:
			return True
		return False

	def re_generate(self) -> None:
		self.large, self.small = random.choices(SHAPE_CONST, k = 2)

	def text(self) -> str:
		if self.large == '':
			return '\033[31m' + 's' + self.small + '\033[0m'
		elif self.small == '':
			return '\033[31m' + 'l' + self.large + '\033[0m'
		else:
			return '\033[31m' + 's' + self.large + '\033[0m' + ' is in ' + '\033[31m' + 'l' + self.small + '\033[0m'
