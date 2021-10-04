import random
import copy
from typing import List
from shape_info import ShapeInfo

def create_question(question_cnt):
	trans_types = []
	ans: int = 0
	ans_trans_type = []
	example_shape: ShapeInfo = ShapeInfo()
	test_shape: ShapeInfo = ShapeInfo()
	transed_test_shapes = []

	while(dup_check(transed_test_shapes)):
		trans_types: List[int] = random.sample(list(range(1, 10, 1)), question_cnt)
		# 答え生成
		ans: int = random.randrange(question_cnt)
		ans_trans_type: int = trans_types[ans]
		# 例と問題生成
		example_shape: ShapeInfo = ShapeInfo()
		test_shape: ShapeInfo = ShapeInfo()
		transed_test_shapes = []

		while example_shape.is_same(test_shape):
			test_shape.re_generate()

		for type in trans_types:
			tmp = trans_shape(test_shape, type)
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
	_shape: ShapeInfo = copy.copy(shape)

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

def dup_check(shapes: List) -> bool:
	if not shapes:
		return True
	for shape1 in shapes:
		for shape2 in shapes:
			if shape1 != shape2 and shape1.is_same(shape2):
				return True
	return False
