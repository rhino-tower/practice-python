import random
import copy

class ShapeInfo:
	small: str = ''
	large: str = ''

	def __init__(self, _large: str, _small: str) -> None:
		self.large = _large
		self.small = _small

	def is_same(self, _shape) -> bool:
		if self.small == _shape.small and self.large == _shape.large:
			return True
		return False

	def text(self) -> str:
		if self.large == '':
			return '\033[31m' + 's' + self.small + '\033[0m'
		elif self.small == '':
			return '\033[31m' + 'l' + self.large + '\033[0m'
		else:
			return '\033[31m' + 's' + self.large + '\033[0m' + ' is out of ' + '\033[31m' + 'l' + self.small + '\033[0m'


def create_question(question_cnt):
	SHAPE_CONST: List[str] = ['TRI', 'RECT', 'CIR', 'STAR']
	trans_types: List[int] = random.sample(list(range(1, 10, 1)), question_cnt)
	ans: int = random.randrange(question_cnt)
	ans_trans_type: int = trans_types[ans]
	example_shape: ShapeInfo = ShapeInfo(*random.choices(SHAPE_CONST, k = 2))
	test_shape: ShapeInfo = ShapeInfo(*random.choices(SHAPE_CONST, k = 2))
	transed_test_shapes = []

	while example_shape.is_same(test_shape):
		test_shape: ShapeInfo = ShapeInfo(*random.choices(SHAPE_CONST, k = 2))

	for type in trans_types:
		tmp = trans_shape(copy.copy(test_shape), type)
		transed_test_shapes.append(tmp)


	print('=======================start=======================')
	print('例と同じ変換規則を適用すると0,...,4のどれになるか直感的に考えよ.')
	while True:
		print('(例) ' + example_shape.text() + ' → ' + trans_shape(example_shape, ans_trans_type).text() + ' \n')
		cnt = 0
		print('ans' + str(ans))
		for transed_test_shape in transed_test_shapes:
			print(str(cnt) + ' : ' + test_shape.text() + ' → ' + transed_test_shape.text())
			cnt += 1
		your_ans: int = int(input('解答番号 : '))
		if your_ans == ans:
			print('正解です!')
			break
		print('不正解です\n\n')





def trans_shape(shape: ShapeInfo, type: int):
	_shape: ShapeInfo = shape

	if type == 1:
		_shape.small = ''
	elif type == 2:
		_shape.large = ''
	elif type == 3:
		_shape.small = 'TRI'
	elif type == 4:
		_shape.large = 'TRI'
	elif type == 5:
		_shape.small = 'RECT'
	elif type == 6:
		_shape.large = 'RECT'
	elif type == 7:
		_shape.small = 'CIR'
	elif type == 8:
		_shape.large = 'CIR'
	elif type == 9:
		_shape.small = 'STAR'
	elif type == 10:
		_shape.large = 'STAR'

	return _shape

def main():
	question_cnt: int = 5

	create_question(question_cnt)

if __name__ == '__main__':
	main()
