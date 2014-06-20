array_x = [88, 12, 78, 87, 89, 95, 16, 82]

def Selection(n, array):
	for indexTop in range(n, 0, -1):
		IndexOfBiggest = 0
		Biggest = array[0]
		for TestDex in range(0, indexTop + 1, 1):
			if Biggest < array[TestDex]:
				Biggest = array[TestDex]
				IndexOfBiggest = TestDex
		swap(IndexOfBiggest, indexTop, array)
	return array

def swap(L, U, A):
	temp = A[L]
	A[L] = A[U]
	A[U] = temp

if __name__ == '__main__':
    result = Selection(len(array_x) - 1, array_x)
    print array_x
